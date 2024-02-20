from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_structure = models.JSONField(null=True, blank=True)  # Для хранения структурированного контента
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news')
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    video = models.FileField(upload_to='news_videos/', null=True, blank=True)
    file = models.FileField(upload_to='news_files/', null=True, blank=True)

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return f"Image for {self.news.title}"

class NewsVideo(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='news_videos/')

    def __str__(self):
        return f"Video for {self.news.title}"

class NewsFile(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='news_files/')

    def __str__(self):
        return f"File for {self.news.title}"


class Comment(models.Model):
    news = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.created_at}'