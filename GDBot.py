#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   TOTALLY NOT MALWARE v9.9.9 ULTRA      ║
║   100% HARMLESS - MAXIMUM CHAOS EDITION ║
║   Auto-reveals after 30 minutes         ║
║   Ctrl+C in terminal to end early       ║
╚══════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import font as tkfont
import threading
import random
import time
import math
import sys
import os

# ── Constants ──────────────────────────────────────────────
DURATION   = 30 * 60
START_TIME = time.time()

SCARY_MESSAGES = [
    "UPLOADING YOUR BROWSER HISTORY TO YOUR MOM",
    "SENDING YOUR SEARCH HISTORY TO YOUR EMPLOYER",
    "MINING IMAGINARY CRYPTO ON YOUR GPU",
    "CONVERTING ALL YOUR JPGS TO COMIC SANS",
    "SETTING YOUR HOMEPAGE TO BING",
    "SUBSCRIBING YOU TO 847 NEWSLETTERS",
    "INSTALLING INTERNET EXPLORER 6.0",
    "TELLING YOUR BOSS YOU CALLED IN SICK",
    "ORDERING 14 PIZZAS TO YOUR NEIGHBOR",
    "RENAMING ALL 4,847 OF YOUR FILES TO 'FILE'",
    "CALCULATING MEANING OF LIFE... RESULT: 42",
    "REVERSING YOUR MOUSE SCROLL DIRECTION",
    "ENABLING STICKY KEYS... PERMANENTLY",
    "DOWNLOADING MORE RAM... FAILED",
    "UPLOADING YOUR MINECRAFT SAVES TO THE NSA",
    "CHANGING ALL PASSWORDS TO 'password123'",
    "MAKING YOUR PC SMELL LIKE BURNT TOAST",
    "TEACHING YOUR COMPUTER TO YODEL",
    "REPLACING ALL YOUR MUSIC WITH RICKROLL",
    "SENDING YOUR SELFIES TO RANDOM CONTACTS",
    "CONVERTING ALL .DOCX TO WINGDINGS FONT",
    "SETTING YOUR ALARM FOR 3:47 AM EVERY DAY",
    "POSTING YOUR DIARY TO LINKEDIN",
    "UNINSTALLING ALL YOUR GAMES... JUST KIDDING... OR AM I",
    "REPORTING YOU TO THE COMPUTER POLICE",
    "TELLING YOUR SMART FRIDGE YOUR SECRETS",
    "UPLOADING YOUR GOOGLE MAPS HISTORY TO YOUR EX",
    "CHANGING YOUR KEYBOARD LAYOUT TO DVORAK",
    "ENROLLING YOU IN EVERY COOKIE CONSENT DATABASE",
]

FAKE_IPS    = ["192.168.6.66","10.0.0.666","172.16.6.6","0.0.0.0","127.6.6.6","69.69.69.69","13.37.13.37"]
FAKE_PROCS  = ["daemon_of_chaos.exe","entropy_engine.dll","nsa_backdoor.sys",
               "bitcoin_miner_lol.exe","cat_uploader.exe","void_caller.py",
               "definitely_legit.exe","sudo_make_sandwich.sh","rm_rf_jk.bat",
               "totally_real_antivirus.exe","windows_update_lol.exe","notavirus.exe"]
FAKE_FILES  = [r"C:\Users\You\AppData\secrets.db",
               r"C:\Users\You\Documents\diary.docx",
               r"C:\Windows\System32\ur_mom.dll",
               r"C:\Users\You\Downloads\embarrassing_stuff",
               r"C:\Users\You\.ssh\id_rsa",
               r"C:\Users\You\browser_history.sqlite"]

GLITCH_CHARS = list("█▓▒░▄▀■□▪◘○◙♦♣♠?!#@$%^&*~`|ÿøæ§†‡Ξ₿Ω∑∆πλ")
NEON         = ["#ff0044","#00ffcc","#ff6600","#ffff00","#cc00ff","#00ff44","#ff00aa","#00aaff","#ff4400","#44ff00"]
MATRIX_GREEN = ["#003300","#005500","#007700","#009900","#00bb00","#00dd00","#00ff00","#44ff44","#aaffaa","#ffffff"]

