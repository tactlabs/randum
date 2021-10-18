import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate different middle names for people

    """

    def restaurants(self):

        restaurant_places = ["Indian Accent", "Travertino Restaurant", "Bukhara Restaurant",
                            "Koh Restaurant", "Zen Restaurant", "Villa 39 Restaurant",
                            "Karavalli Restaurant", "Italia Restaurant", "Wharf Restaurant",
                            "Sakura Restaurant", "Paasha Restaurant", "Barbeque Nation",
                            "Udupi International Restaurant", "Roma Restaurant",
                            "6 Ballygunge Place", "The Table", "The Embassy", "The Fatty Bao",
                            "Ginger House", "Hotel Saravana Bhavan", "Indigo", "Lodi — The Garden Restaurant",
                            "Masala Library", "The Raintree", "Toast & Tonic", "The Water Front",
                            "Villa Shanti", "Trishna Restaurant", " Thalassa", "Sheesh Mahal",
                            "Dindigul Thalappakatti", "Olive Qutub", "Artusi Ristorante", "Bomra's",
                            "Masque", "Slink & Bardot", "Megu Restaurant", "O Pedro", "Bastian",
                            "The Black Sheep Bistro", "Gunpowder", "La Plage", "The China Kitchen",
                            "Annamaya", "Yauatcha", "Mocambo", "Place to Bee", "Dimora",
                            "The Spice-Hablis", "Oasis Restaurant", "Tovo Infusion", "L'attitude 49"]

        result = self.random_element(restaurant_places)

        return result

  

    


    


