from urllib.parse import urlparse#ref: Stackoverflow
import requests
from bs4 import BeautifulSoup  #ref: GeekforGeeks (https://www.youtube.com/watch?v=O6nnVHPjcJU&t=2s)
import json


#Greeting the user
user_name = input("Enter your name:")
print("Hello", user_name, "Welcomt to the Advanced Browser Tabs Simulation")
main_dict = {"all_tabs": []}



def openTab(title, url):  #0(1)
  #creating a tab by appending a dictionary contianing the tab title and content into the list of dictionaries(tabs)
  if urlparse(url).scheme != '' and urlparse(url).netloc != '':#ref: Stackoverflow (https://stackoverflow.com/questions/53992694/what-does-netloc-mean) scheme will check if the user url contains http or https,netloc identifies the network location where the resource is hosted
    open_tab = {}
    open_tab["tab_title"] = title
    open_tab["tab_url"] = url
    open_tab["nested_tab"] = []
    main_dict["all_tabs"].append(open_tab)
    print("A new tab has been opened")
  else:
    print("Invalid URL")


def closeTab(i):  #worst case---> 0(N) where N represents the length of the list of opened tabs
  if i == "":  #Check if the user did not give any index
    main_dict["all_tabs"].remove(main_dict["all_tabs"][-1])  #closing the last opened tab in the list of tabs
    print("The last opened tab has been closed")
  elif len(main_dict["all_tabs"]) == 0:
    print("There is no opened tabs to close.Try opening a new tab first")  #we can't close tabs if they are not opened
  elif int(i) >= 0 and int(i) < len(main_dict["all_tabs"]):  #check if the index entered by the user represents the number of element found in the list of tabs
    for x in range(len(main_dict["all_tabs"])):#0(N) 
      if x == int(i):
        main_dict["all_tabs"].remove(main_dict["all_tabs"][x])
        print("the tab at index", i, "has been closed") #remove thetab at the index that the user provided
  else:
    print("Invalid input.Try to Enter a correct index")



def switchTab(num): #worst case---> 0(N^2) where N represents the length of the list of opened tabs 
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



def displayAllTabs(all_tabs):#worst case---> 0(N^2) where N represents the length of the list of parent tabs and N for the length of list of nested tabs in the parent tab so N*N-->O(N^2)
  if len(all_tabs) == 0:
    print("There is no opened tabs yet.try opening a new tab first")
  else:
    print("Titels of all opened tabs:")
    for i in range(len(all_tabs)):#O(N)  #looping throughout the list
      if len(all_tabs[i]["nested_tab"]) > 0:  #check if the tab has nested tabs
        print("Title",i+1,"(Parent):",all_tabs[i]['tab_title'])  #print the tab title for the parent tab
        for x in range(len(all_tabs[i]["nested_tab"])):#O(N)
          print("\t_Nested title",x+1,":", all_tabs[i]["nested_tab"][x]["tab_title"])  #print the tab title for the child tab
      elif len(all_tabs[i]["nested_tab"]) == 0:  #if the tab is nested only print the title of the tab
        print("Title",i+1,":",all_tabs[i]['tab_title'])



def openNestedTab(parent_tab_index):#worst case---> 0(1)
  if len(main_dict["all_tabs"]) == 0:
    print("You can't create a nested tab since there is no opened tab yet.try opening a new tab first")
  else:
    if parent_tab_index == "":
      print("you can't enter an empty index")
    elif int(parent_tab_index) >= 0 and int(parent_tab_index) < len(main_dict["all_tabs"]):
      nested_tab = {}
      nested_tab_title = input("Enter the title of the nested tab:")
      nested_tab_url = input("Enter the URL of the nested website:")
      if urlparse(nested_tab_url).scheme != '' and urlparse(nested_tab_url).netloc != '':
        nested_tab["tab_title"] = nested_tab_title
        nested_tab["tab_url"] = nested_tab_url
        main_dict["all_tabs"][int(parent_tab_index)]["nested_tab"].append(nested_tab)  #created a dictionary containing the title and the url of the child tab then adding this dictionary(child tab) to the nested tab key in the parent dictionary(tab)
        print(main_dict)
      else:
        print("Invalid URL")
    else:
      print("Invalid input.the index you entered is out of range of lenght of the list")



def clearAllTabs(opened_tabs):#worst case---> 0(1)
  opened_tabs.clear()  #.clear will delet everything in the list containing all opened tabs
  print("All opened tabs have been cleared")



def saveTabs(file_path):#worst case---> 0(1)
  json_string = json.dumps(main_dict,indent=1)  #dumps will take the json object and turn it into string
  with open(file_path, "w") as f:
    f.write(json_string)  #save everything created by the user into a json file



def importTabs(file_path):#worst case--->O(1)
  global main_dict
  with open(file_path, "r") as f:
    main = json.loads(f.read())
  main_dict = main


def displayMenu():#worst case--->O(1)
  print("1. Open Tab\n2. Close Tab\n3. Switch Tab")
  print("4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs")
  print("7. Save Tabs\n8. Import Tabs\n9. Exit")  #using 3 print statment only for better visualization

  

def main():#worst case--->O(N^2) where main handeles the worst case among all function which is O(N^2) for (displayAllTabs function)
  displayMenu()
  choice = eval(input("Enter a number: "))

  while choice != 9:
    if choice == 1:
      title = input("Enter the title of the tab:")
      url = input("Enter the URL of the website:")
      openTab(title, url)
    elif choice == 2:
      index = input("Enter the index of the tab you want to close:")
      closeTab(index)
    elif choice == 3:
      number = input("Enter the index of the tab you whant to display its content: ")
      switchTab(number)
    elif choice == 4:
      all_tabs = main_dict["all_tabs"]
      displayAllTabs(all_tabs)
    elif choice == 5:
      parent_tab_index = input("Enter the index of the parent tab:")
      openNestedTab(parent_tab_index)
    elif choice == 6:
      opened_tabs = main_dict["all_tabs"]
      clearAllTabs(opened_tabs)
    elif choice == 7:
      file_path = input("Enter the path of your json file")
      saveTabs(file_path)
    elif choice == 8:
      file_path = input("Enter the path of your json file")
      importTabs(file_path)
    elif choice != 9:
      print("Invalid input.Try to choose a number from 1 to 9")

    displayMenu()
    choice = eval(input("Enter a number: "))

  print("Exited")  #if choice = 9 the while loop will be entered thus exiting and terminating the program.


main()
#####end#####
