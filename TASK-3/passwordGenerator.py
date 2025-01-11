import string,random
def main():
    uppercase=string.ascii_uppercase
    lowercase = string.ascii_lowercase
    # numbers = "1234567890"
    numbers = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    # print(uppercase,"\n",numbers,"\n",numbers)
    
    user = input("Choose Difficulty level (E,M,H) ->> ")
    length = int(input("Length->> "))

    while True:
        if user == "e" or user == "E":
            res = "".join(random.choices(lowercase, k=(length//3))) + "".join(random.choices(numbers, k=(length//2)))
            print(res)
            break

        elif user == "m" or user == "M":
            blueprint = "".join(random.choices(lowercase, k=(length//3))) + "".join(random.choices(numbers, k=(length//5))) + "".join(random.choices(uppercase, k=(length//5))) + "".join(random.choices(special, k=1))
            list1 = list(blueprint)
            random.shuffle(list1)
            res = "".join(list1)
            print(res)
            break
        elif user == "h" or user == "H":
            blueprint = "".join(random.choices(lowercase, k=(length//2))) + "".join(random.choices(numbers, k=(length//3))) + "".join(random.choices(uppercase, k=(length//3))) + "".join(random.choices(special, k=(length//2)))
            list1 = list(blueprint)
            random.shuffle(list1)
            res = "".join(list1)
            print(res)       
            break
        else:
            print("Invalid")
              
if __name__ == "__main__":
    main()

