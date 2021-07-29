import datetime

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from web.forms import C_YF
from web.models import POEM, YOURFEELS, V_PROMO


class Index(TemplateView):
    template_name= 'index.html'

    def get_context_data(self,  **kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['LAST_POEM']=POEM.objects.all().filter().order_by('date_create').reverse()[0]
        context['YF']=YOURFEELS.objects.all().filter(own_poem=context.get('LAST_POEM'))
        context['TOTALPOEMS']=POEM.objects.all().order_by('date_create')
        context['VIDEO_PROMO']=V_PROMO.objects.all().order_by('?')[0]
        return context

class CREATE_YFEEL(CreateView):
    template_name = 'create_yfeel.html'
    form_class = C_YF
    success_url = reverse_lazy('Index')

    def form_valid(self, form):
        form.instance.own_poem=POEM.objects.all().get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class SEEARCHIVE(TemplateView):
    template_name = 'archive.html'

    def get_context_data(self,  **kwargs):
        context=super(SEEARCHIVE, self).get_context_data(**kwargs)
        context['obj']=POEM.objects.all().get(pk=self.kwargs['pk'])
        context['YF']=YOURFEELS.objects.all().filter(own_poem=context.get('obj'))
        context['TOTALPOEMS']=POEM.objects.all().order_by('date_create')
        context['VIDEO_PROMO']=V_PROMO.objects.all().order_by('?')[0]
        return context
