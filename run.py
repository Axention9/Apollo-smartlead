from app import create_app

#  Uygulama fabrikasından Flask uygulamasını oluşturur.
app = create_app()

# Bu dosya doğrudan çalıştırıldığında Flask uygulamasını başlatır.
if __name__ == "__main__":
    app.run()

    