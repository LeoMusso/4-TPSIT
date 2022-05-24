from statistics import mode
import gmaps
from ipywidgets.embed import embed_minimal_html
import os
import csv

os.chdir("G:\\Mappe")
#os.chdir("C:\\Users\\belli\\Desktop\\Monumenti_Italiani")
gmaps.configure(api_key = 'AIzaSyAi6gSnUGuagE8c9sdlwx8UotHXmXO6kK4')
comune = str(input("Inserisci il comune: "))
comune = comune.upper()
print(comune)
monumento = str(input("Inserisci un monumento: "))

with open('.\Mappa-dei-monumenti-in-Italia.csv', 'r') as file:
    reader = csv.reader(file,delimiter=";")
    dati = [(linea[0],linea[1],linea[2],linea[3],linea[8],linea[9]) for linea in reader if linea[3]==monumento and linea[0]==comune and linea[3] != ""]

for line in dati:
    latitude = float(line[4])
    longitude = float(line[5])
    monuments = [{'Nome': line[3], 'Location': (longitude, latitude), 'Comune': line[0], 'Provincia': line[1], 'Regione': line[2]}]
    plant_locations = [plant['Location'] for plant in monuments]
    info_box_template = """
    <dl>
    <dt>Nome:</dt><dd>{Nome}</dd>
    <dt>Comune:</dt><dd>{Comune}</dd>
    <dt>Provincia:</dt><dd>{Provincia}</dd>
    <dt>Regione:</dt><dd>{Regione}</dd>
    </dl>
    """
    plant_info = [info_box_template.format(**plant) for plant in monuments]

    marker_layer = gmaps.marker_layer(plant_locations, info_box_content=plant_info)
    fig = gmaps.figure(map_type = 'SATELLITE')
    fig.add_layer(marker_layer)

    embed_minimal_html('maps.html', views=[fig])