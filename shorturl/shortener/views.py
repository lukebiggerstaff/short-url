from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import FormView, DetailView
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError

from .models import Url
from .forms import UrlForm
from . import base34

class Home(FormView):
    form_class = UrlForm
    template_name = 'shortener/home.html'

    def form_valid(self, form):
        form_url = form.cleaned_data['url']
        new_url = Url(url=form_url)
        new_url.save()
        return HttpResponseRedirect(
            reverse(
                'short-url',
                kwargs={'url': base34.encode(new_url.pk)}
            )
        )

class ShortUrl(DetailView):
    model = Url
    template_name = 'shortener/short_url.html'

    def get_object(self):
        url = self.kwargs['url']
        return get_object_or_404(Url, pk=base34.decode(url.lower()))


def redirect_to_url(request, url):
    pk = int(base34.decode(url))
    new_url = get_object_or_404(Url, pk=pk).url
    return redirect(new_url, permanent=True)

def store_and_return_shorturl(request):

    if request.method == 'GET':
        try:
            request_url = request.GET['url']
        except MultiValueDictKeyError as e:
            return JsonResponse(
                {"error" : "Invalid or missing get request"},
                status=400
            )
        new_url = Url(url=request_url)
        try:
            new_url.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=400)
        new_url.save()
        # join the hostname with the encoded primary key
        short_url = request.META['HTTP_HOST'] + '/' + base34.encode(new_url.pk)
        new_url = {
            'old url' : request_url,
            'short url' : short_url,
        }
        return JsonResponse(new_url)
