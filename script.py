import convert

def main():
    celsius = float(input("Enter Celsius:"))
    convert.c_to_f(celsius)

    fahrenheit = float(input("Enter Fahrenheit:"))
    convert.f_to_c(fahrenheit)
    
if __name__ == '__main__':
    print("inside script.py")
    main()