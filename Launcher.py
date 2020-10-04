import BST
import Func_IO
schedule = BST.BSTDemo()
func  = Func_IO.Func_IO()
def launcher():
    print("Wellcome to the job scheduler program")
    print("Press 1 to add a schedule")
    print("Press 2 to delete a schedule")
    print("Press 3 to view all  your schedule")
    print("Press 4 search your  schedule")
    print("Press any number else to exit the program")
    try:

        choice = int(input("---- .>"))
        if (choice == 1):
            name = input("What's the Name of the Schedule ...  ? ")
            time = input("Enter the schedule appointment time in 12hr format (h:m AM or PM ) ")
            duration = input("Enter appointment  duration (h:m) ")
            if (func.convert24(time)):
                appointment = BST.Node(func.convert24(time),name,duration)
                schedule.insert(appointment , False)
                
            else:
                print("Please enter a correct time format !!!")


        elif (choice == 2):
            try:
               time_lists =  display_deleting_schedule()
               if time_lists != "no_data":
                   print("Which of the following schedules do you want to delete ? ")
                   delete_appointment = int(input("----> ")) - 1
                   if (delete_appointment >= 0):
                       del_time = time_lists[delete_appointment]
                       deleted = schedule.delete_val(del_time)
                       if deleted:
                           read_write(None, "w")
                           print("Item Deleted !!!!")
                   else:
                       time_lists[len(time_lists)]
            except IndexError:
                print("Please enter a correct number found in the table above !!!")


        elif (choice == 3):
            display_deleting_schedule()

        elif (choice == 4):
            time = input("What's the time of the schedule ? Enter the time  in 12hr format (h:m AM or PM ) ")
            if(func.check_time_format(time)):
                search_result =  schedule.find_val(func.convert24(time))
                if search_result != False:
                    print("        Time                 Duration               Schedule Name     ")
                    print("________________________________________________________________")
                    print(f" {func.convert12(search_result.data)}       {func.convert12(search_result.data)}  - "
                          f"{func.convert12(func.calculate_duration(search_result.data, search_result.duration)[:-3])}          {search_result.name}")
                else:
                    print("There is no appointment recorded  on that time .... ")
            else:
                print("Please enter the correct time format !!!!!")
        else:
            print("Bye")
            return
    except ValueError:
        print("Please enter a number for the choices above !!!!")


    launcher()


def display_deleting_schedule():
        try:
            with open("jobscheduler.txt") as file:
                r = file.read()
                if r == "":
                    print("There is no data to display or delete.")
                else:
                     return schedule.in_order()
            return  "no_data"



        except FileNotFoundError:
            print("There is no data to display or delete.")




def read_write(key, rw):
    try:
        if rw == "r":
            with open("jobscheduler.txt") as file:
                for line in file:
                    if line != "\n":
                        x = line.split(",")
                        appointment = BST.Node(x[0], x[2], x[1])
                        schedule.insert(appointment, True)


        elif rw == "w":
            with open("jobscheduler.txt" , "w") as file:
                file.write("")
            new_data_tree = schedule.pre_order()
            file = open("jobscheduler.txt", "a")
            for i in new_data_tree:
                file.write(i.data +"," + i.duration + "," + i.name +"\n")
            file.close()
        else:

            with(open("jobscheduler.txt", "a")) as file:
                '''This code creates the jobscheduler.txt file if the program is run for the first time '''
                pass;
            with open("jobscheduler.txt") as file:
                r = file.read()
                if r == "":
                    return False
                else:
                    return True


    except IOError:
        print("Storage file deleted by someone on your side !!!!")



file_has_data =  read_write(None , "find_file")
if(file_has_data):
    read_write(None , "r")

launcher()


