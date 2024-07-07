def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
# p1=Person("Tamim",25)
# print(p1.name)
# print(p1.age)

def is_palindrome(input_string):
    new_string=""
    reverse_string=""


    for letter in input_string:
        if letter!="":
            new_string=new_string+letter.lower()
            reverse_string=letter.lower()+reverse_string

    if new_string == reverse_string:
        return True
    return False



def nametag(first_name,last_name):
    return("{} {}.".format(first_name,last_name[0]))


print(nametag("Farman","Arefin"))