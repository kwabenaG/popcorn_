from django.contrib import admin

from .models import Offers, ApplyForm, JobAlert, RequestOffers, Tags, SkillNeeded


class AdminOffer(admin.ModelAdmin):
    list_display = ['offer_name', 'company_name', 'offer_location', 'offer_status', 'offer_min_max_limit', 'user_interested']
    model = Offers
    fields = [
        'user_interested', 'offer_name', 'offer_number', 'company_name', 'offer_location', 'offer_status',
        'offer_min_max_limit', 'offer_phone_number', 'offer_type',
        'company_description', 'offer_description', 'offer_date_created', 'offer_tag', 'skill_qualified_offer'
    ]


admin.site.register(Tags)
admin.site.register(SkillNeeded)
admin.site.register(Offers, AdminOffer)
admin.site.register(JobAlert)
admin.site.register(ApplyForm)
admin.site.register(RequestOffers)



