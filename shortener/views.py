from django.http import HttpResponse
from django.shortcuts import render, redirect
from scripts.main import ParentValues
from scripts.gen import Generator
from scripts.retrieval import Retrieve

# Create your views here.
output = ''


def home(request):
    return render(request, 'html/index.html', {'input': '', 'output': output})


def upload(request):
    urlobject = Generator()
    output = urlobject.validateURL(request.POST['entry'])
    # print(output + 'lol')
    return render(request, 'html/index.html', {'input': '', 'output': output})


def a(request):
    part = request.GET['i']  # i is key associated to value. e.g. localhost:8000/a?i=ooo
    print(part)
    # gotta append https:// to link
    r = Retrieve(part)
    return redirect(r.searchLink())
    # call retrieval for 'part' variable
