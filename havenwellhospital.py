import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
class Patient:
    def __init__(self, patient_id, name, age, phone, medical_issue):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone
        self.medical_issue = medical_issue

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.appointments = []

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, time, medical_issue):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.time = time
        self.medical_issue = medical_issue

class HospitalSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Patient Scheduling System")

        # Load and display background image
        self.bg_image = Image.open("/Users/tejaswinitalla/Documents/projects/havenwell.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas = tk.Canvas(self.root, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # Data
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.appointment_counter = 1

        self.available_times = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30",
                                "2:00", "2:30", "3:00", "3:30", "4:00", "4:30"]

        self.issue_mapping = {
            "heart": "Cardiology", "chest pain": "Cardiology", "cardiac": "Cardiology",
            "child": "Pediatrics", "baby": "Pediatrics", "kids": "Pediatrics",
            "fever": "General Medicine", "cold": "General Medicine", "headache": "General Medicine",
            "bone": "Orthopedics", "fracture": "Orthopedics", "joint": "Orthopedics",
            "skin": "Dermatology", "rash": "Dermatology", "acne": "Dermatology"
        }

        doctors_data = [
            ("D001", "Dr. Smith", "Cardiology"),
            ("D002", "Dr. Johnson", "Pediatrics"),
            ("D003", "Dr. Brown", "General Medicine"),
            ("D004", "Dr. Davis", "Orthopedics"),
            ("D005", "Dr. Wilson", "Dermatology")
        ]

        for doctor_id, name, specialization in doctors_data:
            self.doctors[doctor_id] = Doctor(doctor_id, name, specialization)

        self.create_main_menu()

    def create_main_menu(self):
        widgets = [
            tk.Label(self.root, text="Hospital Patient Scheduling System", font=("Helvetica", 16, "bold"), bg="white"),
            tk.Button(self.root, text="Register New Patient", width=30, command=self.register_patient),
            tk.Button(self.root, text="View Available Specializations", width=30, command=self.view_specializations),
            tk.Button(self.root, text="View Today's Schedule", width=30, command=self.view_schedule),
            tk.Button(self.root, text="Search Patient", width=30, command=self.search_patient),
            tk.Button(self.root, text="Exit", width=30, command=self.root.quit),
        ]

        y_position = 40
        for widget in widgets:
            self.canvas.create_window(400, y_position, window=widget)
            y_position += 50

    def register_patient(self):
        patient_window = tk.Toplevel(self.root)
        patient_window.title("Register New Patient")

        fields = ["Name", "Age", "Phone"]
        entries = {}

        for idx, field in enumerate(fields):
            tk.Label(patient_window, text=field).grid(row=idx, column=0, padx=10, pady=5, sticky='e')
            entry = tk.Entry(patient_window)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entries[field] = entry

        # Medical Issue dropdown
        tk.Label(patient_window, text="Medical Issue").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        issue_var = tk.StringVar()
        issue_dropdown = ttk.Combobox(patient_window, textvariable=issue_var, state="readonly")
        issue_dropdown['values'] = sorted(set(self.issue_mapping.keys()))
        issue_dropdown.grid(row=3, column=1, padx=10, pady=5)

        def submit():
            name = entries["Name"].get().strip()
            age = entries["Age"].get().strip()
            phone = entries["Phone"].get().strip()
            medical_issue = issue_var.get().strip()

            if not name or not age.isdigit() or not (1 <= int(age) <= 149):
                messagebox.showerror("Invalid Input", "Please enter valid name and age (1-149).")
                return
            if not medical_issue:
                messagebox.showerror("Invalid Input", "Please select a medical issue.")
                return

            patient_id = f"P{len(self.patients) + 1:03d}"
            patient = Patient(patient_id, name, int(age), phone, medical_issue)
            self.patients[patient_id] = patient

            doctor = self.assign_doctor(medical_issue)
            time_slot = self.get_next_available_slot(doctor)

            if not time_slot:
                messagebox.showinfo("No Slot", "No available time slots today.")
                return

            appointment_id = f"APT{self.appointment_counter:03d}"
            self.appointment_counter += 1

            appointment = Appointment(appointment_id, patient_id, doctor.doctor_id, time_slot, medical_issue)
            self.appointments[appointment_id] = appointment
            doctor.appointments.append(time_slot)

            messagebox.showinfo("Success", f"Appointment Scheduled:\n"
                                           f"Patient: {name}\nDoctor: {doctor.name}\n"
                                           f"Time: {time_slot}\nAppointment ID: {appointment_id}")
            patient_window.destroy()

        tk.Button(patient_window, text="Submit", command=submit).grid(row=4, columnspan=2, pady=10)

    def assign_doctor(self, issue):
        issue = issue.lower()
        for keyword, spec in self.issue_mapping.items():
            if keyword == issue:
                for doctor in self.doctors.values():
                    if doctor.specialization == spec:
                        return doctor
        return next((d for d in self.doctors.values() if d.specialization == "General Medicine"), None)

    def get_next_available_slot(self, doctor):
        for time in self.available_times:
            if time not in doctor.appointments:
                return time
        return None

    def view_specializations(self):
        specs = {}
        for doc in self.doctors.values():
            specs.setdefault(doc.specialization, []).append(doc.name)
        spec_text = "\n".join([f"{spec}: {', '.join(names)}" for spec, names in specs.items()])
        messagebox.showinfo("Specializations", spec_text)

    def view_schedule(self):
        if not self.appointments:
            messagebox.showinfo("Schedule", "No appointments scheduled today.")
            return

        schedule_window = tk.Toplevel(self.root)
        schedule_window.title("Today's Schedule")

        tree = ttk.Treeview(schedule_window, columns=("Time", "Patient", "Doctor", "Issue"), show='headings')
        tree.heading("Time", text="Time")
        tree.heading("Patient", text="Patient")
        tree.heading("Doctor", text="Doctor")
        tree.heading("Issue", text="Medical Issue")

        sorted_appointments = sorted(self.appointments.values(), key=lambda a: a.time)
        for apt in sorted_appointments:
            patient = self.patients[apt.patient_id]
            doctor = self.doctors[apt.doctor_id]
            tree.insert("", tk.END, values=(apt.time, patient.name, doctor.name, apt.medical_issue))

        tree.pack(fill='both', expand=True, padx=10, pady=10)

    def search_patient(self):
        name = simpledialog.askstring("Search", "Enter patient name:")
        if not name:
            return
        name = name.strip().lower()

        results = []
        for patient in self.patients.values():
            if name in patient.name.lower():
                result = f"{patient.name} (ID: {patient.patient_id})"
                appointments = [apt for apt in self.appointments.values() if apt.patient_id == patient.patient_id]
                if appointments:
                    for apt in appointments:
                        doc = self.doctors[apt.doctor_id]
                        result += f"\n  - {apt.time} with Dr. {doc.name}"
                else:
                    result += "\n  - No appointments"
                results.append(result)

        if results:
            messagebox.showinfo("Search Results", "\n\n".join(results))
        else:
            messagebox.showinfo("Not Found", "No patient found with that name.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalSystemGUI(root)
    root.mainloop()
