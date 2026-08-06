'''[LEARNING LOGS] Season'''
def main():

    month = int(input("Enter month "))
    day = int(input("Enter day "))

    winter = [1,2,3]
    spring = [4,5,6]
    summer = [7,8,9]
    fall = [10,11,12]

    if month != month+1 :
        if month in winter:
            if day >= 21 and month % 3 == 0:
                print("spring")
            else:
                print("winter")
        elif month in spring:
            if day >= 21 and month % 3 == 0:
                print("summer")
            else:
                print("spring")
        elif month in summer:
            if day >= 21 and month % 3 == 0:
                print("fall")
            else:
                print("summer")
        elif month in fall:
            if day >= 21 and month % 3 == 0:
                print("winter")
            else:
                print("fall")
main()
