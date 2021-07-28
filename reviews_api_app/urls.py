from django.urls import path
from .views import ReviewsListView
from .views import ReviewsDetailsView


urlpatterns = [
    
    path('', ReviewsListView.as_view(), name='reviws_api'), 
  

    path('<int:pk>', ReviewsDetailsView.as_view(), name='details_api'), 
   
]