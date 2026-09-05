from flask import Blueprint, render_template, request, jsonify
# Blueprint, rotaları mantıksal gruplara ayırmamızı sağlar.
# render_template, HTML sayfalarını kullanıcıya göstermemizi sağlar.
# request, kullanıcının gönderdiği HTTP verilerine erişmemizi sağlar.
# jsonify, Python verilerini JSON HTTP cevabına dönüştürmemizi sağlar.

# Veritabanı işlemlerini database katmanından alır.
from app.database import lead_ekle, tum_leadler

# Yapay zeka işlemlerini AI servis katmanından alır.
from app.services.ai_service import ai_service, AIServiceError

# Sayfa rotalarını bir arada tutar.
pages_bp = Blueprint("pages", __name__)

# API rotalarını /api öneki altında gruplar
api_bp = Blueprint("api", __name__, url_prefix="/api")

# Ana sayfa isteğinde index.html dosyasını kullanıcıya gösterir.
@pages_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Dashboard isteğinde dashboard.html dosyasını kullanıcıya gösterir.
@pages_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

# Kullanıcın mesajını alıp yapay zeka servisine yönlendiren API endpointidir.
@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    # Frontend'den JSON formatında gönderilen veriyi alır.
    veri = request.get_json(silent=True) or {}

    # JSON içinden kullanıcının mesajını ve konuşma geçmişini alır.
    mesaj = veri.get("mesaj", "").strip()
    gecmis = veri.get("gecmis", [])

    # Boş mesajların yapay zeka servisine gönderilmesini engeller.
    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj boş olamaz."
        }), 400

    # Mesajı ve konuşma geçmişini AI servis katmanına gönderir.
    try:
        yanit = ai_service.yanit_uret(mesaj, gecmis)

        # Yapay zekadan gelen yanıtı frontend'e JSON olarak döndürür.
        return jsonify({
            "basari": True,
            "yanit": yanit
        })

    except AIServiceError as hata:
        # AI servisinde oluşan hatayı kontrollü bir HTTP cevabına dönüştürür.
        return jsonify({
            "basari": False,
            "hata": str(hata)
        }), 503

# Frontend'den gelen müşteri bilgilerini veritabanı katmanına yönlendirir.
@api_bp.route("/leads", methods=["POST"])
def lead_olustur():
    # Frontend'den JSON formatında lead verisini alır.
    veri = request.get_json(silent=True) or {}

    # Lead için gerekli alanları JSON içinden alır.
    isim = veri.get("isim", "").strip()
    telefon = veri.get("telefon", "").strip()
    mesaj = veri.get("mesaj", "").strip()

    # İsim ve telefon zorunlu olduğu için boş bırakılmalarını engeller.
    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon boş olamaz."
        }), 400

    # Doğrulanmış lead bilgilerini veritabanı katmanına gönderir.
    lead_ekle(isim, telefon, mesaj)

    # Kayıt başarılıysa frontend'e başarılı cevap döndürür.
    return jsonify({
        "basari": True,
        "mesaj": "Lead başarıyla kaydedildi."
    }), 201

# Kayıtlı tüm leadleri veritabanı katmanından alıp frontend'e gönderir.
@api_bp.route("/leads", methods=["GET"])
def leadleri_listele():
    # Veritabanından gelen satırları JSON'a uygun sözlüklere dönüştürür.
    leadler = [dict(lead) for lead in tum_leadler()]

    # Lead listesini başarılı bir JSON cevabı olarak frontend'e döndürür.
    return jsonify({
        "basari": True,
        "leadler": leadler
    }), 200 


