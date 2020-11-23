from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from pprint import pprint
# Create your views here.

@login_required
def page(request):
    user=request.user.username
    logout(request)
    if "?" in request.get_raw_uri():
        query_string=request.get_raw_uri().split("?", 1)[1]
    else:
        query_string=""
    return HttpResponse(user + " - " + query_string)