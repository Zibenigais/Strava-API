import requests
import urllib3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def on_select1(selection):
    print("Dropdown 1 selected:", selection)

def on_select2(selection):
    print("Dropdown 2 selected:", selection)

def on_select3(selection):
    print("Dropdown 3 selected:", selection)


def apstiprinat():
    root.destroy()

def toggle_menu(menu, options, selected_option, on_select_func):
    menu.delete(0, tk.END)
    for item in options:
        menu.add_command(label=item, command=lambda value=item: [selected_option.set(value), on_select_func(value)])
    menu.tk_popup(root.winfo_pointerx(), root.winfo_pointery())

root = tk.Tk()
root.title("Three Dropdowns")

    # Define options for the dropdowns
options1 = ["Skriesana", "Ritenbrauksana"]
options2 = ["Ilgums", "Distance", "Kapuma metri"]
options3 = ["7 dienas", "30 dienas", "90 dienas"]

    # Create variables to store selected values
sports = tk.StringVar(root)
veids = tk.StringVar(root)
periods = tk.StringVar(root)

    # Set default values for the dropdowns
sports.set(options1[0])
veids.set(options2[0])
periods.set(options3[0])

    # Create style
style = ttk.Style()
style.theme_use("clam")

    # Create big title label
big_title_label = tk.Label(root, text="Kādus datus vēlaties iegūt?", font=("Arial", 16, "bold"))

    # Create small title labels
title_label1 = tk.Label(root, text="Sporta veids", font=("Arial", 12))
title_label2 = tk.Label(root, text="Datu tips", font=("Arial", 12))
title_label3 = tk.Label(root, text="Laika periods", font=("Arial", 12))

    # Create dropdowns
menu1 = tk.Menu(root, tearoff=0)
menu2 = tk.Menu(root, tearoff=0)
menu3 = tk.Menu(root, tearoff=0)

dropdown1 = tk.OptionMenu(root, sports, *options1)
dropdown2 = tk.OptionMenu(root, veids, *options2)
dropdown3 = tk.OptionMenu(root, periods, *options3)

dropdown1["menu"] = menu1
dropdown2["menu"] = menu2
dropdown3["menu"] = menu3

    # Bind events to dropdowns to handle selection behavior
dropdown1.bind("<Button-1>", lambda event: toggle_menu(menu1, options1, sports, on_select1))
dropdown2.bind("<Button-1>", lambda event: toggle_menu(menu2, options2, veids, on_select2))
dropdown3.bind("<Button-1>", lambda event: toggle_menu(menu3, options3, periods, on_select3))

    # Create confirm button
apstiprinat_poga = tk.Button(root, text="Apstiprināt", command=apstiprinat)

    # Pack the labels, dropdowns, and confirm button
big_title_label.pack(pady=10)
title_label1.pack()
dropdown1.pack(pady=5)
title_label2.pack()
dropdown2.pack(pady=5)
title_label3.pack()
dropdown3.pack(pady=5)
apstiprinat_poga.pack(pady=10)

root.mainloop()


auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "86521",
    'client_secret': 'a6778e8cc680cd6b7094c87a85ab1dfc69e80604',
    'refresh_token': '72f9e696ea3e96237ad452093aa9aa07e79fb9e3',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n") 
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

request_page_num = 1
all_activities = []

while True:
    param = {'per_page': 200, 'page': request_page_num}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    if len(my_dataset) == 0:
        print("breaking")
        break
    
    if all_activities:
        print("pievieno")
        all_activities.extend(my_dataset)
    else:
        print("jauns")
        all_activities = my_dataset
    
    request_page_num += 1
print(len(all_activities))


atbilstosas = []
laika_periods = periods.get()
sporta_veids = sports.get()


if laika_periods.startswith('7'):
    aktivitates_beigas = datetime.today() - timedelta(days=7)

elif laika_periods.startswith('30'):
    aktivitates_beigas = datetime.today() - timedelta(days=30)
    
else:
    aktivitates_beigas = datetime.today() - timedelta(days=90)


for k in all_activities:
    datums, parejais = k["start_date_local"].split("T")
    gads, menesis, diena = map(int, datums.split("-"))
    aktivitates_datums = datetime(gads, menesis, diena)
    if aktivitates_datums > aktivitates_beigas:
        if sporta_veids.startswith('S'):
            if k['type'] == "Run":
                atbilstosas.append(k)
            else:
                pass
        else:
            if k['type'] == "Ride":
                atbilstosas.append(k)
            else:
                pass


if veids.get().startswith("I"):
    kopejais = 0
    for k in atbilstosas:
        kopejais += k["moving_time"]

elif veids.get().startswith("D"):
    kopejais = 0
    for k in atbilstosas:
        kopejais += k["distance"]
    kopejais = round(kopejais / 1000, 2)

else:
    kopejais = 0
    for k in atbilstosas:
        kopejais += k["total_elevation_gain"]


def pazinojums():
    def show_message_and_exit():
        if sporta_veids.startswith('S'):
            if veids.get().startswith("I"): 
                zina = f"Izvēlētajā laika periodā tu esi skrējis {timedelta(seconds=kopejais)}!"
            elif veids.get().startswith("D"):
                zina = f"Izvēlētajā laika periodā tu esi noskrējis {kopejais} kilometrus!"
            else:
                zina = f"Izvēlētajā laikā tu esi pieveicis {round(kopejais)} kāpuma metrus!"

        else:
            if veids.get().startswith("I"): 
                zina = f"Izvēlētajā laika periodā tu esi braucis {timedelta(seconds=kopejais)}"
            elif veids.get().startswith("D"):
                zina = f"Izvēlētajā laika periodā tu esi nobraucis {kopejais} kilometrus!"
            else:
                zina = f"Izvēlētajā laikā tu esi pieveicis {round(kopejais)} kāpuma metrus!"

        messagebox.showinfo("Apkopojums", zina)
        root.destroy()  # Close the Tkinter window and exit the program

    # Create the main Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window (optional)

    # Show the messagebox
    show_message_and_exit()

# Run the Tkinter event loop
    root.mainloop()
pazinojums()


