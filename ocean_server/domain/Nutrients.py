
from ocean_server.domain.object import Object


class Nutrients(Object):
    def __init__(self, cal, protein, fat, carbs):
        self.cal = cal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
