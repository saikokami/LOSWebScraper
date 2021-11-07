import requests
import datetime
from bs4 import BeautifulSoup
def getDonations():
    page = requests.get("https://legionofsensei.de/gextension/index.php?t=shop")
    soup = BeautifulSoup(page.content, 'html.parser')

    result= soup.find_all(id="donate_latest_donations")
    result_string = str(result)
    index=0
    print("------Legion Of Sensei Spenden------")
    while index < len(result_string):
        
        #Finde UserID

        index = result_string.find(';id=', index)
        if index == -1:
            break 
        result_find=result_string[index+4:index+20]
        print("SteamID:",result_find.split('"')[0])  
        index += 4

        #Finde SteamName        
        index = result_string.find('ank">', index) 
        result_find=result_string[index+5:index+40]
        print("Name:",result_find.split('<')[0])  
        index += 5

        #Finde PacketName       
        index = result_string.find('ank">', index) 
        result_find=result_string[index+5:index+40]
        print("Paket:",result_find.split('<')[0])  
        index += 5

        #Finde Kaufdatum      
        index = result_string.find('<td>', index) 
        result_find=result_string[index+4:index+20]
        print("Datum:",result_find.split('<')[0])  
        index += 5

        #Finde Preis
        index = result_string.find('€', index) #Setze EuroIndex auf: Index wo das nächste € Symbol ab Index gefunden wird.
        result_find=result_string[index:index+10]
        print("Preis:",result_find.split("<")[0])  #Split bewirkt dass aus "10.00<td>"" -> "10.00" wird Ergo alles inkl < wird nicht ausgegeben! 
        print("")  
        index += 1

def test():
    page = requests.get("https://legionofsensei.de/gextension/index.php?t=shop")
    soup = BeautifulSoup(page.content, 'html.parser')

    result= soup.find_all(id="donate_latest_donations")
    re_str = str(result)

    print(re_str)


def getLastDonationDate():
    page = requests.get("https://legionofsensei.de/gextension/index.php?t=shop")
    soup = BeautifulSoup(page.content, 'html.parser')
    result= soup.find_all(id="donate_latest_donations")
    result_string = str(result)
    index = result_string.find("."+str(datetime.datetime.now().year))
    result_find=result_string[index-5:index+11]
    print(result_find)


def main():
    print("----------------Legion of Sensei Menu----------------")
    print("1: Show last 6 Dontions")
    print("2: Show last Donation(date)")
    print("-----------------------------------------------------")
    wahl = input("Enter number:")
    if wahl=="1":
        getDonations()
    elif wahl=="2":
        getLastDonationDate()
    else:
        print("Wrong choice")



main()
