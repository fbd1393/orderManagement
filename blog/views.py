from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title': 'BlogHome',
    }
    return render(request, 'blog/home.html', context)


def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    result = num1 + num2
    return render(request, 'blog/add.html', {'add_result': result})


def multiple(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 * num2
    return render(request, 'blog/multiple.html', {'multiple_result': result})


def submission(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    if num1 >= num2:
        result = num1 - num2
    else:
        result = 'num1 should bigger than num2!'

    return render(request, 'blog/submission.html', {'submission_result': result})
