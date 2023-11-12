#Greeting the user
user_name = input("Enter your name:")
print("Hello", user_name, "Welcome to the Advanced Browser Tabs Simulation")
main_dict = {"all_tabs": []}

def openTab(title,url):#creating a tab by appending a dictionary contianing the tab title and content into the list of dictionaries(tabs)
    open_tab = {}
    open_tab["tab_title"] = title
    open_tab["tab_url"] = url
    open_tab["nested_tab"] = []
    main_dict["all_tabs"].append(open_tab)
    print("A new tab has been opened")
def closeTab():
    pass
def switchTab():
    pass
def displayAllTabs():
    pass
def openNestedTab():
    pass
def clearAllTabs():
    pass
def saveTabs():
    pass
def importTabs():
    pass
def displayMenu():
  print("1. Open Tab\n2. Close Tab\n3. Switch Tab")
  print("4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs")
  print("7. Save Tabs\n8. Import Tabs\n9. Exit")  #using 3 print statment only for better visualization
def main():
  displayMenu()
  choice = eval(input("Enter a number: "))

  while choice != 9:
    if choice == 1:
      title = input("Enter the title of the tab:")
      url = input("Enter the URL of the website:")
      openTab(title,url)
    elif choice == 2:
      closeTab()
    elif choice == 3:
      switchTab()
    elif choice == 4:
      displayAllTabs()
    elif choice == 5:
      openNestedTab()
    elif choice == 6:
      clearAllTabs()
    elif choice == 7:
      saveTabs()
    elif choice == 8:
      importTabs()
    elif choice != 9:
      print("Invalid input.Try to choose a number from 1 to 9")

    displayMenu()
    choice = eval(input("Enter a number: "))

  print("Exited")  #if choice = 9 the while loop will be entered thus exiting and terminating the program.


main()