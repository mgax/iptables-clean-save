import re

comment = re.compile(r'^\s*#')

chain = re.compile(r'^:(?P<name>\S+)\s+'
                   r'(?P<default>\S+)\s+'
                   r'(?P<counters>\[\d+:\d+\])\s*')


def clean(rulestext):
    out = []

    for line in rulestext.splitlines():
        if comment.search(line):
            continue

        if chain.search(line):
            line = re.sub(r'\s+\[\d+:\d+\]', '', line)

        out.append(line)

    return '\n'.join(out) + '\n'
