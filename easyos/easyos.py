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


def env():
    """ Returns a simple to use dictionary of common operating system details"""


    p = {}
    p['platform'] = platform.platform() or None
    p['python_version'] = platform.python_version() or None
    p['homedir'] = os.path.join(os.path.expanduser('~'))
    p['current_user_desktop'] = os.path.join(p['homedir'], 'Desktop') or None
    p['tmp_dir'] = tempfile.gettempdir()

    # Might fail on Windows.  Open a PR or issue on github if this is important to you.
    # This should probably get cleaned up by separating the getgrpid from getpwuid, but AFAIK, it's pass/fail
    try:
        p['current_uid'] = pwd.getpwuid(os.getuid())[2]
        p['current_gid'] = pwd.getpwuid(os.getuid())[3]
        p['current_user'] = pwd.getpwuid(os.getuid())[0]
        p['current_user_group'] = grp.getgrgid(pwd.getpwnam(p['current_user']).pw_gid).gr_name
    except:
        p['current_uid'] = p['current_gid'] = p['current_user'] = None
        p['current_user_group'] = grp.getgrgid(pwd.getpwnam(p['current_user']).pw_gid).gr_name = None

    # Start OS-specific calls.
    if platform.system() == 'Darwin':
        try:
            p['type'] = 'Darwin'
            p['os'] = platform.system_alias(platform.system(), platform.release(), platform.mac_ver())[0] or None
            p['release'] = platform.mac_ver()[0] or None
        except (NameError, IOError) as e:
            raise Exception('Fatal error retrieving OS details on OSX.\n' + please_help_message)

    elif platform.system() == 'Linux':
        try:
            p['type'] = 'Linux'
            p['os'] = platform.linux_distribution()[0] or None
            p['release'] = platform.linux_distribution()[1] or None
        except:
            raise Exception('Fatal error retrieving OS details on Linux.\n' + please_help_message)

    elif platform.system() == 'Windows':
        try:
            p['type'] = 'Windows'
            p['os'] = str(platform.system() + platform.release()) or None
            p['release'] = platform.win32_ver()[0] or None
        except (NameError, IOError) as e:
            raise Exception('Fatal error retrieving OS details on Windows.\n' + please_help_message)

    else:
        # unknown OS. likely odd/new variant of linux/unix or windows
        # linx/unix is more important, so we default to that:
        try:
            p['os'] = platform.linux_distribution()[0] or None
            p['type'] = 'unknown'
            p['release'] = platform.linux_distribution()[1] or None
        except (NameError, IOError) as e:
            raise NotImplementedError('Could not get platform information for unknown OS.')

    return p

if __name__ == '__main__':
    print(user_env())