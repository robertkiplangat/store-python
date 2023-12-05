"""
    COMMENTS FOR MANUAL *** TO BE DELETED ***
    -----------------------------------------

        All of our sales data will be saved in the history folder
        Will create a function create records for another date
        currently, creating records for the current date is working

"""
import datetime
import os # To work with files and folders


def create_record():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    try:  # Create the 'history' folder if it is not present
        os.mkdir("history")
    except:
        pass

    name_and_value = []
    """
        For name_and_value variable/array
        ------------------------
            The data will be entered in the file in the following way; e.g. "Ice cream 8962", "Monthly salary -150000"
                a value e.g. "4359" will be positive and it will just be saved as "4359"
                then, value e.g. "-7861" will be a negative and it will be save as "-7861"
            *** NOTICE THAT THE LAST WORD OF EVERY LINE WILL ALWAYS BE A NUBMBER OR DIGITS WHETHER -ve or +ve ***
                We will take advantage of this later
    """

    print("Sales Input Sub-menu\n--------------------")
    while True:  # Keep looping as items are being added in the name_and_value array
        print(
            "           ** Press Enter without inputting anything when you are done entering the sales data to exit **"
        )
        print(
            "           Please enter the name of the transaction then the value with spaces e.g. Ice cream 8962 , Monthly salary -150000"
        )
        print(
            '           For profit or loss the value to be entered in the following way ** i.e. if it is a loss enter the value beginning with a negative sign if not enter it the without e.g. "-7861" **\n'
        )
        item_name = input(
            "           Please enter the name of the transaction then finalised by the value: "
        )
        if item_name == "":
            break
        outlier_checker = item_name.split()[-1]  # Get the last value
        if (
            not outlier_checker.isdigit()
        ):  # Check if the last value cannot be evaluated to a number
            if not item_name[0] !="-":
                item_name = item_name + " 0"  # Then just add 0 to it
        """
            For outlier_checker variable
            ------------------------
                Suppose someone does not include the value of the transction e.g. "Ice cream"
                without the value e.g. "Ice cream -400"
                then we will simply add 0 at the end and the person will correct it later when s/he sees the data.
                We will also need to do this to calculate the profit and loss
        """
        name_and_value.append(item_name)
        print(f"\n{item_name} Has been added\n")

    if len(name_and_value) == 0:
        return

    profit = 0
    try:  # This is being used if the sales record file is NOT present
        with open(
            "./history/" + year + "_" + month + "_" + day + ".txt", "w"
        ) as f:  # File name will be something like "2023_11_12"
            for lineToEnter in name_and_value:
                for_profit_calculation = lineToEnter.split()[-1]  # The last value will always be a number
                if for_profit_calculation[0] == "-":  # If it is -ve then minus
                    profit += float(for_profit_calculation)
                else:  # If it is +ve simply add
                    profit += float(for_profit_calculation)
                f.write(lineToEnter+"\n")
            print(f"File has been recorded and your profit is {profit}\n")
    except Exception as e:
        print("*** ERROR!!! ***", e)


def view_records():
    try:
        allFilesInDirectoryArray = os.listdir("./history")
        print("View Records Menu\n-----------------")
        print("        Select the file number to view the record and total profit:\n")
        for i in range(len(allFilesInDirectoryArray)):
            print("            ",i+1,". "+allFilesInDirectoryArray[i])
        while True:
            fileNumber = int(input("\n        Please enter the number of the file you want to view or enter any number apart from any assigned number to quit: "))
            for filePosition in allFilesInDirectoryArray:
                if allFilesInDirectoryArray.index(filePosition) == fileNumber-1:
                    print("\n************************* ",filePosition,"*************************\n")
                    with open("./history/" +allFilesInDirectoryArray[fileNumber-1]) as f:
                        allLines = f.read()
                        getLine = allLines.split('\n') # THIS IS AN ARRAY OF FILE LINES, We are getting the line then the last word
                        print(allLines)
                        """
                            Notice that when we are reading lines,
                            the non-last lin1es will technically have a '\n' at the end of the line
                            we now need to prune this '\n' to get the number
                            it has  various checks,
                            think about it, suppose it is something like "0" or "0\n" of "400" or "400\n" FOR ANY LINE
                        """

                        profit=0
                        for lineByLine in getLine:
                            if len(lineByLine)==0: # Skip the last line to avoid errors as the last line will always be empty
                                continue

                            for_profit_calculation = lineByLine.split()[-1]  # The last value will always be a number
                            """
                                For for_profit_calculation variable/array
                                -----------------------------------------
                                    the '\n' is not carried over in the 'lineByLine.split()[-1]' method/array
                            """
                            profit += float(for_profit_calculation)
                    print("\n**************************** End Of File **************************")
                    print(f"\n             Your profit for the date {filePosition} was {profit}\n")
            break
    except FileNotFoundError as fnfError:
        print("You do not have the history file or folder!")
    except Exception as e:
        print(e)


