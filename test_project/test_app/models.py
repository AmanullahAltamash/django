from django.db import models
import uuid

# Create your models here.

class table(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    demo_links = models.CharField(max_length=2000, null = True, blank = True)
    source_links = models.CharField(max_length=2000, null = True, blank = True)
    tags =models.ManyToManyField('tag', blank = True)
    vote_total = models.IntegerField(default=0, null=True, blank = True)
    vote_ratio = models.IntegerField(default=0, null=True, blank = True)
    created = models.TimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def str(self):
        return self.title
    
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'upvote'),
        ('down', 'downvote'),
    )
    
    project = models.ForeignKey(table, on_delete=models.CASCADE)
    body = models.TextField(null = True, blank = True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.TimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    
    def str(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable = False)
    
    def str(self):
        return self.name