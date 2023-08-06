import os

# Storage file settings
HOME_DIR = os.getenv('HOME')
FILE_NAME = 'aliases'
FILE_PATH = '{}/.aman/{}'.format(HOME_DIR, FILE_NAME)

# CLI settings
HELP_TEXT = 'Alias manager for shell lovers'
USAGE_TEXT = '''

USAGE:

  To add / edit an alias: 
  <name>="<value"

  list       List all aliases
  rm         Remove an alias
  --help     Show help
  --version  Show version number'''

COLORS = {
	'SUCCESS': '\033[0;32m',
	'ERROR': '\033[0;31m'
}
