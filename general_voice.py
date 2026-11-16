import asyncio
import edge_tts

TEXT = """
Mau bikin Instagram Reels otomatis sekeren agensi besar, tapi cuma pakai 3 prompt dari iPad? 
Selama ini, edit video bikin capek karena harus potong klip manual, pasang subtitle satu-satu, dan atur transisi. 
Padahal, kita bisa pakai workflow AI berbasis cloud! Cukup siapkan 3 langkah: Pertama, setup workspace dengan tools seperti Whisper dan FFmpeg. 
Kedua, kasih referensi video favoritmu supaya AI paham gaya transisi dan warnamu. 
Ketiga, masukkan footage dan instruksi, biarkan AI merakit draf pertamanya secara otomatis. 
Keunggulannya bukan cuma cepat, tapi konsisten setiap hari tanpa bikin kamu burnout! 
Nggak perlu lagi pusing buka software berat. Mau tahu cara setup otomatisasinya di GitHub Actions langsung dari iPad? 
Komen 'MAU' di bawah dan follow akun ini untuk tutorial AI automation selanjutnya!
"""

VOICE = "id-ID-GadisNeural"
OUTPUT_FILE = "voiceover.mp3"

async def main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="+5%", pitch="+0Hz")
    await communicate.save(OUTPUT_FILE)
    print(f"Voiceover successfully generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
