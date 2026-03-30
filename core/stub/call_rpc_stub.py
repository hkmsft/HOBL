# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

def call_rpc(host, port, method, params, host_ip=None, rpc_callback_port=None, log = True, timeout = 1800, priority="Normal"):
    return ""

def _call_rpc(host, port, payload, log = True, timeout = 1800):
    return ""

def upload(host, port, source, dest):
    pass

def download(host, port, source, dest):
    pass

def plugin_load(host, port, dll_id, dll_class, dll_path):
    return ""

def plugin_call(host, port, dll_id, method, *arg):
    return ""

def plugin_screenshot(host, port, dll_id, x=0.0, y=0.0, w=1.0, h=1.0, screenIndex=0):
    return ""

def plugin_screen_info(host, port, dll_id):
    return []

def get_job_result(host, port, jobid, log=True):
    return ""
