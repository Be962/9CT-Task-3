from data_module import filter, show_plot, show_other_stats, setup

while True:
    setup()
    print("""<--------User Interface-------->""")
    choice = input('What would you like to choose? \n 1. Show the full data \n 2. Filter then show data \n 3. Show other interesting stats \n 4. Exit program \n ')
    if choice == str(1):
        year, average = setup() # Gets the year and average from setup function
        show_plot(year, average) # Plots the whole data from the first year/average 
    elif choice == str(2):
        filter() # Calls the filter function
    elif choice == str(3):
        show_other_stats() # Displays other stats
        overallstd, overallave, overall_rpo = show_other_stats()
        print(f"Overall average: {overallave}")                 # Prints other stats
        print(f"Overall standard deviation: {overallstd}")      # Prints other stats
        print(f"Overall runs per over: {overall_rpo}")          # Prints other stats
        leave = input('Enter anything to go back: ')
        if leave != None: # Any input will trigger this and go back to main loop
            pass
    elif choice == str(4):
        print('Exiting program')
        break # Exits the program
    else:
        print("Please select a number between 1-4") # Handling wrong inputs