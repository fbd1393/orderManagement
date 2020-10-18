from django.shortcuts import render

# Create your views here.


def index(request):
    # return render(request, 'travello/index.html')
    # for using second way we need to change dir property in settings file.
    # DIRS': [os.path.join(BASE_DIR, 'templates')]
    return render(request, 'index.html')
