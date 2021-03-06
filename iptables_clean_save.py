#!/usr/bin/env python

import re

comment = re.compile(r'^\s*#')

table = re.compile(r'^\*')

chain = re.compile(r'^:(?P<name>\S+)\s+'
                   r'(?P<default>\S+)\s+'
                   r'(?P<counters>\[\d+:\d+\])\s*')

icmp_module = re.compile(r'(?<= -p icmp) -m icmp\b')
tcp_module = re.compile(r'(?<= -p tcp) -m tcp\b')
udp_module = re.compile(r'(?<= -p udp) -m udp\b')


def clean(rulestext):
    out = []

    for line in rulestext.splitlines():
        if comment.search(line):
            continue

        if table.search(line) and len(out) > 0:
            out.append('')

        if chain.search(line):
            line = re.sub(r'\s+\[\d+:\d+\]', '', line)

        for auto_module in [icmp_module, tcp_module, udp_module]:
            if auto_module.search(line):
                line = auto_module.sub('', line)

        out.append(line)

    return '\n'.join(out) + '\n'


def main():
    import subprocess
    rulestext = subprocess.check_output(['iptables-save'])
    print clean(rulestext),


if __name__ == '__main__':
    main()
