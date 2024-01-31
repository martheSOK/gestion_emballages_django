from django.db import models

# Create your models here.

class User(models.Model):
    nom=models.CharField(),
    prenom=models.CharField(),
    contact=models.IntegerField(),
    adresse=models.CharField(),


    def __str__(self):
        return self.nom + self.prenom + str(self.contact) + self.adresse
    
    class Meta:
        abstract=True



class Echange(models.Model):
    quantite_echange=models.IntegerField(),
    type=models.CharField(),
    description=models.CharField(),

    def __str__(self):
        return self.quantite_echange + self.type + self.description

    class Meta:
        abstract=True




class Depot(models.Model):
    nom_depot=models.CharField(),
    

    def __str__(self):
        return self.nom_depot 


class Fournisseur(models.Model):
    nom_fournisseur=models.CharField(),

    def __str__(self):
        return self.nom_fournisseur


class Emballage(models.Model):
    designation=models.CharField(),
    quantite=models.IntegerField(),
    echange_externe=models.ManyToManyField(Fournisseur)

    def __str__(self):
        return self.designation + self.quantite
    

class Personne(User):
    depot=models.ForeignKey(Depot, on_delete=models.CASCADE, null=True)
    echange_interne=models.ManyToManyField(Emballage)



