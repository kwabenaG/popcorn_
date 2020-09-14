# from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
#
# from .models import Offers
# from OfferRequest.forms import RequestOfferForm
#
#
# # offers view methods
# def offers(request):
#     offers_all = Offers.objects.all()
#     # pagination
#     context = {'offers': offers_all}
#     return render(request, 'content/offers/offer_index.html', context)
#
#
# # view order details
# def spy_offers(request, offerlabel):
#     get_current_user = request.user
#     offer_item = get_object_or_404(Offers, id=offerlabel)
#     offer_order_forms = RequestOfferForm(instance=offer_item)
#     context = {'offer_item': offer_item, 'offer_req_forms': offer_order_forms, 'current_user': get_current_user}
#     return render(request, 'content/offers/offer_detail.html', context)
#
#
# # send request over to admin
# def order_offer(request):
#     get_current_user = request.user
#     # check the http incoming request
#     if request.method == 'POST':
#         request_form = RequestOfferForm(request.POST)  # declare the Offer request form
#         if request_form.is_valid():  # check the the form validity
#             print(request_form.errors)
#         HttpResponse('not POSTed')
#         # return to a page if validity returns true
#     # redirect to a page if the validity returns to false
#
#
