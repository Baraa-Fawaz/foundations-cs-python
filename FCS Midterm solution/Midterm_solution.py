from urllib.parse import urlparse #ref: Stackoverflow
import requests
from bs4 import BeautifulSoup  #ref: GeekforGeeks (https://www.youtube.com/watch?v=O6nnVHPjcJU&t=2s)
#Greeting the user
user_name = input("Enter your name:")
print("Hello", user_name, "Welcome to the Advanced Browser Tabs Simulation")
main_dict = {"all_tabs": []}

def openTab(title,url):#creating a tab by appending a dictionary contianing the tab title and content into the list of dictionaries(tabs)
    if urlparse(url).scheme != '' and urlparse(url).netloc != '':#ref: Stackoverflow (https://stackoverflow.com/questions/53992694/what-does-netloc-mean) scheme will check if the user url contains http or https,netloc identifies the network location where the resource is hosted
      open_tab = {}
      open_tab["tab_title"] = title
      open_tab["tab_url"] = url
      open_tab["nested_tab"] = []
      main_dict["all_tabs"].append(open_tab)
      print("A new tab has been opened")
    else:
      print("Invalid URL")  
def closeTab(i):
    if i == "":  #Check if the user did not give any index
     main_dict["all_tabs"].remove(main_dict["all_tabs"][-1])#closing the last opened tab in the list of tabs
     print("The last opened tab has been closed")
    elif len(main_dict["all_tabs"]) == 0:
     print("There is no opened tabs to close.Try opening a new tab first")  #we can't close tabs if they are not opened
    elif int(i) >= 0 and int(i) < len(main_dict["all_tabs"]):  #check if the index entered by the user represents the number of element found in the list of tabs
     for x in range(len(main_dict["all_tabs"])):#0(N) 
      if x == int(i):
        main_dict["all_tabs"].remove(main_dict["all_tabs"][x])
        print("the tab at index", i, "has been closed") #remove the tab at the index that the user provided
    else:
        print("Invalid input.Try to Enter a correct index")

def switchTab(num):
    if num == "":  #check if the user did not provide any index
      html_url = main_dict["all_tabs"][-1]["tab_url"]
      req = requests.get(html_url)
      html = BeautifulSoup(req.content, "html.parser")
      html_content = html.prettify()
      print(html_content)  #displaying the html content of the last oppened tab
    elif len(main_dict["all_tabs"]) == 0:  #can't display the html content of a tab that is not opened
     print("There is no opened tabs to see its conent")
    elif int(num) >= 0 and int(num) < len(main_dict["all_tabs"]):
     for x in range(len(main_dict["all_tabs"])):#O(N)
      if int(num) == x:
        html_url = main_dict["all_tabs"][x]["tab_url"]
        req = requests.get(html_url)
        html = BeautifulSoup(req.content, "html.parser")
        html_content = html.prettify()
        print(html_content)  #displaying the html content of the tab that the user provided its index
    else:
     print("Invalid input")
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
      index = input("Enter the index of the tab you want to close:")
      closeTab(index)
    elif choice == 3:
      number = input("Enter the index of the tab you whant to display its content: ")
      switchTab(number)
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