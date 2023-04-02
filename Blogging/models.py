from django.db import models
from tinymce.models import HTMLField
# category model
class category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    decs = HTMLField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

# post model
class post(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey("category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    



