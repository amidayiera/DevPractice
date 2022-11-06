from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students' : Student.objects.all()
    })
    # 'students' name of the variable that the html template will have access to
    # on the right : value that the variable students takes on