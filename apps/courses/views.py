from django.shortcuts import render, redirect, HttpResponse
from .models import Course
# Create your views here.
def index(request):
	context = {
	"course" : Course.objects.all()  
	}
	
	return render(request, 'courses/index.html', context)




def add(request):
	if request.method == 'POST':
		
		Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
		print(Course.objects.all())
		return redirect('/')



def confirm(request, id):
	if request.method == 'GET':
		print id
		context = {
		"course" : Course.objects.get(id=id)
		}

	
	return render(request, 'courses/confirmation.html', context)



def delete(request, id):
	if request.method == 'POST':
		print 'check for post'
		if request.POST['name'] == 'yes':
			Course.objects.get(id=id).delete()
			print 'check inside'
			print id

		return redirect('/')


