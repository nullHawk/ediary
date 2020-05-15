# E-Diary

A secure digital diary application built with PyQt5 that allows users to write, save, and retrieve encrypted diary entries with a beautiful graphical interface.

## Features

- **Secure Authentication**: User registration and login system
- **Encrypted Entries**: All diary entries are encrypted for privacy and security
- **Calendar Integration**: Interactive calendar widget to select dates
- **Date-based Organization**: Entries are automatically organized by date
- **User-friendly Interface**: Modern GUI with custom backgrounds and styling
- **File Management**: Save, read, and manage diary entries efficiently

## Prerequisites

Before running the application, make sure you have Python and PyQt5 installed:

```bash
pip install PyQt5
```

## Installation & Usage

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python login.py
```

## How It Works 

1. **Login/Register**: Start by creating an account or logging in with existing credentials
2. **Calendar View**: Select a date from the interactive calendar
3. **Write Entry**: Write your diary entry in the text editor
4. **Auto-save**: Entries are saved with encryption to protect your privacy
5. **Retrieve Entries**: Click on any date to view previously written entries

## File Structure

- `login.py` - Main entry point with authentication system
- `register.py` - User registration interface
- `calendar.py` - Calendar widget for date selection
- `diary.py` - Main diary writing interface
- `encrypt.py` - Encryption/decryption utilities
- `*_rc.py` - Resource files for UI elements

## Security

All diary entries are encrypted using a custom encryption algorithm before being stored locally. Each entry is saved as an encrypted text file organized by user and date.

## Author 

Made by **Suryansh Shakya**

## License

Copyright © Suryansh Shakya. All rights reserved.

---

*Keep your thoughts safe and organized with E-Diary!* ✍️