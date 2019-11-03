from django.db import models

PROPERTY_TYPES = (
    ('Residential', 'Residential'),
    ('Business', 'Business'),
    
)
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Property(models.Model):
    name = models.CharField(max_length=100)
    place = models.ForeignKey('Location',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='img',blank=True,null=True)
    filename=models.SlugField(max_length=30)
    cost=models.IntegerField()
    property_type= models.CharField(max_length=15, choices=PROPERTY_TYPES)
    description=models.CharField(max_length=700)

    def __str__(self):
        return self.name



