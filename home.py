import time
import pyautogui
from dataclasses import dataclass
from typing import Union, List

@dataclass
class Note:
    key: Union[str, int, List[str]]
    delay: float  # Delay after this key is pressed
    press: float = 0.01  # Duration to hold down the key

    def play(self):
        # Handle single keys
        if isinstance(self.key, int) or isinstance(self.key, str):
            pyautogui.keyDown(str(self.key))
            time.sleep(self.press)
            pyautogui.keyUp(str(self.key))
        # Handle simultaneous keys
        elif isinstance(self.key, list):
            for k in self.key:
                pyautogui.keyDown(k)
            time.sleep(self.press)
            for k in self.key:
                pyautogui.keyUp(k)
        # Apply delay after pressing
        time.sleep(self.delay)

# Define delays and durations
PRESS = 0.01
DELAY = 0.05
EXTRA_DELAY = 0.12

# Create sequence of Notes
sequences = [
    [Note(1, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(2, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("Y", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(3, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY),
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY), 
     Note("E", DELAY), Note("R", DELAY), Note("Y", DELAY), Note(" ", EXTRA_DELAY)],
    
    [Note(1, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(2, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(4, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("Y", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(7, DELAY), Note("Y", DELAY), Note("T", DELAY), Note("R", DELAY), Note(" ", EXTRA_DELAY), Note("W", DELAY), 
     Note("E", DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY)],
    
    [Note(1, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(2, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(3, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY),
     Note(" ", EXTRA_DELAY), Note("Y", DELAY), Note("T", DELAY), Note("R", DELAY), Note("W", DELAY), Note("E", DELAY), 
     Note("R", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(6, DELAY), Note(["W", "T"], DELAY), Note(" ", EXTRA_DELAY), Note("Y", DELAY), Note("E", DELAY), 
     Note("R", DELAY), Note(" ", EXTRA_DELAY)],
    
    [Note(1, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY),
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("Y", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(2, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("Y", DELAY),
     Note(" ", EXTRA_DELAY)],
    [Note(5, DELAY), Note("T", DELAY), Note("R", DELAY), Note("E", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(3, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY),
     Note(" ", EXTRA_DELAY), Note("E", DELAY), Note("R", DELAY), Note("T", DELAY), Note(" ", EXTRA_DELAY)],
    [Note(6, DELAY), Note("W", DELAY), Note(" ", EXTRA_DELAY), Note("R", DELAY), Note("T", DELAY), 
     Note(["E", "R", "Y"], DELAY)]
]

def press_sequence(sequences):
    for sequence in sequences:
        for note in sequence:
            note.play()

if __name__ == '__main__':
    # Execute the sequences with a countdown
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    
    press_sequence(sequences)
