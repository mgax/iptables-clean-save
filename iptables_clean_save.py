import re

comment = re.compile(r'^\s*#')


def clean(rulestext):
    out = []

    for line in rulestext.splitlines():
        if comment.search(line):
            continue

        out.append(line)

    return '\n'.join(out) + '\n'
