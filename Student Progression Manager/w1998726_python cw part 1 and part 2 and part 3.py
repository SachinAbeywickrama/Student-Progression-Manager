# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# student Name: Sachin Suranjana Abeywickrama.
# UOW ID: w1998726
# IIT Student ID: 20221177
# Date: 2023/4/15

# part 1 and 2 ----------------------------------------------------------------------------------------------------------------------------------------

Integers = [0, 20, 40, 60, 80, 100, 120]
Pass_values = [120, 100, 100, 80, 80, 80, 60, 60, 60, 60, 40, 40, 40, 40, 40, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0]
Defer_values = [0, 20, 0, 40, 20, 0, 60, 40, 20, 0, 80, 60, 40, 20, 0, 100, 80, 60, 40, 20, 0, 120, 100, 80, 60, 40, 20, 0]           #https://www.w3schools.com/python/python_lists.asp            
Fail_values = [0, 0, 20, 0, 20, 40, 0, 20, 40, 60, 0, 20, 40, 60, 80, 0 ,20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100, 120]
Progression_values = ["Progress","Progress (module trailer)","Progress (module trailer)","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Module retriever","Exclude","Module retriever","Module retriever","Module retriever","Module retriever","Exclude","Exclude","Module retriever","Module retriever","Module retriever","Module retriever","Exclude","Exclude","Exclude"]
results = []

def stop_program():       #https://www.w3schools.com/python/python_functions.asp
    exit()

#Define a function to check input
def user_checker(user):
    while True:    
        user_status = input(user)
        if user_status.lower() == "staff" or user_status.lower() == "student":
            return user_status.lower()
        else:
            print("INVALID")
            True

#Define a function to check ID length (8 characters)
def user_id(student_id):
    while True:
        id = input(student_id)
        if len(id) == 8:
            return id
        else:
            print("INVALID INPUT")
            True

#variables used
Progress = 0
trailer = 0
retriever = 0
exclude = 0 

#Ask about what version you want to access
print('Enter "student" if you want access STUDENT VERSION or Enter "staff" to access STAFF VERSION')
user = user_checker("Are you a Student or a member of the Staff (Type Student or Staff): ")

while True:
    if user.lower() == "staff":
            id = user_id("Input your student ID: ")
            print()

    try:
        
        p = int(input("Please input your Pass credit : "))
        if p not in Integers:
            print("Out of range")
            continue

        d = int(input("please input your defer credit : "))
        if d not in Integers:
            print("Out of range")
            continue

        f = int(input("Please input your Fail credit : "))
        if f not in Integers:
            print("Out of range")
            continue

        if (p+d+f) != 120:
            print("Total incorrect")
            stop_program()
            
    except ValueError:
        print("Integer required")
        continue

    i = 0

    for i in range (len(Pass_values)):
        if Pass_values[i] == p and Defer_values[i] == d and Fail_values[i] == f:
            print()
            print(Progression_values[i])

            if user == "student":
                    exit()
            
            elif Progression_values[i] == "Progress":
                Progress = Progress + 1
                
            elif Progression_values[i] == "Progress (module trailer)":
                trailer = trailer + 1

            elif Progression_values[i] == "Module retriever":
                retriever = retriever + 1

            else:
                exclude = exclude + 1
                
            total = Progress + trailer + retriever + exclude

            result_values = Progression_values[i] + " - " + str(Pass_values[i]) + ", " + str(Defer_values[i]) + ", " + str(Fail_values[i])
            results.append(result_values)

           

#----------------------------------------------------------------------------------------------------------------------------------------------
    print()
    print("Would you like to enter another set of data?\n\tEnter 'y' for yes\n\tEnter 'q' to quit and view results")
    other_set = input("Would you like to enter another set of data (y or q) ? ")
    print()
    if other_set == "q":
        break

    elif other_set == "y":
        other_set = "y"
        continue

    else:
        while True:
            print("Please enter 'y' or 'q' ")
            other_set = input("Would you like to enter another set of data (y or q) ? ")
            if other_set == "y":
                other_set = "y"
                break
            
            elif other_set == "q":
                break

            else:
                print("INVALID INPUT, THE PROGRAM WILL NOW EXIT WITH THE ABOVE INFORMATION")
                break
    
#Creation of a Histogram.
print("-"*75)
print("Histogram ")
print("Progress  ", Progress  ,  ": " , "*" * Progress)
print("Trailer   ", trailer   ,  ": " , "*" * trailer)
print("Retriever ", retriever ,  ": " , "*" * retriever)
print("Excluded  ", exclude   ,  ": " , "*" * exclude)
print()
total = Progress + trailer + retriever + exclude
print(total , " outcomes in total. ")
print("-"*75)

#----------------------------------------------------------------------------------------------------------------------------------------------

print()                                              #https://www.w3schools.com/python/python_lists.asp  
i = 0
for i in range(total):
    print(results[i])
    
#part 3 ----------------------------------------------------------------------------------------------------------------------------------------                

#Creation of a text file call SD 1 course_work.
with open("SD 1 course_work.txt", 'w') as output:    #https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file
        output.write("part 3:\n")                    #https://www.youtube.com/watch?v=Uh2ebFW8OYM
        output.write("\n")
        for row in results:
            output.write(str(row) + '\n')                
            
    