def update_record():
    try:
        allFilesInDirectoryArray = os.listdir("./TestingFolder")
        print("Update Records Menu\n-----------------")
        print("        Select the file number you would like to update the record. It will calculate for you your new total profit:\n")
        for i in range(len(allFilesInDirectoryArray)):
            print("            ",i+1,". "+allFilesInDirectoryArray[i])
        while True:
            # fileNumber = int(input("\n        Please enter the number of the file you would like to update or enter any number apart from any assigned number to quit: "))
            fileNumber = 2
            for filePosition in allFilesInDirectoryArray:
                if allFilesInDirectoryArray.index(filePosition) == fileNumber-1:
                    print("\n** Line Number | ******* Start of",filePosition,"File *******")
                    print("-------------------------------------------------------------\n")
                    with open("./TestingFolder/" +allFilesInDirectoryArray[fileNumber-1]) as f:
                        allLines = f.read()
                        getLine = allLines.split('\n') # THIS IS AN ARRAY OF FILE LINES, We are getting the line then the last word
                        # print(allLines)
                        # print(getLine)
                        for i in range(len(getLine)):
                            print("            ",i+1,"| "+getLine[i])
                        """
                            Notice that when we are reading lines,
                            the non-last lin1es will technically have a '\n' at the end of the line
                            we now need to prune this '\n' to get the number
                            it has  various checks,
                            think about it, suppose it is something like "0" or "0\n" of "400" or "400\n" FOR ANY LINE
                        """
                        print("\n-------------------------------------------------------------")
                        print("\n               | ************* End Of File **************************")

                        profit=0
                        for lineByLine in getLine:
                            if len(lineByLine)==0: # Skip the last line to avoid errors as the last line will always be empty
                                continue

                            for_profit_calculation = lineByLine.split()[-1]  # The last value will always be a number
                            """
                                For for_profit_calculation variable/array
                                -----------------------------------------
                                    the '\n' is not carried over in the 'lineByLine.split()[-1]' method/array
                            """
                            profit += float(for_profit_calculation)
                        # print(f"\n             Your profit for the date {filePosition} was {profit}\n")
                        # choice = int(input("\n        Please enter the line number of the transaction you would like to update or enter any number apart from any assigned number to quit: "))
                        print("\n        ** Press Enter without inputting anything when you are done entering the sales data to exit **")
                        print("        Please enter the line number of the transaction you would like to update or enter any number apart from any assigned line number to quit: ")
                        choice = 3
                        print("        What would you like to do with line,",choice,"? (edit - e / delete - d):")
                        edit_or_delete = 'delete'
                        if edit_or_delete.lower()=='e' or edit_or_delete.lower()=="edit":
                            for i in range(len(getLine)):
                                if i+1 == choice:
                                    print("            ",i+1,"| "+getLine[i])
                                    print("            Enter the your desired update")
                                    edit = "man uhunye"
                                    outlier_checker = edit.split()[-1]  # Get the last value
                                    """
                                        ERROR HERE IF THE VALUE IS -VE IT WILL APPEND THE 0
                                    
                                    """
                                    if (not outlier_checker.isdigit()):  # Check if the last value cannot be evaluated to a number
                                        edit = edit + " 0"  # Then just add 0 to it
                                    # print(edit,7777777)
                                    for_profit_calculation = edit.split()[-1]  # The last value will always be a number
                                    if for_profit_calculation[0] == "-":  # If it is -ve then minus
                                        profit += float(for_profit_calculation)
                                    else:  # If it is +ve simply add
                                        profit += float(for_profit_calculation)
                                    print("            Would you like to edit the line :",getLine[i],": <to> :",edit,": ? (y / n):")
                                    yes_or_no = 'y'
                                    if yes_or_no == 'y' or yes_or_no=='yes': # Now add changes to the file
                                        """
                                            Since our getLine variable is an array containing our individual lines,
                                            we simply modify that line/position in our array with our new data
                                        """
                                        getLine[i] = edit
                                        """
                                            we now rewrite the WHOLE FILE FROM SCRATCH ADDING OUR NEW EDIT
                                        """
                                        with open("./TestingFolder/" +allFilesInDirectoryArray[fileNumber-1],"w") as f:
                                            # for i in range(len(getLine)):
                                                # print("            ",i+1,"| "+getLine[i])
                                            profit=0
                                            for lineToEnter in getLine:
                                                # print(len(lineToEnter))
                                                if len(lineToEnter)<2: # if the value is say '\n' then thats an outlier
                                                    continue
                                                for_profit_calculation = lineToEnter.split()[-1]  # The last value will always be a number
                                                # print(lineToEnter)
                                                if for_profit_calculation[0] == "-":  # If it is -ve then minus
                                                    profit += float(for_profit_calculation)
                                                else:  # If it is +ve simply add
                                                    profit += float(for_profit_calculation)
                                                f.write(lineToEnter+"\n")
                                            print(f"File has been recorded and your profit is {profit}\n")
                        elif edit_or_delete.lower()=='d' or edit_or_delete.lower()=="delete":
                            for i in range(len(getLine)):
                                if i+1 == choice:
                                    print("            Would you like to delete the line :",getLine[i],": ? (y / n):")
                                    yes_or_no = 'y'
                                    if yes_or_no == 'y' or yes_or_no=='yes': # Now add changes to the file
                                        """
                                            Since our getLine variable is an array containing our individual lines,
                                            we simply delete that line/entry in our array
                                        """
                                        getLine.pop(i)
                                        """
                                            we now rewrite the WHOLE FILE FROM SCRATCH WITHOUT THE DELETED LINE
                                        """
                                        with open("./TestingFolder/" +allFilesInDirectoryArray[fileNumber-1],"w") as f:
                                            # for i in range(len(getLine)):
                                                # print("            ",i+1,"| "+getLine[i])
                                            profit=0
                                            # print(getLine)
                                            for lineToEnter in getLine:
                                                # print(len(lineToEnter))
                                                if len(lineToEnter)<2: # if the value is say '\n' then thats an outlier
                                                    continue
                                                for_profit_calculation = lineToEnter.split()[-1]  # The last value will always be a number
                                                # print(lineToEnter)
                                                if for_profit_calculation[0] == "-":  # If it is -ve then minus
                                                    profit += float(for_profit_calculation)
                                                else:  # If it is +ve simply add
                                                    profit += float(for_profit_calculation)
                                                f.write(lineToEnter+"\n")
                                            print(f"File has been recorded and your profit is {profit}\n")
            break
    except FileNotFoundError as fnfError:
        print("You do not have the history file or folder!")
    except Exception as e:
        print(e)


