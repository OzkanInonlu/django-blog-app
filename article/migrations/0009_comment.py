# Generated by Django 3.2.5 on 2022-02-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20220212_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Comment Writer')),
                ('comment_content', models.TextField(max_length=200, verbose_name='Comment')),
                ('comment_date', models.DateField(auto_now_add=True, verbose_name='Comment Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='Article')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]