# Generated by Django 2.0.6 on 2020-07-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=80)),
                ('img', models.ImageField(default='pic/33.jpg', upload_to='pic')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'tb_employee',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('real_name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('status', models.SmallIntegerField(default=False)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_user',
            },
        ),
    ]
