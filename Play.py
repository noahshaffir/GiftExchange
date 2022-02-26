import GiftExchange
cont = True #if user wants to continue 
names = []
while cont:
    name = input("Please enter a name to the gift exchange. Say 'Done' if you are done, must be an even number of names.")
    if name == "Done":
        cont = False
    else:
        names.append(name)
if len(names)%2!=0:
    name=input("There needs to be an even number of names in a gift exchange. Add another name here.")
    names.append(name)
GiftExchange.pair_name(names)
