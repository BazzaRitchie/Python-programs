#Codecademy_Project_Number_1.py
print("jobbie. Jobbie! JOBBIE!")
def jobbie_generator(num_jobbies):
    jobbie_counter = num_jobbies
    jobbie_tracker = num_jobbies
    while jobbie_tracker > 0:
        print("Jobbie!")
        jobbie_tracker -= 1
    print("You printed " + str(jobbie_counter) + " jobbies!")
    return jobbie_counter

jobbie_generator(89)  
