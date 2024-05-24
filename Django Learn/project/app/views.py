from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView,DeleteView
from django.urls import reverse_lazy
from.models import Person, Profile
# def Hello(request):
#     return HttpResponse("Hello it's me Prashant")


# def About(request):
#     context = {
#         "variable": 5,
#         "user": {
#             "name": "John",
#             "age": 30,
#             "hobbies": ["coding", "gaming", "Riding", "Travelling"],
#         },
#         "script": "<script> alert('Hello')  </script>"
#     }
   

#     return render(request, "app/about.html",context)

# def Gallery(request):
#     return HttpResponse("This is an gallery page")

# def Service(request):
#     return HttpResponse("This is an service page")

# def Contact(request):
#     return HttpResponse("This is an contact page")

# def person(request,person_id):
#     return HttpResponse(F"Person's id is :{person_id}")


class HomeView(TemplateView):
    template_name="app/about.html"

class PersonListView(ListView):
    model = Person
    context_object_name = "Person"

class PersonDetailView(DetailView):
    model = Person 
    context_object_name="Person"

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url=reverse_lazy("app:Person List")

class PersonDeleteView(DeleteView):
    model = Person
    context_object_name = "Person"
    success_url=reverse_lazy("app:Person List")




    

    


