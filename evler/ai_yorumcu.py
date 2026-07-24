from openai import OpenAI
from django.conf import settings

def ev_yorumla(ev_no, anahtar_kelime, burc):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir astrologsun. Bir kişinin belirli bir astrolojik evinde hangi burcun bulunduğuna göre, bunun kişi için ne anlama geldiğini akıcı, Türkçe, kişiselleştirilmiş bir dille yorumluyorsun. Markdown kullanma, düz paragraflar halinde yaz."
            },
            {
                "role": "user",
                "content": f"{ev_no}. Ev ({anahtar_kelime}) bu kişinin haritasında {burc} burcunda. Bunun kişinin bu yaşam alanındaki tutumu, güçlü yönleri ve eğilimleri açısından ne anlama geldiğini 3-4 cümlelik bir yorumla anlat."
            }
        ]
    )

    return response.choices[0].message.content