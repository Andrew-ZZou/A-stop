from django.shortcuts import render

# Create your views here.
def backdoor(request):
    return render(request, 'backdoor.html')

def management(request):
    return render(request, 'management.html')