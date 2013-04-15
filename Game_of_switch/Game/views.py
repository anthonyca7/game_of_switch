# Create your views here.
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, HttpResponseRedirect, render_to_response
from Game import gameboard
from django.http import HttpResponse

def index(request):
    context = {'title':'welcome',
               'message':'Hello this page works prefectly',
                'style' : 'index',
    }
    return render(request, 'Games/index.html', context)


def register(request):
    return HttpResponse("It worked")


def login(request):
    return HttpResponse("log in page")

def board(request):
    game = gameboard.GameBoard()
    game.start()
    gboard = game.board
    return render_to_response("Games/board.html", {"board": gboard})
