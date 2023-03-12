from importlib.resources import contents
from turtle import tilt, title
from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def markdown_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()#markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPath(request,title):
    htmlContent = markdown_to_html(title)
    if htmlContent == None:
        return render(request,"encyclopedia/handleError.html",{
            "message":"This is an invalid entry"
        })
    else:
        return render(request,"encyclopedia/entries.html",{
            "title": title,
            "content": htmlContent
        })

def search(request):
    if request.method == "POST":
        search_entry = request.POST['q']
        htmlContent = markdown_to_html(search_entry)
        if htmlContent is not None:
            return render(request,"encyclopedia/entries.html",{
               "title": search_entry,
               "content": htmlContent
            })
        else:
            all_entries = util.list_entries()
            listRecommend = []
            for entry in all_entries:
                if search_entry.lower() in entry.lower():
                    listRecommend.append(entry)
            return render(request, "encyclopedia/searchPage.html",{
                "listRecommend":listRecommend
            })

def new_Page(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newPage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exist = util.get_entry(title)
        if title_exist is not None:
            return render(request, "encyclopedia/handleError.html",{
                "message":"This page already exist"
            })
        else:
            util.save_entry(title,content)
            htmlContent = markdown_to_html(title)
            return render(request,"encyclopedia/entries.html",{
                "title": title,
                "content": htmlContent
            })

def editPage(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title":title,
            "content":content
        })

def edit_save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        htmlContent = markdown_to_html(title)
        return render(request,"encyclopedia/entries.html",{
            "title": title,
            "content": htmlContent
        })

def rand(request):
    Enteries = util.list_entries()
    random_entry = random.choice(Enteries)
    htmlContent = markdown_to_html(random_entry)
    return render(request,"encyclopedia/entries.html",{
        "title": random_entry,
        "content": htmlContent
    })