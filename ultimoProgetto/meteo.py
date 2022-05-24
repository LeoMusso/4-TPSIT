from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from datetime import datetime
import folium, webbrowser
import os, time, csv, urllib, urllib.parse, requests
#import pkg_resources.py2_warm

class Meteo(App):
    path = os.getcwd()
    print(path)
    pathDati = path + "\\Meteo\\Data"
    pathMap = path + "\\Meteo\\Maps"

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5 , "center_y":0.5}
        Window.size = (360, 640)

        self.citta = Label(
            text = "Cerca una città:"
        )
     
        self.inputCitta = TextInput(
            size_hint = (0.3, 0.3),
            font_size = '13sp',
            padding_y = '12sp',
            halign = "center"
        )

        self.bottone = Button(
            text="Invia",
            size_hint = (1, 0.3),
            bold = True,
            background_color = '#0099ff'
        )

        self.cercaMappa = Button(
            text="Cerca",
            size_hint=(1, 0.3),
            bold=True,
            background_color='#0099ff'
        )

        self.clearButton = Button(
            text="Pulisci",
            size_hint=(1, 0.3),
            bold=True,
            background_color='#0099ff'
        )

        self.LabelMex = Label(
            text = "In attesa"
        )

        self.resetta = Button(
            text="Resetta",
            size_hint=(1, 0.3),
            bold=True,
            background_color='#0099ff'
        )
        self.window.add_widget(Image(source = "logo.png"))
        self.window.add_widget(self.citta)
        self.window.add_widget(self.inputCitta)
        self.window.add_widget(self.bottone)
        self.window.add_widget(self.cercaMappa)
        self.window.add_widget(self.clearButton)
        self.window.add_widget(self.LabelMex)
        self.window.add_widget(self.resetta)
        self.bottone.bind(on_press = self.invia)
        self.cercaMappa.bind(on_press = self.cercaGmaps)
        self.clearButton.bind(on_press = self.clear)
        self.resetta.bind(on_press = self.resettaFile)
    
        return self.window

    def clear(self, instance):
        self.inputCitta.text = ""
        self.LabelMex.text = "In attesa"

    def invia(self, instance):
        
        citta = f"{self.inputCitta.text}"
        if citta == "":
            self.LabelMex.text = "Inserire una città!!"
        else:
            try:
                def edit_label(request, result):
                    temp = result["main"]["temp"]
                    self.LabelMex.text = f"Oggi a {citta} ci sono {temp} gradi"
                    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(self.inputCitta.text) + '?format=json'
                    response = requests.get(url).json()
                    lat_lng = [float(response[0]["lat"]),
                            float(response[0]["lon"])]
                    date_time = datetime.now()
                    date = str(date_time.day) + "/" + str(date_time.month) + "/" + str(date_time.year)
                    time = str(date_time.hour) + ":" + str(date_time.minute)

                    city = (citta, lat_lng[0], lat_lng[1], float(temp), date, time)
                    os.chdir(self.pathDati)
                    with open("citta.csv", "a", newline="")as file:
                        writer = csv.writer(file, delimiter=",")
                        writer.writerow(city)
                        file.close()
                link = f"https://api.openweathermap.org/data/2.5/weather?q={citta}&appid=06c7c246532d397cb256e2b094ab8455&units=metric"
                UrlRequest(link, edit_label)
            except(IndexError):
                print("Errore")
    
    def cercaGmaps(self, instance):
        try:
            path = os.getcwd()
            print(path)
            map = folium.Map()
            os.chdir(self.pathDati)
            with open("citta.csv", 'r') as filecsv:
                reader = csv.reader(filecsv, delimiter=',')
                elemento = [(linea[0], linea[1], linea[2], linea[3])for linea in reader if linea[0] != "" and linea[0] != "CITTA"]
                for dato in elemento:
                    lat_lng = (dato[1], dato[2])
                    folium.Marker(lat_lng, popup=dato[0]).add_to(map)
                os.chdir(self.pathMap)
                map.save("maps.html")
                webbrowser.open_new_tab('maps.html')
        except(IndexError):
            print("Errore, città non trovata")

    def resettaFile(self, instance):
        os.chdir(self.pathDati)
        with open("citta.csv", "w", newline="")as file:
            writer = csv.writer(file, delimiter=",")
            header = (["CITTA", "LATITUDINE", "LONGITUDINE", "TEMPERATURA", "DATA", "ORA"])
            writer.writerow(header)
            file.close()


######################_MAIN_##################################
if __name__ == '__main__':
    path = os.getcwd()
    pathM = path + "\\Meteo"
    if os.path.exists(pathM) == False:
        os.chdir(path)
        os.mkdir("Meteo")
        os.chdir(pathM)
        os.mkdir("Maps")
        os.mkdir("Data")
        path = pathM + "\\Data\\citta.csv"
        pathM = pathM + "\\Data" 
        fileName = path
        ceck = os.path.isfile(fileName)
        if ceck == False:
            os.chdir(pathM)
            with open("citta.csv", "w", newline="")as file:
                writer = csv.writer(file, delimiter=",")
                header = (["CITTA", "LATITUDINE", "LONGITUDINE", "TEMPERATURA", "DATA", "ORA"])
                writer.writerow(header)
                file.close()
    else:
        print("Cartella creata")
        path = pathM + "\\Data\\citta.csv"
        pathM = pathM + "\\Data"
        fileName = path
        ceck = os.path.isfile(fileName)
        if ceck == False:
            os.chdir(pathM)
            with open("citta.csv", "w", newline="")as file:
                writer = csv.writer(file, delimiter=",")
                header = (["CITTA", "LATITUDINE", "LONGITUDINE", "TEMPERATURA", "DATA", "ORA"])
                writer.writerow(header)
                file.close()
    Meteo().run()
#########################################################################################################































#####################_LINK_###################################
#link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_lng[0]}&lon={lat_lng[1]}&appid=06c7c246532d397cb256e2b094ab8455&units=metric"

####################_PROVA-CARTELLE_################################
'''
path = os.getcwd()
pathM = path + "\\Meteo"
print(pathM)
if os.path.exists(pathM) == False:
    os.chdir(path)
    os.mkdir("Meteo")
    os.chdir(pathM)
    os.mkdir("Maps")
    os.mkdir("Data")
    path = pathM + "\\Data\\citta.csv"
    print(path)
    pathM = pathM + "\\Data" 
    fileName = path
    ceck = os.path.isfile(fileName)
    if ceck == False:
        os.chdir(pathM)
        with open("citta.csv", "w", newline="")as file:
            writer = csv.writer(file, delimiter=",")
            header = (["CITTA", "LATITUDINE", "LONGITUDINE", "TEMPERATURA", "DATA", "ORA"])
            writer.writerow(header)
            file.close()
'''