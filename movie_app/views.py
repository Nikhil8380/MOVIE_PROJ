from django.shortcuts import render
from .forms import REGFORM,AddMovie
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movies
from django.views.generic import UpdateView,DeleteView,ListView,DetailView
from django.utils import timezone
from django.db.models import Q

def List(request):
    query=request.GET.get('q',None)
    qs=Movies.objects.all()

    if query is not None:
        qs=qs.filter(
            Q(title__icontains=query)|
            Q(Region__icontains=query)|
            Q(Lead_Actor__icontains=query)|
            Q(Lead_Actress__icontains=query)

        )
    context={
        'object_list':qs
    }
    return render(request, 'list.html', context)


class LIST(ListView):
    model = Movies

    def get_queryset(self):
        return Movies.objects.filter(Release_year__lte=timezone.now()).order_by('-Release_year')

    template_name = 'list.html'

def home(request):
    return render(request,'home.html')

def Register(request):
    form1=REGFORM()
    if request.method=='POST':
        form1=REGFORM(request.POST)
        if form1.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
          return HttpResponse("<h1>ENTER VALID INFORMATION</h1>")

    else:
      return render(request, 'register.html', {'form1': form1})

@login_required
def Create(request):
    form2=AddMovie()
    if request.method=='POST':
        form2=AddMovie(request.POST,request.FILES)
        if form2.is_valid():
            nix_auth=form2.save(commit=False)
            nix_auth.admin=request.user
            nix_auth.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("<h1>INFO DOES NOT MATCH</h1>")
    else:
        return render(request,'CRTorUDT.html',{'form2':form2})


class Update(LoginRequiredMixin,UpdateView):
    model = Movies
    fields ={'title','rating','summary'}
    template_name ='CRTorUDT.html'

class DETAIL(DetailView):
    model = Movies
    template_name = 'detail.html'

class DELETE(LoginRequiredMixin,DeleteView):
    model = Movies
    template_name = 'delete.html'
    success_url = reverse_lazy('list')


# Create your views here.
