from django.urls import path
from .import views

app_name = "app"

urlpatterns = [
    #static paths
    # path("", views.Hello, name = "Hello"),
    # path("about/",views.HomeView.as_view(),name = "About"),
    path("personlist/",views.PersonListView.as_view(),name = "Person List"),
    path("person/<int:pk>",views.PersonDetailView.as_view(), name= "Person Detail"),
    path("person/create/", views.PersonCreateView.as_view(), name= "Create View"),
    path("person/delete/<int:pk>", views.PersonDeleteView.as_view(), name= "Delete View")
    
    # path("service/",views.Service,name="Service"),
    # path("contact/",views.Contact,name="Contact"),
    # path("gallery/",views.Gallery,name="Gallery"),

    # #dynamic paths
    # path("person/<int:person_id>",views.person, name ='person')

]
