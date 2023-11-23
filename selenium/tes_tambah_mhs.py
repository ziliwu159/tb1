from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Chrome()

try:
  driver.get("http://127.0.0.1:9999/mahasiswa/tambah")
  nim = driver.find_element(By.NAME, "nim")
  nama_lengkap = driver.find_element(By.NAME, "nama_lengkap")
  alamat = driver.find_element(By.NAME, "alamat")
  tambah = driver.find_element(By.XPATH, "//button[text()='Tambah']")

  nim.send_keys('3312301053')
  time.sleep(2)
  nama_lengkap.send_keys('Yurisha Anindya')
  time.sleep(2)
  alamat.send_keys('Batam, Batu Aji')
  time.sleep(2)

  tambah.click()
  time.sleep(5)

  if "mahasiswa" in driver.current_url:
    status = "Sukses Menambahkan Data mahasiswa.."
  else:
    status = "Gagal menambahkan data.."  

except Exception as e:
  status = "Gagal"  
  print(f"Terjadi Kesalahan : {e}")

finally:
  with open("hasil-tambah-mhs.txt", "a") as file:
    waktu_uji = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    file.write(f"{waktu_uji} - Fitur CRUD - Status : {status} \n ")


driver.quit()
# except Exception as e:

  
