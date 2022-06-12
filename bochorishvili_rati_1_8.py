class Flower():
    def __init__(self, name, color, price):
        self.__name=name
        self.__color=color
        self.__price=price
    def getName(self):
        return self.__name
    def getColor(self):
        return self.__color
    def getPrice(self):
        return self.__price
    def setName(self, nem):
        self.__name = nem
    def setColor(self, colo):
        self.__color = colo
    def setPrice(self, pric):
        self.__price = pric
    def print_info(self):
        return f"Flower name -> | {self.name} |, Flower color -> | {self.color} |, Flower price -> | {self.price} |"
    def __gt__(self, other):
        selfprice = self.__price
        otherprice = other.__price
        if selfprice>otherprice:
            return (f"This flower is more bougee than {other.__name}")
        else:
            return (f"This flower is a bootleg compared to {other.__name}")
flower1 = Flower("rose","red",200)
flower2 = Flower("rose2","yellow",400)
flower3 = Flower("rose3","white",600)