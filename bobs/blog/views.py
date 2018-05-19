# Create your views here.
from django.shortcuts import render_to_response
from bobs.blog.models import posts
from django.shortcuts import render

def home(request):
	ent=posts.objects.all()[:5]
	return render_to_response('index.html', {'posts' :ent})
	#return render(request, 'tempelates/index.html')