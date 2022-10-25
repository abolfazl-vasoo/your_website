from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


# class IndexPage(TemplateView):
#     template_name = "home_module/index_page.html"
from site_module.models import SiteSetting


class ContactPage(TemplateView):
    template_name = "home_module/contact-us.html"


def index(request):
    return render(request, 'home_module/index_page.html')


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    # footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        # 'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_component.html', context)
