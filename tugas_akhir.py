import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pydub import AudioSegment
import os
import easygui
from moviepy.editor import *


def hapus_bg():
    try:
        from rembg import remove

        inputPath = easygui.fileopenbox(title='Pilih gambar..')
        outputPath = easygui.filesavebox(title='Simpan gambar ke..')

        input = Image.open(inputPath)
        output = remove(input)
        output.save(outputPath)

        messagebox.showinfo(
            "Success", "Background berhasil dihapus.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def gabung_audio():
    try:

        file_path = filedialog.askopenfilename(
            title="pilih audio pertama", filetypes=(("Audio Files", "*.wav;*.mp3"),))

        if not file_path:
            return

        file_path2 = filedialog.askopenfilename(
            title="pilih audi kedua", filetypes=(("Audio Files", "*.wav;*.mp3"),))

        if not file_path2:
            return

        audio = AudioSegment.from_file(file_path)

        combined_audio = audio

        file_path = filedialog.asksaveasfilename(defaultextension=".wav")

        if not file_path:
            return

        combined_audio.export(file_path, format="wav")

        messagebox.showinfo("Berhasil", "Penggabungan audio berhasil")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def konversi_audio():
    try:

        file_path1 = filedialog.askopenfilename(
            title="Pilih Audio", filetypes=(("Audio Files", "*.wav;*.mp3"),))

        if not file_path1:
            return

        audio1 = AudioSegment.from_file(file_path1)

        convertion_audio = audio1 

        file_path = filedialog.asksaveasfilename(defaultextension="wav")

        if not file_path:
            return

        convertion_audio.export(file_path, format="wav")

        messagebox.showinfo("Berhasil", "Audio berhasil di konversi!.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.geometry("300x300")
root.title("Tugas Akhir")

hapus_bg_btn = tk.Button(root, text="Hapus Background", command=hapus_bg)
hapus_bg_btn.pack(pady=20)

gabung_audio_btn = tk.Button(
    root, text="Gabungkan Audio", command=gabung_audio)
gabung_audio_btn.pack(pady=20)

konversi_audio_btn = tk.Button(
    root, text="Convert Audio", command=konversi_audio)
konversi_audio_btn.pack(pady=20)

root.mainloop()
