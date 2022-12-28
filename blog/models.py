from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

#from ckeditor.widgets import CKEditorWidget

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    sub_content = models.CharField(max_length=200)
    #content = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)  
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
