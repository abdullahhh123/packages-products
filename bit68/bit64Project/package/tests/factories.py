import factory
# from django.contrib.auth.models import User
from datetime import datetime
from package.models import Package
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_app.settings")

django.setup()


class PackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Package
    
    product_name  = 'test product name'
    product_price = 1200