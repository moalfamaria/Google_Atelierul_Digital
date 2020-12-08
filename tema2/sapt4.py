# functia lambda
my_sum = lambda a, b : a+b
print(my_sum(2,5))

#lista
players = [{
    'first_name': 'A1',
    'last_name':'B1',
    'rank':3,
},
{
    'first_name': 'A2',
    'last_name':'B2',
    'rank':1
}]
#key primeste o functie
#rank nu e index
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)

x = map(lambda:1, sorted_players)
print(list(x))