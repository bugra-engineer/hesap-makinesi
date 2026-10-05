def topla(a, b):
    return a + b


def cikar(a, b):
    return a - b


def carp(a, b):
    return a * b


def bol(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölme yapılamaz!")
    return a / b


def sayi_al(mesaj):
    """Kullanıcı geçerli bir sayı girene kadar tekrar sorar."""
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")


def menu_goster():
    print("\n=== HESAP MAKİNESİ ===")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Çıkış")


def main():
    islemler = {
        "1": ("+", topla),
        "2": ("-", cikar),
        "3": ("*", carp),
        "4": ("/", bol),
    }

    while True:
        menu_goster()
        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "5":
            print("Görüşmek üzere!")
            break

        if secim not in islemler:
            print("Hata: Geçersiz seçim, 1-5 arasında bir değer girin.")
            continue

        sayi1 = sayi_al("Birinci sayı: ")
        sayi2 = sayi_al("İkinci sayı: ")

        sembol, fonksiyon = islemler[secim]
        try:
            sonuc = fonksiyon(sayi1, sayi2)
            print(f"Sonuç: {sayi1} {sembol} {sayi2} = {sonuc}")
        except ZeroDivisionError as hata:
            print(f"Hata: {hata}")


if __name__ == "__main__":
    main()