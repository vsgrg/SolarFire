from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class UserDetail(models.Model):
    name=models.CharField(max_length=30,null=True,blank=False)
    def __str__(self):
        return str(self.name)
    
class Basicdata(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    date=models.DateField(null=True)
    start_time=models.TimeField(null=True)
    stop_time=models.TimeField(null=True)
    total_time=models.TimeField(null=True)
    first_perception=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],null=True)
    last_perception=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],null=True)
    total_drawing=models.IntegerField(null=True)
    correct=models.CharField(max_length=30,null=True)
    displaced=models.CharField(max_length=30,null=True)
    total_meld=models.CharField(max_length=30,null=True)
    correct_meld=models.CharField(max_length=30,null=True)
    incorect_meld=models.CharField(max_length=30,null=True)
    type=models.CharField(max_length=30,null=True)
    opp=models.CharField(max_length=10,null=True)
    multiple_opposition=models.CharField(max_length=10,null=True)
    bracketedIROR=models.CharField(max_length=10,null=True)
    giantsquare=models.CharField(max_length=10,null=True)
    house=models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.name)

class BoostAngle(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    boostanglebody=models.CharField(max_length=10,null=True)
    body=models.CharField(max_length=10,null=True)
    degree=models.CharField(max_length=10,null=True)  
    degree_type=models.CharField(max_length=10,null=True) 
     
    def __str__(self):
        return str(self.name)
       
class BoostAngleDetail(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    boostanglebody=models.CharField(max_length=10,null=True)
    body=models.CharField(max_length=10,null=True)
    boost_symbol=models.IntegerField(null=True)
    body1=models.CharField(max_length=10,null=True)
    degree=models.CharField(max_length=10,null=True)  
    degree_type=models.CharField(max_length=10,null=True)
    energy=models.CharField(max_length=10,null=True) 
     
    def __str__(self):
        return str(self.name)
    
class Condition(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    conditionbody=models.CharField(max_length=10,null=True)
    first_condition=models.CharField(max_length=10,null=True)
    degree=models.CharField(max_length=10,null=True) 
    degree_type=models.CharField(max_length=10,null=True)
    energy=models.CharField(max_length=10,null=True) 
    
     
    def __str__(self):
        return str(self.name)
    
class Irsupport(models.Model):

    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    body=models.CharField(max_length=10,null=True) 
    degree=models.CharField(max_length=10,null=True)
    sym=models.IntegerField(null=True)  
    degree_type=models.CharField(max_length=10,null=True)
    body1=models.CharField(max_length=10,null=True) 
    
    def __str__(self):
        return str(self.name)
    
class Bracketed(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    bracket=models.CharField(max_length=30,null=True,blank=False)
    body=models.CharField(max_length=30,null=True) 
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Gasgiant(models.Model): 
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE) 
    gas=models.CharField(max_length=10,null=True)
    symbol=models.IntegerField(null=True)
    body=models.CharField(max_length=10,null=True)
    degree=models.CharField(max_length=10,null=True) 
    degree_type=models.CharField(max_length=10,null=True)
    energy=models.CharField(max_length=10,null=True,)  
    
    
    def __str__(self):
        return str(self.name)
class C(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    body=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    body1=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=10,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)
    
    
class Opposition(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    body1=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    body2=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=30,null=True)
    degree_type=models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.name)
    
class Sextile(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    body=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    body1=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=10,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    
    def __str__(self):
        return str(self.name)

class Trine(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE) 
    body=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    body1=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=10,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)

    
class BracketedC(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    body=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    body1=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=10,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)
     
class MultipleSquare(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE) 
    body=models.CharField(max_length=30,null=True)
    symbol=models.IntegerField(null=True)
    degree=models.CharField(max_length=30,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Moon(models.Model):
    name=models.ForeignKey(UserDetail,null=True,on_delete=models.CASCADE)
    sym=models.IntegerField(null=True)
    body=models.CharField(max_length=30,null=True)
    degree=models.CharField(max_length=10,null=True)
    degree_type=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return str(self.name)