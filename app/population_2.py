import csv
import matplotlib.pyplot as plt

def read_csv(path):
    percentage = []
    countries = []
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        reader = list(filter(lambda item: item['Continent']=='South America',reader))
        """ years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population']
            population =  [int(data[0][year]) for year in years]
        """
        for row in reader:
            percentage.append(float(row['World Population Percentage']))
            countries.append(row['Country/Territory'])
    return percentage,countries

def generate_pie_char(percentage,countries):
  fig, ax = plt.subplots()
  ax.pie(percentage,labels=countries)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
    percentage,countries = read_csv('app.py/population.csv')
    generate_pie_char(percentage,countries)
    