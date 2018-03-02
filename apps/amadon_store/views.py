from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "Success!"
	return HttpResponse(response)