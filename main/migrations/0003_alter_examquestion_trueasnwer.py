# Generated by Django 5.0.4 on 2024-04-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_examquestion_trueasnwer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examquestion',
            name='TrueAsnwer',
            field=models.CharField(choices=[('answer1', models.CharField(max_length=200, verbose_name='Answer 1')), ('answer2', models.CharField(max_length=200, verbose_name='Answer 2')), ('answer3', models.CharField(max_length=200, verbose_name='Answer 3')), ('answer4', models.CharField(max_length=200, verbose_name='Answer 4'))], max_length=200, verbose_name='True Asnwer'),
        ),
    ]
