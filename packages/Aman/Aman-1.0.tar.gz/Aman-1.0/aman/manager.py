''' Aliases are managed here'''

from . import storage
from .alias import Alias

from .exceptions import (
    AliasNotFoundError,
    AliasExistsError,
    InvalidAliasValueError,
)

class Manager():
    def __init__(self):
        self.aliases = []
        for name, value in storage.load_aliases():
            self.aliases.append(Alias(name, value))

    def add(self, name, value):
        self.aliases.append(Alias(name, value))

        self.save()

    def edit(self, name, value):
        if not value:
            raise InvalidAliasError
        alias = self.get_alias(name)

        if alias:
            alias.value = value

        self.save()

    def modify(self, current_name, new_name):
        existing_alias = self.get_alias(new_name)
        if existing_alias:
            raise AliasExistsError

        alias = self.get_alias(current_name)
        alias.name = new_name

        self.save()

    def delete(self, name):
        alias = self.get_alias(name)
        if alias:
          self.aliases.remove(alias)

        self.save()

    def get_all(self):
        return self.aliases

    def get_alias(self, name):
        try:
            return list(filter(lambda a: a.name == name, self.aliases))[0]
        except IndexError:
            raise AliasNotFoundError

    def save(self):
        storage.save_aliases([(alias.name, alias.value) for alias in self.aliases])
        pass
