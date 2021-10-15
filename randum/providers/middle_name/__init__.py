import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate different middle names for people

    """

    def middle_name(self):

        middle_names = ['Jai','Jeeva','William','David','laligam','Mandi','Jey']

        result = self.random_element(middle_names)

        return result

    def girl_middle_names(self):

        g_middle_names = ['Jay','Iris','Ameera','Anisha','Amori','Betty','Rumble','Honey','Sunny']

        result = self.random_element(g_middle_names)

        return result

    


    


