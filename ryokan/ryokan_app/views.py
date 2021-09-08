from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(self.request, self.template_name, context)