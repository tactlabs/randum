import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate different food items

    """

    def food(self):

        food_items = ['Paneer','Dhokla','Noodles','momos','sushi']

        result = self.random_element(food_items)

        return result

    def indian_food(self):

        indian_items = ['roti','rasam','dosa','idli','kurma','naan','sambhar']

        result = self.random_element(indian_items)

        return result

    def italian_food(self):

        italian_items = ['pizza','pasta','meatballs','soup','brushchetta','baguette','lasagna']

        result = self.random_element(italian_items)

        return result


    


