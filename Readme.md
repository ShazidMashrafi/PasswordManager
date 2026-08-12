# 🔐 Desktop Password Manager

A lightweight, user-friendly desktop application built with Python and Tkinter for generating, managing, and securely storing website credentials locally.

Developed as a first-year 2nd-semester academic project by **[Shazid Mashrafi](https://github.com/ShazidMashrafi)** and **[Shahriar Hasnat Shafin Ahmed](https://github.com/shafinkun)**.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Running](#installation--running)
- [Usage Guide](#-usage-guide)
  - [Generating Passwords](#1-generating-passwords)
  - [Saving Credentials](#2-saving-credentials)
  - [Updating Passwords](#3-updating-passwords)
- [Data Storage Format](#-data-storage-format)
- [Authors](#-authors)

---

## 🌟 Overview

The **Password Manager** provides a clean graphical interface (GUI) to help users generate strong, customizable passwords and save login details for various online platforms. Credentials are saved locally on the machine in a simple structured text file (`Passwords.txt`), eliminating reliance on cloud servers or external database dependencies.

---

## ✨ Key Features

- 🎲 **Customizable Password Generator**:
  - Configurable password lengths (from 8 to 32 characters).
  - Dynamic inclusion options for Uppercase letters, Digits, and Symbols.
  - Proportional character distribution and random shuffling for high entropy.
- 💾 **Local Credentials Storage**:
  - Record Website Name, Email/Username, and Password.
  - Automatically appends records to a clean local storage file (`Passwords.txt`).
- 🔄 **Account Detection & Updates**:
  - Detects existing website/username entries to prevent unintended duplicates.
  - Prompts options to update existing credentials or save as a new entry.
- ✅ **Input Validation & Safety**:
  - Validates character inputs and username/email structure.
  - Ensures password lengths adhere to security guidelines (8-32 characters).
  - Clean error dialogs and confirmation popups (`tkinter.messagebox`).
- 🎨 **Custom GUI Design**:
  - Auto-centers window on desktop screen startup.
  - Custom branded window icon and header banner artwork.

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **GUI Framework:** `tkinter` (Built-in Python Standard Library)
- **Modules Used:** `random`, `tkinter.messagebox`
- **Assets:** Custom PNG icons and banners (`Assets/`)

---

## 📁 Project Structure

```text
password-manager/
├── Assets/
│   ├── banner.png       # GUI Top Header Banner
│   └── logo.png         # Application Window Icon
├── Passwords.txt        # Local storage for saved credentials
├── main.py              # Main Application Entry Point & GUI logic
└── Readme.md            # Project Documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
  - *Linux users:* If `tkinter` is not pre-installed with Python, install it via package manager:
    ```bash
    sudo apt-get install python3-tk
    ```

### Installation & Running

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ShazidMashrafi/Password-Manager.git
   cd Password-Manager
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```
   *(or `python3 main.py` depending on your system configuration)*

---

## 📖 Usage Guide

### 1. Generating Passwords
1. Enter the desired **Password Length** (between 8 and 32).
2. Select character inclusion checkboxes: **Uppercase**, **Digit**, and/or **Symbol**.
3. Click **Generate Password** to instantly populate a randomized password.

### 2. Saving Credentials
1. Fill in **Website Name**, **Email/Username**, and **Password**.
2. Click **Save**.
3. Review and confirm details in the popup dialog box.

### 3. Updating Passwords
- If an entry matching the Website and Email/Username already exists, a dialog will ask whether to **update the password** or **create a duplicate entry**.

---

## 📄 Data Storage Format

Credentials are stored in `Passwords.txt` using structured pipe-delimited format:

```text
Website : github.com | Email/Username : user@example.com | Password : K9#pQ2!vL8
Website : google.com | Email/Username : admin@gmail.com  | Password : X7$mR1@wN4
```

---

## 👥 Authors

- **Shazid Mashrafi** - [*GitHub Profile*](https://github.com/ShazidMashrafi)
- **Shahriar Hasnat Shafin Ahmed** - [*GitHub Profile*](https://github.com/shafinkun)

---
*Created as part of First Year, Second Semester coursework.*