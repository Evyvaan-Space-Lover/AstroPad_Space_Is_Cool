# AstroPad 

A space-themed 4-key macropad built using the Seeeduino XIAO, designed to bring astronomy, chaos, and peak productivity together.

> Why settle for volume controls when you can have a dedicated Bruh button?

---

## Features

-  **Stellarium Launcher** – Instantly open an interactive sky map.
-  **ISS Tracker** – Check the International Space Station's location with a single press.
-  **Bruh Button** – Play the legendary Bruh sound effect.
-  **NASA APOD** – Open NASA's Astronomy Picture of the Day.

### Bonus
- 0.91" OLED display support (planned)
-  Custom-designed PCB
-  Custom 3D-printed case
-  Mechanical switch support

---

## Hardware

| Component | Part |
|------------|-------|
| Microcontroller | Seeeduino XIAO (SAMD21) |
| Switches | 4 × MX-compatible mechanical switches |
| Display | 0.91" I²C OLED (SSD1306) |
| Case | Custom-designed 3D printed enclosure |
| Plate | Custom switch plate |
| Firmware | KMK Firmware |

---

## Schematic Overview

### Switch Connections

| Switch | XIAO Pin |
|---------|-----------|
| SW1 | D0 |
| SW2 | D1 |
| SW3 | D2 |
| SW4 | D3 |

### OLED Connections

| OLED Pin | XIAO Pin |
|-----------|-----------|
| VCC | 3V3 |
| GND | GND |
| SDA | D4 |
| SCL | D5 |

---

## Keymap

| Key | Action |
|------|---------|
|  SW1 | Open Stellarium |
|  SW2 | Open ISS Tracker |
|  SW3 | Play Bruh sound effect |
|  SW4 | Open NASA APOD |

---

## Software

AstroPad works by sending keyboard shortcuts using KMK firmware.

These shortcuts are intercepted on the host computer using AutoHotkey.

### AutoHotkey Bindings

| Shortcut | Action |
|-----------|---------|
| Ctrl + Alt + S | Open Stellarium |
| Ctrl + Alt + I | Open ISS Tracker |
| Ctrl + Alt + B | Play Bruh sound |
| Ctrl + Alt + N | Open NASA APOD |

Example AutoHotkey script:

```ahk
^!s::{
    Run "https://stellarium-web.org/"
}

^!i::{
    Run "https://spotthestation.nasa.gov/"
}

^!n::{
    Run "https://apod.nasa.gov/apod/astropix.html"
}

^!b::{
    SoundPlay "C:\Path\To\bruh.mp3"
}
```

---

## Firmware

AstroPad uses **KMK Firmware** running on CircuitPython.

The firmware is responsible for sending the keyboard shortcuts corresponding to each key.

OLED functionality will be implemented once the hardware arrives.

---

## 3D Printed Case

The enclosure was custom-designed in Fusion 360.

Features include:

- USB access cutout
- Mechanical switch support
- Dedicated OLED mounting area
- Compact footprint
- Space for future upgrades

---

## Project Structure

```
AstroPad/
├── PCB/
│   ├── AstroPad.kicad_sch
│   ├── AstroPad.kicad_pcb
│   └── Gerbers.zip
├── Case/
│   ├── AstroPad.f3d
│   ├── AstroPad.stl
│   └── Plate.dxf
├── Firmware/
│   └── code.py
├── Scripts/
│   └── AstroPad.ahk
└── README.md
```

---

## Future Improvements

- OLED status display
- ISS information display
- Animated graphics
- Multiple layers and modes
- Additional space-themed macros
- Integration with astronomy software APIs

---

## Inspiration

Most macropads focus on productivity.

AstroPad focuses on **space, curiosity, and occasionally pressing a dedicated Bruh button at the worst possible moment**.

---

## Status

```
PCB Design       ██████████ 100%
Case Design      ██████████ 100%
Plate Design     ██████████ 100%
Firmware         ███████░░░ 70%
OLED Features    ██░░░░░░░░ 20%
Sanity           ░░░░░░░░░░ 0%
```

---

Built by **Evyvaan Singh**.

*"The universe is under no obligation to make sense to you."*  
— Neil deGrasse Tyson
