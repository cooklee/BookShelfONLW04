# Generated by Django 3.2.3 on 2021-05-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0005_bookreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book'),
            preserve_default=False,
        ),
    ]
