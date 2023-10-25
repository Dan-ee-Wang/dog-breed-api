
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DogDB(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1) 
    breed = models.ForeignKey("BreedDB", on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    favoritefood = models.CharField(max_length=30)
    favoritetoy = models.CharField(max_length=30)
        
    def __str__(self):
        return str(self.id)+ " : " + str(self.name)

class BreedDB(models.Model):
    name = models.CharField(max_length=30)
    sizechoices = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large")]
    size = models.CharField(choices=sizechoices, max_length=30)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0) 
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0) 
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0) 
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0) 
        
    def __str__(self):
        return str(self.id)+ " : " + str(self.name)