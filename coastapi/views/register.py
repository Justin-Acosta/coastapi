import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from coastapi.models import Player

@csrf_exempt
def login_user(request):
    # {
    #     "username": "boonie",
    #     "password": "fart"
    # }

    body = request.body.decode('utf-8')
    req_body = json.loads(body)

    if request.method == 'POST':

        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key, "id": authenticated_user.id})
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

    return HttpResponseNotAllowed(permitted_methods=['POST'])


@csrf_exempt
def register_user(request):
    # {
	# "username": "boonie",
	# "password": "fart",
	# "email": "fart@fart.com",
	# "first_name": "Justin",
	# "last_name": "Acosta",
    # "nickname": "farter"
    # }

    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    player = Player.objects.create(
        nickname=req_body['nickname'],
        user = new_user,
    )

    player.save()

    token = Token.objects.create(user=new_user)

    data = json.dumps({"token": token.key, "id": new_user.id})
    return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)
