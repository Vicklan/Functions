 #Calculates the inclusive price and returns its value
def calculateIncPrice(exclusivePrice,vatTax ):
    #Calculates the inclusive price
    inclusivePrice = exclusivePrice+(exclusivePrice*vatTax)
     #returns value of inclusive Price
    return(inclusivePrice)
 #Enters the user's Exclusive price and Tax Rate 
def userExclTaxRate():
    #inputs exlusive price
    exclusivePrice = float(input("Enter exclusive Price: "))
    #inputs tax rate
    vatTax = float(input("Enter tax rate: "))
#Calls the previous function
    return  calculateIncPrice(exclusivePrice,vatTax )
#Prints out the value of Inclusive Price
print(userExclTaxRate())  


 