def delete_record():
    try:
        allFilesInDirectoryArray = os.listdir("./history")
        print("Delete Records Menu\n-----------------")
        print("        Select the file number to delete the record and view profit:\n")
        for i in range(len(allFilesInDirectoryArray)):
            print("            ",i+1,". "+allFilesInDirectoryArray[i])
        
        while True:
            fileNumber = int(input("\n        Please enter the number of the file you want to delete or enter any number apart from any assigned number to quit: "))
            for filePosition in allFilesInDirectoryArray:
                if allFilesInDirectoryArray.index(filePosition) == fileNumber-1:
                    # print(555555555)
                    os.remove("./hicstory/"+filePosition)
                    print("        File has been succesfully deleted!\n")
                else:
                    raise FileNotFoundError("        There is no such file! Nothing has been deleted.\n")
            break
    except FileNotFoundError as fnfError:
        print("        There is no such file! Nothing has been deleted.\n")
    except Exception as e:
        print(e)


def credit_screen():
    print("\n     **********************************************************")
    print("     **********************************************************")
    print("     **********************************************************")
    print("     *********   Robert Kiplangat - Lead Programmer  **********")
    print("     *********   Daniella Chege - Program Designer   **********")
    print("     *********   Nicole Kiruiru - Software Architect **********")
    print("     *********   Rachael Momita - Project Manager    **********")
    print("     *********   George Chuchu - Chief Engineer      **********")
    print("     **********************************************************")
    print("     **********************************************************")
    print("     **********************************************************\n")
    return


def __DEBUGGER__():  # For testing purposes ONLY and it has no relation to the final program
    pass


if 0:  # The starting point or main() function of our program
    print("     Mr. Benson's kiosk \n     ------------------ \n")
    while True:
        print(" Welcome Menu\n -----------")
        print("         Enter 1 To create sales record")
        print("         Enter 2 To view sales records")
        print("         Enter 3 To update sales record or delete line")
        print("         Enter 4 To delete sales record")
        print("         Enter 5 To view credits")
        print("         Enter any value apart from above to exit the program")
        option = input("\n         Please enter your desired option: ")
        print()
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
    print(" You have exited © 2023")

if "for Testing Only" == "for Testing Only":
    print("********** PLEASE RUN | main.py |")
    # create_record()
    # view_records()
    # delete_record()
    # credit_screen()
    # update_record()
    # exit()
