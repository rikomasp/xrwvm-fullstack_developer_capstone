"""URL routing for the djangoapp."""
from django.urls import path
from . import views

urlpatterns = [
    path('get_dealers', views.get_dealers, name='get_dealers'),
    path('get_dealers/<int:dealer_id>', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('get_dealers/state/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('get_cars', views.get_all_car_makes, name='get_all_car_makes'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('register', views.register_user, name='register_user'),
    path('add_review', views.add_review, name='add_review'),
    path('analyze_review/<str:review_text>', views.analyze_review, name='analyze_review'),
]
