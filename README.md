# Voice Control System

A Python-based system that allows full control of a Windows laptop using voice commands.

## Features

- **Voice Input**: Continuous listening and speech-to-text conversion.
- **System Control**: Volume, brightness, shutdown, restart, sleep.
- **App Control**: Open Notepad, Calculator, Chrome, VS Code, File Explorer.
- **Input Control**: Mouse click, scroll, keyboard typing.
- **Browser Control**: Google search, open websites (YouTube, Google).
- **File Control**: Open specific folders (Documents, Downloads, etc.).
- **Feedback**: Text-to-speech confirmation for actions.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: `pyaudio` might require manual installation of a `.whl` file on some Windows systems if `pip install pyaudio` fails.*

3.  **Run the Application**:
    ```bash
    python main.py
    ```

## Usage

Speak clearly into your microphone once "Listening..." appears.

### Example Commands

- **System**: "Volume up", "Mute", "Brightness down", "Shutdown" (requires confirmation).
- **Apps**: "Open Notepad", "Open VS Code", "Open Calculator".
- **Folders**: "Open folder downloads", "Open folder documents".
- **Web**: "Search for Python tutorials", "Open YouTube".
- **Input**: "Click", "Scroll down", "Type Hello World".

## Configuration

Edit `src/config.py` to:
- Change voice rate/volume.
- Add new folder shortcuts (`FOLDERS` dictionary).
- Adjust microphone sensitivity (`ENERGY_THRESHOLD`).

## Project Structure

See `folder_structure.txt` for details.
