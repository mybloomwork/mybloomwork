# Generated by Django 3.0.5 on 2020-07-10 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200710_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='feature',
            new_name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
