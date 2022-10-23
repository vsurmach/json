import requests
from django.shortcuts import render, redirect
import pprint

from getuser.models import Chel


url = 'https://jsonplaceholder.typicode.com/users'
person_id = 1

def get_user(request):

    global person_id
    person = Chel.objects.last()
    if person:
        person_id = person.id + 1
    if request.method == 'POST':
        response = requests.get(f'{url}/{person_id}').json()
        # print(response)
        model = Chel()
        model.id = response['id']
        model.name = response['name']
        model.username = response['username']
        model.phone = response['phone']
        model.addr_city = response['address']['city']
        model.save()
        # print(model.username)
    all_person = Chel.objects.all()
    context = {'all_person': all_person,
               'person_id': person_id,
               }
    return render(request, 'get_person.html', context)

def delete_users(request):
    global person_id
    if request.method == 'POST':
        Chel.objects.all().delete()
        person_id = 1
        return redirect('getuser:get_persons')


def get_detail_user(request, id):
    person = Chel.objects.get(id=id)
    context = {'person': person}
    return render(request, 'get_detail_person.html', context)