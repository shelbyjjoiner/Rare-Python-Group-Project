# Generated by Django 4.1.3 on 2022-11-22 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('image_url', models.CharField(max_length=400)),
                ('content', models.CharField(max_length=200)),
                ('approved', models.BooleanField()),
                ('publication_date', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rareapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RareUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=24)),
                ('profile_image', models.CharField(max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rareapi.tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(through='rareapi.PostTag', to='rareapi.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rareapi.rareuser'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rareapi.rareuser')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
            ],
        ),
    ]
