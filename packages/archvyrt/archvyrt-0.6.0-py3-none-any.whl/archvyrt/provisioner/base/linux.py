import logging
import os

import archvyrt.tools as tools
from archvyrt.provisioner.base import Base

LOG = logging.getLogger('archvyrt')


class LinuxProvisioner(Base):
    """
    Linux Provisioner
    """

    def __init__(self, domain, target="/provision", proxy=None):
        """
        Initializes and runs the provisioner.
        """
        super().__init__(domain)
        self._proxy = proxy
        self._target = target
        self._uuid = {}
        self._cleanup = []

        self._prepare_disks()
        self._install()
        self._network_config()
        self._locale_config()
        self._boot_config()
        self._access_config()

    @property
    def proxy(self):
        """
        Proxy server used by this provisioner
        """
        return self._proxy

    @property
    def target(self):
        """
        Temporary provisioning target, where the domains disks are mounted
        """
        return self._target

    def run(self, cmds, output=False, failhard=True, **kwargs):
        """
        Runs a command, ensures proper environment
        """
        run_env = kwargs.pop('env', None)
        if not run_env:
            run_env = os.environ.copy()
            if self.proxy:
                run_env['http_proxy'] = 'http://%s' % self.proxy
                run_env['ftp_proxy'] = 'http://%s' % self.proxy
        return self._runcmd(cmds, output, failhard, env=run_env, **kwargs)

    def runchroot(self, cmds, output=False, failhard=True, **kwargs):
        """
        Runs a command in the guest
        """
        raise NotImplementedError

    def writetargetfile(self, filename, lines, mode='w'):
        """
        Writes a file in the guest
        """
        targetfilename = "%s%s" % (self.target, filename)
        self.writefile(targetfilename, lines, mode)

    def chmodtargetfile(self, filename, chmod):
        """
        Change permission of file in the guest
        """
        targetfilename = "%s%s" % (self.target, filename)
        os.chmod(targetfilename, chmod)

    def deletetargetfile(self, filename):
        """
        Delete a file in the guest
        """
        targetfilename = "%s%s" % (self.target, filename)
        os.remove(targetfilename)

    def cleanup(self):
        """
        Cleanup actions, such as unmounting and disconnecting disks
        """
        for cmd in reversed(self._cleanup):
            self.run(cmd)

    def _prepare_disks(self):
        """
        Format and mount disks
        """
        LOG.info('Prepare disks')
        for disk in self.domain.disks:
            dev = '/dev/nbd%s' % disk.number
            cur_part = 0
            # "mount" qcow2 image file as block device
            self.run([
                tools.QEMU_NBD,
                '-n',
                '-c',
                dev,
                disk.path,
            ])
            self._cleanup.append([
                tools.QEMU_NBD,
                '-d',
                dev,
            ])
            # create empty partition table
            self.run([
                tools.SGDISK,
                '-o',
                dev,
            ])
            # On first disk, we create a bios boot partition
            if disk.number == '0':
                cur_part += 1
                self.run([
                    tools.SGDISK,
                    '-n', '%d:2048:4095' % cur_part,
                    '-t', '%d:ef02' % cur_part,
                    dev
                ])
                endsector = self.run([
                    tools.SGDISK,
                    '-E',
                    dev
                ], output=True).strip()
                cur_part += 1
                self.run([
                    tools.SGDISK,
                    '-n', '%d:4096:%s' % (cur_part, endsector),
                    dev
                ])
            else:
                # create single partition
                cur_part += 1
                self.run([
                    tools.SGDISK,
                    '-n', '%d' % cur_part,
                    dev
                ])
            if disk.fstype == 'ext4':
                # format ext4
                self.run([
                    tools.MKFS_EXT4,
                    '%sp%d' % (dev, cur_part)
                ])
                mountpoint = '/provision/%s' % disk.mountpoint.lstrip('/')
                if disk.mountpoint == '/':
                    # set a filesystem label to aid grub configuration
                    self.run([
                        tools.TUNE2FS,
                        '-L',
                        'ROOTFS',
                        '%sp%d' % (dev, cur_part),
                        ])
                else:
                    # create mountpoint
                    os.makedirs(mountpoint)
                self.run([
                    tools.MOUNT,
                    '%sp%d' % (dev, cur_part),
                    mountpoint,
                    ])
                self._cleanup.append([
                    tools.UMOUNT,
                    mountpoint,
                ])
                uuid = self.run([
                    tools.BLKID,
                    '-s',
                    'UUID',
                    '-o',
                    'value',
                    '%sp%d' % (dev, cur_part),
                    ], output=True).strip()
                self._uuid.setdefault('ext4', {})[disk.mountpoint] = uuid
            elif disk.fstype == 'swap':
                # set partition type to linux swap
                self.run([
                    tools.SGDISK,
                    '-t',
                    '%d:8200' % cur_part,
                    dev
                ])
                # format swap space
                self.run([
                    tools.MKSWAP,
                    '-f',
                    '%sp%d' % (dev, cur_part)
                ])
                self.run([
                    tools.SWAPON,
                    '%sp%d' % (dev, cur_part)
                ])
                self._cleanup.append([
                    tools.SWAPOFF,
                    '%sp%d' % (dev, cur_part)
                ])
                uuid = self.run([
                    tools.BLKID,
                    '-s',
                    'UUID',
                    '-o',
                    'value',
                    '%sp%d' % (dev, cur_part),
                    ], output=True).strip()
                self._uuid.setdefault('swap', []).append(uuid)
            else:
                raise RuntimeError('Unsupported fstype %s', disk.fstype)

    def _install(self):
        """
        Linux base installation
        """
        raise NotImplementedError

    def _network_config(self):
        """
        Domain network configuration
        """
        raise NotImplementedError

    def _locale_config(self):
        """
        Domain locale/language settings
        """
        raise NotImplementedError

    def _boot_config(self):
        """
        Domain fstab, bootloader, initrd configuration
        """
        raise NotImplementedError

    def _access_config(self):
        """
        Domain access configuration such as sudo/ssh and local users
        """
        raise NotImplementedError
