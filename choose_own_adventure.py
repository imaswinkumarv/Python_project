name=input("Type you name: ")
print("welcome",name,"to this adventure")

answer=input("You are in a dirty road ur choice left or right: ").lower()

if(answer=="left"):
    answer=input("You come to river,you can walk or swim: ")

    if answer=="swim":
       print("You swim across and were eaten by alligator")
    elif answer=="walk":
       print("You walked for many miles,ran out of water and you lost the game")
    else:
       print("Not a valid option.You lose")

elif(answer=="right"):
    answer=input("You come to the bridge,it looks wobbly,do you want to across it or head back (cross/back): ")
    
    if answer=="back":
       print("You go back and lose")
    elif answer=="cross":
       answer=input("You cross the bridge and meet a stranger.Do you talk to them(Yes/no): ")
       if answer=="yes":
          print("You talk to the stranger and they give a gold.You win")
       elif answer=="no":
          print("You ignore the stranger and they are offened and you lose")
       else:
        print("Not a valid option.You lose")

    else:
       print("Not a valid option.You lose")

else:
    print("Not a valid option.You lose")

print("Thanks for trying",name)