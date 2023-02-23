# Generated by Django 4.1.6 on 2023-02-11 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gbill.bill')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gbill.person')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='payee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_payees', to='gbill.person'),
        ),
    ]