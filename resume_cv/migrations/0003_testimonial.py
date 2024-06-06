# Generated by Django 5.0.6 on 2024-06-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_cv', '0002_alter_programminglanguage_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('profession', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='static/images/testimonials')),
            ],
        ),
    ]
