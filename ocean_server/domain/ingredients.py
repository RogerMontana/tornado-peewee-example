class Ingridient:
    def __init__(self, item):
        self.item = item

    def get_list(self):
        return str(self.item).split("|")
