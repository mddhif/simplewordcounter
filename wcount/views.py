from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render_to_response
import re, string
from django.views.decorators.csrf import csrf_exempt

text = ""
newtext = ""
myval = 6
def wordcount(req):
	text = req.GET.get('txt')
	
	newtext = ""

	if text is None:
		novalue = 0
	else:

		newtext = re.findall(r'\w+',text)
		
		#newtext =""
		#for c in text:
		#	if c in '!,.? ':
		#		c =""
		#	newtext += c

		 

	novalue = len(newtext)
	myval = novalue

	return render_to_response("typing.html",{"texthere":novalue}) 

@csrf_exempt
def jquery(req):

	

	text = req.POST.get('text', None)
	newtext = ""
	if text is None:
		newtext = "from none"
	else:

		newtext = re.findall(r'\w+',text)
	

	if(len(newtext) >= 50):
		return HttpResponse("max reached")

	return HttpResponse(len(newtext))

