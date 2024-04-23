import requests
import urllib3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import sqlite3
import warnings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Tiek paziņots lietotājam, kura opcija ir tika izvēlēta uzlēcošajā logā.
def on_select1(izvele):
    print("Pirmaja izkritosaja saraksta izvelejas:", izvele)

def on_select2(izvele):
    print("Otraja izkritosaja saraksta izvelejas:", izvele)

def on_select3(izvele):
    print("Tresaja izkritosaja saraksta izvelejas:", izvele)

    # Izveidotas pogas funkcionalitātes uzlēcošajā logā, t.i. gan izvēles pogas, gan "Apstiprināt" poga.
def apstiprinat():
    root.destroy()

def toggle_menu(menu, options, selected_option, on_select_func):
    menu.delete(0, tk.END)
    for item in options:
        menu.add_command(label=item, command=lambda value=item: [selected_option.set(value), on_select_func(value)])
    menu.tk_popup(root.winfo_pointerx(), root.winfo_pointery())

    # Tiek izveidots uzlēcošais logs, kurš lietotājam paziņo par iegūto rezultātu.

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
root = tk.Tk()

root.title("Izvēlies datus")

    # Izveidotas opcijas izkrītošajiem sarakstiem
sporti = ["Skriesana", "Ritenbrauksana"]
veidi = ["Ilgums", "Distance", "Kapuma metri"]
periodi = ["7 dienas", "30 dienas", "90 dienas"]

    # Mainīgie, kas glabā izvēletos rezultāatus
sports = tk.StringVar(root)
veids = tk.StringVar(root)
periods = tk.StringVar(root)

    # Iestādīti mainīgie, lai gadījumā, ja lietotājs nemaina izvēli tā būtu uz pirmās opcijas
sports.set(sporti[0])
veids.set(veidi[0])
periods.set(periodi[0])

style = ttk.Style()
style.theme_use("clam")

lielais_nosaukums = tk.Label(root, text="Kādus datus vēlaties iegūt?", font=("Arial", 16, "bold"))

pirma_nosaukums = tk.Label(root, text="Sporta veids", font=("Arial", 12))
otra_nosaukums = tk.Label(root, text="Datu tips", font=("Arial", 12))
tresa_nosaukums = tk.Label(root, text="Laika periods", font=("Arial", 12))

    # Izveidoju izkrītošos sarakstus
menu1 = tk.Menu(root, tearoff=0)
menu2 = tk.Menu(root, tearoff=0)
menu3 = tk.Menu(root, tearoff=0)

dropdown1 = tk.OptionMenu(root, sports, *sporti)
dropdown2 = tk.OptionMenu(root, veids, *veidi)
dropdown3 = tk.OptionMenu(root, periods, *periodi)

dropdown1["menu"] = menu1
dropdown2["menu"] = menu2
dropdown3["menu"] = menu3

    # Katram sarakstam piesaistu pogu, ar funkcionalitāti
dropdown1.bind("<Button-1>", lambda event: toggle_menu(menu1, sporti, sports, on_select1))
dropdown2.bind("<Button-1>", lambda event: toggle_menu(menu2, veidi, veids, on_select2))
dropdown3.bind("<Button-1>", lambda event: toggle_menu(menu3, periodi, periods, on_select3))

apstiprinat_poga = tk.Button(root, text="Apstiprināt", command=apstiprinat)

    # Pack-oju visus objektus
lielais_nosaukums.pack(pady=10)
pirma_nosaukums.pack()
dropdown1.pack(pady=5)
otra_nosaukums.pack()
dropdown2.pack(pady=5)
tresa_nosaukums.pack()
dropdown3.pack(pady=5)
apstiprinat_poga.pack(pady=10)

root.mainloop()


auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

