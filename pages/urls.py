# dir - pages - url

from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.home_page_view, name='homepage'),  # homepage
    
    path('offer-details/<uuid:offer_type_id>',
         views.display_latest_offer_details, name='page-offers-details'),  # GET all job or intern offers
    path('latest-offer/request-offer-claim', views.send_offer_request, name='request_offer_send'),  # offer request
    path('get-job-alerts', views.get_job_alerts, name='job-alerts'),  # job alert

    # category url links
    path('category/category-education/', views.education_training, name='cat-education'),
    path('category/category-human-resource/', views.human_resource, name='cat-human-resource'),
    path('category/category-accounting-finance/', views.accounting_finance, name='cat-accounting-finance'),
    path('category/category-telecom/', views.telecom, name='cat-telecom'),
]

