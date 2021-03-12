from django.urls import path
from core.erp.views.categoria.views import *

app_name = 'erp'

urlpatterns = [
    path('categoria/list/', CategoriaListView.as_view(), name="categorialist"),
    # path('categoria/list2/', category_list, name="category_list"),
    path('categoria/create/', CategoriaCreateView.as_view(), name="categoriaCreate"),
    path('categoria/edit/<int:pk>/', CategoriaUpdateView.as_view(), name="categoriaEdit"),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name="categoriaDelete"),
    path('categoria/form/', CategoriaFormView.as_view(), name="categoriaForm")
]