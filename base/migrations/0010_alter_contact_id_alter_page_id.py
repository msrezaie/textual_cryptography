# Generated by Django 4.1.5 on 2023-01-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_profile_resume_alter_contact_id_alter_page_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]