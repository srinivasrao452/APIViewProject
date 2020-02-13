



from django.db import models

class Emp(models.Model):
    eno =   models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esal =  models.IntegerField()
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename

