from django.shortcuts import render,redirect,get_object_or_404
from Bitly.form import createform
from Bitly.models import Links
# Create your views here.


def home(requests):
    all_links=Links.objects.all()
    context={'all_links':all_links}
    return render(requests,'Bitly/index.html',context)

def createforms(requests):
    if requests.method=="POST":
        form=createform(requests.POST)
        if form.is_valid():
            form.save()
            return(redirect('home'))
    else:
        form=createform()
    context={"forms":form}
    return(render(requests,'Bitly/create.html',context))

def redict(requests,slug):
    actual_url=get_object_or_404(Links,slug=slug).url

    return redirect(actual_url)
