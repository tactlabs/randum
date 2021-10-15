import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate different middle names for people

    """

    def middle_name(self):

        middle_names = ['Jai','Jeeva','William','David','laligam','Mandi','Jey','Anika',
                        'Bhagya:','Chahna','Gana','Henry','Robert','Alexander','Lucas','Maximus',
                        'Ryder','Angel','Beven','Zion','Tristan','Brixton','Thatcher','Kenji']

        result = self.random_element(middle_names)

        return result

    def girl_middle_names(self):

        g_middle_names = ['Jay','Iris','Izna','Anisha','Amori','Betty','Rumble','Honey','Sunny',
                          'Kaia','Ladli','Mahika','Mirai','Nira','Omala','Prisha','Ruhi','Salena',
                          'Suvarna','Taara','Udaya','Vahini','Zaina','Vidya','Urja','Sneha','Rina']

        result = self.random_element(g_middle_names)

        return result

    


    


