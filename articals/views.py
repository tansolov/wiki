from django.shortcuts import render
# from . import util
from encyclopedia import util


def index(request):
     return render(request,"wiki/entries",{
    "entries": util.get_entry("entries/{title}.md")
    })
