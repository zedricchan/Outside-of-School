#inventory with 10 item slots
#every item slot can contain 10 items of the same kind
#if slot exceeds 10 items, new slot is used 
bag = []
bagcounter = []
#Add item
def add():
    v = True
    while v:
        ad = input("What item would you like to put in the inventory? ").lower()
        #add a new variable
        if ad not in bag and len(bag) < 10:
            bag.append(ad)
            bagcounter.append('1')
            print(bag)
            print(bagcounter)
        #add up the number within the slot
        elif ad in bag and int(bagcounter[bag.index(ad)]) < 10 and len(bag) < 10:
            new = str(int(bagcounter[bag.index(ad)]) + 1)
            bagcounter.remove(bagcounter[bag.index(ad)])
            bagcounter.insert(bag.index(ad), new)
            print(bag)
            print(bagcounter)
        elif ad not in bag and len(bag) == 10:
            print("All slots have been used. Unable to add new items. ")
        #new slot used due to too many items in 1 slot
        else:
            bag.append(ad)
            bagcounter.append('1')
            print(bag)
            print(bagcounter)
        more = input("Would you like to add more items in the inventory? Y/N ").upper()
        while more != 'Y' and more != 'N':
            print("Enter either Y or N. ")
            more = input("Would you like to add more items in the inventory? Y/N ").upper()
        if more == 'Y':
            v = True
        else:
            v = False
    return
#Remove item
def remov():
    p = True
    while p:
        re = input("What item would you like to remove from the inventory? ").lower()
        while re not in bag:
            print("{} is not in the inventory. ".format(re))
            re = input("What item would you like to remove from the inventory? ").lower()
        if int(bagcounter[bag.index(re)]) > 1: #can still be removed if item amount is 1
            hm = str(int(bagcounter[bag.index(re)]) - 1)
            bagcounter.remove(bagcounter[bag.index(re)])
            bagcounter.insert(bag.index(re), hm)
            print(bag)
            print(bagcounter)
        elif int(bagcounter[bag.index(re)]) == 1: #no more after removal resulting in removing the slot
            bagcounter.remove(bagcounter[bag.index(re)])
            bag.remove(re)
            print(bag)
            print(bagcounter)
        less = input("Would you like to remove more items from the inventory? Y/N ").upper()
        while less != 'Y' and less != 'N':
            print("Enter either Y or N. ")
            less = input("Would you like to remove more items from the inventory? Y/N ").upper()
        if less == 'Y':
            p = True
        else:
            p = False
#Let user choose to add or remove item
def choose():
    print(bag)
    print(bagcounter)
    adorre = input("Would you like to add items or remove items from the inventory? A/R ").upper()
    while adorre != 'A' and adorre != 'R':
        print("Enter either A or R. ")
        adorre = input("Would you like to add items or remove items from the inventory? A/R ").upper()
    if adorre == 'A':
        add()
        any = input("Do you want to remove item too? Y/N ").upper()
        while any != 'Y' and any != 'N':
            print("Enter either Y or N. ")
            any = input("Do you want to remove item too? Y/N ").upper()
        if any == 'Y':
            remov()
    else:
        remov()
        lol = input("Do you want to add in item too? Y/N ").upper()
        while lol != 'Y' and lol != 'N':
            print("Enter either Y or N. ")
            lol = input("Do you want to add in item too? Y/N ").upper()
        if lol == 'Y':
            add()
#Main program
choose()
