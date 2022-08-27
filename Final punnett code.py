dictmono={'TT':"Tall plant",'Tt':"Tall plant",'tt':"Dwarf plant",
          'YY':"Yellow seed",'Yy':"Yellow seed",'yy':"Green seed",
          'GG':"Green pod",'Gg':"Green pod",'gg':"Yellow pod",
          'AA':"Axial flowering",'Aa':"Axial flowering",'aa':"Terminal flowering",
          'VV':"Violet flower",'Vv':"Violet flower",'vv':"White flower",
          'II':"Inflated pod",'Ii':"Inflated pod",'ii':"Constricted pod",
          'RR':"Round seed",'Rr':"Round seed",'rr':"Wrinkled seed"}
w=["height","pod colour","pod shape","flower position","seed colour","seed shape","flower colour","1","2","3","4","5","6","7"]
def mpheno(io,nulm):
    if io in nulm and io in dictmono:
        print("The Phenotype of the desired Genotype is: ",end=" ")
        return dictmono[io]
    else:
        return "YOU HAVE ENTERED A WRONG GENOTYPE !..."

def dpheno(ip,nuldi):
    lg=[ip[0:2],ip[2:4]]
    if ip in nuldi and lg[0] in dictmono and lg[1] in dictmono:
        print("Phenotype is: ",end=" ")
        return dictmono[lg[0]]+" and "+dictmono[lg[1]]
    else:
        return "YOU HAVE ENTERED A WRONG GENOTYPE !..."
print("|--------------------------------------------------------------------------|")
print("|                       **PUNNETT SQUARE GENERATOR**                       |")
print("|                                                                          |")
print("|  *Punnett Square is a graphical representation of all possible genotypes |")
print("|    of offsprings in a genetic cross.                                     |")
print("|  *It was developed by a British geneticist REGINALD.C. PUNNETT.          |")
print("|                                                                          |")
print("|                              **INSTRUCTIONS**                            |")
print("|  1.Follow the statements in the code and enter the values accordingly.   |")
print("|  2.Once the value entered cannot be retraced back.                       |")
print("|  3.For Monohybrid genetic cross,                                         |")
print("|      *format of the genotype should be XX or Xx etc.                     |")
print("|      *must use the same alphabet to represent genotype as instructed.    |")
print("|  4.For Dihybrid genetic cross,                                           |")
print("|      *format of the genotype should be XXYy or XxYy etc.                 |")
print("|      *while selecting the character, must select 2 different character.  |")
print("|--------------------------------------------------------------------------|")
print()
from final_module2 import*
choice=input("Press 'M' for monohybrid cross and 'D' for dihybrid cross: ")
print()
if choice=='M' or choice=='m':
    lm=[]
    print("""The following are the Characters for which a Monohybrid cross can be used:
1.Height
2.Pod colour
3.Pod shape
4.Flower position
5.Seed colour
6.Seed shape
7.Flower colour\n""")
    print("""    For Entering the character, you can either type the character name
                                  OR
           Enter the number associated with the character\n""")
    f=input("Enter the character to be used: ")
    while f.lower() not in w:
        print()
        print("INVALID INPUT. Enter any ONE character from ABOVE LIST.")
        print()
        v=input("Press enter to continue. Or 'Q' or 'q' to Quit. ")
        print()
        if v!="Q" and v!="q":
            f=input("Enter the character to be used: ")
        else:
                exit()
    print()
    character(f," ")
    print()
    print("Enter Genotype of plant 1 among",character(f,"0"),end=": ")
    a=input()
    print("Enter Genotype of plant 2 among",character(f,"0"),end=": ")
    b=input()
    print()
    a=" "+a
    b=" "+b
    for i in range(0,3):
        for j in range(0,3):
            s=a[i]+b[j]
            c="".join(sorted(s))
            print(c,end=" | ")
            lm.append(c)
            nulm=[x for x in lm if " " not in x]
            nulm1=list(set(nulm))
        print()
        print("--------------")
    print()
    print("The list of Output of Genotypes is",nulm1)
    print()
    ipc=input("Press 'Q' to quit or Press ENTER key to continue: ")
    while ipc!='Q' and ipc!='q':
        io=input("Enter the Genotyope that you expect:")
        if io in lm:
            print()
            print("The chances of",io,"Genotype is",lm.count(io)*25,"%")
            print(mpheno(io,nulm))
        else:
            print("Expected Genotype is NOT AVAILABLE")
        print()
        ipc=input("Press 'Q' to quit or Press ENTER key to continue: ")
