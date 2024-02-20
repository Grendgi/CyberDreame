from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название", blank=True, null=True)
    content = models.TextField(verbose_name="Контент", blank=True, null=True)
    image = models.ImageField(upload_to='slides/', verbose_name="Изображение", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else "Без названия"

