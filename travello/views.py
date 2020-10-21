from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    # return render(request, 'travello/index.html')
    # for using second way we need to change dir property in settings file.
    # DIRS': [os.path.join(BASE_DIR, 'templates')]

    destination1 = Destination()
    destination1.name = 'Hawaii'
    destination1.desc = 'The most beautiful island in the world.'
    destination1.price = '900$'
    destination1.img = 'destination_1.jpg'
    destination1.offer = False

    destination2 = Destination()
    destination2.name = 'Malaysia'
    destination2.desc = 'A great place to visit.'
    destination2.price = '750$'
    destination2.img = 'destination_2.jpg'
    destination2.offer = False

    destination3 = Destination()
    destination3.name = 'San Francisco'
    destination3.desc = 'Most expensive city in the USA.'
    destination3.price = '1050$'
    destination3.img = 'destination_3.jpg'
    destination3.offer = True

    destinations = [destination1, destination2, destination3]

    return render(request, 'index.html', {'destinations': destinations})
