from data_module import filter, show_plot, show_other_stats, setup

while True:
    setup()
    print("""<--------User Interface-------->""")
    choice = input('What would you like to choose? \n 1. Show the full data \n 2. Filter then show data \n 3. Show other interesting stats \n 4. Exit program \n ')
    if choice == str(1):
        year, average = setup()
        show_plot(year, average)
    if choice == str(2):
        filter()
    if choice == str(3):
        show_other_stats()
        overallstd, overallave, overall_rpo = show_other_stats()
        print(f"Overall average: {overallave}")
        print(f"Overall standard deviation: {overallstd}")
        print(f"Overall runs per over: {overall_rpo}")
        leave = input('Enter anything to go back: ')
        if leave != None:
            pass
    if choice == str(4):
        print('Exiting program')
        break
    else:
        print("Please select a number between 1-4")