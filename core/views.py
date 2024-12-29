from django.views.generic import TemplateView 
from .models import Servico
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages



class IndexView(TemplateView):
    template_name = 'index.html'

class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContatoForm
    sucess_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        return context
    
    def form_valid(self,form,*args,**kwargs):
        form.send_email()
        messages.success(self.request,'E-mail enviado com sucesso')
        return super(IndexView,self).form_valid(form,*args,**kwargs)

    def form_invalid(self, form,*args,**kwargs):
        messages.error(self.request,'Erro ao enviar e-mail')
        return super(IndexView,self).form_invalid(form,*args,**kwargs)


