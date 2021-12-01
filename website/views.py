from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import ContatoForm
from django.contrib.auth import logout
from django.contrib.auth.forms import *
import json
from django.views import View
from django.contrib.auth import update_session_auth_hash
from django.conf import settings

# Create your views here.

def index(request):
    form = ContatoForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect("index")
    return render(request, 'website/index.html',{"form": form})

# -------------------------------- CHATTERBOT -------------------------------------------------------------------
'''
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })'''