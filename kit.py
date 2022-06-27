
yg=input("guess name: \n")

if(yg.startswith("s")):
    print("you enter loop")

    gy=int(input("enter number between 1 to 3"))
    while(gy!=3):
        print("try again..\n")
        gy=int(input("enter number between 1 to 3"))

    
    print("yo correctly guess")


else:
    print("endo")
        

