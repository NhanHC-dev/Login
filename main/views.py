from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'content/templates/main/index.html'
