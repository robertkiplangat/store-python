import datetime  # To give me dates e.g year and month etc.
import os  # To work with files and folders.
import random  # To generate a PIN combination for password checking.


def file_writer(nameOfFile, linesArray, status="recorded"):
    try:  # Create the 'history' folder if it is not present
        os.mkdir("history")
    except:
        pass
    profit = 0
    try:  # This is being used if the sales record file is NOT present
        with open("./history/" + nameOfFile,
                  "w") as f:  # File name will be something like "2023 11 12"
            for lineToEnter in linesArray:
                for_profit_calculation = lineToEnter.split()[
                    -1]  # The last value will always be a number
                if for_profit_calculation[0] == "-":  # If it is -ve then minus
                    profit += float(for_profit_calculation)
                else:  # If it is +ve simply add
                    profit += float(for_profit_calculation)
                f.write(lineToEnter + "\n")
            print(
                f"\n     ✓✓✓ Data has been {status} and your profit is {profit}\n"
            )
    except Exception as e:
        print("     *** ERROR!!! ***", e)


def file_reader(nameOfFile):
    try:
        rows = []
        print(
            "\n---------------|---------------------------------------------")
        print("  Line Number  | ******* Start of", nameOfFile, "File *******")
        print(
            "---------------|---------------------------------------------\n")
        with open("./history/" + nameOfFile) as f:
            allLines = f.read()
            getLine = allLines.split(
                '\n'
            )  # THIS IS AN ARRAY OF FILE LINES, We are getting the line then the last word
            for i in range(len(getLine)):
                if len(getLine[i]) == 0:
                    continue
                print("            ", i + 1, "| " + getLine[i])
            """
                Notice that when we are reading lines,
                the non-last lines will technically have a '\n' at the end of the line
                we now need to prune/remove this '\n' to get the number
                it has  various checks,
                think about it, suppose it is something like "0" or "0\n" of "400" or "400\n" FOR ANY LINE
            """

            profit = 0
            for lineByLine in getLine:
                if len(
                        lineByLine
                ) == 0:  # Skip the last line to avoid errors as the last line will always be empty
                    continue
                rows.append(lineByLine)
                for_profit_calculation = lineByLine.split()[
                    -1]  # The last value will always be a number
                """
                    For for_profit_calculation variable/array
                    -----------------------------------------
                        the '\n' is not carried over in the 'lineByLine.split()[-1]' method/array
                """
                profit += float(for_profit_calculation)
        print(
            " \n                 ************* End Of File **************************"
        )
        print(
            f"\n     Your profit for the date and file {nameOfFile} was {profit}\n"
        )
        print(
            "---------------|---------------------------------------------\n")
        return {"lines": rows, "nameOfFile": nameOfFile}
    except FileNotFoundError as fnfError:
        print("You do not have the history file or folder!")
    except Exception as e:
        print(e)


def view_records():
    while True:
        print("View Records Menu\n-----------------")
        print(
            "     Select the file number to view the record and total profit:\n"
        )
        allFilesInDirectoryArray = os.listdir("./history")
        print("               YYYY MM DD.txt")
        for i in range(len(allFilesInDirectoryArray)):
            print("          ", i + 1, ". " + allFilesInDirectoryArray[i])
        fileNumber = int(
            input(
                "\n     Please enter the number of the file you want to view or enter any number apart from any assigned number to quit: "
            ))
        try:  # If the file number is not in the array then we IMMEDIATELY exit the function
            file_reader(allFilesInDirectoryArray[
                fileNumber - 1])  # We are passig the name of the file
        except:
            break


