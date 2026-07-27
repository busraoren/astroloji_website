from openai import OpenAI
from django.conf import settings

def uyumluluk_yorumla(isim1, gezegenler1, isim2, gezegenler2):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    def veri_metnine_cevir(isim, veri):
        metin = f"\n{isim.upper()} GEZEGEN KONUMLARI:\n"
        for gezegen, bilgi in veri['gezegenler'].items():
            metin += f"{gezegen}: {bilgi['burc']} burcunda\n"
        if veri.get('yukselen'):
            metin += f"Yükselen: {veri['yukselen']['burc']}\n"
        return metin

    veri_metni = veri_metnine_cevir(isim1, gezegenler1) + veri_metnine_cevir(isim2, gezegenler2)

    response = client.chat.completions.create(
        max_tokens=300,
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir astrologsun. İki kişinin gezegen konumlarını karşılaştırıp aralarındaki uyumu (aşk, iletişim, uzun vadeli ilişki potansiyeli açısından) değerlendiren, akıcı, Türkçe bir uyumluluk analizi yazıyorsun. Markdown kullanma, düz paragraflar halinde yaz."
            },
            {
                "role": "user",
                "content": f"Aşağıdaki iki kişinin gezegen konumlarına göre bir uyumluluk analizi yaz:\n{veri_metni}"
            }
        ]
    )

    return response.choices[0].message.content