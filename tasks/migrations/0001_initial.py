# Generated by Django 4.2.2 on 2023-06-08 18:01

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
            name='Actividad',
            fields=[
                ('COD_actividad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Costo', models.FloatField(max_length=(9, 2))),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Tipo_de_identificacion', models.IntegerField(choices=[(1, 'Seleccione'), (2, 'Cedula de ciudadania'), (3, 'Cedula de extranjeria'), (4, 'NIT')], default=1)),
                ('NID', models.IntegerField(primary_key=True, serialize=False)),
                ('Razon_social', models.CharField(max_length=70)),
                ('Direccion', models.CharField(max_length=70)),
                ('Email', models.CharField(max_length=70)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingeniero',
            fields=[
                ('Tipo_de_identificacion', models.IntegerField(choices=[(1, 'Seleccione'), (2, 'Cedula de ciudadania'), (3, 'Cedula de extranjeria')], default=1)),
                ('Identificacion', models.IntegerField()),
                ('COD_ingeniero', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=70)),
                ('Apellidos', models.CharField(max_length=70)),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=70)),
                ('ROL', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=80)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Costo', models.FloatField(max_length=(9, 2))),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente')),
                ('ingenieros_a_cargo', models.ManyToManyField(to='tasks.ingeniero')),
            ],
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('Fecha', models.DateField()),
                ('COD_bitacora', models.AutoField(primary_key=True, serialize=False)),
                ('Horas_laboradas', models.FloatField(max_length=5)),
                ('Cantidad_de_fuentes_trabajados', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], default=1)),
                ('Tipos_de_fuentes_trabajados', models.IntegerField(choices=[(1, 'Seleccione'), (2, 'RPG'), (3, 'RPGLE'), (4, 'RPGLE y RPG')], default=1)),
                ('Estado_de_los_fuentes_trabajados', models.IntegerField(choices=[(1, 'Seleccione'), (2, 'En proceso'), (3, 'Terminado')], default=1)),
                ('Nota', models.TextField(blank=True, max_length=300, null=True)),
                ('Actividad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.actividad')),
                ('Proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.proyecto')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='ingeniero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.ingeniero'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.proyecto'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
