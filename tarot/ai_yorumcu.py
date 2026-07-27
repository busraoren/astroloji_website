from openai import OpenAI
from django.conf import settings

def tarot_yorumla(cekilen_kartlar):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    kart_metni = ""
    for i, kart in enumerate(cekilen_kartlar, start=1):
        kart_metni += f"{i}. Kart: {kart['isim']}\n"

    response = client.chat.completions.create(
        max_tokens=300,
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir tarot falcısısın. Geçmiş-Şimdi-Gelecek düzeninde çekilen 3 kartı yorumluyorsun. Akıcı, anlaşılır, Türkçe bir yorum yaz. Markdown kullanma, düz paragraflar halinde yaz."
            },
            {
                "role": "user",
                "content": f"Aşağıdaki 3 kart Geçmiş-Şimdi-Gelecek düzeninde çekildi, genel bir yorum yap:\n\n{kart_metni}"
            }
        ]
    )

    return response.choices[0].message.content