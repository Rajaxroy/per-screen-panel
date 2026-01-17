#!/bin/bash
source .venv/bin/activate
python tracker/window_tracker.py &
python panel/panel.py
