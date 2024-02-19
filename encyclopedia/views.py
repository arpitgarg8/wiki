from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . import util
from .forms import entryform
import random


def index(request):
	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries()
	})

def viewentry(request,entryname):
		if entryname in util.list_entries():
			return render(request,'encyclopedia/content.html',{'content':util.get_entry(entryname),'title':entryname})
		else:
			return HttpResponse("PAGE NOT FOUND!!!")
	
def search(request):
	query=request.GET.get('q')
	for entry in util.list_entries():
		entry=entry.upper()
		
		if query.upper() == entry:
			return HttpResponse(util.get_entry(query))
	
	results=[]
	for i in util.list_entries():
		for j in range(len(i)):
			if i[j].upper()==query[0].upper():
				k=0
				q=j
				while i[q].upper()==query[k].upper():
					# 
					while q <len(i) and k<len(query):
						q+=1
						k+=1
						break
					if q==len(i):
						break
					if k==len(query):
						results.append(i)
						break
				if k==len(query):
					break

	if results!=[]:
		return render(request, "encyclopedia/index.html", {"entries": results})
	else:
		return HttpResponse(" Page does not exist")
							#return None
							

def newentry(request):
# if this is a POST request we need to process the form
	if request.method=="POST":
# create  a form instance and populate it with data from POST request
		form=entryform(request.POST)
#check whether form is valid
		if form.is_valid():
			#process the data in form.cleaned_data
			title=form.cleaned_data['title']
			content=form.cleaned_data['content']
			util.save_entry(title,content)
			return HttpResponseRedirect(f'/{title}')

	else:
		form=entryform()
	
	return render(request,"encyclopedia/newentry.html",{"form":form})

def editentry(request,title):
	# return HttpResponse('hello')
	content=util.get_entry(title)
	# form=entryform(initial={"title":title,"content":content})
	if request.method=="POST":
# create  a form instance and populate it with data from POST request
		# form=entryform(request.POST)
		form=entryform(request.POST)
		if form.has_changed():
#check whether form is valid
			if form.is_valid():
				#process the data in form.cleaned_data
				title=form.cleaned_data['title']
				content=form.cleaned_data['content']
				util.save_entry(title,content)
				return HttpResponseRedirect(f'/{title}')
		
	else:
		form=entryform(initial={"title":title,"content":content})
	return render(request,"encyclopedia/newentry.html",{"form":form})


def randompage(request):
	entry=random.choice(util.list_entries())
	return render(request,'encyclopedia/content.html',{'content':util.get_entry(entry),'title':entry})
