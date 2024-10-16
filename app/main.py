import utils

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
def run():
    keys, values = utils.get_ppopulation()
    print(keys, values)

    country = input('Ingresa el Pais: ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__=='__main__':
    run()
