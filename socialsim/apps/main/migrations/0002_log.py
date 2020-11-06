# Generated by Django 2.2 on 2020-11-03 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('result', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='main.Character')),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='main.Connections')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieved_actions', to='main.Character')),
            ],
        ),
    ]