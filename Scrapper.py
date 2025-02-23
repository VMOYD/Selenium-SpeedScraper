from selenium import webdriver
from selenium.webdriver.common.by import By
import concurrent.futures
import threading
import csv
import time

filename = "sample.csv"  # Adjust path for local system
header = "Roll_no,NAME,NET_FRAMEWORK_Internal,cyber_laws_Internal,computer_graphics_I,Linux_i,optimization_i,net_framework_E,Cyber_E,ComputerGraph_E,Linux_E,OT_E,RESULT,TOTAL\n"

# Lock for thread-safe writing to CSV
write_lock = threading.Lock()

# Write header once
with open(filename, 'w', newline='') as f:
    f.write(header)

def fetch_data(roll):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        driver = webdriver.Chrome(options=options)

        url = "https://exam.bujhansi.ac.in/frmViewCampusCurrentResult.aspx?cd=MwA3ADkA/"
        driver.get(url)

        select_internal = driver.find_element(By.XPATH, "/html/body/form/div[3]/table/tbody/tr[4]/td[6]/select/option[20]")
        select_external = driver.find_element(By.XPATH, "/html/body/form/div[3]/table/tbody/tr[5]/td[3]/select/option[2]")
        input_roll = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[4]/td[3]/input')
        button_view = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[5]/td[4]/input')

        select_internal.click()
        select_external.click()
        input_roll.send_keys(str(roll))
        button_view.click()

        name = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[3]/span').text
        NET_FRAMEWORK_Internal = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td[3]').text
        cyber_laws_Internal = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[7]/td[3]').text
        computer_graphics_I = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[8]/td[3]').text
        Linux_i = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[9]/td[3]').text
        optimization_i = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[10]/td[3]').text
        net_framework_E = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td[5]').text
        Cyber_E = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[7]/td[5]').text
        ComputerGraph_E = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[8]/td[5]').text
        Linux_E = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[9]/td[5]').text
        OT_E = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[10]/td[5]').text
        RESULT = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/table/tbody/tr[2]/td/div/table/tbody/tr[18]/th[2]').text
        TOTAL = driver.find_element(By.XPATH, '//*[@id="tblMarksContent"]/table/tbody/tr[16]/th[12]').text

        row = f"{roll},{name},{NET_FRAMEWORK_Internal},{cyber_laws_Internal},{computer_graphics_I},{Linux_i},{optimization_i},{net_framework_E},{Cyber_E},{ComputerGraph_E},{Linux_E},{OT_E},{RESULT},{TOTAL}\n"

        with write_lock:
            with open(filename, 'a', newline='') as f:
                f.write(row)

        print(f"Fetched data for Roll No: {roll}")

    except Exception as e:
        print(f"No data found for roll number {roll}. Error: {e}")

    finally:
        driver.quit()

# Roll numbers to process
roll_numbers = list(range(211341133001, 211341133114))

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch_data, roll_numbers)

print("Data extraction complete!")
