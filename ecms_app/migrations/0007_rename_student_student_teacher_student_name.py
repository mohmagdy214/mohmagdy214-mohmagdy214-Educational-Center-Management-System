# Generated by Django 4.2.6 on 2024-09-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecms_app', '0006_remove_student_name_student_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
