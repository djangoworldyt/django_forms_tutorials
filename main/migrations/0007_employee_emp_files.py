# Generated by Django 4.2.1 on 2023-07-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_employee_emp_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_files',
            field=models.FileField(blank=True, null=True, upload_to='file_uploads/'),
        ),
    ]
