import os
import sys
import time
import platform
import tempfile
import subprocess


def print_help():
    print("""
Usage: jennfier run <startup_command ...>

startup_command: your wsgi service startup command and options
""")


def run_master(bin, config, sock_file):
    arch = {
        'x86_64': 'amd64',
        'x86': '386',
    }[platform.machine()]
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read(config)

    log_stream  = open(cfg['JENNIFER']['log_path'], 'w+')

    path = os.path.join(bin, sys.platform, arch, 'jennifer_agent')
    process = subprocess.Popen(
        [
            path,
            config,
            sock_file,
        ],
        stdout=log_stream,
        stderr=log_stream,
    )

def run(args):
    if len(args) < 2:
        print_help()
        return
    startup_path = args[1]
    config_file = os.environ.get('JENNIFER_CONFIG_FILE')
    if config_file is None:
        raise EnvironmentError("JENNIFER_CONFIG_FILE is not set")
    config_file = os.path.join(os.getcwd(), config_file)
    if not os.path.exists(config_file):
        raise FileNotFoundError("JENNIFER_CONFIG_FILE not exist")

    root_dir = os.path.dirname(__import__('jennifer').__file__)
    bootstrap = os.path.join(root_dir, 'bootstrap')

    python_path = bootstrap
    if 'PYTHONPATH' in os.environ:
        path = os.environ['PYTHONPATH'].split(os.path.pathsep)
        if bootstrap not in path:
            python_path = os.path.pathsep.join([bootstrap] + path)
    os.environ['PYTHONPATH'] = python_path

    if not os.path.dirname(startup_path):
        for path in os.environ.get('PATH', '').split(os.path.pathsep):
            path = os.path.join(path, startup_path)
            if os.path.exists(path) and os.access(path, os.X_OK):
                startup_path = path
                break

    if not os.path.exists(startup_path):
        raise FileNotFoundError('{0} not found'.format(startup_path))

    sock = os.path.join(tempfile.gettempdir(), 'jennifer-%d.sock' % time.time())
    os.environ['JENNIFER_MASTER_ADDRESS'] = sock
    # Start!
    pid = os.fork()
    if pid > 0:  # parent process
        os.waitpid(pid, 0)
        os.execl(startup_path, *args[1:])
    else:  # child process
        run_master(os.path.join(root_dir, 'bin'), config_file, sock)
