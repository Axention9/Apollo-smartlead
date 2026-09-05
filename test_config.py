# Config sınıfını config.py dosyasından içe aktarır.
from config import Config

# .env dosyasındaki SECRET_KEY değerinin Config tarınfdan doğru şekilde okunmadığını kontrol eder.
print(Config.SECRET_KEY)