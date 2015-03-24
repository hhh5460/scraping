from django.shortcuts import render_to_response
from django.template import RequestContext
from fetchcar.models import Car, Brand
from fetchcar.forms import SelectForm

# Create your views here.


def index(request):
	car_list = Car.objects.order_by('-id')
	return render_to_response("fetchcar/index.html",dict(car_list=car_list))


def detail(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if car is None:
        return render_to_response("fetchcar/404.html")
    return render_to_response("fetchcar/detail.html", dict(car=car))


'''def search(request):
		context = {'state': None, "brands": Brand.objects.all().order_by('name')}
		if 'brand' in request.POST:
			print(request.POST['country'])

		return render_to_response("fetchcar/search.html", context)'''

def search(request):
	form = SelectForm
	return render_to_response("fetchcar/search.html", dict(form=form))