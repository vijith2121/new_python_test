# Generated by Django 4.0 on 2021-12-23 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('updated_by', models.CharField(max_length=100)),
                ('updatedon', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr_line1', models.CharField(max_length=200)),
                ('addr_line2', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('updated_by', models.CharField(max_length=50)),
                ('updatedon', models.DateTimeField(auto_now_add=True)),
                ('custome_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_list.customer')),
            ],
        ),
    ]
