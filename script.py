# This section of code was created to understand core functionality through the console.
# The function "full_supplement_tracker()" when called, manages everything from a GUI perspective.
import json
def supplement_tracker():
    choice1 = False
    choice2 = False
    choice3 = False
    choice4 = False

    # open up the file if exists
    try:
        with open("supplements.json", "r") as f:
            current_supplements = json.load(f)
    # define dictionary if file doesn't exist yet
    except:
        current_supplements = {}

    while True:
        with open("supplements.json", "w") as f:
            json.dump(current_supplements, f)
        print("""
    ===== SUPPLEMENT TRACKER =====
    1) Add a new supplement
    2) View all supplements
    3) Search for a supplement
    4) Delete a supplement
    5) Exit
    """)
        choice = input("Enter your choice: ")

        if choice == "1":
            choice1 = True
        if choice == "2":
            choice2 = True
        if choice == "3":
            choice3 = True
        if choice == "4":
            choice4 = True

        # Saving user data/exiting application
        if choice == "5":
            print("Saving results...")
            print("Exiting program...")
            print("See you next time!")
            break

        # Adding supplements
        while choice1:
                supplement_choice = input("Type the supplement name: ").title()
                dosage = input("Enter dosage: ")
                unit = input("Enter measurement unit: ")
                frequency = input("Enter frequency (times per day): ")
                current_supplements[supplement_choice] = ["", ""]
                current_supplements[supplement_choice][0] = dosage + unit
                current_supplements[supplement_choice][1] = frequency + " time(s)/day"

                print(f"{supplement_choice} ({current_supplements[supplement_choice][0]}, {current_supplements[supplement_choice][1]}) has been added to your tracker.")

                continue_clause = input("Do you want to continue adding supplements? Type 'y'/'n'")

                if continue_clause == "y":
                    continue
                else:
                    choice1 = False

        # Viewing supplements
        while choice2:
            if not bool(current_supplements):
                print("You have no supplements! Add a supplement to get started")
                choice2 = False
            for key, value in current_supplements.items():
                print(f"{key}, {value[0]}, {value[1]}")
                choice2 = False

        # searching through supplements
        while choice3:
            user_input = input("Enter your search term: ").lower()
            matches_count = 0
            found_any = False

            for key, value in current_supplements.items():
                if user_input in key:
                    matches_count += 1
                    print(f"Match {matches_count}: {key} => {value}")
                    found_any = True

            if not found_any:
                print("Could not find any match.")

            choice3 = False

        # Deleting supplements
        while choice4:
            user_input = input("Enter the name of the supplement to delete: ").title()
            if user_input not in current_supplements:
                print("Supplement could not be found.")
                choice4 = False
            if user_input in current_supplements:
                del current_supplements[user_input]
                print(f"{user_input} has been removed from your protocol.")
                choice4 = False

