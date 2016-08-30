from time import sleep
from selenium import webdriver
import re
def septa(str1,str2,str3,str4,str6):  
    driver = webdriver.Firefox()
    driver.get('http://www.septa.org/')
    sleep(3)
    fromAddress = driver.find_element_by_xpath("//div[@class='septa_destination_container']/input[@id='from']")
    fromAddress.clear()
    fromAddress.send_keys(str1)
    toAddress = driver.find_element_by_xpath("//div[@class='septa_destination_container']/input[@id='to']")
    toAddress.clear()
    toAddress.send_keys(str2)
    # Put in date and time
    Date = driver.find_element_by_xpath("//input[@id='datepicker']")
    Date.clear()
    Date.send_keys(str6)
    Time = driver.find_element_by_xpath("//input[@id='time']")
    Time.clear()
    Time.send_keys(str3)
    DARadio = driver.find_element_by_xpath("//div[@class='gray_container round_all']")
    if str4 == "D":
        Departing = DARadio.find_element_by_xpath("//input[@value='depart']")
        Departing.click()
    else:
        Arriving = DARadio.find_element_by_xpath("//input[@value='arrive']")
        Arriving.click()
    submitButton = driver.find_element_by_xpath("//p[@class='septa_trip_planner_apps']/input[@value='Plan My Trip']")
    submitButton.click()
    MoreOptionsButton = driver.find_element_by_xpath("//input[@value='More']")
    MoreOptionsButton.click()
    CheckBoxesList = driver.find_elements_by_xpath("//input[contains(@id,'HFS_product')]")
    for i in range(0, len(CheckBoxesList) - 1):
        CheckBoxesList[i].click()
    newSubmitButton = driver.find_element_by_xpath("//div[@class='buttons']/input[@value='Plan my trip']")
    newSubmitButton.click()
    TripResult = driver.find_element_by_tag_name("tbody")
    DepartStationsList = TripResult.find_elements_by_xpath("//tr[@class='tpDetails first']/td[@class='first station']/a")
    ArriveStationsList = TripResult.find_elements_by_xpath("//tr[@class='tpDetails last']/td[@class='first station']/a")
    TripTime = TripResult.find_element_by_xpath("//tr[@class='tpDetails']/td").text
    TripTimeRegMatch = re.search(r'\d+:\d\d', TripTime)
    TripTime = TripTimeRegMatch.group(0)
    Price = TripResult.find_element_by_xpath("//tr[@class='tpDetails']/td[@class='sepline']").text
    PriceRegMatch = re.search(r'\$\d+\.\d\d', Price)
    Price = PriceRegMatch.group(0)
    p="Below is the best itinerary:\n"
    for j in range(0,len(DepartStationsList)):
        des=DepartStationsList[j].text
        ars=ArriveStationsList[j].text
        p=p+" From "+str(des)+" to "+str(ars)+"\n"
    p=p+"Trip takes "+TripTime+" And the fare is "+Price
    driver.quit()
    return p
