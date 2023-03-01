from datetime import datetime, timedelta

class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm
        
    def distance(self):
        return self.nbKm
    
    def getNumero(self):
        return self.numero
    
    def getNom(self):
        return self.nom
    
    def getAdresse(self):
        return self.adresse
    
    def getCodePostale(self):
        return self.codePostale
    
    def getVille(self):
        return self.ville
    
    def getNbKm(self):
        return self.nbKm