# post.py

import random
import requests
import datetime
import json
import os

# إعدادات API
GEMINI_API_KEY = "AIzaSyDybAXRfYv832CWNwY7rrVt_YNfYmkHpz8"
PAGE_ACCESS_TOKEN = "EAAUmqjbT57QBP3Hxf5hdsggsZChWbi5EBmhaAM9hLtUEJZAYDMgdRBGCZAGrk5aGeDXfWEMbNj4fvmjAIY4ZB1ZCQY2G72rjLVHyxb6tyojulCcyuwZA1dOd6DlWryufVsVwzFV7HXn1md1athB5QeRuDsEeQHGw0RH9QW0ExTDckZB4ZCVFbe3dUjNp437boeozCrCgEmcHoPYtZBRDoIw4ZD"
PAGE_ID = "90118319153"
GRAPH_API_URL = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
COMMENT_API_TEMPLATE = "https://graph.facebook.com/v19.0/{post_id}/comments"

headers = {
    "Content-Type": "application/json",
}

def get_gemini_message():
    # خليك تعتمد GEMINI_API_KEY من البيئة بدل الحط المباشر
    api_key = "AIzaSyBKWx2oL_nm3EVjpPHifQ0nZYn2NEIE1h0"
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json", "X-goog-api-key": api_key}
    data = {
        "contents": [
            {"parts": [{"text": "اكتب لي رسالة مشجعة من السيد المسيح موجهة للقارئ بأسلوب شخصي مكونة حوالي 150-250 حرف."}]}
        ]
    }
    resp = requests.post(url, headers=headers, json=data, timeout=30)
    if resp.status_code == 200:
        j = resp.json()
        try:
            return j["candidates"][0]["content"]["parts"][0]["text"].strip()
        except Exception as e:
            print("❌ لم أجد النص في رد Gemini:", e, j)
            return None
    else:
        print(f"❌ فشل في طلب رسالة من Gemini: {resp.status_code} - {resp.text}")
        return None


def post_to_facebook(text):
    payload = {
        "message": text,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(GRAPH_API_URL, data=payload)
    if response.status_code == 200:
        post_id = response.json().get("id")
        print(f"✅ تم نشر المنشور: {post_id}")
        return post_id
    else:
        print("❌ فشل النشر على فيسبوك:", response.text)
        return None

def comment_on_post(post_id, comment):
    url = COMMENT_API_TEMPLATE.format(post_id=post_id)
    payload = {
        "message": comment,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("💬 تم إضافة تعليق بنجاح")
    else:
        print("❌ فشل في إضافة التعليق:", response.text)

def main():
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    message_templates = [
        f"رسالة المسيح ليك اليوم {month}/{day}\n+\n+\n+\n+\n+\n+\n+\nشوف اول تعليق",
        f"النهاردة {month}/{day}، المسيح باعتلك رسالة مخصوص\n+\n+\n+\n+\n+\n+\nشوف أول تعليق يا حبيب قلبه",
        f"من قلب المسيح ليك: {month}/{day}\n+\n+\n+\n+\n+\n+\n+\nشوف أول تعليق", f"""
رسالة العدراء مريم ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا كيرلس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة تماف ايريني ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة مارمينا ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة مارجرجس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا فلتاؤس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابو سيفين ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا كيرلس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا شنودة ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا مينا عبود {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا بيشوى كامل {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة الانبا موسي الاسود {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
"""
    ]

    post_text = random.choice(message_templates)
    post_id = post_to_facebook(post_text)

    if post_id:
        gemini_message = get_gemini_message()
        if gemini_message:
            comment_on_post(post_id, gemini_message)

if __name__ == "__main__":
    main()
