from random import randint


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.contacts = {}
        self.interests = {}

    def add_contact(self, contact):
        self.contacts[contact.first_name] = contact
        return self
    def remove_contact(self, contact):
        self.contacts.pop(contact)
        return self
    def add_interest(self, interest):
        self.interests[interest.name] = interest
        return self
    def remove_interest(self, interest):
        self.interests.pop(interest)
        return self

class Interest:
    def __init__(self):
        self.name = ""
        self.activity = None

moral = 5
amoral = 0
immoral = -5

def wheel_of_morality():
    morality = [moral, amoral, immoral]
    while True:
        values = morality[randint(0, len(morality)-1)]
        yield values

class State:
    name=''
    morality = wheel_of_morality()


class Values:
    def __init__(self):
        self.loyalties={"state":{'name':'', 'morality':wheel_of_morality()}, "people":[]}
        self.love = randint(1,100)
        max_love = 100
        self.empathy = randint(1, 10)
        self.honesty = self.empathy+next(self.loyalties['state']['morality'])
        self.respect={'for':{'others':self.empathy+self.love, 'self':self.love+self.honesty}}



class Session:
    def __init__(self):
        self.list_of_interests = []
        self.list_of_people = []
        self.page_width = 50
        self.filler_character = '='
    
    def main_menu(self):
        print("Social Sim".center(self.page_width, self.filler_character))
        print("New Game".center(self.page_width, " "))
        print("Load Game".center(self.page_width, " "))
        print("Options".center(self.page_width, " "))
        print("Quit".center(self.page_width, " "))
        nav = input('>')
        if(nav.lower() == "new game"):
            self.newgame()

    def newgame(self):
        print("You Got to the new game")
        new_person = Values()
        self.list_of_people.append(new_person)
        print(self.list_of_people[0])
'''
begin = Session()
begin.main_menu()
'''

newperson = Values()
print(newperson.honesty)