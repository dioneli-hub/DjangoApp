# Generated by Django 3.2.4 on 2021-06-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_alter_book_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='remarks',
            field=models.TextField(default='no remarks', max_length=500),
        ),
    ]
