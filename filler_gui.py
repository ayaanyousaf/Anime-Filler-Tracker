import customtkinter as ctk 
from PIL import Image
from filler_tracker import get_filler_episodes, get_filler_percentage, find_url

def search(): 
    anime_name = entry.get()

    # Clear previous results
    heading_label.configure(text='')
    output_label.configure(text='')

    try: 
        url, matched_name = find_url(anime_name)
        episodes = get_filler_episodes(matched_name, url)
        percentage = get_filler_percentage(matched_name, url)

        # Configure heading and output labels
        heading_label.configure(text=f"All Filler Episodes for: {matched_name}", 
                    font=ctk.CTkFont(family='Viner Hand ITC', weight='bold', size=20))
        output_label.configure(text=f"{episodes}\n{percentage}",
                    font=ctk.CTkFont(family='Roboto', weight='bold', slant='italic', size=14))

    except Exception as e: 
        heading_label.configure(text="ERROR", font=('Roboto', 14))

        print(str(e))
        
        if "Invalid URL" in str(e): 
            error = f"Show {anime_name} not found. Please try a different name."
        elif "output" in str(e): 
            error = "Unable to retrieve filler episodes."
        elif "percentage" in str(e): 
            error = "Unable to retrieve filler percentage."
        else: 
            error = "Unknown Error"
        
        output_label.configure(text=error, font=('Roboto', 12))

# Function to bind enter key to search button 
def search_bind(pressed):
    search()

# Window Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x650")
root.title("Anime Filler Tracker")
root.iconbitmap("assets/icon.ico")

# Scrollable Frame
frame = ctk.CTkScrollableFrame(master=root, scrollbar_button_color='white', scrollbar_button_hover_color='grey')
frame.pack(padx=(10, 10), pady=(15, 15), fill="both", expand=True)

# Logo
logo_img = ctk.CTkImage(dark_image=Image.open('assets/logo.png'), size=(300, 300))
logo_label = ctk.CTkLabel(master=frame, text="", image=logo_img)
logo_label.pack(padx=30)

# Search Bar
entry = ctk.CTkEntry(master=frame, placeholder_text="Enter an anime", width=270)
entry.pack(padx=10)
entry.bind("<Return>", search_bind) # binds Enter key to search function

# Search Button
button = ctk.CTkButton(master=frame, 
                    text="Search", 
                    font=('Roboto', 14), 
                    command=search,
                    fg_color='white', 
                    text_color='black', 
                    hover_color='grey')
button.pack(padx=10, pady=10)

# Output Labels
heading_label = ctk.CTkLabel(master=frame, 
                    text="", 
                    anchor="center", 
                    justify="center", 
                    wraplength=600)
heading_label.pack(padx=6, pady=10)

output_label = ctk.CTkLabel(master=frame, 
                    text="", 
                    anchor="center", 
                    justify="left", 
                    wraplength=700)
output_label.pack(pady=10)

root.mainloop()