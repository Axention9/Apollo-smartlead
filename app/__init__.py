from flask import Flask
from flask_cors import CORS
# Flask, ana uygulama nesnesini oluşturmamızı sağlar.
# CORS, frontend'in backend API'sine farklı origin üzerinden erişebilmesini sağlar.

# Config, uygulama ayarlarını içerir.
from config import config 

# init_db, uygulama başlarken veritabanı tablosunu hazırlar.
from app.database import init_db

# Blueprint'ler, sayfa ve API rotalarını Flask uygulamasına bağlamamızı sağlar.
from app.routes import pages_bp, api_bp

def create_app(config_name="development"):
    # Hangi ortamda çalıcağanı seçer
    app = Flask(__name__)

    # Config sınıfındaki ayarları Flask uygulamasına yükler.
    app.config.from_object(config[config_name])

    # Frontend'in backend API'sine farklı origin üzerinden erişmesine izin verir.
    CORS(app, origins=app.config["CORS_ORIGINS"])

    # Flask uygulamasını veritabanı katmanına göndererek tabloyu hazırlar.
    init_db(app)

    # /api öneki api_bp oluşturulurken routes.py'de tanımlandığı için burada tekrar verilmez.
    # Sayfa ve API rotalarını Flask uygulamasına kaydeder.
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    #  Sunucunun çalışıp çalışmadığını kontrol etmek için sağlık endpointi.
    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    # Hazırlanan Flask uygulamasını çağıran koda geri döndürür.
    return app