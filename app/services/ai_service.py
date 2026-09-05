import requests
from config import Config
# requests, Groq API'sine HTTP isteği göndermemizi sağlar.
# Config, uygulamanın AI ayarlarına ve işletme bilgilerine erişmemizi sağlar.

class AIServiceError(Exception):
    # Yapay zeka servisine özel hataları temsil eder.
    pass

class AIService:
    # Groq API'sine istek göndereceğimiz adres.
    API_URL = "https://api.groq.com/openai/v1/chat/completions"

    # Yönergedeki model deprecated olduğu için Groq'un güncel replacement modeli kullanılır.
    MODEL = "openai/gpt-oss-20b"

    def _business_context_ai(self):
        # Config sınıfından işletme bilgilerini alır.
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis):
        # Groq API anahtarını Config sınıfından alır.
        api_key = Config.GROQ_API_KEY

        # API anahtarı yoksa gerçek servise bağlanmadan demo yanıtı döndürür.
        if not api_key:
            return "Demo modu: Yapay zeka servisi için API anahtari tanimlanmamiş."

        # Yapay zeka modeline gönderilecek mesaj listesini oluşturur.
        messages = [
            {
                "role": "system",
                "content": self._business_context_ai()

            },
        ]

        # Önceki konuşmaları mesaj listesine ekler.
        for onceki_mesaj in gecmis:
            messages.append(onceki_mesaj)

        # Kullanıcının yeni mesajını listenin en sonuna ekler.
        messages.append({
            "role": "user",
            "content": mesaj
        })

        #  Groq API isteği için gerekli başlıkları oluşturur.
        # API anahtarını Bearer formatında göndererek Groq'a yetkilendirme sağlar.
        # Content-Type, gönderilen verinin JSON formatında olduğunu belirtir.
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"

        }

        # Groq'a hangi modelin kullanılacağını ve modele hangi mesajların gönderileceğini belirtir.
        payload = {
            "model": self.MODEL,
            "messages": messages
        }

        # Groq API isteğini try-except içinde gönderir.
        # Böylece ağ veya API kaynaklı hataları kontrollü şekilde yönetebiliriz.
        try:
            response = requests.post(
                self.API_URL,
                headers=headers,
                json=payload,
                timeout=30  # 30 saniye içinde yanıt gelmezse isteği iptal eder.
            )
                
            # 4xx veya 5xx HTTP hatalarında exception oluşturur.
            response.raise_for_status()

            # Groq'un JSON formatındaki cevabını Python sözlüğüne dönüştürür.
            data = response.json()

            #  Groq cevabındaki ilk seçeneğin assistant mesajını alır.
            yanit = data["choices"][0]["message"]["content"]

            # Elde edilen yapay zeka yanıtını çağıran koda geri döndürür.
            return yanit

        except requests.RequestException as hata:

            # Ağ, bağlantı veya HTTP hatalarını AI servisine özel hataya dönüştürür.
            raise AIServiceError(f"Groq API hatasi: {hata}") from hata

        except (KeyError, IndexError, ValueError) as hata:
            # API'den beklenmeyen veya eksik veri gelirse kontrollü hata üretir.
            raise AIServiceError(f"Groq yaniti islenemedi: {hata}") from hata
        

# Uygulamanın farklı bölümlerinde aynı AI servis örneğini kullanmamızı sağlar.
ai_service = AIService()
