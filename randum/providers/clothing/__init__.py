import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate Indian CLothing
    """

    def clothing(self):

        clothes = ['suit','tie','shoes','belt','hat']

        result = self.random_element(clothes)

        return result

    def men_clothing(self):

        men_clothes = ['a','b']

        result = self.random_element(men_clothes)

        return result


