# Generated by Django 4.2.6 on 2024-10-02 09:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecms_app', '0017_alter_teacherprofile_birthday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matirial',
            new_name='Material',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='matirial_name',
            new_name='material_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='matirial',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='matirial',
        ),
        migrations.AddField(
            model_name='student',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_material', to='ecms_app.material'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_material', to='ecms_app.material'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
