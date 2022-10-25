# Generated by Django 3.2.15 on 2022-09-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام محصول')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
        ),
    ]
