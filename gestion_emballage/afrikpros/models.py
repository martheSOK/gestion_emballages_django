from django.db import models

# Create your models here.

class User(models.Model):
    nom=models.CharField(max_length=50,null=True)
    prenom=models.CharField(max_length=50,null=True)
    contact=models.IntegerField( null=True)
    adresse=models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.nom + self.prenom + str(self.contact) + self.adresse
    
    class Meta:
        abstract=True



class Echange(models.Model):
    quantite_echange=models.IntegerField()
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.quantite_echange + self.type + self.description

    class Meta:
        abstract=True




class Depot(models.Model):
    nomdepot=models.CharField(max_length=50)
    

    def __str__(self):
        return self.nomdepot 


class Fournisseur(models.Model):
    nom_fournisseur=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom_fournisseur


class Emballage(models.Model):
    designation=models.CharField(max_length=50, null=True)
    quantite=models.IntegerField(null=True)
    echange_externe=models.ManyToManyField(Fournisseur)

    # def __str__(self):
    #     return self.designation + self.quantite
    

class Personne(User):
    depot=models.ForeignKey(Depot, on_delete=models.CASCADE, null=True)
    echange_interne=models.ManyToManyField(Emballage)



    
