# Generated by Django 4.1.7 on 2023-03-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('questions_answered', models.PositiveIntegerField(default=0)),
                ('answers_correct', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
