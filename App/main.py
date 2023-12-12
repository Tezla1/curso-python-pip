import charts
import read_csv
import utils

def run():
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda x: x["Continent"] == "South America", data))
  countries = list(map(lambda i:i["Country/Territory"], data))
  percentages = list(map(lambda i:i["World Population Percentage"], data))  
  charts.generate_pie_chart(countries, percentages) 

if __name__ == "__main__":
   run()


def run():
    data = read_csv.read_csv("data.csv")
    Country = input("Type Country: ")
    print(Country)

    result = utils.population_pais(data, Country) 

    if len(result) > 0:
        Country = result[0]
        print(Country)
        keys, values = utils.get_population(Country)
        charts.generate_bar_chart(Country["Country/Territory"], keys, values)  

if __name__ == "__main__":
   run()


'''
Cuando utilizamos name == 'main' estamos dando dualidad a cierta función para que sea 
ejecutada en dos archivos distintos.

Para ello debemos tener en cuenta que su uso esta catalogado de dos maneras:

Se puede ejecutar el archivo como un script.
Importando el codding de un archivo a otro archivo python.
Para Python, es independiente cual de las dos formas estemos utilizando el código,ya que
python define una variable especial llamada __name__ la cual contiene un string y cuyo 
resultado dependerá de la forma en como sea usada.
'''