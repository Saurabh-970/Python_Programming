def main():

    StringX = input("Enter the string \n")
    reversed_string = ""

    for ch in StringX:
        reversed_string = ch + reversed_string
    print(reversed_string)

main()    