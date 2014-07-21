import grp
import platform
import pwd
import tempfile
import os


def return_error(facility, message=''):
    """ Receives an error message to send to whatever facility is appropriate for a project. defaults to print. """
    if facility:
        facility(message)
    else:
        print(message)


def main():
    """ Returns a simple to use dictionary of common operating system details"""

    p = {}

    if platform.system() == 'Darwin':
        try:
            #someday, the next line may be helpful for OSX
            p['os'] = platform.system_alias(platform.system(), platform.release(), platform.mac_ver())[0] or None
            p['type'] = 'Darwin'
            p['release'] = platform.mac_ver()[0] or None
            p['platform'] = platform.platform() or None
            p['python_version'] = platform.python_version() or None
            p['current_uid'] = pwd.getpwuid(os.getuid())[2]
            p['current_gid'] = pwd.getpwuid(os.getuid())[3]
            p['current_user'] = pwd.getpwuid(os.getuid())[0]
            p['current_user_group'] = grp.getgrgid(pwd.getpwnam(p['current_user']).pw_gid).gr_name
            p['current_user_desktop'] = os.path.join(os.path.expanduser('~'), 'Desktop')
            p['current_user_homedir'] = os.path.expanduser('~')
            p['tmp_dir'] = tempfile.gettempdir()
            #Dot is there as a hack until joining ~ and a dir does more than just give [1:]
            p['current_user_plist_dir'] = os.path.join(os.path.expanduser('~'), './Library/LaunchAgents/')
            p['mount_dir'] = '/Volumes'
        except IOError:
            return_error('Could not get more specific information for Darwin-based platform')
    elif platform.system() == 'Linux':
        try:
            p['os'] = platform.linux_distribution()[0] or None
            p['type'] = 'Linux'
            p['release'] = platform.linux_distribution()[1] or None
            p['platform'] = platform.platform() or None
            p['python_version'] = platform.python_version() or None
            p['current_uid'] = pwd.getpwuid(os.getuid())[2]
            p['current_gid'] = pwd.getpwuid(os.getuid())[3]
            p['current_user'] = pwd.getpwuid(os.getuid())[0]
            p['current_user_group'] = grp.getgrgid(pwd.getpwnam(p['current_user']).pw_gid).gr_name
            p['tmp_dir'] = tempfile.gettempdir()
            p['mount_dir'] = '/mnt'
        except:
            return_error('Could not get more specific information for Linux-based platform')
    elif platform.system() == 'Windows': #Pull requests _very_ welcome.
        try:
            #This next entry returns something akin to 7_SP1.  Commented in case a pull request prefers this
            #type of format.  I'm not a Windows dev, so I don't know the preferred response.
            #p['os'] = "{0}_{1}".format(platform.win32_ver()[0], platform.win32_ver()[2] or '') or None
            p['os'] = str(platform.system() + platform.release()) or None
            p['type'] = 'Windows'
            p['release'] = platform.win32_ver()[0] or None
            p['platform'] = platform.platform() or None
            p['python_version'] = platform.python_version() or None
            p['current_user_desktop'] = os.path.join(os.path.expanduser('~'), 'Desktop')
            p['tmp_dir'] = tempfile.gettempdir()
            p['mount_dir'] = None #Windows requires drive letters.
        except:
            return_error('Could not get more specific information for Windows-based platform')
    else:
        try:
            p['os'] = platform.linux_distribution()[0] or None
            p['type'] = 'unknown'
            p['release'] = platform.linux_distribution()[1] or None
            p['platform'] = platform.platform() or None
            p['python_version'] = platform.python_version() or None
            p['tmp_dir'] = tempfile.gettempdir() or None
            p['current_uid'] = p['current_gid'] = None
            p['current_user'] = p['current_user_group'] = p['current_user_desktop'] = None
        except:
            raise NotImplementedError('Could not get platform information.')

    return p

if __name__ == '__main__':
    print main()