def create_record():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    name_and_value = []
    """
        For name_and_value variable/array
        ------------------------
            The data will be entered in the file in the following way; e.g. "Ice cream 8962", "Monthly salary -150000"
                a value e.g. "4359" will be positive and it will just be saved as "4359"
                then, value e.g. "-7861" will be a negative and it will be save as "-7861" WITHOUT being separated by an hyphen. 
            *** NOTICE THAT THE LAST WORD OF EVERY LINE WILL ALWAYS BE A NUBMBER OR DIGITS WHETHER -ve or +ve ***
                We will take advantage of this later
    """

    print("Sales Input Sub-menu\n--------------------")
    while True:  # Keep looping as items are being added in the name_and_value array
        print(
            "     ** Press Enter without inputting anything when you are done entering the sales data to exit **"
        )
        print(
            "     Please enter the name of the transaction then the value with spaces e.g. Ice cream 8962 , Monthly salary -150000"
        )
        print(
            '     For profit or loss the value to be entered in the following way ** i.e. if it is a loss enter the value beginning with a negative sign if not enter it the without e.g. "-7861" **\n'
        )
        item_name = input(
            "     Please enter the name of the transaction then finalised by the value: "
        )
        if item_name == "":
            break
        outlier_checker = item_name.split()[-1]  # Get the last value/word
        if (not outlier_checker.isdigit()
            ):  # Check if the last value cannot be evaluated to a number
            if outlier_checker[0] != "-":
                item_name = item_name + " 0"  # Then just add 0 to it
        """
            For outlier_checker variable
            ------------------------
                Suppose someone does not include the value of the transction e.g. "Ice cream"
                without the value e.g. "Ice cream -400"
                then we will simply add 0 at the end and the person will correct it later when s/he sees the data.
                We will also need to do this zero to calculate the profit and loss without any runtime errors.
        """
        name_and_value.append(item_name)
        print(f"\n{item_name} Has been added\n")

    if len(name_and_value) == 0:
        return
    dateOfFile = input(
        "\n     Are the values you entered for today or another date? (yes - y / no - n): "
    )
    if dateOfFile.lower() == 'y' or dateOfFile.lower() == "yes":
        file_writer(year + " " + month + " " + day + ".txt", name_and_value)
    else:
        print(
            "     You will be prompted to enter the date you desire. Please ensure the details are correct."
        )
        exact_year = input("     Please enter the year: ")
        exact_month = input(
            "     Please enter the month (january - 1 ; December 12): ")
        exact_month = "0" + exact_month if len(
            exact_month
        ) == 1 else exact_month  # we are adding zero before the number which is a string to conform with our naming of file rules.
        if not (int(exact_month) > 0 and int(exact_month) <= 12):
            print(
                "     You have input", exact_month,
                "which is an unfamilar month number!!! please confirm the dates."
            )
            return
        exact_dateOfMonth = input(
            "     Please enter the date of the month (1 - 31): ")
        exact_dateOfMonth = "0" + exact_dateOfMonth if len(
            exact_dateOfMonth
        ) == 1 else exact_dateOfMonth  # we are adding zero before the number which is a string to conform with our naming of file rules.
        if not (int(exact_dateOfMonth) > 0 and int(exact_dateOfMonth) <= 31):
            print(
                "     You have input", exact_dateOfMonth,
                "which is an unfamilar date of monthmonth number!!! please confirm the dates."
            )
            return
        file_writer(
            exact_year + " " + exact_month + " " + exact_dateOfMonth + ".txt",
            name_and_value)
        """
            For exact_month variable
            ------------------------
                Since we are saving the name of files such as 2023 11 27.txt
                The month is saved in 2 digits ==> 11 <== representing November in this case
                Now if the user inputs any number that is not in between 1/01 to 12
                We exit the function, we will not be using a loop because we would be forcing
                the user to input the wrong dates and maybe the person needs to confirm the dates
                outside the program
            ^^^ Similar logic applies for the exact_dateOfMonth variable
            -----------------------------------------------------------
        """


def delete_record():
    try:
        print("Delete Records Menu\n-------------------")
        print(
            "     Select the file number you would want to delete the record and view profit:\n"
        )
        allFilesInDirectoryArray = os.listdir("./history")
        for i in range(len(allFilesInDirectoryArray)):
            print("          ", i + 1, ". " + allFilesInDirectoryArray[i])
        fileNumber = int(
            input(
                "\n     Please enter the number of the file you would like to delete or enter any number apart from any assigned number to quit: "
            ))
        for nameOfFile in allFilesInDirectoryArray:
            if allFilesInDirectoryArray.index(nameOfFile) == fileNumber - 1:
                choice = input(
                    "     Are you sure you would want to delete the file | " +
                    nameOfFile + " | (yes - y / no - n): ")
                if choice.lower() == 'y' or choice.lower() == "yes":
                    password = random.randint(
                        1000, 9999
                    )  # generate a random 4 digit number to be used as a password
                    pass_input = int(
                        input("     Enter the random generated password | " +
                              str(password) + " | to confirm the deletion: "))
                    if password == pass_input:
                        os.remove("./history/" + nameOfFile)
                        print("     File has been succesfully deleted!\n")
                    else:
                        print(
                            "     !!! Wrong password, No file Has been deleted.\n"
                        )
                else:
                    print()  # To add a line to make it appear better
    except FileNotFoundError as fnfError:
        print("     There is no such file! Nothing has been deleted.\n")
    except Exception as e:
        print(e)


