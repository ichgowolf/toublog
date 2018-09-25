from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.


def post_create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "SAVED!!")
    return HttpResponseRedirect(instance.get_absolute_url())

  
  context = {
    "form": form,
  }
  return render(request, "post_form.html", context)



def post_details(request, id=None):
  instance = get_object_or_404(Post, id=id)
  context = {
    "title": instance.title,
    "instance": instance,
    
  }
  return render(request, "post_details.html", context)



def post_lists(request):
  # if request.user.is_authenticated:
  #   context = {
  #     "title":  "my user list"
  #   }
  # else:
  #   context = {
  #     "title": "list"
  #   }
  queryset_list = Post.objects.all() #.order_by("-timestamp") orders by time in view bu being done in model
  paginator = Paginator(queryset_list, 25) # 25 is num of post per page 
  page_request_var = "abc"
  page = request.GET.get(page_request_var)
  queryset = paginator.get_page(page)
  context = {
      "object_list": queryset,
      "title": "list",
      "page_request_var": page_request_var
    }
  return render(request, "post_list.html", context, page_request_var)


def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=instance)
  
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "UPDATED!!")
    return HttpResponseRedirect(instance.get_absolute_url())
  
  context = {
    "title": instance.title,
    "instance": instance,
    "form": form,
    
  }
  return render(request, "post_form.html", context)


 


  

def post_delete(request, id=None):
  instance = get_object_or_404(Post, id=id)
  instance.delete()
  messages.success(request, "Deleted!!")
  return redirect("posts:list")
