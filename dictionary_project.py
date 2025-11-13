


empty_dictionary={}
while True:
    print("1.Add a word..")
    print("2.Search the Meaning")
    print("3.Display all words")
    print("4.Update the Meaning")
    print("5.Delete word in dictionary")
    print("6.Exit")

     
    choice=input("Enter the option...")
    
    if choice=="1":
        word=input("Enter the word...").lower()
        meaning=input("Enter the meaning...")
        empty_dictionary[word]=meaning
        print("word added successfully")



    elif choice=="2":
        word=input("Enter the word to search...").lower()
        if word in empty_dictionary:
            print("Meaning",empty_dictionary[word])
        else:
            print("word not found")


    elif choice=="3":
         if empty_dictionary:
            print("Words and their meanings:")
            for word, meaning in empty_dictionary.items():
                print(f"{word}: {meaning}")
         else:
            print("Dictionary is empty.")

        
    elif choice=="4":
        word=input("Enter the word to update..").lower()
        if word in empty_dictionary:
            new_meaning=("Enter the new meaning")
            empty_dictionary[word]=new_meaning
            print("meaning added successfully..")
        else:
            print("word not found")


        
    elif choice=="5":
        word=input("Enter the word to delete..").lower()
        if word in empty_dictionary:
            del empty_dictionary[word]
            print("word deleted successfully")
        else:
            print("word not found")

            

    elif choice=="6":
        print("exit the program")
        break
    else:
        print("Enter valid choice")








