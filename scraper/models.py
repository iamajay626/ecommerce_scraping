from django.db import models

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    selling_status = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
