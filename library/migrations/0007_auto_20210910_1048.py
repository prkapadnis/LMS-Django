# Generated by Django 3.2.7 on 2021-09-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210910_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebookmodel',
            name='data_created',
        ),
        migrations.AddField(
            model_name='issuebookmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]