''' This module handles storing and retrieval of aliases from a file'''

import re
from . import config

ALIAS_DEFINITION_REGEX = r'\s*alias (\w+)=[\'\"](.+)[\'\"]'
ALIAS_SAVING_FORMAT = '\nalias {name}="{value}"'

def load_aliases():
    alias_pairs = []

    with open(config.FILE_PATH) as f:
        lines = f.readlines()

    for line in lines:
        m = re.match(ALIAS_DEFINITION_REGEX, line)
        if m:
            alias_pairs.append(m.groups())
    return alias_pairs

def save_aliases(alias_pairs):
    """ Write aliases to a file """
    lines = []
    with open(config.FILE_PATH, 'w') as f:
        for name, value in alias_pairs:
            lines.append(ALIAS_SAVING_FORMAT.format(name=name, value=value))
        f.writelines(lines)
