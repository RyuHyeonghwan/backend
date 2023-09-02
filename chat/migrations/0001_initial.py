# Generated by Django 4.2.4 on 2023-09-02 06:15

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'chatMessage',
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('blacklist', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=list, null=True, size=None)),
            ],
            options={
                'db_table': 'chatRoom',
            },
        ),
        migrations.CreateModel(
            name='ChatRoomJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('chatroom', models.ForeignKey(db_column='chatroom_id', on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom')),
            ],
            options={
                'db_table': 'chatRoomJoin',
                'ordering': ['updated_at'],
            },
        ),
    ]
