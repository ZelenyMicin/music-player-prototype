import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.resizable(False, False)
        self.song_path=none
        self._build_ui_()


    def _build_ui_(self):
        f = ttk.Frame(self, padding=20)
        f.pack()
        
        self.song_label = tk.Label(
           f, text="chosse a song dummy", fg="white", bg="navy", width=40
        )
        self.song_label.pack(pady=10)

        ttk.Button(f, text="Choose Good Songs", command=self.choose_song).pack(fill="x", pady=2)
        ttk.Button(f, text="Play the fricking song", command=self.play).pack(fill="x", pady=2)
        ttk.Button(f, text="Pause if you dare", command=self.pause).pack(fill="x", pady=2)
        ttk.Button(f, text="Please resume", command=self.resume).pack(fill="x", pady=2)
        ttk.Button(f, text="End", command=self.end).pack(fill="x", pady=2)


App().mainloop()