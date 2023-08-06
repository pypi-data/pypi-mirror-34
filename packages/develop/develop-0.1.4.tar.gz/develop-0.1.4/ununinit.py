# coding: utf-8

from __future__ import print_function, absolute_import, division, unicode_literals

import os
import sys

from ruamel.std.pathlib import Path

ununinitpy = '__init__.py'


def version_list(s):
    if not isinstance(s, list):
        for c in ',.':
            if c in s:
                s = s.split(c)
                break
    version = []
    for vs in s:
        try:
            vs = vs.strip()
        except AttributeError:
            pass
        try:
            version.append(int(vs))
        except ValueError:
            version.append(vs[1:-1])
    return version


def version_init_files(base_dir, show_subdirs=False):
    for root, directory_names, file_names in os.walk(base_dir):
        if not show_subdirs:
            for d in directory_names[:]:
                directory_names.remove(d)
        else:
            # anyway skipnon-interesting subdirs (before any continue)
            for d in ['.tox', '.hg', '.git', 'build', 'dist', '.cache']:
                if d in directory_names:
                    directory_names.remove(d)
        if ununinitpy not in file_names:
            continue
        full_name = os.path.join(root, ununinitpy)
        res = extract_version(full_name)
        if res:
            yield res


short_prefix = 'version_info'
prefixes = [
    ('    ' + short_prefix + '=(', ')', ', ', ""),  # NOQA PON tuple
    ('    ' + short_prefix + '=[', ']', ', ', 'PON list'),  # NOQA PON list
    ('    "' + short_prefix + '": (', ')', ', ', 'PON tuple {}'),  # NOQA PON list
    ('    "' + short_prefix + '": [', ']', ', ', 'PON'),  # NOQA JSON files
    (short_prefix + ' = (', ')', ', ', 'old'),  # NOQA old format
]


def extract_version(full_name):
    json = False
    with open(full_name) as fp:
        for line in fp:
            if 'JSON' in line:
                json = True
            for prefix, end, split, comment in prefixes:
                if line.startswith(prefix):
                    version = version_list(line[len(prefix) :].split(end, 1)[0].split(split))
                    if json:
                        comment += '/JSON'
                    return full_name, version, comment
            else:
                if line.startswith(short_prefix):
                    print('prefix', short_prefix, line, end="")
                    print('warning: version_info formatting in:', full_name)


def set_dev_lines(dev, save=False, inc_micro=False):
    """update just two line, leave rest as is"""
    initpy_path = Path(ununinitpy)
    orig_path = Path(ununinitpy + '.orig')
    if not orig_path.exists():
        initpy_path.copy(orig_path)
    lines = initpy_path.read_text().splitlines()
    prefix = prefixes[0]
    for idx, line in enumerate(lines):
        if line.startswith(prefix[0]):
            assert "__version__='" in lines[idx + 1]
            val, comment = line.split(prefix[0])[1].split(prefix[1], 1)
            val = val.split(', ')
            if ('dev' in val[-1]) == (bool(dev)):
                if dev:
                    print('dev already in version')
                else:
                    print('dev not in version')
                    return
                sys.exit(1)
            if dev:
                val.append("'dev'")
            else:
                val = val[:3]
            if inc_micro:
                val[2] = str(int(val[2]) + 1)
            print(val)
            lines[idx] = '{}{}{}{}'.format(prefix[0], ', '.join(val), prefix[1], comment)
            c2 = lines[idx + 1].split("'")
            c2[1] = '.'.join(val).replace("'", "")
            lines[idx + 1] = "'".join(c2)
            break
    else:
        raise ValueError('version info not found')
    if False:
        print(lines[idx])
        print(lines[idx + 1])
    if save:
        initpy_path.write_text('\n'.join(lines) + '\n')


set_dev = set_dev_lines