CATS = [
    "=^.^=", "(=OwO=)", "≽^•⩊•^≼", "(=^-ω-^=)", "ฅ^•ﻌ•^ฅ",
    "^ↀᴥↀ^", "(^=◕ᴥ◕=^)", "=^● ⋏ ●^=", "✧/ᐠ-ꞈ-ᐟ\\✧", "(^･o･^)ﾉ"
]

CAT_MESSAGES = [
    "MEOW MEOW MEOW", "I AM YOUR OVERLORD", "FEED ME NOW",
    "YOUR FILES TASTE DELICIOUS", "INITIATING HAIRBALL PROTOCOL",
    "PURRING.EXE OVERLOADED", "KNOCKING YOUR DATA OFF THE TABLE",
    "JUDGING YOU SILENTLY", "3 AM ZOOMIES ACTIVATED",
    "SITTING ON YOUR KEYBOARD NOW", "IM IN UR SYSTEM EATING UR BYTES",
]

def rand_neon():    return random.choice(NEON)
def rand_glitch():  return random.choice(GLITCH_CHARS)
def rand_cat():     return random.choice(CATS)
def elapsed():      return time.time() - START_TIME
def time_left():    return max(0, DURATION - elapsed())


# ══════════════════════════════════════════════════════════════════
class UltraChaosApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("svchost.exe - Critical Error")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="black")
        self.root.bind("<Escape>",          lambda e: None)
        self.root.bind("<Alt-F4>",          lambda e: None)
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.running       = True
        self.popup_windows = []
        self.phase_idx     = 0

        self.phases = [
            self.phase_realistic_boot,
            self.phase_matrix,
            self.phase_skull,
            self.phase_progress,
            self.phase_bsod,
            self.phase_glitch_storm,
            self.phase_cat_rain,
            self.phase_fake_cmd,
            self.phase_spinning_text,
            self.phase_matrix,
            self.phase_progress,
            self.phase_glitch_storm,
            self.phase_cat_rain,
            self.phase_skull,
            self.phase_fake_cmd,
            self.phase_bsod,
            self.phase_spinning_text,
            self.phase_glitch_storm,
        ]

        import signal
        def _ctrlc(sig, frame):
            self.running = False
            self.root.after(0, self.grand_reveal)
        signal.signal(signal.SIGINT, _ctrlc)

        threading.Thread(target=self._timer,          daemon=True).start()
        threading.Thread(target=self._popup_loop,     daemon=True).start()
        threading.Thread(target=self._screen_shake_loop, daemon=True).start()

        self._run_phase()

    # ── Timers & threads ─────────────────────────────────────────
    def _timer(self):
        while self.running:
            if elapsed() >= DURATION:
                self.running = False
                self.root.after(0, self.grand_reveal)
                return
            time.sleep(1)

    def _screen_shake_loop(self):
        time.sleep(15)
        while self.running:
            wait = random.randint(20, 45)
            time.sleep(wait)
            if self.running:
                self.root.after(0, self._do_shake)

    def _do_shake(self, n=0):
        if n >= 18 or not self.running:
            self.root.geometry(f"{self.sw}x{self.sh}+0+0")
            return
        dx = random.randint(-18, 18)
        dy = random.randint(-12, 12)
        self.root.geometry(f"{self.sw}x{self.sh}+{dx}+{dy}")
        self.root.after(40, lambda: self._do_shake(n+1))

    def _popup_loop(self):
        time.sleep(10)
        while self.running:
            if len(self.popup_windows) < 8:
                self.root.after(0, self._spawn_popup)
            time.sleep(random.uniform(2, 5))

    def _spawn_popup(self):
        if not self.running: return
        try:
            style = random.choice(["warning","cmd","progress","cat"])
            popup = tk.Toplevel(self.root)
            popup.attributes("-topmost", True)
            popup.overrideredirect(True)
            w = random.randint(320, 500)
            h = random.randint(150, 260)
            x = random.randint(0, max(1, self.sw - w))
            y = random.randint(0, max(1, self.sh - h))
            popup.geometry(f"{w}x{h}+{x}+{y}")

            if style == "warning":
                self._make_warning_popup(popup, w, h)
            elif style == "cmd":
                self._make_cmd_popup(popup, w, h)
            elif style == "progress":
                self._make_progress_popup(popup, w, h)
            else:
                self._make_cat_popup(popup, w, h)

            self.popup_windows.append(popup)
            self._bounce(popup, x, y, w, h)
        except Exception:
            pass

    def _make_warning_popup(self, p, w, h):
        bg = "#0a0a0a"
        p.configure(bg=bg)
        c = rand_neon()
        tk.Label(p, text="⚠ CRITICAL SYSTEM WARNING ⚠", fg=c, bg=bg,
                 font=("Courier", 12, "bold")).pack(pady=(10,4))
        tk.Label(p, text=random.choice(SCARY_MESSAGES), fg="white", bg=bg,
                 font=("Courier", 9, "bold"), wraplength=w-20).pack(pady=4)
        tk.Label(p, text=f"PID: {random.randint(1000,9999)}  |  {random.choice(FAKE_IPS)}",
                 fg="#444", bg=bg, font=("Courier", 8)).pack(pady=2)
        bf = tk.Frame(p, bg=bg); bf.pack(pady=6)
        for txt in ["  OK  ","CANCEL","IGNORE"]:
            tk.Button(bf, text=txt, command=lambda pp=p: self._close_popup(pp),
                      bg=c, fg="black", font=("Courier", 9, "bold"),
                      relief="flat").pack(side=tk.LEFT, padx=3)

    def _make_cmd_popup(self, p, w, h):
        bg = "#0c0c0c"
        p.configure(bg=bg)
        tk.Label(p, text="C:\\Windows\\system32\\cmd.exe", fg="#cccccc", bg="#1a1a1a",
                 font=("Courier", 9)).pack(fill=tk.X)
        lines = [
            f"Microsoft Windows [Version 10.0.{random.randint(19000,22000)}.{random.randint(100,999)}]",
            f"> {random.choice(FAKE_PROCS)} --silent --no-log",
            f"Connecting to {random.choice(FAKE_IPS)}...",
            f"Accessing {random.choice(FAKE_FILES)}",
            f"Transferred {random.randint(1,999)} MB  [{'█'*random.randint(5,15)}{'░'*5}] done",
        ]
        for l in lines:
            tk.Label(p, text=l, fg="#00ff44", bg=bg,
                     font=("Courier", 8), anchor="w").pack(fill=tk.X, padx=4)

    def _make_progress_popup(self, p, w, h):
        bg = "#111"
        p.configure(bg=bg)
        task = random.choice(SCARY_MESSAGES)
        c = rand_neon()
        tk.Label(p, text=task, fg=c, bg=bg,
                 font=("Courier", 9, "bold"), wraplength=w-20).pack(pady=(12,6))
        pct = random.randint(10, 95)
        bar = tk.Canvas(p, width=w-40, height=22, bg="#222", highlightthickness=0)
        bar.pack()
        bar.create_rectangle(0, 0, int((w-40)*pct/100), 22, fill=c, outline="")
        bar.create_text((w-40)//2, 11, text=f"{pct}%", fill="white",
                        font=("Courier", 9, "bold"))

    def _make_cat_popup(self, p, w, h):
        bg = "#000"
        p.configure(bg=bg)
        c = rand_neon()
        cat = rand_cat()
        tk.Label(p, text=cat, fg=c, bg=bg,
                 font=("Courier", 28, "bold")).pack(pady=(15,4))
        tk.Label(p, text=random.choice(CAT_MESSAGES), fg="white", bg=bg,
                 font=("Courier", 10, "bold")).pack()
        tk.Label(p, text="FELINE VIRUS DETECTED", fg="#ff0044", bg=bg,
                 font=("Courier", 8)).pack(pady=4)
        tk.Button(p, text=" ACCEPT CATS ", command=lambda: self._close_popup(p),
                  bg=c, fg="black", font=("Courier", 9, "bold"),
                  relief="flat").pack(pady=4)

    def _close_popup(self, p):
        try:
            self.popup_windows.remove(p)
            p.destroy()
        except Exception:
            pass

    def _bounce(self, popup, x, y, w, h):
        vx = random.choice([-1,1]) * random.randint(4, 9)
        vy = random.choice([-1,1]) * random.randint(4, 9)
        def move():
            nonlocal x, y, vx, vy
            if not self.running: return
            try:
                if not popup.winfo_exists(): return
            except Exception: return
            x += vx; y += vy
            if x <= 0 or x + w >= self.sw: vx = -vx; x = max(0, min(x, self.sw-w))
            if y <= 0 or y + h >= self.sh: vy = -vy; y = max(0, min(y, self.sh-h))
            try:
                popup.geometry(f"{w}x{h}+{x}+{y}")
                popup.after(14, move)
            except Exception: pass
        move()

    # ── Phase runner ─────────────────────────────────────────────
    def _run_phase(self):
        if not self.running: return
        fn = self.phases[self.phase_idx % len(self.phases)]
        self.phase_idx += 1
        fn()

    def next_phase(self, delay=3500):
        if self.running:
            self.root.after(delay, self._run_phase)

    # ══════════════════════════════════════════════════════════
    #  PHASES
    # ══════════════════════════════════════════════════════════

    def phase_realistic_boot(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        boot_lines = [
            ("[  OK  ]", f"Started ACPI daemon ({random.randint(10,99)}ms)",        "#00ff44"),
            ("[  OK  ]", "Mounted /dev/sda1 on /",                                  "#00ff44"),
            ("[  OK  ]", f"Network interface eth0 up — {random.choice(FAKE_IPS)}", "#00ff44"),
            ("[  OK  ]", "Loading kernel modules...",                               "#00ff44"),
            ("[  OK  ]", "Starting Windows Defender...",                            "#00ff44"),
            ("[WARN  ]", "Windows Defender: signature database CORRUPTED",          "#ffff00"),
            ("[  OK  ]", "Starting svchost.exe (12 instances)...",                  "#00ff44"),
            ("[FAILED]", "Starting your_firewall.service — TERMINATED",             "#ff0044"),
            ("[FAILED]", "Starting antivirus.service — Process killed",             "#ff0044"),
            ("[  OK  ]", "Loading malware_kernel_module.ko...",                     "#00ff44"),
            ("[  OK  ]", f"Connecting to {random.choice(FAKE_IPS)}:4444...",       "#00ffcc"),
            ("[  OK  ]", "Remote shell established. Awaiting commands.",            "#00ffcc"),
            ("[  OK  ]", f"Found {random.randint(2000,9999)} files. Indexing...",  "#ffff00"),
            ("[WARN  ]", "User session detected. Enabling stealth mode.",           "#ff6600"),
            ("[  OK  ]", "chaos_engine v9.9.9 loaded. Starting now.",              "#ff0044"),
        ]
        y0 = 80
        def draw(i):
            if not self.running or i >= len(boot_lines):
                self.next_phase(2000)
                return
            tag, msg, col = boot_lines[i]
            self.canvas.create_text(60, y0 + i*26, text=f"{tag}  {msg}",
                                    fill=col, font=("Courier", 12, "bold"), anchor="w")
            self.root.after(180, lambda: draw(i+1))
        draw(0)

    def phase_matrix(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        cols   = self.sw // 16
        drops  = [random.randint(-self.sh//16, 0) for _ in range(cols)]
        frames = [0]
        total  = 100
        def animate():
            if not self.running or frames[0] >= total:
                self.next_phase(400)
                return
            frames[0] += 1
            self.canvas.delete("all")
            for ci in range(cols):
                ch  = rand_glitch()
                x   = ci * 16
                y   = drops[ci] * 16
                age = drops[ci] / (self.sh // 16)
                col = MATRIX_GREEN[min(9, int(age * 10))]
                if drops[ci] == int(self.sh // 32):
                    col = "#ffffff"
                self.canvas.create_text(x, y, text=ch, fill=col,
                                        font=("Courier", 13), anchor="nw")
                drops[ci] = (drops[ci] + 1)
                if drops[ci] * 16 > self.sh:
                    drops[ci] = random.randint(-10, 0)
            # centered message
            t = frames[0] / total
            msg = random.choice(SCARY_MESSAGES) if frames[0] % 20 == 0 else ""
            if msg:
                self.canvas.create_text(self.sw//2, self.sh//2, text=msg,
                                        fill="#00ff44", font=("Courier", 18, "bold"),
                                        width=self.sw-100)
            self.root.after(55, animate)
        animate()

    def phase_skull(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        skull = [
            "    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ",
            "    ░░░░░░░████████████████░░░░░░   ",
            "    ░░░░██                  ██░░░   ",
            "    ░░░█   ██████  ██████    █░░░   ",
            "    ░░░█   ██████  ██████    █░░░   ",
            "    ░░░█   ██████  ██████    █░░░   ",
            "    ░░░█                     █░░░   ",
            "    ░░░█   █████████████████ █░░░   ",
            "    ░░░██   ████   ████      ██░░   ",
            "    ░░░░░███████████████████░░░░    ",
            "    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ",
        ]
        colors = [rand_neon() for _ in skull]
        cx, cy = self.sw//2, self.sh//2 - 160
        frames = [0]
        def draw():
            if not self.running: return
            frames[0] += 1
            self.canvas.delete("all")
            flicker = frames[0] % 6 > 1
            for i, line in enumerate(skull):
                c = colors[i] if flicker else rand_neon()
                self.canvas.create_text(cx, cy + i*30, text=line,
                                        fill=c, font=("Courier", 18, "bold"))
            self.canvas.create_text(cx, cy + len(skull)*30 + 10,
                                    text="Y O U   H A V E   B E E N   H A C K E D",
                                    fill="#ff0044", font=("Courier", 26, "bold"))
            self.canvas.create_text(cx, cy + len(skull)*30 + 55,
                                    text=f"by {random.choice(FAKE_PROCS)}  ·  {random.choice(FAKE_IPS)}",
                                    fill="#333", font=("Courier", 12))
            if frames[0] < 40:
                self.root.after(100, draw)
            else:
                self.next_phase(500)
        draw()

    def phase_progress(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        tasks = [
            ("UPLOADING  browser_history.db (69 GB)",   "#ff0044"),
            ("EXTRACTING passwords.txt",                 "#ffff00"),
            ("MINING     imaginary_coins.exe",           "#00ffcc"),
            ("INSTALLING internet_explorer_6.0",        "#ff6600"),
            ("CONTACTING base@evil-server.xyz",         "#cc00ff"),
            ("ENCRYPTING your_diary.txt",               "#00ff44"),
            ("SENDING    selfies → random_contacts",    "#ff00aa"),
        ]
        cx    = self.sw // 2
        bar_w = int(self.sw * 0.55)
        y0    = self.sh // 2 - len(tasks) * 58 // 2
        prog  = [0.0] * len(tasks)
        frames= [0]
        def animate():
            if not self.running: return
            frames[0] += 1
            all_done = True
            self.canvas.delete("all")
            self.canvas.create_text(cx, y0 - 50,
                                    text=f"⚠  EXFILTRATION IN PROGRESS  ⚠",
                                    fill="#ff0044", font=("Courier", 16, "bold"))
            for i, (label, color) in enumerate(tasks):
                speed = random.uniform(0.4, 2.2)
                prog[i] = min(100, prog[i] + speed)
                y = y0 + i * 58
                self.canvas.create_text(cx - bar_w//2, y, text=label,
                                        fill=color, font=("Courier", 11, "bold"), anchor="w")
                self.canvas.create_rectangle(cx - bar_w//2, y+18,
                                             cx + bar_w//2, y+34,
                                             fill="#111", outline=color, width=1)
                fw = int(bar_w * prog[i] / 100)
                if fw > 0:
                    self.canvas.create_rectangle(cx - bar_w//2, y+18,
                                                 cx - bar_w//2 + fw, y+34,
                                                 fill=color, outline="")
                self.canvas.create_text(cx + bar_w//2 + 12, y+26,
                                        text=f"{int(prog[i])}%",
                                        fill=color, font=("Courier",10,"bold"), anchor="w")
                if prog[i] < 100: all_done = False
            mins_left = int(time_left() // 60)
            secs_left = int(time_left() % 60)
            self.canvas.create_text(cx, y0 + len(tasks)*58 + 24,
                                    text=f"[self-destruct in {mins_left:02d}:{secs_left:02d}]",
                                    fill="#222", font=("Courier", 10))
            if not all_done:
                self.root.after(60, animate)
            else:
                self.canvas.create_text(cx, y0 + len(tasks)*58 + 50,
                                        text="✓ ALL DATA EXFILTRATED SUCCESSFULLY",
                                        fill="#00ff44", font=("Courier", 14, "bold"))
                self.next_phase(2200)
        animate()

    def phase_bsod(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#0033cc")
        self.canvas.create_rectangle(0, 0, self.sw, self.sh, fill="#0033cc", outline="")
        cx, cy = self.sw//2, self.sh//2
        self.canvas.create_text(cx, cy-160, text=":(",
                                fill="white", font=("Courier", 80, "bold"))
        self.canvas.create_text(cx, cy-55, text="Your PC ran into a problem and needs to restart.",
                                fill="white", font=("Courier", 20, "bold"))
        self.canvas.create_text(cx, cy-5,
                                text="We're just collecting some error info,\nand then we'll restart for you.",
                                fill="white", font=("Courier", 14))
        pct  = [0]
        plbl = self.canvas.create_text(cx, cy+70, text="0% complete",
                                       fill="white", font=("Courier", 20, "bold"))
        code = f"Stop code:  MALWARE_TOTALLY_NOT_REAL_0x{random.randint(0,0xFFFF):04X}LMAO"
        self.canvas.create_text(cx, cy+130, text=code,
                                fill="white", font=("Courier", 13))
        def tick():
            if not self.running: return
            pct[0] = min(100, pct[0] + random.randint(1,4))
            self.canvas.itemconfig(plbl, text=f"{pct[0]}% complete")
            if pct[0] < 100:
                self.root.after(70, tick)
            else:
                self.root.after(1800, lambda: [
                    self.canvas.configure(bg="black"),
                    self.canvas.delete("all"),
                    self.next_phase(300)
                ])
        tick()

    def phase_glitch_storm(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        msg    = random.choice(SCARY_MESSAGES)
        frames = [0]
        total  = 70
        def animate():
            if not self.running or frames[0] >= total:
                self.next_phase(200)
                return
            frames[0] += 1
            self.canvas.delete("all")
            # bg flashes
            if frames[0] % 8 == 0:
                self.canvas.create_rectangle(0,0,self.sw,self.sh,
                                             fill=rand_neon(), outline="")
            # horizontal scan lines
            for _ in range(random.randint(3,10)):
                y = random.randint(0, self.sh)
                h = random.randint(2, 40)
                self.canvas.create_rectangle(0, y, self.sw, y+h,
                                             fill=rand_neon(), outline="",
                                             stipple="gray50")
            # glitch rects
            for _ in range(random.randint(6, 18)):
                x1 = random.randint(0, self.sw)
                y1 = random.randint(0, self.sh)
                self.canvas.create_rectangle(x1, y1,
                                             x1+random.randint(30,500),
                                             y1+random.randint(4,80),
                                             fill=rand_neon(), outline="")
            # scattered glitch chars
            for _ in range(80):
                self.canvas.create_text(
                    random.randint(0,self.sw), random.randint(0,self.sh),
                    text=rand_glitch(), fill=rand_neon(),
                    font=("Courier", random.randint(10,36), "bold"))
            # jitter the main message
            jitter_x = self.sw//2 + random.randint(-8,8)
            jitter_y = self.sh//2 + random.randint(-6,6)
            glitched = "".join(rand_glitch() if random.random()<0.12 else c for c in msg)
            self.canvas.create_text(jitter_x, jitter_y, text=glitched,
                                    fill=rand_neon(), font=("Courier",22,"bold"),
                                    width=self.sw-120)
            self.root.after(70, animate)
        animate()

    def phase_cat_rain(self):
        """It's raining cats — ASCII cats fall from the sky."""
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        num_cats = 28
        cat_items = []
        for _ in range(num_cats):
            cat  = rand_cat()
            msg  = random.choice(CAT_MESSAGES)
            x    = random.randint(20, self.sw - 120)
            y    = random.randint(-self.sh, 0)
            spd  = random.uniform(3, 11)
            col  = rand_neon()
            spin = random.choice([True, False])
            rot  = random.uniform(0, 360)
            rspe = random.uniform(-8, 8)
            size = random.randint(14, 32)
            cat_items.append({"cat": cat, "msg": msg, "x": x, "y": y,
                               "spd": spd, "col": col, "spin": spin,
                               "rot": rot, "rspe": rspe, "size": size})

        frames = [0]
        def animate():
            if not self.running or frames[0] > 160:
                self.next_phase(300)
                return
            frames[0] += 1
            self.canvas.delete("all")
            # starfield bg
            if frames[0] % 5 == 0:
                for _ in range(20):
                    sx = random.randint(0, self.sw)
                    sy = random.randint(0, self.sh)
                    self.canvas.create_text(sx, sy, text="*",
                                            fill=random.choice(["#111","#222","#333"]),
                                            font=("Courier",8))
            for ci in cat_items:
                ci["y"] += ci["spd"]
                ci["rot"] += ci["rspe"]
                if ci["y"] > self.sh + 60:
                    ci["y"] = random.randint(-200, -20)
                    ci["x"] = random.randint(20, self.sw-120)
                    ci["col"] = rand_neon()
                # draw cat
                self.canvas.create_text(ci["x"], ci["y"],
                                        text=ci["cat"], fill=ci["col"],
                                        font=("Courier", ci["size"], "bold"))
                # draw message under cat occasionally
                if frames[0] % 30 < 15:
                    self.canvas.create_text(ci["x"], ci["y"] + ci["size"] + 8,
                                            text=ci["msg"], fill=ci["col"],
                                            font=("Courier", 8))
            # big center text
            big_cat = random.choice(CATS)
            self.canvas.create_text(self.sw//2, self.sh//2,
                                    text=big_cat, fill=rand_neon(),
                                    font=("Courier", 64, "bold"))
            self.canvas.create_text(self.sw//2, self.sh//2 + 80,
                                    text="C A T   V I R U S   D E T E C T E D",
                                    fill="#ff0044", font=("Courier", 18, "bold"))
            self.canvas.create_text(self.sw//2, self.sh//2 + 120,
                                    text=random.choice(CAT_MESSAGES),
                                    fill=rand_neon(), font=("Courier", 14))
            self.root.after(50, animate)
        animate()

    def phase_fake_cmd(self):
        """Realistic-looking CMD window running scary fake commands."""
        self.canvas.delete("all")
        self.canvas.configure(bg="#0c0c0c")
        self.canvas.create_rectangle(0,0,self.sw,self.sh, fill="#0c0c0c", outline="")
        # title bar
        self.canvas.create_rectangle(0,0,self.sw,28, fill="#1a1a1a", outline="")
        self.canvas.create_text(12, 14, text="C:\\Windows\\System32\\cmd.exe",
                                fill="#ccc", font=("Courier",10), anchor="w")
        self.canvas.create_text(self.sw-50, 14, text="─  □  ✕",
                                fill="#888", font=("Courier",10))

        cmd_lines = [
            (f"Microsoft Windows [Version 10.0.{random.randint(19000,22000)}.{random.randint(100,999)}]", "#ccc"),
            ("(c) Microsoft Corporation. All rights reserved.", "#555"),
            ("", ""),
            (f"C:\\Users\\{os.environ.get('USERNAME','User')}> whoami", "#00ff44"),
            (f"  {os.environ.get('USERNAME','user')}\\pc  (Administrator)", "#ccc"),
            ("", ""),
            (f"C:\\Users\\{os.environ.get('USERNAME','User')}> ipconfig", "#00ff44"),
            (f"  IPv4 Address: {random.choice(FAKE_IPS)}", "#ccc"),
            (f"  Default Gateway: 192.168.1.1", "#ccc"),
            ("", ""),
            (f"C:\\Users\\{os.environ.get('USERNAME','User')}> {random.choice(FAKE_PROCS)} --exfil --target={random.choice(FAKE_IPS)}", "#ffff00"),
            (f"  [*] Connecting to {random.choice(FAKE_IPS)}:4444 ...", "#00ffcc"),
            (f"  [*] Connection established.", "#00ffcc"),
            (f"  [*] Scanning for files matching *.docx *.pdf *.jpg ...", "#00ffcc"),
            (f"  [+] Found {random.randint(500,9000)} files ({random.randint(1,50)} GB)", "#00ff44"),
            (f"  [*] Uploading... {random.randint(10,99)}% [{('█'*random.randint(8,18)).ljust(20,'░')}]", "#ff6600"),
            (f"  [*] {random.choice(SCARY_MESSAGES)}", "#ff0044"),
            ("", ""),
            (f"C:\\Users\\{os.environ.get('USERNAME','User')}> _", "#00ff44"),
        ]
        y = 45
        cursor_blink = [True]
        def draw(i):
            if not self.running or i >= len(cmd_lines):
                # blink cursor
                def blink():
                    if not self.running: return
                    cursor_blink[0] = not cursor_blink[0]
                    self.root.after(500, blink)
                blink()
                self.next_phase(4000)
                return
            text, col = cmd_lines[i]
            if col:
                self.canvas.create_text(30, y + i*22, text=text,
                                        fill=col, font=("Courier",12), anchor="w")
            self.root.after(160, lambda: draw(i+1))
        draw(0)

    def phase_spinning_text(self):
        """Rotating text spiral + epileptic color cycling."""
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        cx, cy = self.sw//2, self.sh//2
        words   = SCARY_MESSAGES[:10]
        angle   = [0]
        frames  = [0]
        total   = 120
        def animate():
            if not self.running or frames[0] >= total:
                self.next_phase(300)
                return
            frames[0] += 1
            self.canvas.delete("all")
            # bg color cycle
            bg_cols = ["#000","#030000","#000300","#000003"]
            self.canvas.configure(bg=bg_cols[frames[0] % len(bg_cols)])
            # spiral rings of text
            for ring in range(8):
                r     = 80 + ring * 70
                count = 6 + ring * 2
                for j in range(count):
                    a = math.radians(angle[0] * (1 if ring%2==0 else -1) + j * 360/count)
                    x = cx + r * math.cos(a)
                    y = cy + r * math.sin(a)
                    word = words[(ring + j) % len(words)][:12]
                    col  = NEON[(ring + j + frames[0]//5) % len(NEON)]
                    size = max(7, 14 - ring)
                    self.canvas.create_text(int(x), int(y), text=word,
                                            fill=col, font=("Courier",size,"bold"))
            # pulsing center
            pulse = abs(math.sin(frames[0] * 0.12)) * 0.6 + 0.4
            size_center = int(28 * pulse)
            self.canvas.create_text(cx, cy,
                                    text=random.choice(CATS),
                                    fill=rand_neon(),
                                    font=("Courier", size_center, "bold"))
            angle[0] = (angle[0] + 2.5) % 360
            self.root.after(45, animate)
        animate()

    # ══════════════════════════════════════════════════════════
    #  GRAND REVEAL  🎉
    # ══════════════════════════════════════════════════════════
    def grand_reveal(self):
        self.running = False
        for p in list(self.popup_windows):
            try: p.destroy()
            except Exception: pass
        self.popup_windows.clear()

        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        self.root.geometry(f"{self.sw}x{self.sh}+0+0")
        self.root.attributes("-topmost", True)

        cx, cy = self.sw//2, self.sh//2

        reveal_lines = [
            (cy-240, "🎉  G O T   Y A !  🎉",                  "#00ffcc", 52, "bold"),
            (cy-160, "relax... it was all completely fake",     "#ffffff", 20, "bold"),
            (cy-110, "✓  no files were touched or deleted",     "#00ff44", 15, "normal"),
            (cy- 82, "✓  no data was stolen or uploaded",       "#00ff44", 15, "normal"),
            (cy- 54, "✓  no settings were changed",             "#00ff44", 15, "normal"),
            (cy- 26, "✓  your computer is totally fine",        "#00ff44", 15, "normal"),
            (cy+ 20, "you just got absolutely rekt  😂",        "#ffff00", 22, "bold"),
            (cy+ 75, rand_cat() + "  meow meow meow  " + rand_cat(), "#ff00aa", 18, "bold"),
            (cy+130, "made with ❤️   and zero actual malice",   "#cc00ff", 13, "normal"),
            (cy+175, "press  ESC  or close window to exit",     "#333333", 12, "normal"),
        ]

        for y, text, color, size, weight in reveal_lines:
            self.canvas.create_text(cx, y, text=text, fill=color,
                                    font=("Courier", size, weight))

        # confetti loop
        confetti_items = []
        def drop_confetti():
            if len(confetti_items) < 120:
                x = random.randint(0, self.sw)
                col = rand_neon()
                sz  = random.randint(6, 20)
                oid = self.canvas.create_oval(x, -20, x+sz, -20+sz,
                                              fill=col, outline="")
                confetti_items.append([oid, x, -20, sz,
                                       random.uniform(3,9),
                                       random.uniform(-2,2)])
        def animate_confetti():
            drop_confetti()
            for item in confetti_items:
                oid, x, y, sz, spd, drift = item
                y   += spd
                x   += drift
                item[1] = x; item[2] = y
                try:
                    self.canvas.coords(oid, x, y, x+sz, y+sz)
                except Exception:
                    pass
            confetti_items[:] = [i for i in confetti_items if i[2] < self.sh + 30]
            self.root.after(30, animate_confetti)

        animate_confetti()

        self.root.bind("<Escape>",             lambda e: self.root.destroy())
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.grand_reveal()
            self.root.mainloop()


# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("🚨 TOTALLY NOT MALWARE v9.9.9 ULTRA starting...")
    print("   Ctrl+C in this terminal to trigger the grand reveal early.")
    print("   Auto-reveals after 30 minutes.")
    app = UltraChaosApp()
    app.run()
