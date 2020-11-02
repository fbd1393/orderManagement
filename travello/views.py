from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    # return render(request, 'travello/index.html')
    # for using second way we need to change dir property in settings file.
    # DIRS': [os.path.join(BASE_DIR, 'templates')]

    destinations = Destination.objects.all()

    return render(request, 'index.html', {'destinations': destinations})


def newpost(request):
    return render(request, 'new_post.html')
