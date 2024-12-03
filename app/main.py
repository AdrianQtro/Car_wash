import utils
import read_csv
import charts
import json
'''import pandas as pd'''

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    print(result)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        print(labels, values)  # Verificar datos antes de generar el gráfico
        charts.generate_bar_chart(country['Country'],labels, values)
        print(f'Bar chart saved successfully {country["Country"]}!')
    else:
        print(f'No data found for country: {country}')

if __name__ == '__main__':
    data = read_csv.read_csv('data.csv')
    run()