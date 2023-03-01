from datetime import date
from Client import Client
from Contrat import Contrat
from Grade import Grade
from Employe import Employe
from Intervention import Intervention

# Création des grades
grade1 = Grade('A', 'Technicien', 15)
grade2 = Grade('B', 'Superviseur', 20)
grade3 = Grade('C', 'Manager', 25)

# Création des employés
employe1 = Employe(1, 'Dupont', grade1, '01/01/2000')
employe2 = Employe(2, 'Martin', grade2, '01/01/2005')
employe3 = Employe(3, 'Durand', grade3, '01/01/2010')

# Création du client
client1 = Client(1, 'Client1', '1 rue des Champs', '75001', 'Paris', 50)

# Création du contrat
contrat1 = Contrat(1, '01/01/2022', client1, 1000)

# Création des interventions
intervention1 = Intervention(1, '02/01/2022', 2, 0.5, employe1)
intervention2 = Intervention(2, '03/01/2022', 3, 0.5, employe2)
intervention3 = Intervention(3, '04/01/2022', 4, 0.5, employe3)

# Ajout des interventions au contrat
contrat1.interventions[0] = intervention1
contrat1.interventions[1] = intervention2
contrat1.interventions[2] = intervention3

# Calcul de l'écart entre le montant du contrat et le coût des interventions
ecart = contrat1.ecart()

print("Le montant du contrat est de : ", contrat1.montant())
print("Le coût total des interventions est de : ", contrat1.coutInterventions())
print("L'écart entre le montant du contrat et le coût des interventions est de : ", ecart)
