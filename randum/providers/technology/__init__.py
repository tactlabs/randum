import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate Technology
    """

    def technology(self):

        tech = ['5G Technology','Internet of Behaviours(IoB)','DevSecOps','Intelligent Process Automation(IPA)','Tactile VR',
                'Big Data Analytics','Human Augmentation','Everything-as-a-Service(XaaS)','Cybersecurity','Data Science',
                'Machine Learning','Robotic Process Automation (RPA)','Edge Computing','Quantum Computing','Virtual Reality and Augmented Reality',
                'Blockchain','Internet of Things (IoT)','Wearables and augmented humans','Big Data and augmented analytics','Intelligent spaces and smart places',
                'Cloud and edge computing','Digitally extended realities',' Digital twins','Natural language processing','Voice interfaces and chatbots',
                'Computer vision and facial recognition','Robots and cobots','Autonomous vehicles',' Genomics and gene editing','Machine co-creativity and augmented design',
                'Digital platforms', 'Deep Learning', 'Voice Technology', 'LOT', 'Biometrics',
                'Robotics', 'NFT', 'Computer Network', 'Serverless computing', '3D printing',
                'Drones', 'Cognitive Computing', 'DevOps', 'Internet of behaviors (IoB)', 'Human augmentation ',
                'Distributed cloud'
               ]

        result = self.random_element(tech)

        return result
