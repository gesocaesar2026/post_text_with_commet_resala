
# post.py

import random
import requests
import datetime

# إعدادات API
PAGE_ACCESS_TOKEN = "EAAUmqjbT57QBRNAAdlxvgXzweetZCRpl7PK6S3rQXp02vOQZBJTjEBZAPJWSKCG3SglFyELiwvP4N7PDOOZCEO67kPVZClIf91lllcfh17pbZA71NsPuPaaUSU6LTU9MSuNm5Rw1OTcICmPa57KlXSNPNKUu9KwJwi2z9LvvcgrapvRwFs5X1Nx4yBrLVzPnek3u1HvdnAkQ50Bqre0VoZD"
PAGE_ID = "90118319153"


GRAPH_API_URL = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
COMMENT_API_TEMPLATE = "https://graph.facebook.com/v19.0/{post_id}/comments"


# ---------------------------
# الرسائل حسب المصدر
# ---------------------------
messages_by_author = {
    "المسيح": [
        "أنا معاك حتى لو حاسس إنك لوحدك... متخافش ❤️",
        "كل حاجة هتتظبط في وقتها... ثق فيا 🙏",
        "أنا شايف تعبك ومش هسيبك... اصبر شوية 💫",
        "لو الدنيا ضاقت بيك... تعالى عندي وأنا أريحك 🤍",
        "أنا دايمًا جنبك حتى لو مش شايفني 🙏"
    ],

    "البابا شنودة": [
        "اطمئن... الله قادر أن يحوّل كل ألم لبركة 🙏",
        "ثق أن الله لن يتركك أبدًا مهما كانت الظروف ❤️",
        "ربنا شايف تعبك وهيكافئك في الوقت المناسب 💫",
        "عيش بالإيمان مش بالخوف 🤍",
        "الرجاء في الله لا يخيب أبدًا 🙏"
    ],

    "مارجرجس": [
        "اثبت في إيمانك مهما كانت الحرب صعبة ⚔️",
        "القوة مش في إنك متتعبش... القوة إنك تكمل 💫",
        "ربنا معاك في كل معركة بتدخلها 🙏",
        "متخفش... النصر جاي 🤍",
        "خليك شجاع لأن إلهك قوي ❤️"
    ],

    "مارمينا": [
        "ربنا مش بينسى أولاده أبداً 🤍",
        "اطلب بإيمان وهتشوف عجايب 🙏",
        "كل ضيقة وليها نهاية جميلة 💫",
        "ربنا شايلك حتى لو مش حاسس ❤️",
        "ثق إن الفرج قريب جداً 🤍"
    ],

    "ابونا فلتاؤس": [
        "ربنا دايمًا بيدور على قلبك مش شكلك 🙏",
        "اقعد مع ربنا شوية وهتلاقي السلام ❤️",
        "كل حاجة بتعدي... إلا حب ربنا 💫",
        "ربنا عمره ما بيتأخر 🤍",
        "الصلاة بتغير كل حاجة 🙏"
    ]
}


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
        print("❌ فشل النشر:", response.text)
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
        print("❌ فشل في التعليق:", response.text)


def main():
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    # اختيار شخصية عشوائية
    author = random.choice(list(messages_by_author.keys()))

    # اختيار رسالة من نفس الشخصية
    message = random.choice(messages_by_author[author])

    # البوست (حسب الشخصية)
    post_text = f"""
رسالة {author} ليك اليوم {month}/{day}

+
+
+
+
+
+
+
شوف اول تعليق ❤️
"""

    post_id = post_to_facebook(post_text)

    if post_id:
        comment_on_post(post_id, message)


if __name__ == "__main__":
    main()
