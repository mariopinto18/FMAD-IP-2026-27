
def numCities(*cities):
    """
    Recebe um conjunto de cidades e imprime os respetivos nomes
    Args: string. cidades
    """
    for i in range (len(cities)):
        print(cities[i], end =" ")
    print("\n")

numCities("Porto", "Madrid", "Roma", "Paris")
numCities("Vila do Conde")
numCities("Porto", "Lisboa", "Braga", "Vila Real", "Santarém")