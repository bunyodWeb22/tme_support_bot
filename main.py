from flask import Flask
from telethon import TelegramClient, events
import threading
import os

# --- 1. Render port topishi uchun kichik veb-server ---
app = Flask('')


@app.route('/')
def home():
  return 'Userbot ishlayapti!'


def run():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


def keep_alive():
  t = threading.Thread(target=run)
  t.start()


# --- 2. Sizning Telethon userbotingiz ---
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
  await event.edit(
      '🔴 Bandlik rejimi yoqildi! Endi kelgan xabarlarga avtomatik javob'
      ' beriladi.'
  )


# /back buyrug'ini yozsangiz, bot to'xtaydi
@client.on(events.NewMessage(outgoing=True, pattern='/back'))
async def set_back(event):
  global is_away
  is_away = False
  await event.edit('🟢 Bandlik rejimi ochirildi. Avtomatik javob to\'xtatildi.')


# Faqat band bo'lgan paytingizda va boshqalar yozganda javob berish
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_reply(event):
  global is_away
  if is_away:
    await event.reply(
        'Salom! Xabaringizni o\'qib chiqdim. 📌 Hozir bandman, keyinroq'
        ' yozaman.'
    )


if __name__ == '__main__':
  keep_alive()
  print('Userbot ishga tushdi...')
  client.start()
  client.run_until_disconnected()