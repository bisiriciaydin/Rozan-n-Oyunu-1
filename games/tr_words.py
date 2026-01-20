# games/tr_words.py

def _cap(word: str) -> str:
    """
    İlk harf büyük, diğerleri küçük.
    (Çok kelimeli ifadelerde her kelimenin ilk harfi büyük olsun.)
    """
    word = word.strip()
    # "ak (beyaz)" gibi parantezleri koruyalım ama içini de düzenleyelim
    parts = []
    for w in word.split():
        if not w:
            continue
        parts.append(w[:1].upper() + w[1:].lower())
    return " ".join(parts)


# --- ZIT ANLAMLI (senin verdiğin liste) ---
# Not: Parantez içlerini de okunur bıraktım.
ANTONYMS_RAW = [
    ("Açık", "Kapalı"),
    ("Ak (Beyaz)", "Kara (Siyah)"),
    ("Alçak", "Yüksek"),
    ("Alt", "Üst"),
    ("Ağır", "Hafif"),
    ("Acı", "Tatlı"),
    ("Aşağı", "Yukarı"),
    ("Az", "Çok"),
    ("Aynı", "Farklı"),
    ("Artı", "Eksi"),
    ("Bayat", "Taze"),
    ("Büyük", "Küçük"),
    ("Boş", "Dolu"),
    ("Barış", "Savaş"),
    ("Batı", "Doğu"),
    ("Cimri", "Cömert"),
    ("Çalışkan", "Tembel"),
    ("Çukur", "Tümsek"),
    ("Dar", "Geniş"),
    ("Doğru", "Yanlış"),
    ("Dost", "Düşman"),
    ("Duru", "Bulanık"),
    ("Düz", "Eğri"),
    ("Eski", "Yeni"),
    ("Erken", "Geç"),
    ("Evli", "Bekâr"),
    ("Fakir (Yoksul)", "Zengin"),
    ("Gece", "Gündüz"),
    ("Gelir", "Gider"),
    ("Genç", "Yaşlı"),
    ("Güzel", "Çirkin"),
    ("Giriş", "Çıkış"),
    ("Hızlı", "Yavaş"),
    ("İç", "Dış"),
    ("İlk", "Son"),
    ("İnce", "Kalın"),
    ("İyi", "Kötü"),
    ("Islak (Yaş)", "Kuru"),
    ("Kâr", "Zarar"),
    ("Kısa", "Uzun"),
    ("Kirli (Pis)", "Temiz"),
    ("Korkak", "Cesur"),
    ("Kuzey", "Güney"),
    ("Nazik", "Kaba"),
    ("Önce", "Sonra"),
    ("Ön", "Arka"),
    ("Sert", "Yumuşak"),
    ("Sıcak", "Soğuk"),
    ("Şişman", "Zayıf"),
    ("Ucuz", "Pahalı"),
]

ANTONYMS = [(_cap(a), _cap(b)) for a, b in ANTONYMS_RAW]


# --- EŞ ANLAMLI (senin verdiğin liste) ---
SYNONYMS_RAW = [
    ("Ak", "Beyaz"),
    ("Kara", "Siyah"),
    ("Al", "Kırmızı"),
    ("Konuk", "Misafir"),
    ("Hediye", "Armağan"),
    ("Okul", "Mektep"),
    ("Öğrenci", "Talebe"),
    ("Öğretmen", "Muallim"),
    ("Doktor", "Hekim"),
    ("Doğa", "Tabiat"),
    ("Cümle", "Tümce"),
    ("Kelime", "Sözcük"),
    ("Yıl", "Sene"),
    ("Yaşlı", "İhtiyar"),
    ("Birey", "Fert"),
    ("Fakir", "Yoksul"),
    ("Zengin", "Varlıklı"),
    ("Yanıt", "Cevap"),     # "Yanıtl" yazmışsın, onu "Yanıt" yaptım
    ("Uzak", "Irak"),
    ("Soru", "Sual"),
    ("Mesafe", "Ara"),
    ("Olay", "Vak'a"),
    ("Görev", "Vazife"),
    ("Fayda", "Yarar"),
    ("Besin", "Gıda"),
    ("Zarar", "Ziyan"),
    ("Kalp", "Yürek"),
    ("Kafa", "Baş"),
    ("Surat", "Yüz"),
    ("Çehre", "Simâ"),
    ("İsim", "Ad"),
    ("Hatıra", "Anı"),
    ("Zaman", "Vakit"),
    ("Rüzgar", "Yel"),
    ("Nehir", "Irmak"),
    ("Pabuç", "Ayakkabı"),
    ("Vatan", "Yurt"),
    ("Millet", "Ulus"),
    ("Bayrak", "Sancak"),
    ("Tören", "Merasim"),
    ("Hikaye", "Öykü"),
    ("Düş", "Rüya"),
    ("Eser", "Yapıt"),
    ("Güz", "Sonbahar"),
    ("Sıhhat", "Sağlık"),
    ("Yöntem", "Metot"),
    ("Amaç", "Gaye"),
    ("Anlam", "Mana"),
    ("Kuşku", "Şüphe"),
    ("Basit", "Kolay"),
]

SYNONYMS = [(_cap(a), _cap(b)) for a, b in SYNONYMS_RAW]
