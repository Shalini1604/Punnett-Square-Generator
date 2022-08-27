#seven major traits or characters of plant:
#HEIGHT
#POD COLOUR
#POD SHAPE
#FLOWER POSITION
#SEED COLOUR
#SEED SHAPE
#FLOWER COLOUR
def character(feature,m):      #function for monohybrid cross
    if str.lower(feature)=="height" or feature=="1":
        if m=="":
            k=str.lower(feature)
            k="1"
            return(k)
        if m==" ":
         print()
         print("In Height character, 'Tallness' is a dominant trait and 'Dwarfness' is a recessive trait")
         print()
         print("Press 'T' for Dominant allele")
         print("Press 't' for Recessive allele")
        if m=="0":
             return ("['TT','tt','Tt','tT']")
        if m=="TT":
            return("Tall")
        if m=="Tt":
            return("Tall")
        if m=="tt":
            return("Dwarf")
    if str.lower(feature)=="seed colour" or feature=="5":
        if m=="":
            k=str.lower(feature)
            k="5"
            return(k)
        if m==" ":
         print()
         print("In Seed colour character, 'Yellow' is a dominant trait and 'Green' is a recessive trait")
         print()
         print("Press 'Y' for Dominant allele")
         print("Press 'y' for Recessive allele")
        if m=="0":
            return ("['YY','Yy','yy','yY']")
        if m=="YY":
           return("Yellow")
        if m=="Yy":
           return("Yellow")
        if m=="yy":
           return("Green")
    if str.lower(feature)=="pod colour" or feature=="2":
        if m=="":
            k=str.lower(feature)
            k="2"
            return(k)
        if m==" ":
         print()
         print("In Pod colour character, 'Green' is a dominant trait and 'Yellow' is a recessive trait")
         print()
         print("Press 'G' for Dominant allele")
         print("Press 'g' for Recessive allele")
        if m=="0":
            return ("['GG','Gg','gg','gG']")
        if m=="GG":
           return("Green")
        if m=="Gg":
           return("Green")
        if m=="gg":
           return("Yellow")
    if str.lower(feature)=="flower position" or feature=="4":
        if m=="":
            k=str.lower(feature)
            k="4"
            return(k)
        if m==" ":
         print()
         print("In Flower position character, 'Axial flowerring' is a dominant trait and 'Terminal flowering' is a recessive trait")
         print()
         print("Press 'A' for Dominant allele")
         print("Press 'a' for Recessive allele")
        if m=="0":
            return ("['AA','Aa','aa','aA']")
        if m=="AA":
           return("Axial flowering")
        if m=="Aa":
           return("Axial flowering")
        if m=="aa":
           return("Terminal flowering")
    if str.lower(feature)=="flower colour" or feature=="7":
        if m=="":
            k=str.lower(feature)
            k="7"
            return(k)
        if m==" ":
         print()
         print("In Flower colour character, 'Violet' is a dominant trait and 'White' is a recessive trait")
         print()
         print("Press 'V' for Dominant allele")
         print("Press 'v' for Recessive allele")
        if m=="0":
            return ("['VV','Vv','vv','vV']")
        if m=="VV":
           return("Violet")
        if m=="Vv":
           return("Violet")
        if m=="vv":
           return("White")
    if str.lower(feature)=="pod shape" or feature=="3":
        if m=="":
            k=str.lower(feature)
            k="3"
            return(k)
        if m==" ":
         print()
         print("In Pod shape character, 'Inflated pod' is a dominant trait and 'Constricted pod' is a recessive trait")
         print()
         print("Press 'I' for Dominant allele")
         print("Press 'i' for Recessive allele")
        if m=="0":
            return ("['II','Ii','ii','iI']")
        if m=="II":
          return("Inflated")
        if m=="Ii":
           return("Inflated")
        if m=="ii":
           return("Constricted")
    if str.lower(feature)=="seed shape" or feature=="6":
        if m=="":
            k=str.lower(feature)
            k="6"
            return(k)
        if m==" ":
         print()
         print("In Seed shape character, 'Round' is a dominant trait and 'Wrinkled' is a recessive trait")
         print()
         print("Press 'R' for Dominant allele")
         print("Press 'r' for Recessive allele")
        if m=="0":
            return ("['RR','Rr','rr','rR]")
        if m=="RR":
          return("Round")
        if m=="Rr":
           return("Round")
        if m=="rr":
           return("Wrinkled")
     
def di_character(f1,f2,p,q):
    n1=character(f1,p)
    n2=character(f2,q)
    return n1,n2
