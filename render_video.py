import subprocess
import os

def build_reels():
    video_input = "background_stock.mp4"
    audio_input = "voiceover.mp3"
    subtitle_input = "subtitles.srt"
    output_file = "final_reels_output.mp4"
    
    subtitle_filter = f"subtitles={subtitle_input}:force_style='FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=60'"

    cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1", "-i", video_input,
        "-i", audio_input,
        "-filter_complex", f"[0:v]{subtitle_filter}[v]",
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_file
    ]

    print("Rendering video on GitHub Actions cloud runner...")
    subprocess.run(cmd, check=True)
    print(f"Video rendered successfully: {output_file}")

if __name__ == "__main__":
    build_reels()
