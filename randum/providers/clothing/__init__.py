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

        clothes = ['Sarees', 'Kurta', 'Lehenga Choli', 'Salwar Kameez', 'Churidar Suits', 'One Piece Indian Gowns', 'Front Slit Gown',
        'Georgette Gown', 'Kurta Pyjama', 'Patiala Suit', 'Dhoti Suit', 'Mekhela Sador', 'Ghagras', ' Taranga',
        'Mundum Neriyathum', 'Shirt', 'Lungi', 'Langa Voni', 'odhni', 'Dhavani', 'Chaniya Choli',
        'Gurdam', 'Lugda', 'Nav Vari', ' Angami dress', 'Salwars', 'Dhara dress', 'Phanek',
        'Dhardia dress', ' Rignai', 'Puan dress', 'Sanatpuri style dress', 'Jawahar topi', 'mirjai  dress', ' achkan dress',
        'Sherwani', 'Mekhela chador', 'Salwar Kameez', 'Anarkali Suit'
        ]

        result = self.random_element(clothes)

        return result


