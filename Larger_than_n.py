def main():
    n = 7
    num_list = [1, 4, 7, 9, 11, 3, 8, 25, 2, 1]
    print("Figuring out numbers larger than 'n'...")
    numbers(n, num_list)

def numbers(the_num, list):
    for numero in list:
        if numero > the_num:
            print (numero)
main()



