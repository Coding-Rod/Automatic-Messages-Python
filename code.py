#In[]
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import socket

#In[]
#CSV file
#---------------------------------------------
import pandas as pd
df = pd.read_csv("list.csv", encoding='latin-1')

country_code = 591
student_name = [x.split(' ')[0] for x in df['Nombre'].to_list()]
student_number = df['Telefono'].to_list() # list of phone number 

for i in range(0,len(student_number)):
    student_number[i]=int(float(str(country_code) + str(int(student_number[i]))))

no_of_message=1 # no. of time 
def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,name):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            # message to join the official group
            txt_box.send_keys("Hola, "+name+' buenas tardes, gracias buenas tardes, gracias por inscribirte a las charlas de RAS, el link para la charlas "¿Qué es realmente la robótica?" es https://us06web.zoom.us/j/88181175919?pwd=YUtJN0xJRWJnNGo1Wm96cEJDbFJBUT09 , . Asimismo, enviaremos un correo momentos antes del evento como un recordatorio. ¡Te esperamos!')
            txt_box.send_keys("\n")
            
    except Exception as e:
        print("invalid phone no :"+str(phone_no))
        
#for i in range(0,1):
for i,j in zip(student_name,student_number):
    try:
        send_whatsapp_msg(i,j)

    except Exception as e:
        sleep(10)
        is_connected()