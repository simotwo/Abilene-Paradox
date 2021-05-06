from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for ddd_shop."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Product(models.Model):
    # id = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.product_id, self.category_id)


class Store(models.Model):
    name = models.CharField(max_length=50, blanks=True)
    store_id = models.CharField(max_length=50, unique=True)
    owner_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.store_id, self.owner_id)



class Sales(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    store_id = models.CharField(max_length=50, blank=True)
    units_sold = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{} || {}".format(self.store_id, self.units_sold)
