# Generated by Django 2.2 on 2019-12-06 17:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_is_classics'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('tag', models.CharField(max_length=100, verbose_name='章节')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
    ]