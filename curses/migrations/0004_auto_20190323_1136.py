# Generated by Django 2.1.7 on 2019-03-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0003_auto_20190323_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curse',
            old_name='author_id',
            new_name='author',
        ),
    ]
