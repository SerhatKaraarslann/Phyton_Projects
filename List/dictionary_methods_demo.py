"""
player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
"""

#1- add the infos in a list


players = {
    1 : { 
        "name"        : "Cristiano Ronaldo",
        "yearOfBirth" :  1985,
        "nationality" : "Portugal",
        "current_team": "AL Ahli",
        "history"     : "Sporting Lisbon, Manchester United,Real Madrid,Juventus, Al Ahli,Portugal"

    },
    2 :{
        "name"        : "Lionel Messi",
        "yearOfBirth" :  1987,
        "nationality" : "Argentina",
        "current_team": "Inter Miami",
        "history"     : "Barcelona, PSG, Inter Miami, Argentina"

    }
}

print(players)

#2- due to id make a search

id = int(input("Please give an id number for player : "))
print(players.get(id))

#3- due to id delete infos

id = int(input("Please give an id number for player : "))
del players[id]
print(players)

#4 - add new player

id = input("id : ")
name = input('name: ')
nationality = input("nationality: ")
yearOfBirth = input('year of birth: ')
current_team = input('current team: ')
history = input('history: ')

players.update({
    id :
    {
        "name" : name,
        "nationality" : nationality,
        "yearOfBirth" :yearOfBirth,
        "current_team" : current_team,
        "history" : history.split(",")
    }
})

print(players)