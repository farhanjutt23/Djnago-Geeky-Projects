from django.shortcuts import render

# Create your views here.
def home(self):
    return render(self, 'core/home.html')
def contact(self):
    return render(self, 'core/contact.html')
