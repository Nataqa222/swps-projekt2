from django.db import models

# propozycje modeli:

#strazak, woz, zastep, interwencja

#firefighter, firetruck

class Firefighter(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

class Firetruck(models.Model):
    side_number = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    prod_year = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
class Squad(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
    truck = models.ForeignKey(Firetruck, on_delete=models.RESTRICT)

class FirefighterInSquad(models.Model):
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    firefighter = models.ForeignKey(Firefighter, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class Meta:
    unique_together = (("squad", "firefighter"),)