# Generated by Django 4.0.1 on 2022-01-28 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='Learner',
        ),
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='Class',
            field=models.ManyToManyField(blank=True, to='users.Class'),
        ),
    ]
