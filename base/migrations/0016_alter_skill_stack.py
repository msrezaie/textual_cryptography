# Generated by Django 4.1.5 on 2023-01-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_rename_name_skill_skill_remove_skill_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='stack',
            field=models.CharField(blank=True, choices=[('front-end', 'Front-end'), ('back-end', 'Back-end')], max_length=20),
        ),
    ]
