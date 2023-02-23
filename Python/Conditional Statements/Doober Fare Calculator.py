ride_type = "Black"
credits = 4

ride_type = 0
final_price = 0

if ride_type == "DooberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_type = 37.9
else:
    ride_price = 18.7

print("Ride Price:")
print(ride_price)

if credits > 0:
    final_price = ride_price - credits

    print("Final Price:")
    print(final_price)
