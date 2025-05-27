# Kivy Application Demos

This directory contains simple demo applications built using the Kivy Python framework. These examples are intended to showcase basic Kivy functionality and app structure.

## Kivy Installation

To run these demos, you need to have Kivy installed in your Python environment.

### Quick Installation (pip)

Kivy and its core dependencies can be installed using pip:

```bash
pip install kivy
```

Or, to include optional dependencies for features like audio/video and different window backends, you can install `kivy[full]`:

```bash
pip install kivy[full]
```

This was the method used to set up the environment for these demos.

### Comprehensive Installation Guide

For more detailed and platform-specific installation instructions, including troubleshooting and setup for different operating systems, please refer to the official Kivy installation guide:
[https://kivy.org/doc/stable/gettingstarted/installation.html](https://kivy.org/doc/stable/gettingstarted/installation.html)

## Running the Demos

Once Kivy is installed, you can run the demo applications from your terminal. Navigate to this `kivy` directory.

### 1. Hello World App

This is a minimal Kivy application that displays a "Hello, World!" message.

To run it:
```bash
python hello_world.py
```

### 2. Counter App

This application features a label displaying a number and two buttons to increment or decrement that number.

To run it:
```bash
python counter_app.py
```

## Environment Note

Please be aware that Kivy applications are graphical applications that require a desktop environment with graphics support (e.g., X11, Wayland on Linux; Aqua on macOS; standard Desktop on Windows). 

These applications may not run directly in all cloud-based IDEs, headless server environments, or minimalist container setups if a suitable graphical environment is not available or properly configured. If you encounter issues, ensure you are running them in an environment that supports GUI applications.
