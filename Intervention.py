from datetime import datetime, timedelta

class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien
        
    def affiche(self):
        print("Intervention numéro ", self.numero)
        print("Date : ", self.date.strftime("%d/%m/%Y"))
        print("Durée : ", self.duree)
        print("Frais kilométriques : ", self.fraisKm(100))
        print("Frais de main-d'oeuvre : ", self.fraisMo())
        self.technicien.affiche()
        
    def fraisKm(self, dist):
        return dist * self.tarifKm
    
    def fraisMo(self):
        return self.technicien.coutHoraire() * self.duree