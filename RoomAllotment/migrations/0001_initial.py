# Generated by Django 4.0.2 on 2022-02-07 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomNo', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stdID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('password', models.IntegerField(default=123456)),
            ],
        ),
        migrations.CreateModel(
            name='RoomAllotmentRequest',
            fields=[
                ('RequestID', models.AutoField(primary_key=True, serialize=False)),
                ('requestedRoomNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoomAllotment.room')),
                ('stdID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoomAllotment.student')),
            ],
        ),
    ]
