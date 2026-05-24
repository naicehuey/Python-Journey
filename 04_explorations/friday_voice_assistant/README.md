# Friday — Voice Assistant

A simple voice assistant built with Python, inspired by
Iron Man's JARVIS. Built out of pure curiosity.

## What It Does
- Greets the user by voice on startup
- Listens for voice commands through the microphone
- Understands speech using Google's speech recognition
- Responds by speaking back to the user
- Stops when the user says "stop"

## What I Learned
- Installing external Python packages using pip
- Using `speech_recognition` for microphone input
- Using `pyttsx3` for text-to-speech output
- Writing clean reusable functions (`speak` and `listen`)
- Handling specific exceptions (`sr.UnknownValueError`)
- Using `while True` with a `break` condition
- That curiosity is one of the best reasons to build
  something — this was never part of the plan

## Requirements
Install dependencies before running:
```bash
pip install speechrecognition pyttsx3 pyaudio
```

## How To Run
```bash
python friday.py
```

## Note
This project was not part of the original learning plan —
built out of pure curiosity after seeing it online.
Going from Hello World to a working voice assistant
in the same month shows what curiosity can do.