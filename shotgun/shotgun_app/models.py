from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    age = models.IntegerField()
    location = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    author_id = models.IntegerField()
    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=1000)
    publish_time = models.DateTimeField()
    event_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200,default='')
    privacy = models.CharField(max_length=50)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.event_name

class Attending(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.event_id

class Friends(models.Model):
    friendship_id = models.AutoField(primary_key=True)
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    conversation = models.CharField(max_length=100000)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.friendship_id


