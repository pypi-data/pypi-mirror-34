import argparse
import json
import os
import sys
import platform

from pathlib import Path
from textwrap import dedent
from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

kernel_json = {
    "argv": [sys.executable, "-m", "stata_kernel", "-f", "{connection_file}"],
    "display_name": "Stata",
    "language": "stata", }


def install_my_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        # TODO: Copy any resources

        print('Installing Jupyter kernel spec')
        KernelSpecManager().install_kernel_spec(
            td, 'stata', user=user, replace=True, prefix=prefix)


def install_conf():
    if platform.system() == 'Windows':
        execution_mode = 'automation'
    else:
        execution_mode = 'console'

    stata_path = 'stata'
    if platform.system() == 'Windows':
        stata_path = win_find_path()
    conf_default = dedent(
        """\
    [stata_kernel]

    # Path to stata executable. If you type this in your terminal, it should start
    # the Stata console
    stata_path = {}

    # The manner in which the kernel connects to Stata. The default is 'console',
    # which monitors the Stata console. In the future another mode, 'automation',
    # may be added to connect with the Stata GUI on Windows and macOS computers
    execution_mode = {}

    # Directory to hold temporary images and log files
    cache_directory = ~/.stata_kernel_cache

    # Extension and format for images
    graph_format = svg
    """.format(stata_path, execution_mode))

    with open(Path('~/.stata_kernel.conf').expanduser(), 'w') as f:
        f.write(conf_default)


def win_find_path():
    import winreg
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    subkeys = [
        r'Stata15Do\shell\do\command', r'Stata14Do\shell\do\command',
        r'Stata13Do\shell\do\command', r'Stata12Do\shell\do\command']

    fpath = ''
    for subkey in subkeys:
        try:
            key = winreg.OpenKey(reg, subkey)
            fpath = winreg.QueryValue(key, None).split('"')[1]
        except FileNotFoundError:
            pass
        if fpath:
            break
    return fpath


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--user',
        action='store_true',
        help="Install to the per-user kernels registry. Default if not root.")
    ap.add_argument(
        '--sys-prefix',
        action='store_true',
        help="Install to sys.prefix (e.g. a virtualenv or conda env)")
    ap.add_argument(
        '--prefix',
        help="Install to the given prefix. "
        "Kernelspec will be installed in {PREFIX}/share/jupyter/kernels/")
    args = ap.parse_args(argv)

    if args.sys_prefix:
        args.prefix = sys.prefix
    if not args.prefix and not _is_root():
        args.user = True

    install_my_kernel_spec(user=args.user, prefix=args.prefix)
    install_conf()


if __name__ == '__main__':
    main()
