import gmaps
from ipywidgets.embed import embed_minimal_html
import os
import csv
import webbrowser
import math
import time

def stampaProvince(dati):
    str = ''
    for line in dati:
        if line[1] != str:
            str = line[1]
            print('- ' + line[1])

def stampaMonumenti(datiProvincia):
    for line in datiProvincia:
        print("- " + line[3])

os.chdir("G:\\Mappe")
#os.chdir("C:\\Users\\belli\\Desktop\\Monumenti_Italiani")
gmaps.configure('AIzaSyAi6gSnUGuagE8c9sdlwx8UotHXmXO6kK4')
fig = gmaps.figure()
itis = (44.37841102932401, 7.52754954405035)

regione = str(input("Inserisci una regione: "))

with open('.\Mappa-dei-monumenti-in-Italia.csv', 'r') as file:
    reader = csv.reader(file,delimiter=";")
    datiregione = [(linea[0], linea[1], linea[2], linea[3], float(linea[8]), float(linea[9])) for linea in reader if linea[2] == regione and linea[3] != ""]

stampaProvince(datiregione)
     
provincia = input("Inserisci una provincia: ")

with open('.\Mappa-dei-monumenti-in-Italia.csv', 'r') as file:
    reader = csv.reader(file,delimiter=";")
    datiprovincia = [(linea[0], linea[1], linea[2], linea[3], float(linea[8]), float(linea[9])) for linea in reader if linea[1] == provincia and linea[3] != ""]

for line in datiprovincia:
    latitude = line[4]
    longitude = line[5]
    monuments = [{'Nome': line[3], 'Location': (longitude, latitude), 'Comune': line[0]}]
    plant_locations = [plant['Location'] for plant in monuments]
    info_box_template = """
    <dl>
    <dt>Nome:</dt><dd>{Nome}</dd>
    <dt>Comune:</dt><dd>{Comune}</dd>
    </dl>
    """
    plant_info = [info_box_template.format(**plant) for plant in monuments]
    marker_layer = gmaps.marker_layer(plant_locations, info_box_content=plant_info)
    fig.add_layer(marker_layer)

stampaMonumenti(datiprovincia)
monumento = str(input("Inserire il monumento: "))
distanze=[(math.dist(itis, (elemento[5], elemento[4])))*100 for elemento in datiprovincia if elemento[3] == monumento]
print(datiprovincia[0][0] + str(distanze))

time.sleep(10)
embed_minimal_html('maps.html', views=[fig])  
webbrowser.open_new_tab('maps.html')