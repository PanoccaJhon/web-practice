
# Models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Product
from store.forms import ProductForm

# Decorators
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required

# Url
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect

class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        
        try:
            data = Product.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('store:product_create')
        context['list_url'] = reverse_lazy('store:product_list')
        context['entity'] = 'Productos'
        return context
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('store:product_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No se ha ingresado ningun dato'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Agregar un Producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('store:product_list')
        context['action'] = 'add'
        return context

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('store:product_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object  = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        
        try:
            action  =request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No se ha ingresado ninguna accion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edición de Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('store:product_list')
        context['action'] = 'edit'
        return context
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url  =reverse_lazy('store:product_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self. object = self.get_object()
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
        context["title"] = 'Eliminar Producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('store:product_list')
        return context
    
    