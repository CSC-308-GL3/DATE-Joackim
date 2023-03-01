from datetime import datetime

class Contrat:
    def __init__(self, numero, date, client):
        self.numero = numero
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.client = client
        self.montantContrat = 0
        self.interventions = []
        self.nbIntervention = 0
    
    def montant(self):
        return self.montantContrat
    
    def ecart(self):
        totalIntervention = 0
        for intervention in self.interventions:
            totalIntervention += intervention.fraisMo() + intervention.fraisKm(self.client.distance())
        return self.montantContrat - totalIntervention