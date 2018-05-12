from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nim = db.Column(db.String(15), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    tempat_tl = db.Column(db.String(50), nullable=False)
    jk = db.Column(db.Char(1), nullable=False)
    prodi = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(10), nullable=False)

class Dosen(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nip = db.Column(db.String(15), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    jk = db.Column(db.Char(1), nullable=False)
    umur = db.Column(db.String(10), nullable=False)
    agama = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.String(20), nullable=False)