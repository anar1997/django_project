from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import TextField
class Article(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title=models.CharField(max_length=50, verbose_name="Tələbə adı")
    content=models.IntegerField(verbose_name="Kurs Balı", default=100)
    content1=models.IntegerField(verbose_name="Yataqxana balı",default=100)
    content2=models.TextField(verbose_name="Bal çıxma səbəbi")
    created_date=models.DateTimeField(auto_now_add=True, verbose_name="qurulma tarixi")
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Tələbə adı",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Müəllif")
    comment_content = models.CharField(max_length = 500,verbose_name = "Rəy")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
# Create your models here.
