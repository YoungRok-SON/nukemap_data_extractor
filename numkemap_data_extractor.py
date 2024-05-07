"""
Breif
This script has written for web data scraping.
Target website is https://nuclearsecrecy.com/nukemap/

Author: YoungRok Son
email: dudfhr3349@gmail.com

Thanks to NUKEMAP developer, Alex Wellerstein about this awesome website.
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import numpy as np
import time

from collections import defaultdict
import csv

# Install Web driver
service_obj = Service(ChromeDriverManager().install())

# Web driver init. Chorm has choosen in this case.
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 40)




# Open NUKE MAP 
driver.get('https://nuclearsecrecy.com/nukemap/')

wait.until(EC.visibility_of_element_located((By.ID, 'geocodeInput')))
city_input = driver.find_element('id','geocodeInput')  

web_loading = True
while(web_loading):
    if(city_input.is_enabled()):
        # Put a name of City
        city_input.clear()
        city_input.send_keys('Seoul, South Korea')
        city_input.send_keys(Keys.RETURN)
        web_loading = False
    

# Set a Advanced Settings 
wait.until(EC.visibility_of_element_located((By.ID, 'hider-arrow')))
adv_toggle = driver.find_element('id', 'hider-arrow')
adv_toggle.click()

wait.until(EC.visibility_of_element_located((By.ID, 'psi_3000')))

# Set a overpressure ring visualization option
cb_3000psi_pressure = driver.find_element('id', 'psi_3000')
if( cb_3000psi_pressure.is_selected() == False):
    cb_3000psi_pressure.click()

cb_200psi_pressure = driver.find_element('id', 'psi_200')
if( cb_200psi_pressure.is_selected() == False):
    cb_200psi_pressure.click()

cb_20psi_pressure = driver.find_element('id', 'psi_20')
if( cb_20psi_pressure.is_selected() == False):
    cb_20psi_pressure.click()
    
cb_5psi_pressure = driver.find_element('id', 'psi_5')
if( cb_5psi_pressure.is_selected() == False):
    cb_5psi_pressure.click()
    
cb_1psi_pressure = driver.find_element('id', 'psi_1')
if( cb_1psi_pressure.is_selected() == False):
    cb_1psi_pressure.click()

cb_other_pressure = driver.find_element('id', 'psi_other_check_1')
if( cb_other_pressure.is_selected() == True):
    cb_other_pressure.click()    
    
    
# Set a ionizing radiation rings visualization option
cb_100rem_rad = driver.find_element('id', 'rem_100')
if( cb_100rem_rad.is_selected() == False):
    cb_100rem_rad.click()

cb_500rem_rad = driver.find_element('id', 'rem_500')
if( cb_500rem_rad.is_selected() == False):
    cb_500rem_rad.click()

cb_600rem_rad = driver.find_element('id', 'rem_600')
if( cb_600rem_rad.is_selected() == False):
    cb_600rem_rad.click()
    
cb_1000rem_rad = driver.find_element('id', 'rem_1000')
if( cb_1000rem_rad.is_selected() == False):
    cb_1000rem_rad.click()
    
cb_5000rem_rad = driver.find_element('id', 'rem_5000')
if( cb_5000rem_rad.is_selected() == False):
    cb_5000rem_rad.click()

cb_other_rad = driver.find_element('id', 'rem_other_check_1')
if( cb_other_rad.is_selected() == True):
    cb_other_rad.click() 
    
    
# Set a thermal radiation rings visualization option
cb_them_3rd_100 = driver.find_element('id', 'therm_3rd-100')
if( cb_them_3rd_100.is_selected() == False):
    cb_them_3rd_100.click()

cb_them_3rd_50 = driver.find_element('id', 'therm_3rd-50')
if( cb_them_3rd_50.is_selected() == False):
    cb_them_3rd_50.click()

cb_1st_50 = driver.find_element('id', 'therm_2nd-50')
if( cb_1st_50.is_selected() == False):
    cb_1st_50.click()
    
cb_noharm_100 = driver.find_element('id', 'therm_1st-50')
if( cb_noharm_100.is_selected() == False):
    cb_noharm_100.click()
    
cb_therm_noharm_100 = driver.find_element('id', 'therm_noharm-100')
if( cb_therm_noharm_100.is_selected() == False):
    cb_therm_noharm_100.click()
    
cb_therm_35 = driver.find_element('id', 'therm_35')
if( cb_therm_35.is_selected() == False):
    cb_therm_35.click()

cb_other_them = driver.find_element('id', 'therm_other_check_1')
if( cb_other_them.is_selected() == True):
    cb_other_them.click() 
    
    
# Set Other effects
cb_fireball = driver.find_element('id', 'check_fireball')
if( cb_fireball.is_selected() == False):
    cb_fireball.click()
    
cb_crater = driver.find_element('id', 'check_crater')
if( cb_crater.is_selected() == False):
    cb_crater.click()

cb_fallbout = driver.find_element('id', 'fallout_check')
if( cb_fallbout.is_selected() == True):
    cb_fallbout.click()  
    
cb_mcd = driver.find_element('id', 'check_cloud')
if( cb_mcd.is_selected() == True):
    cb_mcd.click()  
    
    
# list for data
data_by_height = defaultdict(list)

# For here from 0 to 200kt of each height.

for height in range(0, 3001, 100):
    print("height: " + str(height))
    for kt in np.arange(0.5, 200.5, 0.5):
        print("kt: " + str(kt))

        wait.until(EC.visibility_of_element_located((By.ID, 'theKt')))

        # Set a weight of warhead
        yield_input = driver.find_element('id','theKt')  # id는 예시일 뿐, 실제 id를 찾아서 사용해야 함
        yield_input.clear()
        yield_input.send_keys(kt)
        
        # click advanced tap toggle
        wait.until(EC.visibility_of_element_located((By.ID, 'hider-arrow')))
        adv_toggle = driver.find_element('id', 'hider-arrow')
        adv_toggle.click()
        
        # Set a height of burst
        surface_of_burst = driver.find_element('id','hob_airburst') # id는 예시일 뿐, 실제 id를 찾아서 사용해야 함
        surface_of_burst.click();
        

        # Set a Airbust setting as Burst height.
        # burst_height = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'hob_option_height')))
        # driver.execute_script("arguments[0].scrollIntoView(true);", burst_height)
        # time.sleep(1)  # 페이지가 정상적으로 로드되고 요소가 활성화될 시간을 주기 위해 추가
        # burst_height.click();
        
        burst_height = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'hob_option_height')))
        driver.execute_script("arguments[0].scrollIntoView(true);", burst_height)
        time.sleep(1)  # 페이지 로드를 기다림
        driver.execute_script("arguments[0].click();", burst_height)
        
        burst_height_add = wait.until(EC.element_to_be_clickable((By.ID, 'hob_h')))
        hob_h = driver.find_element('id', 'hob_h')
        hob_h.clear()
        hob_h.send_keys(height)
        
        burst_height_unit = wait.until(EC.element_to_be_clickable((By.ID, 'hob_h_u')))
        hob_unit = Select(driver.find_element('id','hob_h_u'))
        hob_unit.select_by_index('1')
        loading = False
        
        # 폼 제출
        submit_button = driver.find_element('id','detonate')  # id는 예시일 뿐, 실제 id를 찾아서 사용해야 함
        submit_button.click()

        

        
        elements = driver.find_elements(By.CLASS_NAME, 'effectCaption')
        
        # radius 값들을 추출합니다.
        radius_values = [element.get_attribute('radius') for element in elements]
        print(radius_values)
        data_by_height[height].append((kt, radius_values))
        
                

# Quit the connection
driver.quit()

import pandas as pd

# Excel 파일 생성을 위한 writer 준비
with pd.ExcelWriter('output_data(air).xlsx', engine='openpyxl') as writer:
    for height, data in data_by_height.items():
        # 각 고도별로 데이터 처리 및 데이터프레임 생성
        processed_data = []
        for kt, radius_values in data:
            # 두 번째 원소가 None이면 제거
            if radius_values[1] is None:
                del radius_values[1]
            # 데이터 길이가 19개가 아니면 조정 (예를 들어, 다른 위치에도 None 값이 있을 경우)
            if len(radius_values) > 19:
                radius_values = radius_values[:19]
            processed_data.append([kt] + radius_values)
        
        # 처리된 데이터로 DataFrame 생성
        df = pd.DataFrame(processed_data, columns=['kt'] + ['Crater Inside', 'Crater Lip', 'Air Blast 3000psi', 'Air Blast 200psi', 'Fireball', 'Heavy Blast 20psi', 'Radiation 5000rem', 'Radiation 1000rem', 'Radiation 600rem', 'Radiation 500rem', 'Radiation 100rem', 'Moderate Blast 5psi', 'Thermal Radiation 35cal/cm^2', 'Thermal Radiation 3rd degree burns', 'Thermal Radiation 3rd degree burns(50%)', 'Light Blast 1psi', 'Thermal Radiation 2nd degree burns', 'Thermal Radiation 1st degree burns(50%)', 'Thermal Radiation no harm'])
        # 데이터프레임을 시트로 저장
        df.to_excel(writer, sheet_name=f'Alt={height}(SurfaceBurst)', index=False)



# save the data to csv
for height, data in data_by_height.items():
    # CSV 파일명 설정
    filename = f"data_height_{height}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 헤더 작성
        writer.writerow(['kt', 'Crater Inside', 'Crater Lip', 'Air Blast 3000psi', 'Air Blast 200psi', 'Fireball', 'Heavy Blast 20psi', 'Radiation 5000rem', 'Radiation 1000rem', 'Radiation 600rem', 'Radiation 500rem', 'Radiation 100rem', 'Moderate Blast 5psi', 'Thermal Radiation 35cal/cm^2', 'Thermal Radiation 3rd degree burns', 'Thermal Radiation 3rd degree burns(50%)', 'Light Blast 1psi', 'Thermal Radiation 2nd degree burns', 'Thermal Radiation 1st degree burns(50%)', 'Thermal Radiation no harm'])
        # 데이터 쓰기
        for kt, radius_values in data:
            writer.writerow([kt] + radius_values)
        