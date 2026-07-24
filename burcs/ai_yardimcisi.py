from openai import OpenAI
from django.conf import settings

def burc_yorumu_uret(burc_adi, ay_adi):
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "Sen deneyimli bir astrologsun. Kısa, akıcı, Türkçe aylık burç yorumları yazıyorsun."
            },
            {
                "role": "user",
                "content": f"{burc_adi} burcu için {ay_adi} ayına özel, 3-4 cümlelik bir yorum yaz. Aşk, kariyer ve genel enerji hakkında bilgi ver."
            }
        ]
    )

    return response.choices[0].message.content