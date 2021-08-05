from django.shortcuts import render
import requests
import json
from django.http.response import JsonResponse

# Create your views here.
def dashboard(request):
    '''
    Show dashboard.
    '''

    return render(request, 'index.html')

def test_site(request):
    '''
    Run tests and return JSON.
    '''

    try:
        web_site = request.GET.get('testSite')
        get_site = requests.get(web_site)
    except Exception as err:
        print(err)
        get_site = None
        

    site_status = get_site.status_code if get_site else None
    site_dict ={'site': site_status}

    data = json.dumps(site_dict)

    return JsonResponse(data=data, safe=False)