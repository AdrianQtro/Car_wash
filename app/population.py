import csv
import matplotlib.pyplot as plt


def read_csv(path):
    data = []
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        country = input('type country: ').capitalize()
        for row in reader:
            if row['Country/Territory'] == country:
                data.append({'Country/Territory': row['Country/Territory'], 
                            '2022 Population': row['2022 Population'],'2020 Population': row['2020 Population'],'2015 Population': row['2015 Population'],'2010 Population': row['2010 Population']}) 
                          
        return data

def generate_bar_char(data):
    
    if not data:
        print("No data to display!")
        return
    
    # Extraer el país y la población de los datos
    years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population']
    population =  [int(data[0][year]) for year in years]

    # Extraer y convertir cada valor uno por uno
    #population_2022 = int(data[0]['2022 Population'])
    #population_2020 = int(data[0]['2020 Population'])
    #population_2015 = int(data[0]['2015 Population'])
    #population_2010 = int(data[0]['2010 Population'])

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(years, population)
   
    # Configurar títulos y etiquetas
    ax.set_title(f'Población de {years} en 2022')
    ax.set_ylabel('Población')
    ax.set_xlabel('País')

     # Mostrar el gráfico
    plt.show()

   
if __name__ == '__main__':
    data = read_csv('app.py/population.csv')
    print(data)
    generate_bar_char(data)
    
    
    
    
