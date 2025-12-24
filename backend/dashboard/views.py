from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from offers.models import Offer
from chat.models import Message

def dashboard_home(request):
    product_count = Product.objects.count()
    offer_count = Offer.objects.count()
    message_count = Message.objects.count()

    active_offers = Offer.objects.filter(active=True).count()
    inactive_offers = Offer.objects.filter(active=False).count()

    context = {
        'product_count': product_count,
        'offer_count': offer_count,
        'message_count': message_count,
        'active_offers': active_offers,
        'inactive_offers': inactive_offers,
    }

    return render(request, 'dashboard/home.html', context)
def home(request):
    return HttpResponse("LiveLens backend is running successfully")
#step-8.10.1 new code
def dashboard_stats(request):
    data = {
        "products":Product.objects.count(),
        "offers":Offer.objects.filter(active=True).count(),
        "Message":Message.objects.count(),
    }
    return JsonResponse(data)