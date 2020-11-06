import re
from django.db import connection
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Character, Connections, Log

def error_report(request, errors):
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return True
    else:
        return False

# Create your views here.
def index(request):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        current_user = User.objects.get(id=request.session['current_user'])
        characters = current_user.characters.all()
        request.session['location']='/main/title'
        context = {
            'user': current_user,
            'characters': characters
        }
        return render(request, 'main/index.html', context)

def create_character(request):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method =='POST':
        errors = Character.objects.character_validator(request.POST)
        if error_report(request, errors):
            return redirect(f"{request.session['location']}")
        else:
            current_user = User.objects.get(id=request.session['current_user'])
            Character.objects.create(player=current_user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], bio=request.POST['bio'])
            return redirect(f"{request.session['location']}")
    else:
        return redirect('/')

def add_contact(request):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method =='POST':
        errors = Connections.objects.connection_validator(request.POST)
        if error_report(request, errors):
            return redirect(f"{request.session['location']}")
        else:
            current_character = Character.objects.get(id=request.POST['who'])
            selected_character = Character.objects.get(id=request.POST['to_whom'])
            current_character.connections.create(contact=selected_character)
            return redirect(f"{request.session['location']}")
    else:
        return redirect(f"{request.session['location']}")

def remove_contact(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method =='POST':
        current_connection = Connections.objects.get(id=id)
        connection_owner = current_connection.owner
        print(current_connection)
        print(connection_owner.connections.filter(id=current_connection.id))

        if connection_owner.connections.filter(id=current_connection.id):
            current_connection.delete()
            return redirect(f"/main/title")
        else:
            return redirect(f"/main/title")
    else:
        return redirect(f"/main/title")


def about(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    elif Character.objects.filter(id=id):
        request.session['location']=f'/main/about/{id}'
        current_character =Character.objects.get(id=id)
        other_people = []
        for connections in current_character.connections.all():
            for people in connections.contact.connections.all():
                if people.contact.id == current_character.id:
                    other_people.append(people)
        context={
            'character': current_character,
            'people': other_people,
            'logs': Log.objects.all()
        }
        return render(request, 'main/about.html', context)
    else:
        return redirect(f"{request.session['location']}")

def edit_character(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method == "POST":
        if Character.objects.filter(id=id):
            current_character = Character.objects.get(id=id)
            errors = Character.objects.character_validator(request.POST)
            if error_report(request, errors):
                return redirect(f"{request.session['location']}")
            else:
                current_character.first_name= request.POST['first_name']
                current_character.last_name = request.POST['last_name']
                current_character.bio = request.POST['bio']
                current_character.save()
                return redirect(f"{request.session['location']}")
        else:
            return redirect(f"{request.session['location']}")
    else:
        return redirect(f"{request.session['location']}")

def delete(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    elif Character.objects.filter(id=id):
        current_user = User.objects.get(id=request.session['current_user'])
        current_character = Character.objects.get(id=id)
        if current_user == current_character.player:
            current_character.delete()
    return redirect(f"/main/title")

def interact(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method== "POST":
        if Connections.objects.filter(id=id):
            current_connection = Connections.objects.get(id=id)
            def act(value, word):
                for people in current_connection.contact.connections.all():
                    if people.contact == current_connection.owner:
                        people.opinion += int(value)
                        people.save()
                Log.objects.create(connection=current_connection, actor=current_connection.owner, action=word, recipient=current_connection.contact, result=value)
            if 'compliment' in request.POST:
                act(10, 'Complimented')
            elif 'help' in request.POST:
                act(15, 'Helped')
            elif 'save' in request.POST:
                act(20, 'Saved')
            elif 'insult' in request.POST:
                act(-10, 'Insulted')
            elif 'hinder' in request.POST:
                act(-15, 'Hindered')
            elif 'attack' in request.POST:
                act(-20, 'Attacked')
    return redirect(f"{request.session['location']}")
#====================TODO:=========================#
    #===== Add Update Function for Connections
    #===== Add Interaction system
        #===== 2 types of Interactions
            #===== Positive & Negative
                #===== Positive increases character opinion
                #===== Negative decreases character opinion
            #===== 3 degrees of Interaction
                #===== (Values Subject to change)
                #===== Positive:
                    #===== compliment= +5
                    #===== help = +10
                    #===== defend = +15
                #===== Negative:
                    #===== insult = -5
                    #===== hinder = -10
                    #===== attack = -15
    #===== Add Interaction Buttons on main screen
    #===== Add relationship value system
        #===== Character1.opinion + Character2.opinion
        #===== if either C1 or C2 does not have relationship
        #===== designate as one-sided relationship
        #===== if relationship value > 50 
        #===== cascade effects apply
    #===== Add Cascading relationship system
        #===== EXAMPLE:
            #===== character1, character2, and character3 all know each other:
            #===== if character1 negatively impacts character2,
            #===== and character3 likes character2, character3
            #===== decreases their opinion of character1
        #===== if any involved parties do not know the other,
        #===== only those directly interacting are effected
#==================================================#