import subprocess
import os

def build_reels():
    audio_input = "voiceover.mp3"
    subtitle_input = "subtitles.srt"
    output_file = "final_reels_output.mp4"
    
    # Generate a professional vertical (9:16) dark background automatically using FFmpeg
    # Size: 1080x1920, Color: dark slate blue (#1E1E2F)
    bg_video = "generated_bg.mp4"
    bg_cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "color=c=0x1E1E2F:s=1080x1920:r=30",
        "-t", "60", # temporary duration, will be trimmed by audio length
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        bg_video
    ]
    print("Generating background video...")
    subprocess.run(bg_cmd, check=True)

    # Subtitle styling for TikTok/Reels look
    subtitle_filter = f"subtitles={subtitle_input}:force_style='FontName=Arial,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=100'"

    # Combine generated background, voiceover, and burn subtitles
    cmd = [
        "ffmpeg", "-y",
        "-i", bg_video,
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

    print("Rendering final Reels video...")
    subprocess.run(cmd, check=True)
    print(f"Video rendered successfully: {output_file}")

if __name__ == "__main__":
    build_reels()
