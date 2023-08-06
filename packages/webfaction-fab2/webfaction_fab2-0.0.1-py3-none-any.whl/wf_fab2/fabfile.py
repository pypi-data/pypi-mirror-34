#!/usr/bin/env python
from fabric import task
import os
import logging
from wf_fab2.util import ensure_webfaction, is_dir
from wf_fab2.connection import start_session
from wf_fab2.websites import website_checker
from wf_fab2.ssl_certs import (
    wait_dns_update, renew_certificate, remove_txt_records,
    install_certificate, issue_certificate, install_acme,
    uninstall_acme
)

logging.basicConfig(
    filename=os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        'fab.log'
    ),
    level=logging.DEBUG
)



@task
def acme_install(c, source_directory='src'):
    "Install acme.sh for Letsencrypt certificates on a webfaction host."
    ensure_webfaction(c)
    install_acme(c, source_directory)

@task
def acme_uninstall(c, source_directory='src'):
    "Uninstall acme.sh from a webfaction host."
    ensure_webfaction(c)
    uninstall_acme(c, source_directory)

@task
def secure_domains(
        c,
        account,
        primary_domain,
        *multiple_domains
):
    """ Validate, generate and install Letsencrypt certificates. """
    machine = ensure_webfaction(c)
    server, session_id = start_session(account, machine)
    records = issue_certificate(
        c, server, session_id, primary_domain, *multiple_domains
    )
    wait_dns_update(records)
    renew_certificate(c, server, session_id, primary_domain)
    remove_txt_records(server, session_id, records)
    logging.debug('removed records')
    install_certificate(c, server, session_id, primary_domain)
    logging.debug('installed')

@task
def check_websites(
        c,
        account,
):
    """ Check http response mode of all configured websites. """
    machine = ensure_webfaction(c)
    server, session_id = start_session(account, machine)
    website_checker(server, session_id, machine)
