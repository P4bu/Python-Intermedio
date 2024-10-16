import utils
keys, values = utils.get_ppopulation()
print(keys, values)


data = [
    {
        'country': 'Chile',
        'population': 500
    },
    {
        'country': 'Colombia',
        'population': 700
    }
]
country = input('Ingresa el Pais: ')

result = utils.population_by_country(data, country)
print(result)