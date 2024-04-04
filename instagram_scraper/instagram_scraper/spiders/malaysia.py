from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
file = open("malaysia_membership.txt", mode='w')
driver.get("https://mia.org.my/members-firm-search/members-firm-search-results/?data=aFIvWFhyR2orelNBMm1nczRlL2xBMVpxVFpsemY5amdJcEFlN0xXN3BrR3NhSTVGdXlXOHh0bTRCcHlEL2tWbU9CdGJ5WTdwelF1aG5odUlxTFBoOVBJUzVKRjVjd1ZWWTBHaWJhSGtidjlDdUsvTW13akRzZnBSdlZaOTRDb3BRdTUvci8wRTdXS3Y1Q3VaSFlzUGZnbXI5elVRR04reFFuVXVQd2g4ZW1BPQ==#")
time.sleep(3)

members = driver.find_elements("xpath", "//div[@class='table-2']/table/tbody")
print(len(members))

for member in members:
    firm_no = member.find_element("xpath", '(.//tr/td)[1]').text
    firms_name = member.find_element('xpath', "(.//tr/td)[2]").text
    Address = member.find_element('xpath', "(.//tr/td)[3]").text
    State = member.find_element('xpath', "(.//tr/td)[4]").text
    Country = member.find_element("xpath", "(.//tr/td)[5]").text
    Contact = member.find_element("xpath", "(.//tr/td)[6]").text
    website = member.find_element("xpath", "(.//tr/td)[7]").text

    print('firm_no :' , firm_no,  'firms_name :', firms_name, 'Address :', Address ,'State :', State, 'Country :', Country, 'Contact :', Contact, 'website :', website)

    file.write(f"firm_no: {firm_no}, firms_name: {firms_name}, Address: {Address}, State: {State},Country: {Country},Contact: {Contact},website: {website}, \n")