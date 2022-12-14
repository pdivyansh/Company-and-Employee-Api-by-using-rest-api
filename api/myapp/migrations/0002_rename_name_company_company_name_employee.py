# Generated by Django 4.0.5 on 2022-10-05 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'manager'), ('software developer', 'software developer'), ('Project leader', 'Project leader')], max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
            ],
        ),
    ]
