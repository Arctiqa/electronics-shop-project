from src.item import Item


class Mixin:

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'RU':
            self.language = "EN"
        elif self.language == 'EN':
            self.language = "RU"


class Keyboard(Item, Mixin):

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in ['EN', 'RU']:
            self._language = value
