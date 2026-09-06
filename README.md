# Apollo SmartLead AI

Apollo SmartLead AI, APOLLO markası için geliştirilen yapay zekâ destekli müşteri etkileşimi ve lead yönetim sistemidir.

Proje; Flask tabanlı bir backend, Groq API ile çalışan yapay zekâ servisi, SQLite veritabanı ve Wix Studio / Velo ile oluşturulan iki farklı arayüzden oluşur.

## Özellikler

- Kullanıcıların yapay zekâ ile sohbet edebilmesi
- Kullanıcı adı, telefon ve mesaj bilgilerinin lead olarak kaydedilmesi
- Kaydedilen lead'lerin yönetim panelinde listelenmesi
- Wix frontend ile Flask backend arasında API bağlantısı
- Render üzerinde canlı backend yayını
- Ortam değişkenleri ile güvenli API anahtarı yönetimi

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Studio / Velo
- JavaScript
- Git / GitHub
- Render

## Proje Yapısı

```text
apollo-smartlead/
│
├── app/
│   ├── services/
│   │   └── ai_service.py
│   ├── templates/
│   ├── __init__.py
│   ├── database.py
│   └── routes.py
│
├── config.py
├── requirements.txt
├── run.py
├── smartlead.db
├── .gitignore
└── README.md
```

## API Uç Noktaları

### Health Check

```text
GET /health
```

Uygulamanın çalışıp çalışmadığını kontrol eder.

### AI Sohbet

```text
POST /api/sohbet
```

Kullanıcı mesajını yapay zekâ servisine gönderir ve yapay zekâ yanıtını döndürür.

### Lead Ekleme

```text
POST /api/leads
```

Kullanıcının isim, telefon ve mesaj bilgilerini veritabanına kaydeder.

### Lead Listeleme

```text
GET /api/leads
```

Kaydedilen lead kayıtlarını yönetim panelinde görüntülenmek üzere döndürür.

## Yerel Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/Axention9/Apollo-smartlead.git
cd Apollo-smartlead
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Windows üzerinde sanal ortamı etkinleştirin:

```bash
venv\Scripts\activate
```

Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

Projenin ana dizininde `.env` dosyası oluşturun ve gerekli ortam değişkenlerini tanımlayın:

```env
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
```

Uygulamayı başlatın:

```bash
python run.py
```

Uygulama yerel ortamda çalışmaya başlayacaktır.

## Canlı Backend

Backend Render üzerinde yayınlanmaktadır.

```text
https://apollo-smartlead.onrender.com
```

Health Check:

```text
https://apollo-smartlead.onrender.com/health
```

## Arayüzler

### B2C — Karşılama Sayfası

Kullanıcılar karşılama sayfası üzerinden:

- Yapay zekâya mesaj gönderebilir.
- Yapay zekâdan yanıt alabilir.
- İsim ve telefon bilgilerini bırakabilir.
- Bilgilerini lead olarak sisteme kaydedebilir.

### B2B — Yönetim Paneli

Yönetim panelinde kaydedilen lead'ler:

- İsim
- Telefon
- Mesaj
- Tarih

bilgileriyle görüntülenir.

## Güvenlik

- `.env` dosyası GitHub deposuna dahil edilmez.
- API anahtarları ve gizli bilgiler environment variable olarak saklanır.
- Veritabanı işlemlerinde parametreli SQL sorguları kullanılır.
- Frontend ve backend arasındaki iletişim CORS yapılandırması ile sağlanır.

## Yayınlama

Backend, GitHub repository'sine bağlı Render Web Service üzerinden yayınlanmaktadır.

Render yapılandırması:

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app
```

Wix arayüzleri canlı Render API adresine bağlanarak backend ile iletişim kurar.

## Geliştirici

Berkant Mert