from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import datetime
import time

driver = webdriver.Chrome()

try:
    # Klik tombol "Ubah" pada baris pertama tabel
    driver.get("http://127.0.0.1:9999/mahasiswa")
    time.sleep(5)

    # Tentukan kriteria untuk mencari baris yang akan dihapus (misalnya, NIM atau nama mahasiswa)
    kriteria = "3312301053" #Sesuaikan ini dengan NIM dari user yang terakhir diubah / ditambah

    # Temukan baris yang sesuai dengan kriteria
    baris = driver.find_element(By.XPATH, f"//table[@class='table table-striped text-center']//tbody//tr[td[contains(text(), '{kriteria}')]]")

    # Klik tombol "Hapus" di baris yang sesuai
    tombol_hapus = baris.find_element(By.XPATH, ".//a[text()=' Hapus']")
    tombol_hapus.click()

    # Menghadapi konfirmasi alert dan menyetujui (klik OK)
    alert = Alert(driver)
    alert.accept()
    time.sleep(5)

    # Memeriksa apakah elemen mahasiswa masih ada di halaman (menandakan data masih ada)
    elemen_mahasiswa = driver.find_elements(By.XPATH, f"//table[@class='table table-striped']//tr[td[contains(text(), '{kriteria}')]]")
    if not elemen_mahasiswa:
        status = "Sukses"
    else:
        status = "Gagal - Data mahasiswa masih ada setelah dihapus."

except Exception as e:
    status = "Gagal"
    print(f"Terjadi kesalahan: {e}")

finally:
    with open("uji-hapus.txt", "a") as file:
        waktu_uji = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{waktu_uji} - Fitur CRUD Hapus Mahasiswa - Status: {status}\n")

    driver.quit()
