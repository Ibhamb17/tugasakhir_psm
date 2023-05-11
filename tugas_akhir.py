import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pydub import AudioSegment
import os
import easygui


def hapus_bg():
    try:
        from rembg import remove

        inputPath = easygui.fileopenbox(title='Select image file')
        outputPath = easygui.filesavebox(title='Save file to..')

        input = Image.open(inputPath)
        output = remove(input)
        output.save(outputPath)

        messagebox.showinfo(
            "Success", "Background has been removed successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def gabung_audio():
    try:

        file_path1 = filedialog.askopenfilename(
            title="Select First Audio File", filetypes=(("Audio Files", "*.wav;*.mp3"),))

        if not file_path1:
            return

        file_path2 = filedialog.askopenfilename(
            title="Select Second Audio File", filetypes=(("Audio Files", "*.wav;*.mp3"),))

        if not file_path2:
            return

        audio1 = AudioSegment.from_file(file_path1)
        audio2 = AudioSegment.from_file(file_path2)

        combined_audio = audio1 + audio2

        file_path = filedialog.asksaveasfilename(defaultextension=".mp3")

        if not file_path:
            return

        combined_audio.export(file_path, format="mp3")

        messagebox.showinfo("Success", "Audios have been merged successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def konversi_audio():
    inputPath = easygui.fileopenbox(title='Select video file')
    outputPath = easygui.filesavebox(title='Save file to..')
    video = mp.VideoFileClip(inputPath)
    audio = video.audio
    audio.write_audiofile(outputPath)


root = tk.Tk()
root.geometry("300x300")
root.title("Tugas Akhir")

hapus_bg_btn = tk.Button(root, text="Hapus Background", command=hapus_bg)
hapus_bg_btn.pack(pady=20)

gabung_audio_btn = tk.Button(
    root, text="Gabungkan Audio", command=gabung_audio)
gabung_audio_btn.pack(pady=20)
o
konversi_audio_btn = tk.Button(
    root, text="Konversi Audio", command=konversi_audio)
konversi_audio_btn.pack(pady=20)

root.mainloop()
