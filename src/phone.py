from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__name = name
        self.number_of_sim = int(number_of_sim)
        if isinstance(number_of_sim, int) and number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def name(self):
        return self.__name
