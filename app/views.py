from django.shortcuts import render

# Create your views here.
 from django.http import HttpResponse
 from django.shortcuts import render_to_response
 from django.template import Context, loader
 from django.http import Http404

 def index(request):
     return render(request, "static/index.html")