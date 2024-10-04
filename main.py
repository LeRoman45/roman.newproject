from PyQt5 import *

#massage = input("Бажаєте ")



while True:
    with open(
        "poem.txt", "r", encoding= "utf-8"
        ) as file:
        data = file.read()
    print(data)

    yes_or_no = input("Do U wanna add autor of this poem? Yes or No")
    if yes_or_no == "Yes":
        avtor = input("Напиши автора")
     
        with open(
            "poem.txt", "a", encoding= "utf-8") as file:
                file.write("\nАвтор:"+avtor)
       
    else:
        break

      
    
