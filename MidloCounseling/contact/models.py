from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Interest(models.Model):
    author = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.Email(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    submit_date = models.DateTimeField(blank=True,null=True)

    def submit(self):
        self.submit_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("interest_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.last_name


class Comment(model.Model):
    post = models.ForeignKey('contact.Interest',related_name='comments')
    responder = models.CharField('auth.User')
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("index")

    def __str__(self):
        return self.responder