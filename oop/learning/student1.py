# Modularizes getting student's name and house
# Uses separate functions to get a user's name and house, then prints them in a formatted sentence when the program is run directly.
def main():
    name= get_name()
    house= get_house()
    print(f"{name} from {house}")

def get_name():
    return input ('Names: ')

def get_house():
    return input ('House: ')

if __name__ == '__main__':
    main()