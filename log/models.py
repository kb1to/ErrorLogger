from django.db import models

class Log(models.Model):
    problem_name = models.CharField(max_length=255)
    what_i_didnt_know = models.TextField()
    solution = models.TextField()
    takeaway = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.problem_name

    class Meta:
        ordering = ['-date'] 

class Idea(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    acted_on_it = models.BooleanField(default=False)
    is_it_bs = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    photos = models.ImageField(upload_to='post_photos/', blank=True, null=True) 
    FORMAT_CHOICES = [
        ('MD', 'Markdown'),
        ('TXT', 'Plain Text'),
    ]
    formatting = models.CharField(max_length=3, choices=FORMAT_CHOICES, default='MD')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']