#!/usr/bin/python3

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from random import randint

# This view will return a 404 response
def ierror(request):
    return HttpResponseNotFound("Page was not found")
    
def success(request):
    return HttpResponse("Page was found")


def customheader(request):
    x = {}
    x['learning'] = 'Django' # string:string
    x['speed'] = 55          # string:integer
    x['server'] = 'nonyabuisness'

    return HttpResponse(headers=x)  # adds our custom headers to the response

def customcode(request):
    return HttpResponse("Working on that", status=201)  # return teh response code 201 "created"

def random_response(request):
    roll = randint(1, 10)

    if roll < 3 :
        return HttpResponse("unauthorized", status=401)
    if roll >= 3 and roll < 5 :
        return HttpResponse("forbidden", status=403)
    if roll >= 5 and roll < 7:
        return HttpResponseNotFound
    if roll >= 7 and roll < 9:
        return HttpResponse("whoopsie", status=501)
    if roll >= 9 :
        return HttpResponse("SUCCESS You did it!")

