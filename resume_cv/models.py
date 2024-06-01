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
