# Generated by Django 4.2.1 on 2023-08-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(blank=True, upload_to="Product")),
                ("stock", models.IntegerField()),
                ("available", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Shop.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "ordering": ("name",),
            },
        ),
    ]
