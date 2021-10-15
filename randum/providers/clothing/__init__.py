import itertools

from .. import BaseProvider


class Provider(BaseProvider):
    """
    To generate Indian CLothing
    """

    def simple_profile(self, sex=None):
        """
        Generates a basic profile with personal informations
        """
        SEX = ["F", "M"]
        if sex not in SEX:
            sex = self.random_element(SEX)
        if sex == 'F':
            name = self.generator.name_female()
        elif sex == 'M':
            name = self.generator.name_male()
        return {
            "username": self.generator.user_name(),
            "name": name,
            "sex": sex,
            "address": self.generator.address(),
            "mail": self.generator.free_email(),
            "birthdate": self.generator.date_of_birth(),
        }

    def clothing(self, fields=None, sex=None):
      
        if fields is None:
            fields = []

        d = {
            "job": self.generator.job(),
            "company": self.generator.company(),
            "ssn": self.generator.ssn(),
            "residence": self.generator.address(),
            "current_location": (self.generator.latitude(), self.generator.longitude()),
            "blood_group": "".join(self.random_element(list(itertools.product(["A", "B", "AB", "O"], ["+", "-"])))),
            "website": [self.generator.url() for _ in range(1, self.random_int(2, 5))],
        }

        d = dict(d, **self.generator.simple_profile(sex))
        # field selection
        if len(fields) > 0:
            d = {k: v for k, v in d.items() if k in fields}

        return d
