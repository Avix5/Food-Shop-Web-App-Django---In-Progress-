from django.db import models

# Create your models here.
class item(models.Model):
    def  __str__(self):
        return self.item_name
    
    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField()
    item_price=models.IntegerField()
    item_image=models.CharField(default="https://tse3.mm.bing.net/th/id/OIP.cBTMC58k-3lztDTtMc-6ywHaHa?rs=1&pid=ImgDetMain&o=7&rm=3")

    # after changes in database
    # 1st use "python manage.py makemigrations"
    #  2nd use "python manage.py migrate"