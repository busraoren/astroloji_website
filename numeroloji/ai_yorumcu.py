from openai import OpenAI
from django.conf import settings


def numeroloji_yorumla(isim, hesaplama_sonucu):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    # Promptu daha temiz okuması için veriyi kompakt hale getirdik
    veri_metni = f"İsim: {isim} | Yaşam Yolu: {hesaplama_sonucu['yasam_yolu_sayisi']} | Kader: {hesaplama_sonucu['kader_sayisi']}"

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen mistik, nokta atışı tespitler yapan bilge bir numeroloji uzmanısın. "
                    "Kullanıcıya uzun ve sıkıcı metinler yerine; kısa, çarpıcı ve sarsıcı içgörüler sunarsın. "
                    "Yorumunu sadece 3 kısa paragrafta özetle: "
                    "1. Yaşam Yolunun getirdiği ana enerji ve zorluk, "
                    "2. Kader sayısının kişiye kattığı gizli potansiyel, "
                    "3. Evrenin ona şu anki tavsiyesi. "
                    "Süslü ve derin sözler kullan ama lafı asla uzatma. Markdown (*, #) KULLANMA."
                )
            },
            {
                "role": "user",
                "content": veri_metni
            }
        ],
        max_tokens=350,  # HIZLANDIRICI: Modelin destan yazmasını ve süreyi uzatmasını engeller
        temperature=0.75  # Yaratıcılık ve mistiklik dozajını ayarlar (0.75 idealdir)
    )

    return response.choices[0].message.content
