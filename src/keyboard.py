from src.item import Item


class Mixin:

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'RU':
            self._language = "EN"
        elif self._language == 'EN':
            self._language = "RU"


class Keyboard(Item, Mixin):
    pass
