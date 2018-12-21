#!/bin/sh
{

python3 gifplay.py & 
python3 Det.py  &
python3 id.py &
python3 motor.py &
python3 move.py  
}
python3 cleanu.py
python3 cleanup.py