# Generated by Django 4.1.5 on 2023-02-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_skill_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, default='None', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, default='None', max_length=2000, null=True),
        ),
    ]
