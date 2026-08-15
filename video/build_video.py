"""Assemble the narrated video: say -> wav per segment, then ffmpeg still+audio clips, then concat."""
import os
import subprocess
import wave
import imageio_ffmpeg
from script import SEGMENTS

BASE = os.path.dirname(__file__)
FRAMES = os.path.join(BASE, "frames")
AUDIO = os.path.join(BASE, "audio")
CLIPS = os.path.join(BASE, "clips")
os.makedirs(AUDIO, exist_ok=True)
os.makedirs(CLIPS, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "Samantha"  # clean US female voice, built into macOS


def synth(text, aiff_path):
    subprocess.run(["say", "-v", VOICE, "-r", "175", "-o", aiff_path, text], check=True)


def to_wav(aiff_path, wav_path):
    subprocess.run(
        [FFMPEG, "-y", "-i", aiff_path, "-ar", "44100", "-ac", "2", wav_path],
        check=True, capture_output=True,
    )


def wav_duration(wav_path):
    with wave.open(wav_path, "rb") as w:
        return w.getnframes() / w.getframerate()


def make_clip(image_path, wav_path, duration, out_path, pad=0.6):
    total = duration + pad
    subprocess.run(
        [
            FFMPEG, "-y",
            "-loop", "1", "-i", image_path,
            "-i", wav_path,
            "-vf", "fade=t=in:st=0:d=0.3,fade=t=out:st=%.2f:d=0.4" % (total - 0.4),
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(total),
            "-r", "30",
            out_path,
        ],
        check=True, capture_output=True,
    )


def main():
    clip_paths = []
    for seg in SEGMENTS:
        aiff = os.path.join(AUDIO, seg["id"] + ".aiff")
        wav = os.path.join(AUDIO, seg["id"] + ".wav")
        clip = os.path.join(CLIPS, seg["id"] + ".mp4")
        img = os.path.join(FRAMES, seg["image"])

        print(f"[{seg['id']}] synthesizing narration...")
        synth(seg["text"], aiff)
        to_wav(aiff, wav)
        dur = wav_duration(wav)
        print(f"[{seg['id']}] duration={dur:.1f}s, rendering clip...")
        make_clip(img, wav, dur, clip)
        clip_paths.append(clip)

    list_file = os.path.join(CLIPS, "concat_list.txt")
    with open(list_file, "w") as f:
        for c in clip_paths:
            f.write(f"file '{c}'\n")

    out_path = os.path.join(BASE, "yard_waste_video.mp4")
    print("Concatenating final video...")
    subprocess.run(
        [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", out_path],
        check=True, capture_output=True,
    )
    print("Done:", out_path)


if __name__ == "__main__":
    main()
