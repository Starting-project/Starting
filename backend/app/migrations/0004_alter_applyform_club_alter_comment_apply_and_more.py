# Generated by Django 4.1 on 2022-08-12 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_club_name_timetable_selecttime_notice_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='app.club'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='apply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.apply'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='app.club'),
        ),
        migrations.AlterField(
            model_name='selecttime',
            name='apply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_times', to='app.apply'),
        ),
        migrations.AlterField(
            model_name='selecttime',
            name='select_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_by', to='app.timetable'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='recruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_cells', to='app.recruit'),
        ),
    ]
