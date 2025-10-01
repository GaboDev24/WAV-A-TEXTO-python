import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
import time

def subir_transcribir():
    archivo = filedialog.askopenfilename(
        title = "Seleccionar archivo",
        filetypes=[("Audios", "*.wav *.flac"), ("Audios MP3", "*.mp3"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        lbl_archivo.config(text=f"Archivo Seleccionado:?\n{archivo}")

        audio_file = AudioSegment.from_file(archivo)
        duracion = len(audio_file) / 1000
        tiempo_aprox = round(duracion / 2, 1)
        lbl_estado.config(text=f"Procesando... (Tiempo aproximado: {tiempo_aprox} seg)")
        
        root.update_idletasks()

        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(archivo) as source:
                audio = recognizer.record(source)
                texto = recognizer.recognize_google(audio, language="es-ES")
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, texto)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo transcribir:\n{e}")



#ventana principal

root = tk.Tk()
root.title("Audio a texto by GaboDev")
root.geometry("500x400")
root.option_add('*Font', 'sans 14')
root.iconbitmap("icono.ico")
root.configure(background="#CA5F5F")

btn_subir = tk.Button(root, text="Seleccionar audio", command=subir_transcribir, border=5)
btn_subir.pack(pady=10)

lbl_archivo = tk.Label(root, text="Ningun archivo seleccionado", wraplength=450, justify="center", background="#CA5F5F")
lbl_archivo.pack(pady=5)

lbl_estado = tk.Label(root, text="", fg="#4B0F0F", background="#CA5F5F")
lbl_estado.pack(pady=5)

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()