import sqlite3
from flask import g, current_app

# sqlite3, SQLite veritabaniyla calismamizi saglar.
# g, bir istek boyunca veritabani baglantisini gecici olarak tutar G = geçici saklama alanı olarak düşünülebilir.
# current_app, aktif Flask uygulamasinin ayarlarina ulasmamizi saglar.

def get_db():
    #  Bu istek için daha önce veitabanı bağlantısı açılmadıysa yeni bağlantı açar.
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE_URL"])

        #  Veritabanı sonuçlarına sutün isimleriyle erişmemizi sağlar.
        g.db.row_factory = sqlite3.Row

        #  Mevcut veritabanı bağlantısını geri döndürür.
    return g.db
     
def init_db(app):
    # Flask uygulamasının contextini geçici olarak aktif hale getirir.
    #  Boylece get_db() icindeki current_app hangi uygulamayi kullanacagini bilir.
    with app.app_context():
        #  Veritabanı bağlantısını alır.
        db = get_db()

        # Leads tablosu yoksa oluşturur. Zaten varsa bu komut hiçbir şey yapmaz.
        db.execute("""
         CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            mesaj TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          )
        """)

        # CREATE TABLE işlemini veritabanına kalıcı olarak kaydeder.
        db.commit()

def lead_ekle(isim, telefon, mesaj):
    # Veritabanı bağlantısını alır.
    db = get_db()

    # ? Placeholder kullanarak kullanıcı verisini SQL sorgusundan ayırır ve SQL enjeksiyon saldırılarına karşı koruma sağlar.
    db.execute(
        'INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)',
        (isim, telefon, mesaj)
    )

    #  Eklenen kaydı veritabanına kalıcı olarak kaydeder.
    db.commit()

def tum_leadler():
    # Veritabanı bağlantısını alır.
    db = get_db()

    # Tüm leadleri en yeni kayıttan en eski kayda doğru getirir.
    leadler = db.execute('SELECT * FROM leads ORDER BY tarih DESC').fetchall()

    # Veritabanından alınan lead listesini geri döndürür.
    return leadler
 