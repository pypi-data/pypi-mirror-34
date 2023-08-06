#!/usr/bin/env python
"""
Utility functions to support fabric 2.0 webfaction tasks on Centos 7 servers.

"""

def ensure_webfaction(c):
    if not hasattr(c, 'host') or not c.host.endswith('.webfaction.com'):
        raise ValueError('Host is not a *.webfaction.com server')
    return c.host[:c.host.find('.webfaction.com')]

def is_dir(c, remote_path):
    return c.run(
        f"""if [[ -d "{remote_path}" && ! -L "{remote_path}" ]] ; then echo "True"; fi"""
    )
