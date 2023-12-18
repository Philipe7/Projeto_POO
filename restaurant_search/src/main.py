from time import sleep
from restaurant_data import RestaurantData
from pesquisar_criterio import NameCriterio, RatingCriterio, DistanceCriterio, PriceCriterio, CuisineCriterio

class RestaurantPesquisar:
    def __init__(self, restaurant_data):
        self.restaurant_data = restaurant_data

    def pesquisar(self, Criterio_list):
        resultados = [restaurant for restaurant in self.restaurant_data.restaurants if all(Criterio.pesquisar(restaurant) for Criterio in Criterio_list)]
        resultados.sort(key=lambda r: (r.distance, r.rating, -r.price))
        return resultados[:5]

if __name__ == "__main__":
    data = RestaurantData("data/restaurants.csv", "data/cuisines.csv")
    pesquisar_rest = RestaurantPesquisar(data)

    while True:
        print("------------------------------------------------")
        print("| SEJA BEM-VINDO A PESQUISA DE RESTAURANTES!   |")
        print("|    Faça sua pesquisa segundo a ordem:        |")
        print("------------------------------------------------")
        print("| 1- Buscar restaurante pelo Nome              |")
        print("| 2- Buscar restaurante pela Classificação     |")
        print("| 3- Buscar restaurante pela Distância         |")
        print("| 4- Buscar restaurante pelo Preço             |")
        print("| 5- Buscar restaurante pela Culinária         |")
        print("| 0- Sair                                      |")
        print("------------------------------------------------")
        print()

        opcao = input("Escolha o número do critério de busca (1-5) ou 0 para sair: ")

        if opcao == '0':
            print("Programa Encerrado.")
            break

        try:
            opcao = int(opcao)
            if opcao < 1 or opcao > 5:
                raise ValueError("Opção inválida. Por favor, escolha um número entre 1 e 5.")
        except ValueError:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
            continue

        Criterio_list = []

        if opcao == 1:
            name = input("Digite o nome do restaurante: ")
            Criterio_list.append(NameCriterio(name))
        elif opcao == 2:
            customer_rating = input("Digite a classificação do restaurante: ")
            Criterio_list.append(RatingCriterio(int(customer_rating)))
        elif opcao == 3:
            distance = input("Digite a distância do restaurante: ")
            Criterio_list.append(DistanceCriterio(float(distance)))
        elif opcao == 4:
            price = input("Digite o preço do restaurante: ")
            Criterio_list.append(PriceCriterio(float(price)))
        elif opcao == 5:
            cuisine = input("Digite o nome da culinária do restaurante: ")
            Criterio_list.append(CuisineCriterio(cuisine))

        add_Criterio = input("Deseja adicionar mais critérios? (S para Sim, qualquer outra tecla para não): ")
        while add_Criterio.upper() == 'S':
            opcao = input("Escolha o número do critério adicional (1-5) ou 0 para finalizar: ")

            if opcao == '0':
                break

            try:
                opcao = int(opcao)
                if opcao < 1 or opcao > 5:
                    raise ValueError("Opção inválida. Por favor, escolha um número entre 1 e 5.")
            except ValueError:
                print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
                continue

            if opcao == 1:
                name = input("Digite o nome adicional do restaurante: ")
                Criterio_list.append(NameCriterio(name))
            elif opcao == 2:
                customer_rating = input("Digite a classificação adicional do restaurante: ")
                Criterio_list.append(RatingCriterio(int(customer_rating)))
            elif opcao == 3:
                distance = input("Digite a distância adicional do restaurante: ")
                Criterio_list.append(DistanceCriterio(float(distance)))
            elif opcao == 4:
                price = input("Digite o preço adicional do restaurante: ")
                Criterio_list.append(PriceCriterio(float(price)))
            elif opcao == 5:
                cuisine = input("Digite o nome adicional da culinária do restaurante: ")
                Criterio_list.append(CuisineCriterio(cuisine))

            add_Criterio = input("Deseja adicionar mais critérios? (S para Sim, qualquer outra tecla para não): ")

        resultados = pesquisar_rest.pesquisar(Criterio_list)

        if resultados:
            print("Resultados da pesquisa:")
            print()
            for result in resultados:
                print(result)
            print()
            sleep(2)
