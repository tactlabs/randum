import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate Vehicles
    """

    def vehicles(self):
        vehicle_items = ["Auto Rickshaw",
        "Bike",
        "Bullock Cart ",
        "Bus",
        "Car",
        "Fire Engine",
        "Jeep",
        "Lorry ",
        "Scooter",
        "Tractor ",
        "Horse carriage ",
        "ship",
        "Minibus ",
        "Road grader",
        "Sidecar",
        "Snowplow",
        "Aerial tramway",
        "Airplane",
        "Aircraft",
        "Ambulance",
        "Baby carriage ",
        "Pram",
        "Hot-air balloon",
        "Bulldozer",
        "Bicycle",
        "Boat",
        "Carriage",
        "Cement mixer",
        "Crane",
        "Camper van",
        "Caravan",
        "Dump truck",
        "Delivery van",
        "Fire engine",
        "Forklift",
        "Helicopter",
        "Motorcycle",
        "Mountain bike",
        "Moped",
        "Police car",
        "Rowboat",
        "Skateboard",
        "Subway",
        "Taxi",
        "cab",
        "Tractor",
        "Train",
        "Truck",
        "Tram ",
        "Streetcar",
        "Van"
        ]

        result = self.random_element(vehicle_items)

        return result
