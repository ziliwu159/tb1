from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

# inisialisasi flask
app = Flask(__name__)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbpolibatam'
mysql = MySQL(app)

# APP secret key (bebas)
app.secret_key = "4cc645e832bc2ed0869da6d3a9bdc0ea"

def _ini_(self, judul, deskripsi, sks, programstudi, semester):
        self.judul = judul
        self.deskripsi = deskripsi
        self.sks = sks
        self.programstudi = programstudi
        self.semester = semester
         
# definisi fungsi dan route untuk URL agar bisa diakses oleh browser
@app.route('/', methods = ['GET'])
def login():
    return render_template('login.html',)

@app.route('/verifikasi-login', methods=['POST'])
def verifikasiLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cur.fetchone()
        cur.close()

        if user:
            user_session_data = {
                'id': user[0],
                'email': user[1]
            }
            session['user_id'] = user_session_data['id']
            flash('Login berhasil. Selamat datang!', 'success')
            return redirect('/dashboard')  
        else:
            flash('Email atau password salah', 'error')
            return redirect('/')  

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))     

@app.route('/mahasiswa', methods = ['GET'])
def data_mahasiswa():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id,nim,nama_lengkap,alamat FROM students ORDER BY id')
    data = cur.fetchall()
    cur.close()
    return render_template('mahasiswa/data-mahasiswa.html', mahasiswa = data)
    
@app.route('/mahasiswa/tambah', methods = ['GET'])
def tambah_mahasiswa():
    return render_template('mahasiswa/tambah-mahasiswa.html')

@app.route('/mahasiswa/insert', methods=['POST'])
def add_mahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']
        nama_lengkap = request.form['nama_lengkap']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (nim, nama_lengkap, alamat) VALUES (%s,%s,%s)", 
        (nim, nama_lengkap, alamat))
        mysql.connection.commit()
        flash('Data mahasiswa berhasil ditambahkan!')
        return redirect(url_for('data_mahasiswa'))

@app.route('/mahasiswa/edit/<int:id>', methods = ['GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM students WHERE id = {id}")
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('mahasiswa/ubah-mahasiswa.html', contact = data[0])

@app.route('/mahasiswa/update/<int:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nim = request.form['nim']
        nama_lengkap = request.form['nama_lengkap']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE students
            SET nim = %s, nama_lengkap = %s, alamat = %s
            WHERE id = %s
        """, (nim,nama_lengkap, alamat, id))
        flash('Data mahasiswa berhasil diubah!')
        mysql.connection.commit()
        return redirect(url_for('data_mahasiswa'))

@app.route('/mahasiswa/delete/<int:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM students WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Data mahasiswa berhasil dihapus!')
    return redirect(url_for('data_mahasiswa'))


@app.route('/matakuliah', methods = ['GET'])
def data_kuliah():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mata_kuliah ORDER BY kode')
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah.html', matakuliah = data)
    
@app.route('/matakuliah/tambah', methods = ['GET'])
def tambah_matakuliah():
    return render_template('matakuliah/tambah-matakuliah.html')

@app.route('/matakuliah/insert', methods=['POST'])
def add_kuliah():
    if request.method == 'POST':
        judul = request.form['judul']
        deskripsi = request.form['deskripsi']
        sks = request.form['sks']
        programstudi = request.form['programstudi']
        semester = request.form['semester']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mata_kuliah ( judul, deskripsi, sks, programstudi, semester) VALUES (%s,%s,%s,%s,%s)", 
        (judul, deskripsi, sks, programstudi, semester))
        mysql.connection.commit()
        flash('Mata kuliah berhasil ditambahkan!')
        return redirect(url_for('data_kuliah'))

@app.route('/matakuliah/edit/<int:kode>', methods = ['GET'])
def get_contact1(kode):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM mata_kuliah WHERE kode = {kode}")
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('matakuliah/ubah-matakuliah.html', contact = data[0])

@app.route('/matakuliah/update/<int:kode>', methods=['POST'])
def update_contact1(kode):
    if request.method == 'POST':
        judul = request.form['judul']
        deskripsi = request.form['deskripsi']
        sks = request.form['sks']
        programstudi = request.form['programstudi']
        semester = request.form['semester']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE mata_kuliah
            SET judul = %s, deskripsi = %s, sks = %s, programstudi = %s, semester = %s
            WHERE kode = %s
        """, ( judul, deskripsi, sks, programstudi, semester, kode))
        flash('Mata Kuliah berhasil diubah!')
        mysql.connection.commit()
        return redirect(url_for('data_kuliah'))

@app.route('/matakuliah/delete/<int:kode>', methods = ['POST','GET'])
def delete_contact1(kode):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM mata_kuliah WHERE kode = {0}'.format(kode))
    mysql.connection.commit()
    flash('Mata Kuliah berhasil dihapus!')
    return redirect(url_for('data_kuliah'))

@app.route('/matakuliah/IF', methods = ['GET'])
def IF():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Teknik Informatika'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/IF', matakuliah = data)

@app.route('/matakuliah/TRM', methods = ['GET'])
def TRM():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Teknik Rekayasa Multimedia'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/TRM', matakuliah = data)

@app.route('/matakuliah/GM', methods = ['GET'])
def GM():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Geomatika'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/GM', matakuliah = data)
    
@app.route('/matakuliah/TRPL', methods = ['GET'])
def TRPL():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Teknik Rekayasa Perangkat Lunak'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/TRPL', matakuliah = data)

@app.route('/matakuliah/RKS', methods = ['GET'])
def RKS():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Teknik Rekayasa Keamanan Siber'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/RKS', matakuliah = data)


@app.route('/matakuliah/AN', methods = ['GET'])
def AN():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mata_kuliah WHERE programstudi = 'Animasi'")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah/data-kuliah-prodi/matkul.html', path='/matakuliah/AN', matakuliah = data)

# Jalankan aplikasi dengan port 9999
if __name__ == "__main__":
    app.run(port = 9999, debug = True)

# Jalankan aplikasi dengan port 9999
if __name__ == "__main__":
    app.run(port = 9999, debug = True)