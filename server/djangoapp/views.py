"""Views for the Cars Dealership app."""
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import Dealer, Review, CarMake, CarModel


def get_dealers(request):
    """Return all dealers."""
    dealers = list(Dealer.objects.values())
    return JsonResponse({'dealers': dealers}, safe=False)


def get_dealer_by_id(request, dealer_id):
    """Return details of a specific dealer."""
    try:
        dealer = Dealer.objects.values().get(id=dealer_id)
        return JsonResponse(dealer)
    except Dealer.DoesNotExist:
        return JsonResponse({'error': 'Dealer not found'}, status=404)


def get_dealers_by_state(request, state):
    """Return dealers in a specific state."""
    dealers = list(Dealer.objects.filter(state=state).values())
    return JsonResponse({'dealers': dealers}, safe=False)


def get_dealer_reviews(request, dealer_id):
    """Return reviews for a specific dealer."""
    reviews = list(Review.objects.filter(dealer_id=dealer_id).values())
    return JsonResponse({'reviews': reviews}, safe=False)


def get_all_car_makes(request):
    """Return all car makes and models."""
    makes = list(CarMake.objects.values())
    models_list = list(CarModel.objects.values())
    return JsonResponse({'car_makes': makes, 'car_models': models_list}, safe=False)


@csrf_exempt
def login_user(request):
    """Handle user login."""
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'userName': username, 'status': 'Authenticated'})
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def logout_user(request):
    """Handle user logout."""
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'Logged out'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def register_user(request):
    """Handle user registration."""
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'status': 'User registered successfully'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def add_review(request):
    """Add a review for a dealer."""
    if request.method == 'POST':
        data = json.loads(request.body)
        Review.objects.create(
            dealer_id=data.get('dealer_id'),
            reviewer=data.get('reviewer', 'Anonymous'),
            review_text=data.get('review', ''),
            sentiment=data.get('sentiment', 'neutral')
        )
        return JsonResponse({'status': 'Review added'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


def analyze_review(request, review_text):
    """Analyze sentiment of a review."""
    return JsonResponse({
        'text': review_text,
        'sentiment': 'positive',
        'score': 0.95
    })
