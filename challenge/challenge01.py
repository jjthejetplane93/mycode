#!/usr/bin/python3

''' Challenge task for python course '''

wordbank= ["indentation", "spaces"] 

tlgstudents= ["Aaron", "Andy", "Brian", "Chris", "Cliff", "Daniel", "Erin", "Joseph", "Justin", "Linda", "Michael", "Rupesh", "Samuel", "Zachary"]


def main():
    wordbank.append(4)

    print(wordbank)

    num = ''
    while not num and num != 0:
        try:
            num = int(input(f"please enter a number between 1 and {len(tlgstudents)}\n")) - 1
            if num >= len(tlgstudents) or num < 0:
                print("Invalid Entry!")
                num = None
        except Exception as e:
            print("Invalid Entry!")

    print(num)

    student_name = tlgstudents[num]

    print(f'{student_name} always uses {wordbank[-1]} {wordbank[-2]} to indent.')




if __name__ == "__main__" :
    main()


