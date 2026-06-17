from django.db import models

class Category(models.Model):
    #keeping the name unique
    name = models.CharField(
        max_length=100,
        unique=True
    )

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(
        max_length=255
    )
    content = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title