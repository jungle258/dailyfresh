from django.http import HttpResponseRedirect


def login_decorator(func):
    def login_func(request, *args, **kwargs):
        if request.session.has_key('id'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_func
