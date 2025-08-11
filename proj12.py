

user = input('Please enter your name: ')
print(f'\nwelcome {user}')
def eligiblity_check():
    while True:
        print('-------------------')
        gpa = input('Enter your college CGPA: ')
        if gpa.isdigit():
            gpa = int(gpa)

            if gpa >= 4:
                print('-------------------')
                print('\nwelcome to our university.')
                break
            else:
                print('-------------------')
                print('Sorry you are not eligible')
                break
        else:
            print('Please write a numeric value')

def major_subject():
    pass

def main():
    eligiblity_check()

main()