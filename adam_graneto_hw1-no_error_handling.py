### Insturctions to Run: ###
# On the OSU Engineering servers, this python code can be run by typing: python3 adam_graneto_hw1.py
# You can also type just python instead: python adam_graneto_hw1.py
# 
# In the Visual Studio Code terminal, I am able to run this python code by typing: py adam_graneto_hw1.py
# However, I have seen the python command be used instead of py online: python adam_graneto_hw1.py
# The latter approach does not work for me personally, I think it may be a library discrepancy but I am not sure 

def main():
    year = int(input("Enter a year: ")) # get a year from the user
    if(year % 4 == 0): # if year is divisible by 4
        if(year % 100 != 0 or year % 400 == 0): # if year is not divisble by 100 unless divisible by 400
            print(str(year) + " is a leap year")
            return
    print(str(year) + " is not a leap year")

main()