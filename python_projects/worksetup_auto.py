import webbrowser as wb
import os 

def workauto():
    codepath =  "C:\\Windows\\notepad.exe"
    # os.startfile(codepath)
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # URLS = ("gmail.com", "google.com", "youtube.com")
    
    url = input("Enter name of the website:- ")
    wb.get(chrome_path).open(url)
        
    # for url in URLS:
    #     wb.get(chrome_path).open(url)

workauto()