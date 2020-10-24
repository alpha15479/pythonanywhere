# Generated by Django 2.2.7 on 2020-10-22 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Farm_Name', models.CharField(default='ชื่อฟาร์ม', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SeasonName', models.CharField(default='ฤดูร้อน', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vegetable_Name', models.CharField(max_length=100)),
                ('Price', models.FloatField()),
                ('FarmName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Farm')),
                ('Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Season')),
            ],
        ),
        migrations.DeleteModel(
            name='Fresh',
        ),
        migrations.RemoveField(
            model_name='freshy',
            name='Fresh_Type',
        ),
        migrations.DeleteModel(
            name='FreshType',
        ),
        migrations.DeleteModel(
            name='Freshy',
        ),
    ]
