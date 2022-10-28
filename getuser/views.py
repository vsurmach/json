import requests
from django.shortcuts import render, redirect
import pprint

from getuser.models import Chel


users = 'https://jsonplaceholder.typicode.com/users'
posts = 'https://jsonplaceholder.typicode.com/posts'
comments = 'https://jsonplaceholder.typicode.com/comments'

person_id = 1
comm_id = 0


def get_user(request):
    global person_id
    person = Chel.objects.last()
    if person:
        person_id = person.id + 1
    if request.method == 'POST':
        response = requests.get(f'{users}/{person_id}').json()
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
    Chel.objects.all().delete()
    person_id = 1
    return redirect('getuser:get_persons')


def get_detail_user(request, id):
    person = Chel.objects.get(id=id)
    context = {'person': person,
               'id': id,
               }
    return render(request, 'get_detail_person.html', context)


def get_posts(request, id):
    response = requests.get(f'{posts}').json()
    # print(response)
    all_posts = []
    for item in response:
        # print(item)
        if item['userId'] == id:
            all_posts.append(item)
    # print(all_posts)
    context = {'all_posts': all_posts}
    return render(request, 'get_posts.html', context)


def get_comments(request, id):
    response = requests.get(f'{comments}?postId={id}').json()
    # print(response)
    if request.method == 'POST':
        all_comments = []
        global comm_id
        for item in range(len(response)):
            all_comments.append(response[item])
            if item == comm_id:
                comm_id += 1
                break
        context = {'all_comments': all_comments}
        return render(request, 'get_comments.html', context)
    comm_id = 0
    return render(request, 'get_comments.html')
