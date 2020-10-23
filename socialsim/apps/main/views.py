from django.shortcuts import render, redirect
from .models import User, Character, Connections

# Create your views here.
def index(request):
    current_user = User.objects.get(id=request.session['current_user'])
    characters = current_user.characters.all()

    context = {
        'user': current_user,
        'characters': characters
    }
    return render(request, 'main/index.html', context)

def create_character(request):
    current_user = User.objects.get(id=request.session['current_user'])
    new_character = Character.objects.create(player=current_user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'], title=request.POST['title'])
    return redirect('/main/title')

def add_contact(request):
    current_character = Character.objects.get(id=request.POST['who'])
    selected_character = Character.objects.get(id=request.POST['to_whom'])
    current_character.connections.create(contact=selected_character, opinion=100)
    return redirect("/main/title")


#====================TODO:=========================#
    #===== Prettify UI
    #===== Add Update Function for Characters
    #===== Add Update Function for Connections
    #===== Add About Page for each Character
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