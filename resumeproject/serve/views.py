from django.shortcuts import render

# Create your views here.
def serve(self):
    return render(self, 'serve/services.html')