from telethon import TelegramClient, events

API_ID = 35014950
API_HASH = 'a4fb1b1895017c8b0a72c2e40c4a63d6'

client = TelegramClient('shaxsiy_session', API_ID, API_HASH)

# Bandlik holatini saqlash uchun o'zgaruvchi
is_away = False

# /away buyrug'ini yozsangiz, bot faollashadi
@client.on(events.NewMessage(outgoing=True, pattern='/away'))
async def set_away(event):
    global is_away
    is_away = True
    await event.edit("🔴 Bandlik rejimi yoqildi! Endi kelgan xabarlarga avtomatik javob beriladi.")

# /back buyrug'ini yozsangiz, bot to'xtaydi
@client.on(events.NewMessage(outgoing=True, pattern='/back'))
async def set_back(event):
    global is_away
    is_away = False
    await event.edit("🟢 Bandlik rejimi o'chirildi. Avtomatik javob berish to'xtatildi.")

# Faqat band bo'lgan paytingizda va boshqalar yozganda javob berish
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_reply(event):
    global is_away
    # Agar is_away True bo'lsa va xabarni boshqa odam yozgan bo'lsa
    if is_away:
        await event.reply("Salom! Xabaringizni o'qib chiqdim. 📌 Hozir bandman, keyinroq o'zim yozaman.")

if __name__ == '__main__':
    print("Userbot ishga tushdi...")
    client.start()
    client.run_until_disconnected()