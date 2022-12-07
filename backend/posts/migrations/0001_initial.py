# Generated by Django 4.1.3 on 2022-12-07 06:33

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=posts.models.user_directory_path)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('category', models.BigIntegerField(null=True)),
                ('creator', models.BigIntegerField()),
                ('remover', models.BigIntegerField(null=True)),
                ('modifier', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('category', models.BigIntegerField(null=True)),
                ('creator', models.BigIntegerField()),
                ('modifier', models.BigIntegerField(null=True)),
                ('remover', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.BigIntegerField()),
                ('parent', models.BigIntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('creator', models.BigIntegerField()),
                ('remover', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCommentReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BigIntegerField()),
                ('reaction', models.IntegerField(default=1)),
                ('creator', models.BigIntegerField()),
                ('remover', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.BigIntegerField()),
                ('reaction', models.IntegerField(default=1)),
                ('creator', models.BigIntegerField()),
                ('remover', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
