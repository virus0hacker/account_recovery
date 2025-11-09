# 🇸🇦 Account Recovery — snap: ml-ftt

**Author:** ml-ftt  
**Version:** 1.0  
**License:** MIT

A simple CLI helper that builds professional account recovery messages, copies them to the clipboard, saves them locally, and opens the official support/contact page for the selected platform.

Supported platforms:
- Snapchat
- Instagram
- X (Twitter)
- WhatsApp

---

## 📌 Quick summary:

This tool helps you prepare a complete recovery message when an account is hacked, suspended, disabled, or inaccessible. It:
- Builds a ready-to-send message (English)
- Copies the message to the system clipboard (fallback: saves to file)
- Saves the message as `recovery_<platform>_<id>.txt`
- Opens the official support page for the chosen platform
- Prints colored terminal output for easier usage

**Note:** This tool does NOT contact support automatically. It only helps you compose and submit a message using the official support channels. Use only for accounts you own or manage.

---

## 📥 Quick start:

1. Clone repo:

git clone https://github.com/virus0hacker/account_recovery.git
cd account-recovery

Run:

python account_recovery.py


Follow the prompts: choose a platform, enter account identifier (username/email/phone), describe the issue briefly, and enter a preferred contact. The message will be copied to the clipboard (or saved to recovery_message.txt) and the official support page will open in your browser

Files included

account_recovery.py — main script (CLI, colored output, clipboard copy).

README.md — this file.

LICENSE — MIT license.

.gitignore — recommended ignores.

CHANGELOG.md — simple changelog template.

CONTRIBUTING.md — short contribution guide.


⚖️ Legal & ethical notice:

Use this tool only for lawful, authorized recovery attempts on accounts you own or manage. Misuse (unauthorized access, harassment, fraud) is your responsibility and may be illegal.


استخدم هذه الأداة فقط لاسترجاع حسابات تملكها أو تملك تفويضًا قانونيًا لإدارتها. أي استخدام خاطئ أو غير قانوني يقع على عاتقك.


🔧 Customization:

You can easily add more platforms or update support URLs in the PLATFORM_SUPPORT dictionary inside account_recovery.py. If you want an Arabic message template or extra templates (e.g., for "hacked" vs "suspended"), send a request and I'll add them.



🧰 Contributing:

See CONTRIBUTING.md for simple guidelines.


📄 License:


```
MIT License

Copyright (c) 2025 ml-ftt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
