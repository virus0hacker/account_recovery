#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Account Recovery (Account_recovery)
Author: ml-ftt
License: MIT (see LICENSE)

Supported platforms: Snapchat, Instagram, X (Twitter), WhatsApp
"""

# ───────────────────────────────────────────────────────────────
#  MIT License (summary)
#  Copyright (c) 2025 ml-ftt
# ───────────────────────────────────────────────────────────────

import os
import sys
import datetime
import webbrowser
import textwrap

# === Color Setup ===
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[92m"
    DARK_GREEN = "\033[38;5;22m"
    WHITE = "\033[97m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    DIM = "\033[2m"

def cprint(msg, color=C.RESET, bold=False):
    print(f"{C.BOLD if bold else ''}{color}{msg}{C.RESET}")

# === Banner ===
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_art = f"""
{C.DARK_GREEN}{C.BOLD}
     _                             _             ____                                    
    / \   ___ ___ ___  _   _ _ __ | |_          |  _ \ ___  ___ _____   _____ _ __ _   _ 
   / _ \ / __/ __/ _ \| | | | '_ \| __|  _____  | |_) / _ \/ __/ _ \ \ / / _ \ '__| | | |
  / ___ \ (_| (_| (_) | |_| | | | | |_  |_____| |  _ <  __/ (_| (_) \ V /  __/ |  | |_| |
 /_/   \_\___\___\___/ \__,_|_| |_|\__|         |_| \_\___|\___\___/ \_/ \___|_|   \__, |
                                                                                   |___/ 
{C.BRIGHT_GREEN}                     🇸🇦  Account Recovery — snap: ml-ftt
───────────────────────────────────────────────────────────────────────────────
{C.RESET}
"""
    print(banner_art)

# === Clipboard handling ===
try:
    import tkinter as tk
    _root = tk.Tk()
    _root.withdraw()
    def copy_to_clipboard(text):
        _root.clipboard_clear()
        _root.clipboard_append(text)
        _root.update()
except Exception:
    def copy_to_clipboard(text):
        with open("recovery_message.txt", "w", encoding="utf-8") as f:
            f.write(text)
        cprint("[!] Clipboard not available — message saved to recovery_message.txt", C.YELLOW)

# === Platform data ===
PLATFORMS = {
    "snapchat": {
        "name": "Snapchat",
        "support": "https://help.snapchat.com/hc/requests/new",
        "note": "Use Snapchat Help Center or in-app 'Contact Us'."
    },
    "instagram": {
        "name": "Instagram",
        "support": "https://help.instagram.com/358911864194456",
        "note": "Recovery is handled via in-app flows or help forms."
    },
    "x": {
        "name": "X (Twitter)",
        "support": "https://help.x.com/en/forms/account-access/appeals",
        "note": "Use X appeal forms for locked or suspended accounts."
    },
    "whatsapp": {
        "name": "WhatsApp",
        "support": "https://www.whatsapp.com/contact",
        "note": "Use WhatsApp contact form; official replies are from @support.whatsapp.com."
    }
}

# === Core Functions ===
def choose_platform():
    cprint("Available Platforms:", C.CYAN, bold=True)
    for i, k in enumerate(PLATFORMS, 1):
        cprint(f"  {i}. {PLATFORMS[k]['name']}", C.GREEN)
    cprint("  0. Exit", C.YELLOW)
    while True:
        try:
            c = int(input(f"{C.CYAN}Select platform number: {C.RESET}"))
            if c == 0:
                sys.exit(0)
            if 1 <= c <= len(PLATFORMS):
                return list(PLATFORMS.keys())[c-1]
        except ValueError:
            pass
        cprint("Invalid selection.", C.RED)

def build_message(platform, user_id, details, contact):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""Subject: Account recovery request ({PLATFORMS[platform]['name']})

Hello {PLATFORMS[platform]['name']} Support Team,

I’m contacting you to recover my account.  
Below are my details and a short description of the problem:

• Platform: {PLATFORMS[platform]['name']}
• Account: {user_id}
• Issue noticed: {now}

Problem Summary:
{details or '(Describe briefly what happened — e.g. hacked, suspended, disabled, lost access)'}  

Steps I have already taken:
- Tried in-app password reset/recovery options
- Checked linked email/phone for reset links

Preferred contact for recovery:
{contact or '(Your email or phone here)'}

Please let me know what information you need to verify my identity and recover my account.

Thank you for your time and help,
(Your Full Name)
(Your Contact Email / Phone)
"""

def open_support(platform):
    url = PLATFORMS[platform]["support"]
    note = PLATFORMS[platform]["note"]
    try:
        webbrowser.open(url, new=2)
        cprint(f"\nOpened support page: {url}", C.GREEN)
    except Exception:
        cprint("Unable to open browser.", C.RED)
    cprint(f"Tip: {note}", C.YELLOW)

def save_message(platform, identifier, message):
    safe_id = identifier.replace("@", "_at_").replace(" ", "_")
    fname = f"recovery_{platform}_{safe_id}.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(message)
    return fname

# === Main ===
def main():
    banner()
    cprint("🟢 Author: ml-ftt  |  License: MIT", C.DIM)
    cprint("This tool builds recovery messages for hacked or locked accounts.\n", C.WHITE)

    platform = choose_platform()
    account_id = input("Enter username / email / phone: ").strip()
    contact = input("Your preferred contact (email or phone): ").strip()
    details = input("Describe the issue briefly: ").strip()

    message = build_message(platform, account_id, details, contact)
    copy_to_clipboard(message)
    fname = save_message(platform, account_id, message)

    cprint(f"\n✅ Recovery message copied and saved to: {fname}", C.BRIGHT_GREEN)
    cprint("\nPreview (first lines):", C.MAGENTA)
    print(C.WHITE + "\n".join(message.splitlines()[:12]) + C.RESET)
    cprint("\nOpening official support page...", C.CYAN)
    open_support(platform)
    cprint("\nPaste the message into the contact form and attach your proofs.", C.BRIGHT_GREEN)
    cprint("Good luck 🙏  — stay safe online!", C.BRIGHT_GREEN, bold=True)

# === Run ===
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\nCancelled by user.", C.YELLOW)
