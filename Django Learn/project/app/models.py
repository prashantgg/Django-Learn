from django.db import models
class Person(models.Model):
    first_name= models.CharField(max_length= 30)
    last_name= models.CharField(max_length=30)
    age = models.IntegerField(default="")
    phone_no = models.CharField(max_length=20, default= "")
    email = models.EmailField(default="", max_length= 50)
    profile_picture = models.ImageField(upload_to='profile_picture', blank= True)  


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "People"


class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete= models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.person.first_name}'s Profile"

class ContactNumber(models.Model):
    person = models.ForeignKey(Person, on_delete= models.CASCADE,default="")
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.first_name}'s Number"
    
class Hobby(models.Model):
    persons = models.ManyToManyField(Person)
    hobby = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return f"{self.hobby}"
