def greet(name):
    print(f"Have a nice day,{name}")

def qualification(hle):
    print(f"Your highest level of education is {hle}")

if __name__ == '__main__':
    name = input("Enter your name:")
    hle = input("Enter your highest education level:")
    greet(name.capitalize())
    qualification(hle)