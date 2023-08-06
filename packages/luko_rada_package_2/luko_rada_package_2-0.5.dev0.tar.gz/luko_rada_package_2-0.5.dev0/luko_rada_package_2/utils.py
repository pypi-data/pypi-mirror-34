from luko_rada_package_1.rada_factories import (
    UkraineRadaFactory,
    PolandRadaFactory
)
# Functor sorts deputies by params
class Sorting:

    def __init__(self, *args):
        self.args = args

    def __call__(self, instance):
        values = []
        for value in self.args:
            values.append(getattr(instance, value))
        return values
