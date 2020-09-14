from django.urls import path, include

from . import views

urlpatterns = [
    # offer urls
    path('offers', views.offers, name='offers'),
    path('offers/<str:offerlabel>', views.spy_offers, name='offerItem'),
    path('offers-pick', views.order_offer, name='offer_order'),  # submit pick offer url

]