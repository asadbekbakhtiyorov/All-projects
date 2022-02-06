# Generated by Django 4.0.1 on 2022-01-06 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('brend_nomi', models.CharField(blank=True, max_length=30)),
                ('narx', models.IntegerField()),
                ('miqdor', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='ombor',
            old_name='maxsulot_turi',
            new_name='turi',
        ),
        migrations.RemoveField(
            model_name='client',
            name='joylashish',
        ),
        migrations.RemoveField(
            model_name='ombor',
            name='joyalshish',
        ),
        migrations.AddField(
            model_name='client',
            name='joylashuv',
            field=models.CharField(default=50000, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ombor',
            name='joylashuv',
            field=models.CharField(default=6, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='dokon_nomi',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='ism',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='tel',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ombor',
            name='dokon_nomi',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ombor',
            name='ism',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ombor',
            name='tel',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ombor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Produst',
        ),
        migrations.AddField(
            model_name='product',
            name='ombor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_1.ombor'),
        ),
    ]