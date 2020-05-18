import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


try :
    driver = webdriver.Chrome('C:/temp/chromedriver')
    driver.get('https://bigdataportal.dpt.co.kr')
    driver.find_element_by_css_selector('#lgn_id').send_keys('121600240')
    driver.find_element_by_css_selector('#lgn_pwd').send_keys('lotte0000***')
    driver.find_element_by_css_selector('#login-button').click()
    driver.find_elements_by_css_selector('.list_pa')[0].click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[-1])
    # print(driver.page_source)


    driver.find_element_by_css_selector('#topmenu5').click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element_by_css_selector('.mstr-dskt-lnk.profile').click()
    driver.implicitly_wait(10)


    folders = driver.find_elements_by_css_selector('.mstrLargeIconViewItem')

    for folder in folders :
        name = folder.find_element_by_css_selector('.mstrLargeIconViewItemName')
        print(name.text)
        if name.text == '박성호' :
            folder.click()
            break
    driver.implicitly_wait(10)
    time.sleep(5)


    reports = driver.find_elements_by_css_selector('.mstrLargeIconViewItem')

    for report in reports :
        name = report.find_element_by_css_selector('.mstrLargeIconViewItemName')
        print(name.text)
        if name.text == '19년 가전가구' :
            report.click()
            break
    driver.implicitly_wait(10)

    df_data = pd.DataFrame({})
    cols = ['id', 'age', 'apt', 'job_dong', 'is_emp', 'is_moved', 'sales']

    while True:
        rows = driver.find_element_by_css_selector('#table_UniqueReportID')
        temp = rows.text.split('\n')

        for m, t in enumerate(temp) :
            # print(t[1].split(" "))
            data = {}
            parsed = t.split(" ")
            if len(parsed) > 7 :
                new_parsed = [parsed[0], parsed[1], parsed[2]+" "+parsed[3], parsed[4], parsed[5], parsed[6], parsed[7]]
                parsed = new_parsed
            for n, i in enumerate(parsed) :
                try :
                    data[cols[n]] = i
                except Exception :
                    while True :
                        try : 
                            temp_rows = driver.find_element_by_css_selector('#table_UniqueReportID')
                            temp_temp = temp_rows.text.split('\n')
                            temp_t = temp_temp[m]
                            temp_i = temp_t.split(" ")
                            data[cols[n]] = temp_i
                            break
                        except Exception :
                            print(traceback.format_exc())
                            print(n)
                            print(parsed)
                            pass

            df_data = df_data.append(data, ignore_index=True)
        print(df_data)
    
        try :
            driver.find_element_by_css_selector('.mstrFetchIcon.mstrFetchNext').click()
            driver.implicitly_wait(10)
            time.sleep(1)
        except Exception as e:
            print(traceback.format_exc())
            break

    df_data.to_csv('Z:/data.csv')
    
    print(df_data)



        

finally :
    driver.quit()
    print("")

