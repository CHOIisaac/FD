from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    preview_image = models.ImageField(upload_to="article", null=True, blank=True)
    content = models.TextField()
    show_at_index = models.BooleanField(default=False)
    is_published = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    branch_name = models.CharField(max_length=100, db_index=True)
    preview_image = models.ImageField(upload_to="restaurant", null=True, blank=True)
    address = models.CharField(max_length=255, db_index=True)
    feature = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=12, db_index=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=12, db_index=True)
    phone = models.CharField(max_length=16, help_text="E.164포멧")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default="0.0")
    rating_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        "RestaurantCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField("Tag", blank=True)


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)