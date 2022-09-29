from urllib import request


def auth_user(request):
    if request.session.has_key('user_id'):
        return {"isLogin":True}
    else:
        return {"isLogin":False}