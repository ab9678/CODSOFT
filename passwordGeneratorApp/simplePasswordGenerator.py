import random,string

def main():
    uppercase=string.ascii_uppercase
    lowercase = string.ascii_lowercase
    # numbers = "1234567890"
    numbers = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    user = input("Choose Difficulty level (E,M,H) ->> ").lower()
    length = int(input("Length->> "))

    if user == "e" or user == "easy":
        raw = lowercase+numbers
        res = "".join(random.choices(raw, k=length))
    elif user == "m" or user == "medium":
        raw = lowercase+numbers+special
        res = "".join(random.choices(raw, k=length))
    elif user == "h" or user == "hard":
        raw = lowercase+numbers+special+uppercase
        res = "".join(random.choices(raw, k=length))
    else:
        print("Invalid")
    print(res)


main()