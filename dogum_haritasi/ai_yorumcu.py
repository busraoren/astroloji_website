from openai import OpenAI
from django.conf import settings

def dogum_haritasi_yorumla(hesaplama_sonucu):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    veri_metni = "GEZEGEN KONUMLARI:\n"
    for gezegen, bilgi in hesaplama_sonucu['gezegenler'].items():
        veri_metni += f"{gezegen}: {bilgi['burc']} burcunda, {bilgi['derece']} derece\n"

    if hesaplama_sonucu['yukselen']:
        veri_metni += f"\nYÜKSELEN BURÇ: {hesaplama_sonucu['yukselen']['burc']}\n"

    if hesaplama_sonucu['evler']:
        veri_metni += "\nEVLER:\n"
        for ev_no, bilgi in hesaplama_sonucu['evler'].items():
            veri_metni += f"{ev_no}. Ev: {bilgi['burc']} burcunda\n"

    response = client.chat.completions.create(
        max_tokens=300,
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir astrologsun. Verilen gezegen konumları, yükselen burç ve ev bilgilerine göre, kişinin karakteri ve yaşamı hakkında akıcı, anlaşılır, Türkçe bir doğum haritası yorumu yazıyorsun. Markdown kullanma, düz paragraflar halinde yaz."
            },
            {
                "role": "user",
                "content": f"Aşağıdaki bilgilere göre detaylı bir doğum haritası yorumu yaz:\n\n{veri_metni}"
            }
        ]
    )

    return response.choices[0].message.content
