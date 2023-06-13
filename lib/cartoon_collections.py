def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf) + 1}. {dwarf}')


def summon_captain_planet(planeteers):
    planeteers_list = []
    for planeteer in planeteers:
        planeteers_list.append(f'{planeteer.capitalize()}!')
    
    return planeteers_list


# With list comprehension
# def summon_captain_planet(planeteers):
#     return [planeteer.capitalize() + '!' for planeteer in planeteers]

# Short version with 'any' function
# def long_planeteer_calls(words):
#     return any(len(word) > 4 for word in words)

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
        
    return False    

# With list comprehension
# def find_the_cheese(snacks):
#     cheese_list = ["cheddar", "gouda", "camembert"]
#     cheese_in_snacks = [snack for snack in snacks if snack in cheese_list]
#     return ''.join(cheese_in_snacks) or None

def find_the_cheese(snacks):
    cheese_list = ["cheddar", "gouda", "camembert"]

    for snack in snacks:
        if snack in cheese_list:
            return snack
        
    return None    