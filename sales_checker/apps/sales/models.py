from django.db import models


# /html/body/div[2]/main/div[2]/div/div[1]/div[3]/form/div/div/div/div/div[1]/div[1]/div[1]/div[1]/span
class Sale(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=False, blank=False)
    xpath = models.CharField(max_length=255, null=False, blank=False)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sales'
