# Generated by Django 3.2.5 on 2021-10-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_content2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content2',
            field=models.TextField(verbose_name='Bal çıxma səbəbi'),
        ),
    ]
