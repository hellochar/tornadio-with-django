from django.shortcuts import render_to_response

def index(request):
    #import code
    #code.interact(local=locals())
    return render_to_response('app/index.html', {'port' : request.META['SERVER_PORT']})
