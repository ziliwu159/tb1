from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

driver = webdriver.Chrome()

try:
    # Klik tombol "Ubah" pada baris pertama tabel
    driver.get("http://127.0.0.1:9999/mahasiswa") 
    time.sleep(5) 
    tombol_ubah = driver.find_element(By.XPATH, "(//table[@class='table table-striped text-center']//tr[position()=1]//a[text()=' Ubah'])[1]")    
    tombol_ubah.click()
    time.sleep(5)

    nama_input = driver.find_element(By.NAME, "nama_lengkap")
    alamat_input = driver.find_element(By.NAME, "alamat")

    nama_input.clear()
    time.sleep(2)
    nama_input.send_keys("Jesika Chow")
    time.sleep(5)
    
    alamat_input.clear()
    time.sleep(2)
    alamat_input.send_keys("Jawa Barat") 
    time.sleep(5)

    tombol_update = driver.find_element(By.XPATH, "//button[text()='Update']")
    tombol_update.click()
    time.sleep(5)

    if "mahasiswa" in driver.current_url:
        status = "Sukses"
    else:
        status = "Gagal - Ubah data mahasiswa gagal."

except Exception as e:
    status = "Gagal"
    print(f"Terjadi kesalahan: {e}")

finally:
    with open("uji-edit.txt", "a") as file:
        waktu_uji = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{waktu_uji} - Fitur CRUD Ubah Mahasiswa - Status: {status}\n")

    driver.quit()
