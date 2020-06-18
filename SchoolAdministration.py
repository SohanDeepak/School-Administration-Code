import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","Email ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter in the exact format-| Name Age Contact Email |for student number {} : "
            .format(student_num))
        print("Entered Information: " + student_info)

        info_list = student_info.split(' ')
        print("Split info: " + str(info_list))

        print("\nThe entered info is:- \nName: {}\n Age: {} \nNumber: {} \nEmail: {}"
            .format(info_list[0], info_list[1], info_list[2], info_list[3]))
        
        info_check = input("Is the entered info correct(yes/no):")

        if info_check == "yes":
            write_into_csv(info_list)


            condition_check = input("Enter yes/no for more data: ")
            if condition_check == "yes":
                condition = True
                student_num += 1
            elif condition_check == "no":
                condition = False 
        elif info_check == "no":
            print("Reenter the values")

            