# Supplement Tracker Application
 
# Supplement Tracker

Supplement Tracker is a Python-based GUI application that helps users manage their supplement protocols. Built using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

## Features

- **Add Supplements:**  
  Input supplement details such as name, dosage, measurement unit, and frequency.
  
- **View Supplements:**  
  Displays the current supplement protocol in a scrollable table-like view.
  
- **Delete Supplements:**  
  Remove supplements via a delete checkbox in the view screen.
  
- **Data Persistence:**  
  Stores data locally in a JSON file (saved in a hidden folder in AppData on Windows) for session-to-session persistence.
  
- **Responsive GUI:**  
  Utilizes CustomTkinter to provide a modern, dark-themed interface with responsive layout elements.

## Requirements

- Python 3.8 – 3.13
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Built-in libraries: `json`, `os`
