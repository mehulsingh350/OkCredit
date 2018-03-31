from django.db import models

class todo(models.Model):
    unique_id = models.AutoField(primary_key=True)
    text= models.CharField(max_length =100)
    completed=models.BooleanField(default=False)
    
