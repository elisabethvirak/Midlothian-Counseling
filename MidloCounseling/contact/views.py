from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Interest,Comment
from contact.forms import InterestForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView)
import datetime

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class InterestListView(ListView):
    model = Interest

    def get_queryset(self):
        return Interest.objects.filter(submit_date__lte=datetime.datetime.now()).order_by('-submit_date')


class InterestDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Interest

class CreateInterestView(CreateView):
    redirect_field_name = 'contact/interest_detail.html'

    form_class = InterestForm

    model = Interest

class InterestUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'contact/interest_detail.html'

    form_class = InterestForm

    model = Interest

class InterestDeleteView(LoginRequiredMixin,DeleteView):
    model = Interest
    success_url = reverse_lazy('interest_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'contact/interest_list.html'

    def get_queryset(self):
        return Interest.objects.filter(submit_date__isnull=True).order_by('create_date')


#-------------------COMMENTS----------------------------------
@login_required
def interest_published(request,pk):
    interest = get_object_or_404(Interest,pk=pk)
    interest.publish
    return redirect('interest_detail',pk=pk)

@login_required
def add_comment_to_interest(request,pk):
    interest = get_object_or_404(Interest,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.interest = interest
            comment.save()
            return redirect('interest_detail',pk=interest.pk)

    else:
        form = CommentForm()
    return render(request,'contact/interest_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('interest_detail',pk=comment.interest.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    interest_pk = comment.interest.pk
    comment.delete()
    return redirect('interest_detail',pk=interest_pk)