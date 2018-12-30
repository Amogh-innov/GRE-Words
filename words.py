import os

def check( cfil,val ):
    for line in cfil:
        lin = line.split(":")
        if lin[0].upper() == val.upper():
            return "there"
    else:
        return "not_there"

def add( cfil,val,key ):
    cfil.write(val+":"+key+"\n")
    return "done"

def file():
    
    import os
    if not os.path.exists('words.txt'):
        opn = open('words.txt','w')
        n=0
        
    else:
        opn = open('words.txt','a')
        n=1
        
    return opn,n

def addw():
    
    import os
    vall = input("Enter the word            : ")
    fil,cr = file()

    if cr==0 :
        ke = input("Enter the meaning         : ")
        work = add( fil,vall,ke )
        
    else :
        sfil = open('words.txt','r')
        see = check( sfil,vall )
        if see == "not_there":
            ke = input("Enter the meaning         : ")
            work = add( fil,vall,ke)
        else :
            print()
            print("Redundant word")
            work=""
            fil.close()

    if work == "done":
        print()
        print("Word added sucessfully")
        fil.close()
        
    else :
        print("Try other word")
        fil.close()

def wdisplay():
    
    import os

    if not(os.path.exists('words.txt')) :
        print("Nothing to display")
        menu()
        
    else:
        rfil = open('words.txt','r')
        print()
        print()
        info1 = '{0:7s}{1:20s}{2:40s}'.\
                format("S.no","Word","Meaning")
        print(info1)
        print()
        print()
        a=0    
        for lin in rfil:
            a=a+1
            lin = lin.split(':')
            info = '{0:7s}{1:20s}{2:40s}'.\
                    format(str(a).rjust(4),lin[0],lin[1])
            print(info)
            
        rfil.close()

def wsearch():
    
    import os
    found = 0
    if not(os.path.exists('words.txt')) :
        print("Nothing to display")
        menu()
    
    else:
        vall = input("Enter the word to search  : ")
        rfil = open('words.txt','r')
        for line in rfil:
            lin = line.split(":")
            if lin[0].upper() == vall.upper():
                found = 1
                print()
                info1 = '{0:10s}{1:32s}'.\
                    format("Word","Meaning")
                info = '{0:10s}{1:32s}'.\
                    format(lin[0],lin[1])
                print(info1)
                print(info)

    if found == 0:
        print()
        print("Not Found in the file")

    rfil.close()


def menu():

    print()
    print("Gre Words")
    ext = False
    try:
        while not ext:
            print()
            print("""1.Entry
2.Display
3.Search
4.Exit""")
            print()
            opt = int(input("Enter the option (1-4)    : \t"))
            print()

            if opt == 1:
                addw()

            elif opt == 2:
                wdisplay()

            elif opt == 4:
                ext = True

            elif opt == 3:
                wsearch()
                
            else:
                print("Invalid input")
            
    except :
            print()
            print("Invalid input plz try again")

menu()
