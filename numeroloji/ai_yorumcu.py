from openai import OpenAI
from django.conf import settings

def numeroloji_yorumla(isim, hesaplama_sonucu):
    client = OpenAI(
        api_key= settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )
    veri_metni = f"""
    İsim: {isim}
    Yaşam Yolu Sayısı: {hesaplama_sonucu['yasam_yolu_sayisi']}
    Kader Sayısı: {hesaplama_sonucu['kader_sayisi']}
"""

    response = client.chat.completions.create(
        max_tokens=300,
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir numeroloji uzmanısın. Verilen Yaşam Yolu ve Kader sayılarına göre kişinin karakteri, yaşam amacı ve potansiyeli hakkında akıcı, anlaşılır, Türkçe bir numeroloji yorumu yazıyorsun. Markdown kullanma, düz paragraflar halinde yaz."
            },
            {
                "role": "user",
                "content": f"Aşağıdaki numeroloji sayılarına göre detaylı bir yorum yaz:\n{veri_metni}"
            }
        ]
    )
    return response.choices[0].message.content