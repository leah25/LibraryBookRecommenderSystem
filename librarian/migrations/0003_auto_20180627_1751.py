# Generated by Django 2.0 on 2018-06-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_remove_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='shelf_store_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]