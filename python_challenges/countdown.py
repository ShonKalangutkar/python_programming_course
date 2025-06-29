from time import sleep

def countdown(n):
    print(n)
    sleep(1)
    
    if n == 1:
        return
    else:
        countdown(n-1)

n = int(input("Enter the number for count down: "))
countdown(n)
