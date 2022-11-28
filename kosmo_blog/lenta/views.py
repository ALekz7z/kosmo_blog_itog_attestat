from django.shortcuts import render, redirect
from .models import articles
from .forms import articles_form, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def lenta_home(request):
    lenta = articles.objects.order_by('date')
    return render(request, 'lenta/lenta_home.html', {'lenta': lenta})

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)



class new_detail_view(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = articles
    template_name = 'lenta/details_view.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан'
    
    
    def get_success_url(self):
        return reverse_lazy('new_detail', kwargs={'pk':self.get_object().id})

    
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class new_update_view(UpdateView):
    model = articles
    template_name = 'lenta/create.html'
    form_class = articles_form


class new_delete_view(DeleteView):
    model = articles
    success_url = '/lenta/'
    template_name = 'lenta/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = articles_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно'

    form = articles_form()
    data = {'form': form,
    'error': error,
    }
    return render(request, 'lenta/create.html', data )


