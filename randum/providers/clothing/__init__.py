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

    def indian_clothing(self):

        clothes = ['Sarees', 'Kurta', 'Lehenga Choli', 'Salwar Kameez', 'Churidar Suits', 
        'Georgette Gown', 'Kurta Pyjama', 'Patiala Suit', 'Dhoti Suit', 'Mekhela Sador', 
        'Mundum Neriyathum', 'Shirt', 'Lungi', 'Langa Voni', 'odhni', 'Dhavani', 
        'Gurdam', 'Lugda', 'Nav Vari', ' Angami dress', 'Salwars', 'Dhara dress', 'Phanek',
        'Dhardia dress', ' Rignai', 'Puan dress', 'Sanatpuri style dress', 'Jawahar topi', 
        'Sherwani', 'Mekhela chador', 'Salwar Kameez', 'Anarkali Suit'
        'One Piece Indian Gowns', 'Front Slit Gown', 'Ghagras', ' Taranga',
        'mirjai  dress', ' achkan dress', 'Chaniya Choli'
        ]

        result = self.random_element(clothes)

        return result


