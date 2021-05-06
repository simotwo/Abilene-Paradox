from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class ListProductsView(generics.ListCreateAPIView):
    """
    Get all the products
    """
    queryset = Product.objects.all()
    serializer_class = ShowProductSerializer

  

    def post(self, request, *args, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

list_products_view = ListProductsView.as_view()


class ListSpecificProduct(generics.ListAPIView):
    """
    Get a specific product
    """
    serializer_class = ShowProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the 
                """
        id = self.kwargs['id']
        return Product.objects.filter(id=id)

class ListProductSales(generics.ListCreateAPIView):
    """
    Get all the product sales
    """
    queryset = Sales.objects.all()
    serializer_class = ShowProductSerializer

  

    def post(self, request, *args, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

list_products_sales = ListProductSales.as_view()
