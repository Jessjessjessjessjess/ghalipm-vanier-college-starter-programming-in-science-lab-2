# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    h0= float(input("Enter initial height: "))
    gravity =9.8
    t= float(input("Enter time: "))
    height= (h0)-(((gravity)*(t**2))/2)
    print("height")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed =20
    time= float(input("Enter time for car (in seconds): "))
    distance= speed*time
    print("distance")
