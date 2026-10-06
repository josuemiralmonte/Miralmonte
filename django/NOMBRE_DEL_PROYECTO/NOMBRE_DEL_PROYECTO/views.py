from django.http import HttpResponse

#When homepage has been directed we will receive the word Hello World 
def homepage(request):
    return HttpResponse("Hello World!")