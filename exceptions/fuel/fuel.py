def main():
    while True:
        fraction = input("Fraction: ")  # prompt user
        try:
            x_str, y_str = fraction.split("/")   # split input
            x = int(x_str)
            y = int(y_str)
            
            if x < 0 or y <= 0 or x > y:  # validate
                raise ValueError
            
            percentage = round((x / y) * 100)  # calculate percentage

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            
            break  # valid input processed, exit loop

        except (ValueError, ZeroDivisionError):
            continue  # invalid input, prompt again

if __name__ == "__main__":
    main()
