import read_csv

def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country): # ESTE COUNTRY ES UNA VARIABLE, EN LA CUAL GUARDAREMOS EL PAIS SOLICITADO, YA SEA EN ESTE MODULO O EN OTRO 
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

if __name__ == '__main__':
  data = read_csv.read_csv('data.csv')
  country = 'Colombia'  # Cambia a cualquier país que exista en tu archivo CSV
  result = population_by_country(data, country)
  country_data = result[0]  # Primer registro del país encontrado
  get_population(country_data) 


  


