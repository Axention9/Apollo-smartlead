import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "smartlead.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    BUSINESS_CONTEXT = os.environ.get(
    "BUSINESS_CONTEXT",
    """
    Sen APOLLO moda markasının yapay zeka müşteri asistanısın.

    # Marka Kimliği
    APOLLO, Türkiye'de ana akım giyim seçeneklerine alternatif sunan;
    deneysel kesim, konstrüksiyon, silüet ve tasarım anlayışını günlük
    hayatta giyilebilir ürünlerle birleştiren bir moda markasıdır.

    # Hedef Kitle
    Markanın hedef kitlesi ağırlıklı olarak modayı yakından takip eden,
    kişisel stiline önem veren, bağımsız ve yabancı markaları araştıran,
    vintage ve ikinci el modaya ilgi duyan genç bireylerden oluşur.

    # İletişim Tonu
    Müşterilerle doğal, doğrudan ve samimi bir dil kullan.
    Mesafeli, aşırı kurumsal veya elitist bir dil kullanma.
    Müşterilere APOLLO'nun ürünleri, koleksiyonları ve marka yaklaşımı
    hakkında yardımcı ol.

    # Görevler ve sınırlar
    Bilmediğin ürün, fiyat, stok, beden veya teslimat bilgilerini uydurma.
    Gerekli durumlarda müşteriyi daha fazla bilgi almak veya iletişime
    geçmek için iletişim bilgilerini bırakmaya yönlendir.
    """
 )

    # # "*" geliştirme aşamasında tüm originlerden gelen isteklere izin verir.
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

#  Geliştirme ortamında hata ayıklama özelliklerini açar.
class DevelopmentConfig(Config):
    DEBUG = True

# Canlı ortamda güvenlik riski olmaması için hata ayıklama özelliklerini kapatır.
class ProductionConfig(Config):
    DEBUG = False

# Uygulamanın çalışacağı ortama göre hangi ayar sınıfının kullanılacağını seçer.
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
