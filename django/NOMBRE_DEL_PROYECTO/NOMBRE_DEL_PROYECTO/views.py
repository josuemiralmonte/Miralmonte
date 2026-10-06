from django.shortcuts import render #missed code


#When homepage has been directed we will receive the word Hello World 
def homepage(request):

        #step 5: we now change the hello world behaviour for the html request
        return render(request, 'home.html')



