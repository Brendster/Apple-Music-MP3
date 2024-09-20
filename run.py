from AppleScraper import AppleScraper
from AppleLogin import AppleLogin
from getpass import getpass

url = input("Enter the url for your Apple playlist: ")

username_txt = input("Enter you apple id username or email: ")
password_txt = getpass("Enter your apple id password: ")

login = AppleLogin(username_txt, password_txt, url)

#Scraper = AppleScraper(url)

#Scraper.printHTML()