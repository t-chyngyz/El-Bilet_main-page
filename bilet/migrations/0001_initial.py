# Generated by Django 3.2.7 on 2021-10-06 18:28

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
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Handling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjecthandling', models.CharField(max_length=50)),
                ('solution', models.CharField(max_length=50)),
                ('authorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.category')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.file')),
            ],
        ),
        migrations.CreateModel(
            name='TypeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typerecord', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectproposal', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('authorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.category')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.file')),
                ('handlingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.handling')),
                ('typerecordid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.typerecord')),
            ],
        ),
        migrations.AddField(
            model_name='handling',
            name='typerecordid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilet.typerecord'),
        ),
    ]
