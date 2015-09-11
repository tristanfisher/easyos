try:
    # Unix only modules
    import grp
    import pwd
except ImportError:
    pass
import pip
import platform
import tempfile
import os
import getpass


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
    try:
        p['python_major_version'] =  p['python_version'][0]
    except TypeError:
        p['python_major_version'] = None
    p['python_version_feature_branch'] = '.'.join(platform.python_version().split('.')[0:2]) or None
    p['python_installed_packages'] = ["%s==%s" % (pkg.key, pkg.version) for pkg in pip.get_installed_distributions()]
    p['homedir'] = os.path.join(os.path.expanduser('~'))
    p['current_user_desktop'] = os.path.join(p['homedir'], 'Desktop') or None
    p['tmp_dir'] = tempfile.gettempdir()

    # Might fail on Windows.  Open a PR or issue on github if this is important to you.
    # This should probably get cleaned up by separating the getgrpid from getpwuid, but AFAIK, it's pass/fail
    try:
        pwuid = pwd.getpwuid(os.getuid())
        p['current_uid'] = pwuid[2]
        p['current_gid'] = pwuid[3]
        p['current_user'] = pwuid[0]
        p['current_user_group'] = grp.getgrgid(pwd.getpwnam(p['current_user']).pw_gid).gr_name
    except NameError:
        try:
            p['current_user'] = getpass.getuser()
        except AttributeError:
            # User is on some unknown OS
            p['current_user'] = None
        finally:
            p['current_uid'] = p['current_gid'] = p['current_user_group'] = None

    # Start OS-specific calls.
    if platform.system() == 'Darwin':
        try:
            p['type'] = 'Darwin'
            p['os'] = platform.system_alias(platform.system(), platform.release(), platform.mac_ver())[0] or None
            p['release'] = platform.mac_ver()[0] or None
        except Exception as e:
            raise Exception('Fatal error retrieving OS details on OSX: {}'.format(e))

    elif platform.system() == 'Linux':
        try:
            dist_info = platform.linux_distribution()
            p['type'] = 'Linux'
            p['os'] = dist_info[0] or None
            p['release'] = dist_info[1] or None
        except Exception as e:
            raise Exception('Fatal error retrieving OS details on Linux: {}'.format(e))

    elif platform.system() == 'Windows':
        try:
            p['type'] = 'Windows'
            p['os'] = str(platform.system() + platform.release()) or None
            p['release'] = platform.win32_ver()[0] or None
        except Exception as e:
            raise Exception('Fatal error retrieving OS details on Windows: {}'.format(e))

    else:
        # unknown OS. likely odd/new variant of linux/unix or windows
        # linx/unix is more important, so we default to that:
        try:
            dist_info = platform.linux_distribution()
            p['os'] = dist_info[0] or None
            p['type'] = 'unknown'
            p['release'] = dist_info[1] or None
        except Exception as e:
            raise NotImplementedError('Could not get platform information for unknown OS: {}'.format(e))

    return p

if __name__ == '__main__':
    print(env())
