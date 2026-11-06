import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot RP Online!"

def run():
    app.run(host='0.0.0.0', port=8080)
Thread(target=run, daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

JAWABAN = {
    "join": "🎮 Cara Join One State: Download OneState di Play Store, buat karakter, masuk server Asia, join Discord resminya!",
    "polisi": "👮 Cara Jadi Polisi: Pergi ke lokasi rekrutmen Polisi di game, pencet marker, ikut pelatihan, baru bisa patroli!",
    "army": "🪖 Cara Jadi Army: Ke markas Army, pencet marker rekrutmen. Tugasnya jaga kota & bantu polisi.",
    "medis": "🚑 Cara Jadi Medics: Ke Rumah Sakit, pencet marker. Tugasnya nolongin player pingsan & bawa ke RS.",
    "kerja": "💼 Kerjaan: Polisi, Army, Medics, Taksi, Kurir, Mekanik, Bisnis toko. Mau kaya? Kerja rajin!",
    "rules": "📜 Rules: 1. No RDM 2. No VDM 3. No Metagaming 4. No Powergaming 5. Harus tetap IC!",
    "istilah": "📖 IC = lagi jadi karakter, OOC = lagi jadi diri sendiri, RDM = bunuh sembarangan, VDM = nabrak sembarangan",
    "duit": "💰 Cari Duit: Ambil kerja di City Hall, jadi Taksi/Kurir, jualan, ikut event faksi!",
    "mobil": "🚗 Mobil harus beli di dealer pake duit IC, gak bisa spawn. Jangan curi mobil!",
    "rumah": "🏠 Kamu mulai dari Apartemen. Ke pintu, pencet interaksi, pilih Leave Apartment.",
}

@bot.event
async def on_ready():
    print(f"Bot {bot.user} udah online!")
    await bot.change_presence(activity=discord.Game(name="OneState RP | !help"))

@bot.command()
async def help(ctx):
    await ctx.send("🤖 Ketik: `!join` `!polisi` `!army` `!medis` `!kerja` `!rules` `!istilah` `!duit` `!mobil` `!rumah` atau tag aku!")

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if bot.user in message.mentions:
        text = message.content.lower()
        jawaban = "Halo! Aku Bot RP OneState 🤖 Ketik `!help` ya!"
        for kunci, isi in JAWABAN.items():
            if kunci in text: jawaban = isi; break
        if "polisi" in text: jawaban = JAWABAN["polisi"]
        elif "kerja" in text: jawaban = JAWABAN["kerja"]
        elif "aturan" in text or "rule" in text: jawaban = JAWABAN["rules"]
        elif "duit" in text or "uang" in text: jawaban = JAWABAN["duit"]
        elif "mobil" in text: jawaban = JAWABAN["mobil"]
        elif "medis" in text or "dokter" in text: jawaban = JAWABAN["medis"]
        elif "join" in text or "masuk" in text: jawaban = JAWABAN["join"]
        await message.reply(jawaban)
        return
    await bot.process_commands(message)

bot.run(os.environ.get("TOKEN"))
