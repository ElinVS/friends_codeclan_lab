
def get_name(person5):
 return person5["name"]

def get_favourite_tv_show(banana):
    return banana["favourites"]["tv_show"]

def likes_to_eat(person,food):
    fav_snacks = person["favourites"]["snacks"]
    
    for snack in fav_snacks:
        if food == snack:
           return True
       
    return False

def add_friend(person,friend):
    banana = person["friends"]

    banana.append(friend)

def remove_friend(person,friend):
    banana = person["friends"]

    banana.pop(0)

def total_money():

    total = 0

    






   

    


