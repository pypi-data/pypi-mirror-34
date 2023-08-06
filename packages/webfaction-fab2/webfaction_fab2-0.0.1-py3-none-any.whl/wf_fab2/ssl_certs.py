#!/usr/bin/env python
import re
import os
import logging
import time
import dns.resolver

# set to '--test' to issue certiicates against letsencrypt staging environment
ACME_MODE='' #--test'

def install_acme(c, dest):
    logging.debug('install_acme')
    if not is_dir(c, dest):
        c.run(f'mkdir -p {dest}')
    with c.cd(dest):
        install_dir = 'acme.sh'
        if not is_dir(c, install_dir):
            c.run("git clone 'https://github.com/Neilpang/acme.sh.git'")
        with c.cd(install_dir):
            c.run('./acme.sh --install')
            c.run('./acme.sh --upgrade  --auto-upgrade')


def uninstall_acme(c, dest):
    logging.debug('uninstall_acme')
    if not is_dir(c, dest):
        raise ValueError(f'Acme not installed at {dest}')
    with c.cd(dest):
        install_dir = 'acme.sh'
        if not is_dir(c, install_dir):
            raise ValueError(f'Acme not installed at {install_dir}')
        with c.cd(install_dir):
            c.run('./acme.sh --uninstall')


def clean_acme_line(line):
    logging.debug(f'clean_acme_line {line}')
    line = line.replace('\x1b[1;31;40m', '')
    line = line.replace('\x1b[1;31;32m', '')
    line = line.replace('\x1b[0m', '')
    return line


def issue_certificate(
        c, server, session_id, primary_domain, *multiple_domains
):
    logging.debug('issue certificate')
    command = f'.acme.sh/acme.sh --issue --dns --yes-I-know-dns-manual-mode-enough-go-ahead-please {ACME_MODE} -d {primary_domain}'
    result = c.run(
        command + ' '.join(
            [f'-d {d}' for d in multiple_domains]
        ),
        warn=True
    )
    lines = [l[31:] for l in result.stdout.split('\n')]
    existing_domains = {
        d['domain']: d for d in server.list_domains(session_id)
    }
    records = []
    while len(lines) > 0:
        line = clean_acme_line(lines.pop(0))
        logging.debug('lines {} "{}"'.format(len(lines), line))
        if line == 'Add the following TXT record:':
            line = clean_acme_line(lines.pop(0))
            newsubdom = re.search(
                r"(.+?): '(.+?)'", line
            ).groups()[1]
            logging.debug('adding {}'.format(newsubdom))
            sd = None
            dn = None
            ed = list(existing_domains.keys())
            while sd is None and dn is None:
                ted = ed.pop()
                tedidx = newsubdom.find(ted)
                if len(ted) + newsubdom.find(ted) == len(newsubdom):
                    sd = newsubdom[:tedidx - 1]
                    dn = ted
            create_d = existing_domains[ted]
            create_d['subdomains'].append(sd)
            create_domain(
                server,
                session_id,
                ted,
                *create_d['subdomains']
            )
            # Add DNS override
            line = clean_acme_line(lines.pop(0))
            txt_value = re.search(r"(.+?): '(.+?)'", line).groups()[1]
            logging.info('txt_value {} -- {}'.format(txt_value, line))
            if txt_value not in get_txt_records_for(newsubdom):
                create_dns_override(
                    server,
                    session_id,
                    newsubdom,
                    '',
                    '',
                    '',
                    '',
                    txt_value,
                    '',
                    ''
                )
            records.append((newsubdom, txt_value))
    return records


def get_txt_records_for(domain):
    logging.debug(f'get_txt_records_for {domain}')
    try:
        records = [
            str(n).strip('"') for n in dns.resolver.query(domain, 'TXT')
        ]
    except dns.resolver.NXDOMAIN:
        records = []
    except dns.resolver.NoAnswer:
        records = []
    return records


def wait_dns_update(records):
    logging.debug('wait_dns_update')
    while len(records) > 0:
        domain, txtrecord = records.pop()
        answers = get_txt_records_for(domain)
        count = 0
        while txtrecord not in answers:
            time.sleep(60)
            count += 1
            if count > 1:
                print('waited {} minutes for DNS propagation'.format(count))
                answers = get_txt_records_for(domain)
                logging.debug(answers)


def remove_txt_records(server, session_id, records, delete_domains=False):
    logging.debug('remove_txt_records')
    for r in records:
        delete_dns_override(
            server,
            session_id,
            r[0],
            '',
            '',
            '',
            '',
            r[1],
            '',
            ''
        )
        

def renew_certificate(c, server, session_id, primary_domain, force=False):
    logging.debug('renew_certificate')
    force = '' if not force else '--force'
    command = '.acme.sh/acme.sh --renew {} -d {} {ACME_MODE} --yes-I-know-dns-manual-mode-enough-go-ahead-please'.format(
        force, primary_domain
    )
    result = c.run(command, warn=True)
    return result.exited


def install_certificate(c, server, session_id, primary_domain):
    logging.debug('install_certificate')
    certfolder = os.path.join('.acme.sh', primary_domain)
    certificate = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, '{}.cer'.format(primary_domain))
            )
        )
    )
    private_key = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, '{}.key'.format(primary_domain))
            )
        )
    )
    intermediates = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, 'fullchain.cer')
            )
        )
    )
    resp = create_or_update_certificate(
        server,
        session_id,
        primary_domain,
        certificate,
        private_key,
        intermediates,
    )
    return resp

def create_or_update_certificate(
        server,
        session_id,
        primary_domain,
        certificate,
        private_key,
        intermediates,
        ):
    logging.debug('create_or_update_certificate')
    name = re.sub(r'[^a-z0-9A-Z]', '', primary_domain)
    current_certificates = server.list_certificates(session_id)
    for ccert in current_certificates:
        if ccert['name'] == name:
            return server.update_certificate(
                session_id,
                name,
                certificate,
                private_key,
                intermediates,

            )
    return server.create_certificate(
        session_id,
        name,
        certificate,
        private_key,
        intermediates,
    )

def create_dns_override(
        server,
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
):
    logging.debug('create_dns_override')
    result = server.create_dns_override(
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
    )
    return result


def delete_dns_override(
        server,
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
):
    logging.debug('delete_dns_override')
    result = server.delete_dns_override(
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
    )
    return result


def create_domain(
        server,
        session_id,
        domain_name,
        *subdomains
):
    logging.debug('create_domain')
    result = server.create_domain(
        session_id,
        domain_name,
        *subdomains
    )
    return result


def delete_domain(
        server,
        session_id,
        domain,
        *subdomains
):
    logging.debug('delete_domain')
    try:
        return server.delete_domain(session_id, domain, *subdomains)
    except Fault as e:
        logging.error(e)



