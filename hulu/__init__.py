from django.http import HttpResponse
import json

def jsonp(request, content):
    if request.GET.get('callback'):
        callback = request.GET.get('callback').strip()
        return HttpResponse(callback + '(' + json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=4) + ')', content_type="application/json; charset=utf-8")
    else:
        return HttpResponse(json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=4), content_type="application/json; charset=utf-8")

def resetdb():
    from django.db import connection
    try:
        conn = connection.cursor()
    except OperationalError:
        connected = False
        connection.close()
    else:
        connected = True

def setdomain():
    try:
        if Site.objects.all():
            site = Site.objects.get_current()
            if site.domain != request.get_host():
                site.domain = request.get_host()
                site.save()
        else:
            site = Site()
            site.domain = request.get_host()
            site.save()
    except Site.DoesNotExist:
        site = None
