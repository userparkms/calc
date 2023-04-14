#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit 1: keep")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("plus : ", plus(x,y))
            print("sub : ", sub(x,y))
            print("mul : ", mul(x,y))
            print("div : ", div(x,y))

        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()


# In[ ]:




