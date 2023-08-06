from collections import namedtuple
import sys
import os
import subprocess

from dlvm.common.utils import ExcInfo
from dlvm.common.configure import cfg
from dlvm.wrapper.hook import build_hook_list, run_pre_hook, \
    run_post_hook, run_error_hook
from dlvm.wrapper.local_ctx import backend_local


CmdContext = namedtuple(
    'CmdContext', [
        'req_ctx', 'cmd', 'timeout', 'check', 'inp'])


cmd_hook_list = build_hook_list('cmd_hook')


class CmdPath():

    default_paths = [
        '/bin', '/usr/bin', '/usr/local/bin',
        '/sbin', '/usr/sbin', '/usr/local/sbin',
    ]

    def __init__(self, paths):
        self.paths = []
        for path in paths:
            self.paths.append(path)
        for path in self.default_paths:
            self.paths.append(path)
        self.path_dict = {}
        self.path_dict['dm_dd'] = os.path.join(
            sys.prefix, 'bin/dlvm_bin/dm_dd')
        self.path_dict['pdata_tools'] = os.path.join(
            sys.prefix, 'bin/dlvm_bin/pdata_tools')

    def get_path(self, name):
        if name not in self.path_dict:
            for path in self.paths:
                full_path = os.path.join(path, name)
                if os.path.isfile(full_path):
                    self.path_dict[name] = full_path
                    break
        return self.path_dict[name]


cmd_path = CmdPath(cfg.getlist('cmd', 'path_list'))
cmd_timeout = cfg.getint('cmd', 'timeout')
sudo_path = cmd_path.get_path('sudo')


CmdResult = namedtuple(
    'CmdResult', ['stdout', 'stderr', 'returncode'])


def run_cmd(cmd, check=True, inp=None):
    req_ctx = backend_local.req_ctx
    real_cmd = [sudo_path]
    real_cmd.append(cmd_path.get_path(cmd[0]))
    real_cmd.extend(cmd[1:])
    hook_ctx = CmdContext(
        req_ctx, real_cmd, cmd_timeout, check, inp)
    hook_ret_dict = run_pre_hook(
        'cmd', cmd_hook_list, hook_ctx)
    try:
        if isinstance(inp, str):
            inp = inp.encode('utf-8')
        cp = subprocess.run(
            real_cmd, input=inp,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=cmd_timeout, check=False)
        r = CmdResult(cp.stdout, cp.stderr, cp.returncode)
        if check is True and r.returncode != 0:
            raise Exception('returncode is not zero: %s' % str(r))
    except Exception:
        etype, value, tb = sys.exc_info()
        exc_info = ExcInfo(etype, value, tb)
        run_error_hook(
            'cmd', cmd_hook_list, hook_ctx, hook_ret_dict, exc_info)
        raise
    else:
        run_post_hook(
            'cmd', cmd_hook_list,
            hook_ctx, hook_ret_dict, r)
        return r
