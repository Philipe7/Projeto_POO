# Projeto_POO
![image](https://github.com/Philipe7/Projeto_POO/assets/131879025/74b550d6-5e9a-4cfd-98e5-cfb3cdeda107)

Aplicativo de Pesquisa de Restaurantes
Este repositório contém um aplicativo de pesquisa de restaurantes por linha de comando escrito em Python. A aplicação permite que os usuários pesquisem restaurantes com base em vários critérios, como nome, classificação, distância, preço e culinária. O código está organizado em vários arquivos para melhorar a legibilidade e a manutenção.

# Arquivos:

# main.py
O script principal que conduz a aplicação de pesquisa de restaurantes. Ele solicita a entrada do usuário para os critérios de pesquisa e exibe os 5 principais restaurantes correspondentes.

# pesquisar_criterio.py
Define classes abstratas de base para critérios de pesquisa e classes específicas de critérios (por exemplo, NameCriterio, RatingCriterio). Cada classe de critério implementa o método pesquisar, que é usado para filtrar restaurantes com base nos critérios especificados.

# restaurant_data.py
Responsável por carregar dados de restaurantes de arquivos CSV (restaurantes.csv e cozinhas.csv). Ele cria uma lista de objetos Restaurant com detalhes como nome, classificação, distância, preço e culinária.

# restaurant.py
Define a classe Restaurant, representando um restaurante com vários atributos. Inclui um método __str__ para uma representação de string amigável para o usuário de um restaurante.

# Como Usar:

# Clone o repositório:

git clone https://github.com/seu-nome-de-usuario/aplicativo-pesquisa-restaurantes.git

cd aplicativo-pesquisa-restaurantes

# Execute o script main.py:

python main.py

Siga as instruções na tela para pesquisar restaurantes com base em critérios diferentes.

# Dependências:
Python 3.x

# Contribuição:
Sinta-se à vontade para contribuir para o desenvolvimento deste aplicativo de pesquisa de restaurantes. Você pode abrir problemas, enviar solicitações de recebimento ou sugerir novos recursos.

# Licença:
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.
