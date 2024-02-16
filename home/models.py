from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position',)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category'),
        ]
        unique_together = ['id', 'slug']


class FooterItem(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    working_hours = RichTextField()
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)

class Chef(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    appointment = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='chefs_photos', blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Events(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='events')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(default=1)

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=50)


class Reservation(models.Model):
    name = models.CharField(max_length=255)

    phone_regex = RegexValidator(
        regex=r'^\+?380\d{9}$',
        message="Phone number must be format '+380xxxxxxxxx'. Up to 15 digits"
    )
    phone = models.CharField(max_length=255, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    number_people = models.PositiveSmallIntegerField()

    is_conformed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
