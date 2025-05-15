from django.db import models

class Activity(models.Model):
    title = models.CharField("العنوان", max_length=200)
    description = models.TextField("الوصف")
    image = models.ImageField("الصورة", upload_to='activity_images/')
    date = models.DateField("التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