klienta_informacija = {
    'client_id': "86521",
    'client_secret': 'a6778e8cc680cd6b7094c87a85ab1dfc69e80604',
    'refresh_token': '72f9e696ea3e96237ad452093aa9aa07e79fb9e3',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Iegustu piekluves atslegu...\n") 
res = requests.post(auth_url, data=klienta_informacija, verify=False)
access_token = res.json()['access_token']
print("Piekluves atslega = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

request_page_num = 1
visas_aktivitates = []

    # Par cik vienā API pieprasījumā var iegūt 200 aktvitātes, veidoju ciklu, kas iegūs visas aktivitātes
while True:
    param = {'per_page': 200, 'page': request_page_num}
    patreizejais = requests.get(activites_url, headers=header, params=param).json()
    if len(patreizejais) == 0:
        print("Nav vairak aktivitates")
        break
    
    if visas_aktivitates:
        print("Pievieno esosajam")
        visas_aktivitates.extend(patreizejais)
    else:
        print("Jauns bloks")
        visas_aktivitates = patreizejais
    
    request_page_num += 1


atbilstosas = []
laika_periods = periods.get()
sporta_veids = sports.get()

    # Iegūstu nepieciešamo datumu, balstoties uz laika izkrītošā saraksta izvēlēto

if laika_periods.startswith('7'):
    aktivitates_beigas = datetime.today() - timedelta(days=7)

elif laika_periods.startswith('30'):
    aktivitates_beigas = datetime.today() - timedelta(days=30)
    
else:
    aktivitates_beigas = datetime.today() - timedelta(days=90)

    # Tiek izveidots jauns saraksts, ar aktivitātēm, kuras atbilst izvēlētajam laika periodam un sporta veidam

for k in visas_aktivitates:
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

    # Tiek izveidots mainīgais "kopejais", kurā būs skaitliska vērtība, kas ir balstīta uz datu veida izvēli izkrītošajā sarakstā

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

pazinojums()
    # Datubāzes
def create_main_database():
    conn = sqlite3.connect("lietotaja_atskaite.db")
    cursor = conn.cursor()

    # Create the main table to store user data
    cursor.execute('''CREATE TABLE IF NOT EXISTS lietotaja_dati (
                        id INTEGER PRIMARY KEY,
                        palaisanas_laiks TIMESTAMP,
                        sporta_veids TEXT
                    )''')

    conn.commit()
    conn.close()

# Izveidoju sekundāro datubāzi
def create_additional_database():
    conn = sqlite3.connect("rezultati.db")
    cursor = conn.cursor()

    # Create the additional table to store more user data
    cursor.execute('''CREATE TABLE IF NOT EXISTS rezultati (
                        id INTEGER PRIMARY KEY,
                        lietotaja_id INTEGER,
                        rezultats TEXT,
                        FOREIGN KEY(lietotaja_id) REFERENCES lietotaja_dati(id)
                    )''')

    conn.commit()
    conn.close()

# Funckija, kas ievieto datus galvenajā datubāzē

def insert_data_main(db_name, palaisanas_laiks, mainigais):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO lietotaja_dati (palaisanas_laiks, sporta_veids) VALUES (?, ?)''', (palaisanas_laiks, mainigais))
    
    # Iegūstu user_id, lai varētu to izmantot kā savienoto atslēgu starp datubāzēm
    user_id = cursor.lastrowid

    conn.commit()
    conn.close()
    
    return user_id

# Funkcija, kas ievieto datus sekundārajā datubāzē
def insert_data_additional(db_name, user_id, rezultats):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Insert additional user data into the additional table
    cursor.execute('''INSERT INTO rezultati (lietotaja_id, rezultats) VALUES (?, ?)''', (user_id, rezultats))

    conn.commit()
    conn.close()

create_main_database()
create_additional_database()

# Dati galvenajai datubāzei
laiks = datetime.today()

if sporta_veids.startswith('S'):
    sportaveids = "Skriešana"
else:
    sportaveids = "Riteņbraukšana"

lietotaja_dati = insert_data_main("lietotaja_atskaite.db", laiks, sportaveids)

# Dati sekundārajai datubāzei

insert_data_additional("rezultati.db", lietotaja_dati, round(kopejais))
