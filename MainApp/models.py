from django.db import models
from django.contrib.auth.models import User




LANGS = (
    ("py", "Python"),
    ('js', "JavaScript"),
    ('cpp', 'C++'),
    ('html', "HTML") 
)


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True)  # True = public, False = private

    def __repr__(self) -> str:
        return f"Snippet({self.name})"

class Comment(models.Model):
   text = models.TextField(max_length=500)
   creation_date = models.DateField(auto_now_add=True)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank = True, null = True)
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name='comments')

