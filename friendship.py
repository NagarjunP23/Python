name=input("Enter your name ").lower()
f_name=input("Enter Friend's name ").lower()
n=name+f_name
c=0
for i in n:
    if i in "aeiou":
        c+=5
    elif i in "friends":
        c+=10
    else:
        c+=2

if c>90:
    print("Made for each other")
elif c>70 and c<90:
    print("Best friend")
else:
    print("Friends")