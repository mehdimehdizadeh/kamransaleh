from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120,verbose_name="Başlıq")
    slug = models.SlugField(default="", null=False)

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ['-id']

class Post(models.Model):
    category = models.ManyToManyField(Category,verbose_name="Kateqoriya",blank=True)
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Məzmun")
    image = ResizedImageField(size=[500, 300],quality=75,blank=True,null=True,verbose_name="Şəkil")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Paylaşım vaxtı")
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ['-id']

class Postcads(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    link = models.CharField(max_length=300,verbose_name="Link")
    image = ResizedImageField(size=[500, 300],quality=75,blank=True,null=True,verbose_name="Şəkil")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Paylaşım vaxtı")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Podkast"
        verbose_name_plural = "Podkastlar"
        ordering = ['-id']

class About(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Məzmun")
    logo  = models.ImageField(verbose_name="Logo",blank = True,null= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Haqqında"
        verbose_name_plural = "Haqqında"
        ordering = ['-id']

class Subscribe(models.Model):
    email = models.CharField(max_length=150,verbose_name="email",unique=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Abonə"
        verbose_name_plural = "Abonələr"
        ordering = ['-id']

class Contact(models.Model):
    name = models.CharField(max_length=150,verbose_name="Başlıq")
    email = models.CharField(max_length=300,verbose_name="Link")
    phone = models.CharField(max_length=300,verbose_name="Link")
    subject = models.CharField(max_length=300,verbose_name="Link")
    text = models.CharField(max_length=30000,verbose_name="Link")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Paylaşım vaxtı")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqəıər"
        ordering = ['-id']