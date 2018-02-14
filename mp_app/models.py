from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'mp_user'

class UserGroup(models.Model):
    name = models.CharField(max_length=254)
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mp_user_group'
        
class Music(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'mp_music'

class PlayListType(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mp_playlist_type'

class UserPlayList(models.Model):
    name = models.CharField(max_length=254)
    playlist_type = models.ForeignKey(PlayListType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'mp_user_playlist'