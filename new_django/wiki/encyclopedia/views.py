from django.shortcuts import render
from . import util
from django.http import Http404


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, entry):
    if entry  not in util.list_entries():
        return render(request, Http404)
    

    return render(request, {"entry":util.get_entry()} )

