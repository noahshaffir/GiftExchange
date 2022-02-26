from random import randint
from copy import deepcopy
def pair_name(names):
    counter=0
    true_length = deepcopy(len(names))
    while counter < true_length:
        i = randint(0, len(names)-1)
        j = randint(0,len(names)-1)
        while i == j:
            i = randint(0, len(names)-1)
        first_name = names[i]
        second_name = names[j]
        print(f"{first_name} got paired with {second_name}")
        names.remove(first_name)
        names.remove(second_name)
        counter+=2
def santa(names):
    firsts=[]
    seconds=[]
    counter=0
    true_length = deepcopy(len(names))
    while counter < true_length:
        i = randint(0, len(names)-1)
        j = randint(0,len(names)-1)
        while i == j:
            i = randint(0, len(names)-1)
        first_name = names[i]
        second_name = names[j]
        print(f"{first_name} gets a gift from {second_name}")
        names.remove(first_name)
        names.remove(second_name)
        firsts.append(first_name)
        seconds.append(second_name)
        counter+=2
    counter = 0
    true_length = deepcopy(len(firsts))
    while counter < true_length:
        i = randint(0, len(firsts)-1)
        j = randint(0,len(seconds)-1)
        first_name = firsts[i]
        second_name = seconds[j]
        print(f"{second_name} gets a gift from {first_name}")
        firsts.remove(first_name)
        seconds.remove(second_name)
        counter+=1
