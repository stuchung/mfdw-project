from django.db import models

# Create your models here.
class Page(models.Model):
    """Django data model Page"""
    page_name = models.CharField(max_length=100)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    body_text = models.TextField('Page Content',blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return str(self.page_name)
