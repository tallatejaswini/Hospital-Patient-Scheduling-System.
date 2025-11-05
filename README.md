# 🏥 Hospital Patient Scheduling System

A simple and intuitive desktop application for managing hospital patient registrations, doctor appointments, and scheduling. Built with Python and Tkinter for a user-friendly graphical interface.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)

## Overview

The Hospital Patient Scheduling System is a desktop application designed to streamline the patient registration and appointment booking process. The system automatically assigns patients to appropriate doctors based on their medical issues and manages time slot allocation throughout the day.

## Features

### Core Functionality
- **Patient Registration** - Register new patients with complete details
- **Smart Doctor Assignment** - Automatically assigns doctors based on medical issues
- **Appointment Scheduling** - Intelligent time slot management
- **Schedule Viewing** - See all appointments for the day in organized format
- **Patient Search** - Quickly find patient information and their appointments
- **Specialization Directory** - View all available doctors and their specializations

### Smart Features
- Automatic doctor assignment based on medical issue keywords
- Time slot management (prevents double-booking)
- 12 available time slots per day (morning and afternoon)
- Patient ID auto-generation
- Appointment ID tracking
- Medical issue categorization

## Requirements

### Software Requirements
- Python 3.7 or higher
- Tkinter (usually comes with Python)
- PIL/Pillow library

### Hardware Requirements
- Any computer capable of running Python
- Minimum 4GB RAM recommended
- Display resolution: 800x600 or higher

## Installation

### Step 1: Install Python
Make sure Python 3.7+ is installed on your system. Check by running:
```bash
python --version
```

### Step 2: Install Required Libraries
Install the Pillow library for image handling:
```bash
pip install pillow
```

Note: Tkinter comes pre-installed with most Python distributions. If you encounter issues, install it:
- **Windows/Mac**: Already included with Python
- **Linux**: `sudo apt-get install python3-tk`

### Step 3: Download the Project
Clone or download the project files to your computer.

### Step 4: Prepare Background Image (Optional)
The system can use a background image. Update the image path in the code:
```python
self.bg_image = Image.open("your_image_path_here.png")
```
Or remove the background image code if not needed.

### Step 5: Run the Application
```bash
python havenwellhospital.py
```

## Usage Guide

### Starting the Application

When you run the application, you'll see the main menu with five options:

1. Register New Patient
2. View Available Specializations
3. View Today's Schedule
4. Search Patient
5. Exit

### Registering a New Patient

**Step-by-step process:**

1. Click **"Register New Patient"**
2. A new window opens with a registration form
3. Fill in the patient details:
   - **Name**: Enter patient's full name
   - **Age**: Enter age (must be between 1-149)
   - **Phone**: Enter contact number
   - **Medical Issue**: Select from dropdown menu

4. Click **"Submit"**
5. The system will:
   - Generate a unique Patient ID (e.g., P001)
   - Assign an appropriate doctor based on the medical issue
   - Allocate the next available time slot
   - Create an Appointment ID (e.g., APT001)
   - Show confirmation with all details

**Important Notes:**
- Age must be a number between 1 and 149
- You must select a medical issue from the dropdown
- If no time slots are available, you'll receive a notification

### Understanding Medical Issue Categories

The system automatically assigns doctors based on keywords:

**Cardiology** (Heart Specialist)
- Keywords: heart, chest pain, cardiac

**Pediatrics** (Child Specialist)
- Keywords: child, baby, kids

**General Medicine** (General Doctor)
- Keywords: fever, cold, headache
- Also handles unmatched issues

**Orthopedics** (Bone Specialist)
- Keywords: bone, fracture, joint

**Dermatology** (Skin Specialist)
- Keywords: skin, rash, acne

### Viewing Available Specializations

1. Click **"View Available Specializations"**
2. A popup shows all specializations and their doctors
3. Use this to know which doctors are available

**Example Output:**
```
Cardiology: Dr. Smith
Pediatrics: Dr. Johnson
General Medicine: Dr. Brown
Orthopedics: Dr. Davis
Dermatology: Dr. Wilson
```

### Viewing Today's Schedule

1. Click **"View Today's Schedule"**
2. A new window opens with a table showing:
   - Time slot
   - Patient name
   - Doctor name
   - Medical issue
3. Schedule is automatically sorted by time
4. Empty schedule shows "No appointments scheduled today"

### Searching for a Patient

1. Click **"Search Patient"**
2. Enter patient name (partial names work)
3. System shows:
   - Patient name and ID
   - All appointments for that patient
   - Doctor and time for each appointment

**Search Tips:**
- Search is case-insensitive
- Partial names work (searching "john" finds "Johnson")
- Shows all matching patients if multiple exist

## System Architecture

### Classes Overview

**Patient Class**
- Stores patient information
- Properties: patient_id, name, age, phone, medical_issue

**Doctor Class**
- Stores doctor information
- Properties: doctor_id, name, specialization, appointments
- Tracks assigned time slots

**Appointment Class**
- Links patients with doctors
- Properties: appointment_id, patient_id, doctor_id, time, medical_issue

**HospitalSystemGUI Class**
- Main application controller
- Manages all GUI elements
- Handles business logic

### Data Flow

1. **Patient Registration**
   → Create Patient object
   → Assign appropriate doctor based on medical issue
   → Find available time slot
   → Create Appointment object
   → Update doctor's schedule

2. **Viewing Schedule**
   → Retrieve all appointments
   → Sort by time
   → Display in table format

3. **Searching Patient**
   → Search through patient database
   → Find matching appointments
   → Display results

## How It Works

