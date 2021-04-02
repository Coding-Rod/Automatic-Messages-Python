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
dataframe = pd.read_csv("list.csv", encoding='latin-1')

country_code = 591
student_name = dataframe['NOMBRES'].to_list()
student_number = dataframe['CELULAR'].to_list() # list of phone number 
p1 = dataframe['PROYECTO 1'].to_list() # list of phone number 
p2 = dataframe['PROYECTO 2'].to_list() # list of phone number 
p3 = dataframe['PROYECTO 3'].to_list() # list of phone number
p4 = dataframe['PROYECTO 4'].to_list() # list of phone number  
print(p1)

# Group link
group_sce = {
  "MECA MOBILE": "https://chat.whatsapp.com/FasREUqTr9e8C50Kluwz5u",
  "ROVER HERC NASA": "https://chat.whatsapp.com/I4BOhZ8CVjz0uHN0WiHJnq",
  "QIP CONTROL": "https://chat.whatsapp.com/JOqRSUjEZur35JasTc0wJJ",
  "SOLAR CAR": "https://chat.whatsapp.com/ExiDP6Sd0qnFhwea2T1bdU",
  "ROBOTICA COMPETITIVA": "https://chat.whatsapp.com/D5zMx766Z4J6mThPyqb6R8",
  "ENJAMBRE": "https://chat.whatsapp.com/JxBQJz5ua52BWCGpItfj6e",
  "TECHNOLOTREE": "https://chat.whatsapp.com/FqC79jiScdUCzWDaB2hyI2",
  "MONITOR INTEGRAL DE BEBÉS (MIB)": "https://chat.whatsapp.com/BWlOuM0jm5CE0ZrOdS5NtE",
  "EXOM": "https://chat.whatsapp.com/Bw4dVECs0POItjiV8ehNcl",
  "VOA": "https://chat.whatsapp.com/CVaHrxGXyNB3fCQhpmziOA",
  "SEEKER": "https://chat.whatsapp.com/KiWW09AemTEB7mJpFLDf3P",
  "ASSISTANT ROBOTIC ARM": "https://chat.whatsapp.com/KrH7hOTYc3wFT45ffluMlQ",
  "CUBESAT": "https://chat.whatsapp.com/LfRzsjGraZeE95QQnZkVbR",
  "DEEPRACER-AWS": "https://chat.whatsapp.com/Ec6olzo306Q9QW7qsTu8sy"
}
for i in range(0,len(student_number)):
    student_number[i]=int(float(str(country_code) + str(int(student_number[i]))))
#---------------------------------------------

no_of_message=1 # no. of time 
mensaje_sce = "gracias por ser parte de la Sociedad Científica de ingeniería Mecatrónica *SCE-IMT*, te mando el enlace para que puedas unirte al grupo al grupo oficial:"
link_grupo_oficial = " https://chat.whatsapp.com/IMR0P4LORSw5bdQgLCDwPu"
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

def send_whatsapp_msg(phone_no,name,p1,p2,p3,p4):
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
            txt_box.send_keys("Hola "+name+" buenas noches, "+mensaje_sce+link_grupo_oficial)
            txt_box.send_keys("\n")
            for key in group_sce:
                if p1==key:
                    txt_box.send_keys("Únete a tu primer proyecto: "+key+" "+group_sce[key])
                    txt_box.send_keys("\n")

            for key in group_sce:
                if p2==key:
                    txt_box.send_keys("Únete a tu segundo proyecto: "+key+" "+group_sce[key])
                    txt_box.send_keys("\n")
            
            for key in group_sce:
                if p3==key:
                    txt_box.send_keys("Únete a tu tercer proyecto: "+key+" "+group_sce[key])
                    txt_box.send_keys("\n")
            
            for key in group_sce:
                if p4==key:
                    txt_box.send_keys("Únete a tu cuarto proyecto: "+key+" "+group_sce[key])
                    txt_box.send_keys("\n")
            
            txt_box.send_keys("Por último necesitamos que te unas al Discord general de la SCE-IMT, por acá gestionaremos el avance de todos los proyectos, el apodo en este canal debe ser tu *Nombre* y *Apellido*. Ej: Fabricio Jallaza. De esta manera podrás comunicarte con tu grupo de trabajo. El apodo es lo *más* imporante: https://discord.gg/n8WmWQUJwC")
            txt_box.send_keys("\n")
            
    except Exception as e:
        print("invailid phone no :"+str(phone_no))
        
#for i in range(0,1):
for i in range(0,len(student_number)):
    try:
        send_whatsapp_msg(student_number[i],student_name[i],p1[i],p2[i],p3[i],p4[i])

    except Exception as e:
        sleep(10)
        is_connected()