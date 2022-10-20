# Generated by Django 4.1.2 on 2022-10-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'التصنيف', 'verbose_name_plural': 'التصنيف'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Task'},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'قيد التنفيذ'), (2, 'مكتمل'), (3, 'معلق'), (4, 'ملغى')], default=1),
        ),
    ]