def dihybrid():
    ld=[]
    print("""The following are the Characters for which a Dihybrid cross can be used:
1.Height
2.Pod colour
3.Pod shape
4.Flower position
5.Seed colour
6.Seed shape
7.Flower colour\n""")
    print("""FOR DIHYBRID YOU NEED TO ENTER TWO CHARACTERS\n    For Entering the character you can either type the character name
                                  OR
           Enter the number associated with the character\n""")
    for i in range(0,2):
        if i==0:
            f1=input("Enter Character 1:")
            d1=f1.lower()
        if i==1:
            f2=input("Enter Character 2:")
            d2=f2.lower()
    while (f1 not in range(1,8) or f2 not in range(1,8)) and (d1 not in w or d2 not in w):
        print()
        print("INVALID INPUT. Enter only ONE , from the LIST ABOVE for each character.")
        print()
        v=input("Press enter to continue. Or 'Q' or 'q' to Quit. ")
        print()
        if v!="Q" and v!="q":
            for i in range(0,2):
                if i==0:
                   f1=input("Enter Character 1:")
                   d1=f1.lower()
                if i==1:
                   f2=input("Enter Character 2:")
                   d2=f2.lower()
        else:
                exit()
                
    g1=character(f1,"")
    g2=character(f2,"")
    if g1==g2:
        print()
        print("""SORRY!
Please choose two DIFFERENT features to find the dihybrid cross""")
        print()
        n=input("Press enter to continue")
        if n=="":
          dihybrid()
    di_character(f1,f2," "," ")
    print()
    print("Enter 1st trait of plant 1 from ",character(f1,"0"),end=": ")
    a1=input()
    print("Enter 2nd trait of plant 1 from ",character(f2,"0"),end=": ")
    a2=input()
    print("Enter 1st trait of plant 2 from ",character(f1,"0"),end=": ")
    b1=input()
    print("Enter 2nd trait of plant 2 from ",character(f2,"0"),end=": ")
    b2=input()
    a=a1+a2
    b=b1+b2
    print()
    x=[a[0]+a[2],a[0]+a[3],a[1]+a[2],a[1]+a[3]]
    y=[b[0]+b[2],b[0]+b[3],b[1]+b[2],b[1]+b[3]]
    x.insert(0,"  ")
    y.insert(0," ")
    for i in range(0,5):
        for j in range(0,5):
            s=x[i]+y[j]
            if x[i]!="  " and y[j]!=" ":
                if ord(x[i][0])>=ord(y[j][0]):
                    if ord(x[i][1])>=ord(y[j][1]):
                        s=y[j][0]+x[i][0]+y[j][1]+x[i][1]
                    if ord(x[i][1])<=ord(y[j][1]):
                        s=y[j][0]+x[i][0]+x[i][1]+y[j][1]
                elif ord(x[i][0])<=ord(y[j][0]):
                    if ord(x[i][1])<=ord(y[j][1]):
                        s=x[i][0]+y[j][0]+x[i][1]+y[j][1]
                    if ord(x[i][1])>=ord(y[j][1]):
                        s=x[i][0]+y[j][0]+y[j][1]+x[i][1] 
                elif ord(x[i][0])>=ord(y[j][0]):
                    if ord(x[i][1])<=ord(y[j][1]):
                        s=y[j][0]+x[i][0]+x[i][1]+y[j][1]
                    if ord(x[i][1])>=ord(y[j][1]):
                        s=y[j][0]+x[i][0]+y[j][1]+x[i][1]
                elif ord(x[i][0])<=ord(y[j][0]):
                    if ord(x[i][1])>=ord(y[j][1]):
                        s=x[i][0]+y[j][0]+y[j][1]+x[i][1]
                    if ord(x[i][1])<=ord(y[j][1]):
                        s=x[i][0]+y[j][0]+x[i][1]+y[j][1]
                else:
                    s=x[i]+y[j]
            print(s,end=" | ")
            ld.append(s)
            nuld=[x for x in ld if "  " not in x and " " not in x]
            nuldi=list(set(nuld))
        print()
        print("---------------------------------")
    print()
    print("The list of Output of Genotypes is",nuldi)
    print()
    ipc=input("Press 'Q' to quit or Press any key to continue:")
    while ipc!='Q' and ipc!='q':
        ip=input("Enter the Genotyope that you expect:")
        if ip in ld:
            print()
            print("The chances of",ip,"genotype is",ld.count(ip)*6.25,"%")
            print(dpheno(ip,nuldi))
            print()
        else:
            print("Expected Genotype IS NOT AVAILABLE")
            print()
        ipc=input("Press 'Q' to quit or Press any key to continue:")
if choice=='D' or choice=='d':
    dihybrid()
if str.upper(choice)!="M" and str.upper(choice)!="D":
    print("invalid choice")
