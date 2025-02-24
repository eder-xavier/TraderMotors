# Generated by Django 5.1.6 on 2025-02-25 01:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainTM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='automoveis/')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='carrinho',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='part',
            name='vehicle',
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='pecas/')),
                ('automoveis_compatíveis', models.ManyToManyField(related_name='pecas_compatíveis', to='MainTM.automovel')),
            ],
        ),
        migrations.CreateModel(
            name='InteracaoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_interacao', models.CharField(max_length=50)),
                ('data_interacao', models.DateTimeField(auto_now_add=True)),
                ('automovel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainTM.automovel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('peca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainTM.peca')),
            ],
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='ItemCarrinho',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
