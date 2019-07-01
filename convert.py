def c_to_f(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    print("Its fahrenheit equivalent is " + str(fahrenheit))

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print("Its celsius equivalent is " + str(celsius))
    
def main():
    
    celsius = float(input("Enter Celsius:"))
    c_to_f(celsius)
    
    fahrenheit = float(input("Enter Fahrenheit:"))
    f_to_c(fahrenheit)
    
if __name__ == '__main__':
    print("Inside convert.py")
    main()