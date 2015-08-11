from django.db import models
from product.utils import unique_slugify


class CategoryBanner(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    show_on_home_page = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "category banners"

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def __unicode__(self):
        return self.title


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    banners = models.ManyToManyField(CategoryBanner)
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == '':
            unique_slugify(self, unicode(self.title))
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    publisher = models.CharField(max_length=255, null=True)
    manufacturer = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    popularity = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "products"

    def get_absolute_url(self):
        return "/%s/%s/" % (self.category.slug, self.slug)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == '':
            unique_slugify(self, unicode(self.title))
        super(Product, self).save(*args, **kwargs)
