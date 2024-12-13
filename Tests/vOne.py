from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from os import path, getcwd
import warnings

warnings.simplefilter("ignore")

website = str(path.abspath(__file__))[0:-7]
website = (website, "web.html")
website = "".join(website)
print(website)

driver = None

def ListenInit(Driver): 
  global driver
  
  service = Service(Driver)
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--use-fake-ui-for-media-stream")
  chrome_options.add_argument("--headless=new")
  chrome_options.add_argument("--allow-insecure-localhost")
  chrome_options.add_argument("--disable-web-security")
  chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
  chrome_options.add_argument("--use-fake-device-for-media-stream")
  chrome_options.add_argument("--use-file-for-fake-audio-capture=/path/to/audio.wav")
  chrome_options.add_argument("--log-level=3")  # Suppress warnings and errors
  chrome_options.add_argument("--disable-logging")
  chrome_options.add_argument("--silent")
  
  driver = webdriver.Chrome(service=service, options=chrome_options) 
    
def Listen(printAllowed=False): 
  driver.get(website)
  driver.find_element(by=By.ID, value='start').click()
  if printAllowed: print("Listening ...")
  
  while True:
    text = driver.find_element(by=By.ID, value='output').text
    if text != "":
      if printAllowed: print(f"You : {text}")
      driver.find_element(by=By.ID, value='end').click()
      return text

ListenInit(f"{getcwd()}//Drivers//chromedriver.exe")
while True:
  print(Listen())