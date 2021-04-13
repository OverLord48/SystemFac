from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from core.erp.models import *
from core.erp.form import *

# @method_decorator(csrf_exempt)
# def category_list(request):
#     categorias = Categorias.objects.all()
#     vals = {
#         'title':'Listado de Categorias',
#         'categorias': categorias
#     }
#     return render(request, 'categoria/list.html', vals)

class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class CategoriaListView(ListView):
    model = Categorias
    template_name = 'categoria/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Categorias.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
            #data = Categorias.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias'
        context['create_url'] = reverse_lazy('erp:categoriaCreate')
        return context

class CategoriaCreateView(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('erp:categorialist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
            #   form = CategoriaForm(request.POST) una forma de obtener el valor del formulario
                form = self.get_form() #forma adicional de obtener los valores del formulario
                if form.is_valid():
                   form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    #     print(request.POST)
    #     form = CategoriaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Categoria'
        context['list_url'] = reverse_lazy('erp:categorialist')
        context['action'] = 'add'
        return context

class CategoriaUpdateView(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('erp:categorialist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
            #   form = CategoriaForm(request.POST) una forma de obtener el valor del formulario
                form = self.get_form() #forma adicional de obtener los valores del formulario
                if form.is_valid():
                   form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Categoria'
        context['list_url'] = reverse_lazy('erp:categorialist')
        context['action'] = 'edit'
        return context

class CategoriaDeleteView(DeleteView):
    model = Categorias
    template_name = 'categoria/delete.html'
    success_url = reverse_lazy('erp:categorialist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Categoria'
        context['list_url'] = reverse_lazy('erp:categorialist')
        return context

class CategoriaFormView(FormView):
    form_class = CategoriaForm
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('erp:categorialist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Categoria'
        context['list_url'] = reverse_lazy('erp:categorialist')
        context['action'] = 'add'
        return context
