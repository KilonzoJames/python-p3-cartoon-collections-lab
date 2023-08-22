def roll_call_dwarves(l):
    for index, dwarf in enumerate(l):
        print(f'{index+1}. {dwarf}')
my_list=["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(my_list)

def summon_captain_planet(p):
    list_comprehension=[planet.capitalize() + "!" for planet in p]
    print(list_comprehension)
    # or
    new_planet=[]
    for planet in p:
        modified_plan=planet.capitalize() + "!"
        new_planet.append(modified_plan)
    return new_planet
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
print(summon_captain_planet(planeteer_calls))

def long_planeteer_calls(calls):
    for call in calls:
        if len(call)>4:
            return True
    return False
short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))

def find_the_cheese(foods):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for snack in foods:
        if snack in cheese_types:
            return snack
    return None
snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks))
