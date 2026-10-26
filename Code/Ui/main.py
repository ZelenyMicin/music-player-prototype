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
        pygame.mixer.music.set_volume(0.5)
        self._build_ui_()

    def _build_ui_(self):
        f = ttk.Frame(self, padding=20)
        f.pack()

        self.song_label = tk.Label(
            f, text="choose a song dummy", fg="white", bg="navy", width=40
        )
        self.song_label.pack(pady=10)

        ttk.Button(f, text="choose a song", command=self.choose_song).pack(fill="x", pady=2)
        ttk.Button(f, text="Play", command=self.play).pack(fill="x", pady=2)
        ttk.Button(f, text="Pause", command=self.pause).pack(fill="x", pady=2)
        ttk.Button(f, text="Resume", command=self.resume).pack(fill="x", pady=2)
        ttk.Button(f, text="Stop", command=self.end).pack(fill="x", pady=2)

        tk.Label(f, text="Volume").pack(pady=(10, 0))
        self.volume = ttk.Scale(
            f, from_=0, to=100, orient="horizontal", command=self.set_volume
        )
        self.volume.set(50)
        self.volume.pack(fill="x")

    def choose_song(self):
        path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3 *.wav *.ogg")]
        )
        if path:
            self.song_path = path
            self.song_label.config(text=path.split("/")[-1].split("\\")[-1])

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

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value) / 100)

App().mainloop()