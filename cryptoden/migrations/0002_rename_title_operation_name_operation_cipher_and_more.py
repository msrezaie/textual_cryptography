# Generated by Django 4.1.5 on 2023-02-05 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoden', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='operation',
            name='cipher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cryptoden.cipher'),
        ),
        migrations.AlterField(
            model_name='cipher',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
