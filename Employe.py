from datetime import datetime, timedelta

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = datetime.strptime(dateEmbauche, "%d/%m/%Y")
        
    def coutHoraire(self):
        anciennete = self.getAnciennete()
        coeff = 1.0
        if anciennete > 5 and anciennete <= 10:
            coeff = 1.05
        elif anciennete > 10 and anciennete <= 15:
            coeff = 1.08
        elif anciennete > 15:
            coeff = 1.12
        return self.qualification.tauxHoraire() * coeff
    
    def getNumero(self):
        return self.numero
    
    def getNom(self):
        return self.nom
    
    def getQualification(self):
        return self.qualification
    
    def getDateEmbauche(self):
        return self.dateEmbauche
    
    def getAnciennete(self):
        return (datetime.now() - self.dateEmbauche).days // 365