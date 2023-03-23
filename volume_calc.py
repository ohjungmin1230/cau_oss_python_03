length=input("가로:")
width=input("세로:")
height=input("높이:")
volume=float(length)*float(width)*float(height)
print("부피는"+str(volume)+"입니다.")

total_length=float(length)+float(width)+float(height)

if total_length <= 80:
    charge = 5000
elif total_length <= 100:
    charge = 10000
elif total_length <= 120:
    charge = 13000
else:
    charge = "unavailable"

print("total length:", total_length)
print("charge:", charge)

