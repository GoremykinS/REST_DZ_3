# Generated by Django 3.2.12 on 2022-03-20 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_project_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='todo.project'),
            preserve_default=False,
        ),
    ]
