from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from post.models import mypost, Cities
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import requests
import json
from collections import namedtuple
from post.forms import VCquery
from .filters import myfilter


# Create your views here.
class MyPosts(LoginRequiredMixin,TemplateView):
    template_name = 'app_post/my_posts.html'


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = mypost
    fields = ('post_title','post_text','City','Full_Adress','phone_number','post_text','service_provider')
    template_name = 'app_post/edit_post.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('post:mypost')

class DeletePost(LoginRequiredMixin, DeleteView):
    model = mypost
    template_name='app_post/mypost_confirm_delete.html'
    def get_success_url(self, **kwargs):
        return reverse_lazy('post:mypost')



class postList(ListView):
    context_object_name = 'Posts'
    model=mypost
    template_name = 'app_post/post.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter']=myfilter(self.request.GET, queryset=self.get_queryset())
        return context


class Createpost(LoginRequiredMixin,CreateView):
    model = mypost
    template_name = 'app_post/create_post.html'
    fields = ('post_title','post_text','City','Full_Adress','phone_number','post_text','service_provider')
    
    def form_valid(self, form):
        post_obj = form.save(commit=False)
        post_obj.user = self.request.user
        title = post_obj.post_title
        post_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        post_obj.save()
        return HttpResponseRedirect(reverse('post:postlist'))


def  VC(request):
     form=VCquery(data=request.GET)
     return render(request,'app_post/vaccination_centres.html')

def showresult(request):
   # if request.method=='GET':
     form= VCquery(data=request.GET)
     pincode=form['pincode'].value()
     date=form['date'].value()
     url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={0}&date={1}'.format(str(pincode),str(date))
     response= requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=326001&date=25-6-2021')
     data=response.json()
     context={'pincode':pincode,'date':date, 'data':data}
     return render(request,'app_post/results.html',context)