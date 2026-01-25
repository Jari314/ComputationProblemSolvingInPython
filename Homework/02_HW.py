##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {}
 

  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
while True:
    choice = input("Would you like to (A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?")
    choice = choice.upper()

   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
    if choice == 'A':
        while True:
            name = input("Enter the name of the student to add: ")
            name = name.upper()

            if name in grades:
                print("Sorry, that student is already present.")
                
                break
            else:
                break

        while True:
            try:
                grade = int(input(f"Enter {name}'s grade: "))
            except ValueError:
                print("Please enter grade as a number 0-100")
            else:
                if grade >= 0 and grade <= 100:
                    grades[name] = grade

                    break
                else:
                    print("Please enter grade as number 0-100")
        
      # Handle removing a student if user inputs 'R'
      # Check input for "What student do you want to remove? "
      # use pop to remove key/value form grades
      # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
      # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
    elif choice == 'R':
        name = input("Enter the name of the student to remove: ")
        name = name.upper()

        if name in grades:
            grades.pop(name)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")




    

      # Handle modifying a student grade if user inputs 'M'
      # "Enter the name of the student to modify: "
      # Convert grade into integer
      # If student is in grades dictionary, show existing grade "The old grade is"
      # Gather input for new grade "Enter the new grade: "
      # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
    elif choice == 'M':
        while True:
            name = input("Enter the name of the student to modify: ")
            name = name.upper()

            if name in grades:
                print(f"{name}'s old grade is {grades[name]}")

                while True:
                  try:
                      grade = int(input(f"Enter {name}'s new grade: "))
                  except ValueError:
                      print("Please enter grade as a number 0-100")
                  else:
                      if grade >= 0 and grade <= 100:
                          grades[name] = grade

                          break
                      else:
                          print("Please enter grade as number 0-100")
            else:
                print("Sorry, that student doesn't exist and couldn't be modified.")

            break
    
      # Handle printing grade average as a string if user input is 'P'
      # Use "The average grade is "
      # Handle printing all of the student names with associated grade
      # Display explictly as strings
    elif choice == 'P':
        average = 0

        for name in grades:
            
            print(f"{name}: {grades[name]}")

            average += grades[name]
        
        average = round((average / len(grades)), 1)

        print(f"The average grade is {average}")
        

    
          

      # Handle the case for quiting if user inputs 'Q' "Goodbye!"
    elif choice == 'Q':
        print("Goodbye!")

        break

    

      # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    else:
        print("Sorry, that wasn't a valid choice.")