def update_record():
    while True:
        print("Update Records Menu\n-------------------")
        print(
            "     First select the file number you would like to view and update the records:\n"
        )
        allFilesInDirectoryArray = os.listdir("./history")
        for i in range(len(allFilesInDirectoryArray)):
            print("          ", i + 1, ". " + allFilesInDirectoryArray[i])
        fileNumber = int(
            input(
                "\n     Please enter the number of the file you want to view to update or enter any number apart from any assigned number to quit: "
            ))
        try:  # If the file number is not in the array then we IMMEDIATELY exit the function
            file_reader_Dictionary = file_reader(allFilesInDirectoryArray[
                fileNumber -
                1])  # This is a dictionary of lines and the name of the file
            linesArray = file_reader_Dictionary["lines"]
            nameOfFile = file_reader_Dictionary["nameOfFile"]
            edit_or_delete = input(
                "     What would you want to do? ( add - a / edit - e / delete - d / < any key to exit>): "
            )

            if edit_or_delete.lower() == 'a' or edit_or_delete.lower(
            ) == 'add':
                name_and_value = linesArray
                while True:  # Keep looping as items are being added in the name_and_value array
                    print(
                        "\n     ** Press Enter without inputting anything when you are done entering the sales data to exit **"
                    )
                    print(
                        "     Please enter the name of the transaction then the value with spaces e.g. Ice cream 8962 , Monthly salary -150000"
                    )
                    print(
                        '     For profit or loss the value to be entered in the following way ** i.e. if it is a loss enter the value beginning with a negative sign if not enter it the without e.g. "-7861" **\n'
                    )
                    item_name = input(
                        "     Please enter the name of the transaction you want to add then finalised by the value: "
                    )
                    if item_name == "":
                        break
                    outlier_checker = item_name.split()[
                        -1]  # Get the last value/word
                    if (
                            not outlier_checker.isdigit()
                    ):  # Check if the last value cannot be evaluated to a number
                        if outlier_checker[0] != "-":
                            item_name = item_name + " 0"  # Then just add 0 to it
                    """
                        For outlier_checker variable
                        ------------------------
                            Suppose someone does not include the value of the transction e.g. "Ice cream"
                            without the value e.g. "Ice cream -400"
                            then we will simply add 0 at the end and the person will correct it later when s/he sees the data.
                            We will also need to do this zero to calculate the profit and loss without any runtime errors.
                    """
                    name_and_value.append(item_name)
                    print(f"\n{item_name} Has been added\n")

                if len(name_and_value) == 0:
                    return
                file_writer(nameOfFile, linesArray, "added")
            elif edit_or_delete.lower() == 'e' or edit_or_delete.lower(
            ) == 'edit':
                choice = input(
                    "     Enter the line number you would want to edit: ")
                if not choice.isdigit():
                    print(
                        "     ERROR!!! Please enter a number... starting again..."
                    )
                    continue
                choice = int(choice)
                new_edit = input("     Edit the line | " +
                                 linesArray[choice - 1] + " | to : ")
                linesArray[choice - 1] = new_edit
                file_writer(nameOfFile, linesArray, "edited")
            elif edit_or_delete.lower() == 'd' or edit_or_delete.lower(
            ) == 'delete':
                choice = input(
                    "     Enter the line number you would want to delete: ")
                if not choice.isdigit():
                    print(
                        "     ERROR!!! Please enter a number... starting again..."
                    )
                    continue
                choice = int(choice)
                password = random.randint(
                    1000, 9999
                )  # generate a random 4 digit number to be used as a password
                pass_input = int(
                    input("     Enter the random generated password | " +
                          str(password) + " | to confirm the deletion: "))
                if password == pass_input:
                    linesArray.pop(choice - 1)
                    file_writer(nameOfFile, linesArray, "deleted")
                else:
                    print("     ERROR!!! You entered the wrong password.\n")

        except:
            break


def credit_screen():
    print(
        "#########################################################################\n"
    )
    print("     **********************************************************")
    print("     **********************************************************")
    print("     **********************************************************")
    print("     *********   Robert Kiplangat - Lead Programmer    ********")
    print("     *********   Daniella Chege   - Program Designer   ********")
    print("     *********   Nicole Kiruiru   - Software Architect ********")
    print("     *********   Rachael Momita   - Project Manager    ********")
    print("     *********   George Chuchu    - Chief Engineer     ********")
    print("     **********************************************************")
    print("     **********************************************************")
    print("     **********************************************************\n")
    print(
        "#########################################################################"
    )


if True:  # The starting point or acts as the main() function of our program
    print("     Mr. Benson's kiosk \n     ------------------ \n")
    while True:
        print("Welcome Menu\n------------")
        print(
            "     Enter 1 To create sales record file for today or another date."
        )
        print("     Enter 2 To view sales record file.")
        print("     Enter 3 To add, update sales record file or delete lines.")
        print("     Enter 4 To delete sales record file.")
        print("     Enter 5 To view credits.")
        print("     Enter any value apart from above to exit the program.")
        option = input("\n     Please enter your desired option: ")
        print()  # To add a line to make it appear better
        if option == "1":
            create_record()
        elif option == "2":
            view_records()
        elif option == "3":
            update_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            credit_screen()
        else:
            break
    print("     You have exited © 2023")
if "for Testing Only" == 0:
    # create_record()
    # view_records()
    # delete_record()
    # credit_screen()
    # update_record()
    # exit()
    pass
