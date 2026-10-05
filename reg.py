credits = int(input())
early = input("Early registration? (Y/N)")
if early == "Y" or credits > 90:
    print("now")
elif credits > 60:
    print("1 week")
elif credits > 30:
    print("2 weeks")
else:
    print("3 weeks")