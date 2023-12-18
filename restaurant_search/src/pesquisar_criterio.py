from abc import ABC, abstractmethod

class PesquisarCriterio(ABC):
    @abstractmethod
    def pesquisar(self, restaurant):
        pass

class NameCriterio(PesquisarCriterio):
    def __init__(self, name):
        self.name = name.lower()

    def pesquisar(self, restaurant):
        return self.name in restaurant.name.lower()

class RatingCriterio(PesquisarCriterio):
    def __init__(self, rating):
        self.rating = int(rating)

    def pesquisar(self, restaurant):
        return restaurant.rating >= self.rating

class DistanceCriterio(PesquisarCriterio):
    def __init__(self, distance):
        self.distance = float(distance)

    def pesquisar(self, restaurant):
        return restaurant.distance >= self.distance

class PriceCriterio(PesquisarCriterio):
    def __init__(self, price):
        self.price = float(str(price).replace('R$', ''))

    def pesquisar(self, restaurant):
        return restaurant.price <= self.price

class CuisineCriterio(PesquisarCriterio):
    def __init__(self, cuisine):
        self.cuisine = cuisine.lower()

    def pesquisar(self, restaurant):
        return self.cuisine in restaurant.cuisine.lower()

