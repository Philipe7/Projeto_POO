class Restaurant:
    def __init__(self, name, rating, distance, price, cuisine):
        self.name = name
        self.rating = int(rating)
        self.distance = float(distance)
        self.price = float(price.replace('R$', ''))
        self.cuisine = cuisine
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating):
        self.__rating = rating
        
    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, distance):
        self.__distance = distance
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def cuisine(self):
        return self.__cuisine
    @cuisine.setter
    def cuisine(self, cuisine):
        self.__cuisine = cuisine
        
        
    def __str__(self):
        return f"Nome: {self.name}, Classificação: {self.rating}, Distância: {self.distance}, Preço: {self.price}, Culinária: {self.cuisine}"
