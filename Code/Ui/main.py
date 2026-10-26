import sys
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog

try:
    import pygame
except ImportError:
    print("pygame not found, installing pygame-ce...")
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-ce"])
        import pygame
    except Exception:
        print("Couldn't install pygame-ce. Try Python 3.12 or 3.13.")
        sys.exit(1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.resizable(False, False)
        self.song_path = None
        pygame.mixer.init()
        self._build_ui_()

    def _build_ui_(self):
        f = ttk.Frame(self, padding=20)
        f.pack()

        self.song_label = tk.Label(
            f, text="choose a song dummy", fg="white", bg="navy", width=40
        )
        self.song_label.pack(pady=10)

        ttk.Button(f, text="Choose Good Songs", command=self.choose_song).pack(fill="x", pady=2)
        ttk.Button(f, text="Play the fricking song", command=self.play).pack(fill="x", pady=2)
        ttk.Button(f, text="Pause if you dare", command=self.pause).pack(fill="x", pady=2)
        ttk.Button(f, text="Please resume", command=self.resume).pack(fill="x", pady=2)
        ttk.Button(f, text="End", command=self.end).pack(fill="x", pady=2)

    def choose_song(self):
        path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3 *.wav *.ogg")]
        )
        if path:
            self.song_path = path
            self.song_label.config(text=path.split("/")[-1])

    def play(self):
        if self.song_path:
            pygame.mixer.music.load(self.song_path)
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def end(self):
        pygame.mixer.music.stop()

App().mainloop()