### Time Slot Management

The system has 12 pre-defined time slots:

**Morning Slots:**
- 9:00, 9:30, 10:00, 10:30, 11:00, 11:30

**Afternoon Slots:**
- 2:00, 2:30, 3:00, 3:30, 4:00, 4:30

**How Slots Are Assigned:**
1. When a patient registers, system checks doctor's appointments
2. Finds first available slot from the list
3. Assigns that slot and marks it as taken
4. Next patient gets the next available slot

**Slot Management Rules:**
- Each doctor has their own independent schedule
- No double-booking possible
- Slots are assigned sequentially
- If all slots full, registration is blocked

### Doctor Assignment Logic

The system uses keyword matching:

```
Patient's medical issue → Keywords → Specialization → Assign Doctor
```

**Example:**
- Issue: "heart" → Matches "heart" keyword → Cardiology → Dr. Smith
- Issue: "fever" → Matches "fever" keyword → General Medicine → Dr. Brown
- Issue: "unknown" → No match → Default to General Medicine → Dr. Brown

### Patient ID Generation

Patient IDs are auto-generated in format: **P001, P002, P003...**
- Sequential numbering
- Three-digit padding
- Unique for each patient

### Appointment ID Generation

Appointment IDs follow format: **APT001, APT002, APT003...**
- Sequential numbering
- Three-digit padding
- Tracks total appointments

## Project Structure

```
hospital-system/
│
├── havenwellhospital.py      # Main application file
├── havenwell.png              # Background image (optional)
└── README.md                  # This documentation
```

**Code Organization:**
- **Lines 1-15**: Import statements and Patient class
- **Lines 16-25**: Doctor class definition
- **Lines 26-35**: Appointment class definition
- **Lines 36-300+**: HospitalSystemGUI class (main application)

## Customization

### Adding More Doctors

Add doctors in the `doctors_data` list (around line 55):

```python
doctors_data = [
    ("D001", "Dr. Smith", "Cardiology"),
    ("D002", "Dr. Johnson", "Pediatrics"),
    # Add your new doctor here:
    ("D006", "Dr. Your Name", "Specialization"),
]
```

### Adding New Specializations

1. Add keyword mappings in `issue_mapping` dictionary:
```python
self.issue_mapping = {
    # Existing mappings...
    "new_issue": "New Specialization",
}
```

2. Add a doctor with that specialization in `doctors_data`

### Modifying Time Slots

Change the `available_times` list (around line 48):
```python
self.available_times = ["9:00", "9:30", "10:00", ...]
```

### Changing Window Size

Modify the background image size or canvas dimensions in `__init__` method.

### Removing Background Image

To run without background image:
1. Comment out lines 26-31 (image loading)
2. Use regular frame instead of canvas
3. Update widget placement from `canvas.create_window()` to regular `.pack()` or `.grid()`

## Troubleshooting

### Problem: "No module named 'PIL'"
**Solution:** Install Pillow library
```bash
pip install pillow
```

### Problem: "Cannot open image file"
**Solution:** 
- Check if image path is correct
- Use absolute path or place image in same folder
- Or remove background image functionality

### Problem: "No available time slots"
**Solution:**
- All 12 slots for that doctor are booked
- Either add more time slots in code
- Or add more doctors with same specialization

### Problem: Age validation fails
**Solution:**
- Age must be a number
- Age must be between 1 and 149
- Don't leave age field empty

### Problem: Medical issue dropdown empty
**Solution:**
- Check that `issue_mapping` dictionary is properly defined
- Dropdown populates from dictionary keys

### Problem: Window doesn't appear
**Solution:**
- Check if Tkinter is installed
- Try running from command line to see error messages
- Ensure Python version is 3.7+

### Problem: Search returns no results
**Solution:**
- Search is case-insensitive but checks exact partial matches
- Make sure patient is registered first
- Try searching with just first name

## Future Enhancements

Potential features to add:
- Patient history tracking
- Prescription management
- Bill generation
- Multiple day scheduling
- Doctor availability management
- Emergency appointment handling
- Email/SMS notifications
- Database integration (SQLite/MySQL)
- Appointment cancellation
- Patient medical records
- Doctor notes system

## Technical Notes

**GUI Framework:** Tkinter
- Cross-platform compatibility
- Built-in with Python
- Lightweight and fast

**Data Storage:** In-memory dictionaries
- Current implementation stores data in memory
- Data resets when application closes
- For persistent storage, integrate a database

**Design Pattern:** Object-Oriented Programming
- Separate classes for entities
- Encapsulation of data and methods
- Easy to extend and maintain

## Best Practices for Using This System

1. **Register all doctors first** - Ensure all doctors are added before patient registration
2. **Keep consistent naming** - Use standardized medical issue terms
3. **Regular monitoring** - Check schedule regularly to avoid conflicts
4. **Data backup** - Since data is in-memory, note important appointments
5. **Test thoroughly** - Try different scenarios before real usage

## License

This project is open-source and available for educational purposes. Feel free to modify and extend as needed.

## Support

For issues or questions:
- Review this documentation thoroughly
- Check troubleshooting section
- Ensure all requirements are met
- Verify Python and library versions

## Conclusion

This Hospital Patient Scheduling System provides a solid foundation for managing basic hospital operations. It's designed to be simple, intuitive, and easy to understand for beginners while providing practical functionality for learning purposes.

Perfect for:
- Learning Python GUI programming
- Understanding object-oriented design
- Building healthcare management systems
- Academic projects
- Prototyping scheduling systems

---

**Made with Python & Tkinter** 🐍
