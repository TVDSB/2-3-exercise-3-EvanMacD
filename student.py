def main():
    number = int(input("Enter a number here \n"))

    if number %15==0:
        print("fizzbuzz")

    elif number%5==0:
        print("buzz")

    elif number %3==0:
        print("fizz")

    else:
        print("You have selected nothing congrats!!")
    

if __name__ =='__main__':
    main()
