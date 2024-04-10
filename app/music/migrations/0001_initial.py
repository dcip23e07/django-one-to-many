# Generated by Django 3.2.9 on 2021-11-28 19:22

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='audio')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('author_website', models.URLField(blank=True, null=True)),
                ('album', models.CharField(blank=True, max_length=250, null=True)),
                ('duration', models.DurationField()),
                ('song_style', models.CharField(blank=True, choices=[('Indie', 'Indie'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Funky', 'Funky'), ('Reggaeton', 'Reggaeton'), ('Classic', 'Classic'), ('Orquestra', 'Orquestra'), ('Folk', 'Folk')], max_length=20, null=True)),
                ('playbacks', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[music.models.less_than_five])),
                ('deal_of_the_day', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='song',
            constraint=models.UniqueConstraint(fields=('title', 'author', 'album', 'duration'), name='unique_song'),
        ),
    ]