def full_supplement_tracker():
    import customtkinter as ctk
    import json
    import os

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()

    # Defining location to store the JSON file in a less visible folder for application
    appdata_dir = os.environ.get("APPDATA")  # For Windows
    data_dir = os.path.join(appdata_dir, "SupplementTracker")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    json_file_path = os.path.join(data_dir, "supplement_list2.json")

    # Loading supplement list from JSON or initialize as empty list if doesnt exist.
    try:
        with open(json_file_path, "r") as f:
            supplement_list = json.load(f)
        if not isinstance(supplement_list, list):
            supplement_list = []
    except FileNotFoundError:
        supplement_list = []

    # Global variable for view frame.
    global view_frame
    view_frame = None

    # Defining refresh function to rebuild the view
    def refresh_view():
        global view_frame
        if view_frame is not None:
            view_frame.destroy()
        view_supplements()

    # Defining delete function for a single supplement
    def delete_supplement(index):
        try:
            del supplement_list[index]
        except IndexError:
            print("Invalid index for deletion")
            return
        with open(json_file_path, "w") as f:
            json.dump(supplement_list, f)
        refresh_view()
        print(f"Supplement at index {index} deleted.")

    # DEFINING THE SCREENS
    def add_supplement():
        add_frame = ctk.CTkFrame(root, width=800, height=800)
        add_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        def exit_add_frame():
            add_frame.destroy()

        # ENTERING NAME
        enter_name_label = ctk.CTkLabel(add_frame, text="Enter the supplement name: ", font=("Roboto", 20))
        enter_name_label.place(relx=0.5, y=50, anchor="center")
        textbox_enter_name = ctk.CTkTextbox(add_frame, height=1, width=300, font=("Roboto", 25))
        textbox_enter_name.place(relx=0.5, y=100, anchor="center")

        # ENTERING DOSAGE
        dosage_label = ctk.CTkLabel(add_frame, text="Enter the dosage: ", font=("Roboto", 20))
        dosage_label.place(relx=0.5, y=200, anchor="center")
        textbox_enter_dosage = ctk.CTkTextbox(add_frame, height=1, width=300, font=("Roboto", 25))
        textbox_enter_dosage.place(relx=0.5, y=250, anchor="center")

        # ENTERING MEASUREMENT UNIT
        unit_label = ctk.CTkLabel(add_frame, text="Enter the measurement unit: ", font=("Roboto", 20))
        unit_label.place(relx=0.5, y=350, anchor="center")
        textbox_enter_unit = ctk.CTkTextbox(add_frame, height=1, width=300, font=("Roboto", 25))
        textbox_enter_unit.place(relx=0.5, y=400, anchor="center")

        # ENTERING FREQUENCY
        freq_label = ctk.CTkLabel(add_frame, text="Enter frequency (times per day): ", font=("Roboto", 20))
        freq_label.place(relx=0.5, y=500, anchor="center")
        textbox_enter_freq = ctk.CTkTextbox(add_frame, height=1, width=300, font=("Roboto", 25))
        textbox_enter_freq.place(relx=0.5, y=550, anchor="center")

        # COLLECTING THE INPUTTED DATA
        def collect_data():
            name = textbox_enter_name.get("1.0", "end-1c")
            dosage = textbox_enter_dosage.get("1.0", "end-1c")
            unit = textbox_enter_unit.get("1.0", "end-1c")
            freq = textbox_enter_freq.get("1.0", "end-1c")

            data = {
                "name": name,
                "dosage": dosage,
                "unit": unit,
                "freq": freq
            }
            supplement_list.append(data)
            print("Supplement added:", data)

            with open(json_file_path, "w") as f:
                json.dump(supplement_list, f)

            add_frame.destroy()
            refresh_view()  # Refreshing the view with updated data.

        add_button = ctk.CTkButton(master=add_frame, text="Add Supplement", font=("Roboto", 20), command=collect_data)
        add_button.place(relx=0.5, y=650, anchor="center")

        exit_button = ctk.CTkButton(master=add_frame, text="← GO BACK", font=("Roboto", 20), command=exit_add_frame)
        exit_button.place(x=0, y=0)

    def exit_app():
        print("exit app button was clicked!")
        root.destroy()

    def view_supplements():
        global view_frame
        view_frame = ctk.CTkFrame(root, width=800, height=700, corner_radius=20)
        view_frame.place(x=250, y=50)

        # Creating scrollable container
        scroll_frame = ctk.CTkScrollableFrame(view_frame, width=850, height=700)
        scroll_frame.pack(pady=20, fill="both", expand=True)

        # Creating header row (using grid layout)
        headers = ["Name", "Dosage", "Unit", "Frequency", "Delete"]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(scroll_frame, text=header, font=("Roboto", 20))
            header_label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
            scroll_frame.grid_columnconfigure(col, weight=1, minsize=150)

        # Populating each row with supplement data
        for row, supplement in enumerate(supplement_list, start=1):
            name_label = ctk.CTkLabel(scroll_frame, text=supplement["name"], font=("Roboto", 20))
            name_label.grid(row=row, column=0, padx=10, pady=5)

            dosage_label = ctk.CTkLabel(scroll_frame, text=supplement["dosage"], font=("Roboto", 20))
            dosage_label.grid(row=row, column=1, padx=10, pady=5)

            unit_label = ctk.CTkLabel(scroll_frame, text=supplement["unit"], font=("Roboto", 20))
            unit_label.grid(row=row, column=2, padx=10, pady=5)

            freq_label = ctk.CTkLabel(scroll_frame, text=supplement["freq"], font=("Roboto", 20))
            freq_label.grid(row=row, column=3, padx=10, pady=5)

            # Delete checkbox for this row
            # using lambda to capture the correct index.
            delete_box = ctk.CTkCheckBox(scroll_frame, text="Delete", command=lambda idx=row-1: delete_supplement(idx), font=("Roboto", 20))
            delete_box.grid(row=row, column=4, padx=10, pady=5)

    def main():
        root.title("Supplement Tracker")
        root.geometry("800x800")
        root.minsize(1150, 850)
        root.maxsize(1150, 850)

        protocol_label = ctk.CTkLabel(root, text="Current Protocol:", font=("Roboto", 20))
        protocol_label.place(relx=0.525, rely=0.02)

        header_label = ctk.CTkLabel(root, text="Supplement Tracker", font=("Roboto", 25))
        header_label.place(x=125, rely=0.1, anchor="center")

        add_supplement_button = ctk.CTkButton(root, text="Add Supplements", font=("Roboto", 20), command=add_supplement)
        add_supplement_button.place(x=125, rely=0.2, anchor="center")

        exit_button = ctk.CTkButton(root, text="Exit App", font=("Roboto", 20), command=exit_app)
        exit_button.place(x=125, rely=0.3, anchor="center")

        # Building the initial view with current data.
        refresh_view()

    main()
    root.mainloop()

full_supplement_tracker()

