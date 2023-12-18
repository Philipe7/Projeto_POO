import csv
from restaurant import Restaurant

class RestaurantData:
    def __init__(self, restaurant_file, cuisine_file):
        self.restaurants = self.carregar_restaurants(restaurant_file, cuisine_file)

    def carregar_restaurants(self, restaurant_file, cuisine_file):
        cuisine_lista = self.carregar_cuisine_lista(cuisine_file)

        restaurants = []
        with open(restaurant_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cuisine_name = cuisine_lista.get(int(row["cuisine_id"]), "Other")
                restaurant = Restaurant(name=row["name"], rating=row["customer_rating"], distance=row["distance"], price=row["price"], cuisine=cuisine_name)
                restaurants.append(restaurant)
        return restaurants

    def carregar_cuisine_lista(self, cuisine_file):
        cuisine_lista = {}
        with open(cuisine_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cuisine_lista[int(row["id"])] = row["name"]
        return cuisine_lista
