import customtkinter as ctk 
from filler_tracker import get_filler_episodes, get_filler_percentage, format_name

def search(): 
    """
        Search function that executes when the search button is pressed.
        Receives user input from entry then uses functions from filler_tracker.py
        to display all info.
    """
    anime_name = entry.get()
    url = f'https://www.animefillerlist.com/shows/{format_name(anime_name)}'

    try: 
        episodes = get_filler_episodes(anime_name, url)
        percentage = get_filler_percentage(anime_name, url)

        # Configure heading and output labels
        heading_label.configure(text=f"ALL FILLER EPISODES FOR {anime_name.upper()}")
        output_label.configure(text=f"{episodes}\n{percentage}")

    except: 
        heading_label.configure(text="ERROR")
        output_label.configure(text=f"Show {anime_name} not found. Please try a different name.")

# Setup 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x550")
root.title("Anime Filler Tracker")
root.iconbitmap("assets/app_icon.ico")

# Frame
frame = ctk.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Title Label 
title_label = ctk.CTkLabel(master=frame, text="Anime Filler Tracker", font=("Roboto", 20, "bold"))
title_label.pack(pady=12, padx=10)

# Entry
entry = ctk.CTkEntry(master=frame, placeholder_text="Enter anime")
entry.pack(pady=12, padx=10)

# Button
button = ctk.CTkButton(master=frame, text="Search", command=search)
button.pack(pady=12, padx=10)

# Output Labels
heading_label = ctk.CTkLabel(master=frame, text="", font=("Roboto", 18), anchor="center", justify="center")
heading_label.pack(pady=12, padx=10)

output_label = ctk.CTkLabel(master=frame, text="", font=("Roboto", 14), anchor="center", justify="left")
output_label.pack(pady=12, padx=10)

root.mainloop()