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

# """TASK 3"""

# #Password Generator using Cmd line:

# import random
# import string

# lower_ = string.ascii_lowercase   # i.e abcde
# upper_ = string.ascii_uppercase   # i.e ABCDE
# nos_ = string.digits              # i.e 012345
# Special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# #passwd criteria:

# def easy_pass():
#     return lower_+nos_

# def medium_pass():
#     return lower_+upper_ + nos_

# def strong_pass():
#     return lower_+upper_+nos_+Special_char

# #here the level of difficulty is defined for the user to their passwd:

# def desired_passwd():
#     type_of_pass = input("Enter the level of passwd:- Easy/Medium/Hard:").lower()
#     if type_of_pass == "e":
#         return easy_pass()
#     elif type_of_pass == "m":
#         return medium_pass()
#     else:
#         return strong_pass()

# #define main func:

# def main():
#     while (1):
#         n = int(input("Enter the length of the reqd pass:")) #reqd len of passwd
#         res = random.choices(desired_passwd(), k=n)  #here random func will select out the random chars for the passwd!!
#         print(''.join(res))  #to avoid spacing {''.join is used}

#         #for continuation of new-new passwd!!
#         progress=int(input("Do you want a new passwd: (YES=1 / NO=0)"))
#         if progress==0:
#             break

# main()