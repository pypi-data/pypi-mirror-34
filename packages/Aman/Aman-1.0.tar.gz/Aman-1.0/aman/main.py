''' Alias manager for users of Unix shells'''

import sys
import re
import pkg_resources

from .manager import Manager
from .exceptions import AliasNotFoundError
from .config import HELP_TEXT, USAGE_TEXT, COLORS

manager = Manager()

# Valid command regex
ALIAS_NAME = r'([\w_-]+)'
ALIAS_VALUE = r'(.+)'
ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE
DELETE = r'^rm '+ALIAS_NAME
LIST = r'^(list|ls)$'

def main(args_str):
	if args_str == '--help' or not args_str:
		default('{}{}'.format(HELP_TEXT, USAGE_TEXT))
		return

	if args_str == '--version':
		default(pkg_resources.get_distribution('aman').version)
		return

	for cmd, fn in functions.items():
		match = re.match(cmd, args_str)
		if match:
			fn(match)
			return

	error('Invalid command: {}'.format(args_str.split(' ')[0]))
	default(USAGE_TEXT)

def add_alias(match):
	name = match.group(1)
	value = match.group(2)

	try:
		alias = manager.get_alias(name)
	except AliasNotFoundError:
		manager.add(name, value)
		success('Alias added successfully.')
	else:
		action = prompt('Alias already exists. Edit? (y/n): ');
		if not action in 'yn':
			error('Invalid option: {}'.format(action))
		elif action == 'y':
			manager.edit(name, value)
			success('Alias updated.')

def delete_alias(match):
	name = match.group(1)
	manager.delete(name)

def list_aliases(*args):
	aliases = manager.get_all()

	for alias in aliases:
		success('{} {:<30} -> {}'.format(COLORS['SUCCESS'], alias.name, alias.value))

def prompt(message):
	if sys.version_info.major == 3:
		action = input(message)
	else:
		action = raw_input(message)
	return action

def default(message):
	print(message)

def success(message):
	print('{}{}\033[1;m'.format(COLORS['SUCCESS'], message))

def error(message):
	print('{}{}\033[1;m'.format(COLORS['ERROR'], message))

functions = {
	ADD: add_alias,
	DELETE: delete_alias,
	LIST: list_aliases
}
main(' '.join(sys.argv[1:]))