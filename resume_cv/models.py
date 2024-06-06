from django.db import models

level_choices = (('Bgn', 'Beginner'),
                 ('Int', 'Intermediate'),
                 ('Exp', 'Expert')
                 )

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    level = models.CharField(max_length=3, blank=False, null=False, choices=level_choices)
    text = models.TextField(max_length=500)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    profession = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/images/testimonials', blank=True,)

    def __str__(self):
        return f"{self.name.title()} the {self.profession.title()}."
    

