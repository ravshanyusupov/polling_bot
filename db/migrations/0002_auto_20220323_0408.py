# Generated by Django 3.2.9 on 2022-03-23 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='a_answer',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='b_answer',
            new_name='b',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='c_answer',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='d_answer',
            new_name='d',
        ),
    ]