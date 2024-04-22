import tkinter as tk
from tkinter import ttk
def sportaveidsgui():

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
    options1 = ["Option 1", "Option 2", "Option 3"]
    options2 = ["Option A", "Option B", "Option C"]
    options3 = ["Choice 1", "Choice 2", "Choice 3"]

    # Create variables to store selected values
    selected_option1 = tk.StringVar(root)
    selected_option2 = tk.StringVar(root)
    selected_option3 = tk.StringVar(root)

    # Set default values for the dropdowns
    selected_option1.set(options1[0])
    selected_option2.set(options2[0])
    selected_option3.set(options3[0])

    # Create style
    style = ttk.Style()
    style.theme_use("clam")

    # Create big title label
    big_title_label = tk.Label(root, text="Three Dropdowns", font=("Arial", 16, "bold"))

    # Create small title labels
    title_label1 = tk.Label(root, text="Dropdown 1", font=("Arial", 12))
    title_label2 = tk.Label(root, text="Dropdown 2", font=("Arial", 12))
    title_label3 = tk.Label(root, text="Dropdown 3", font=("Arial", 12))

    # Create dropdowns
    menu1 = tk.Menu(root, tearoff=0)
    menu2 = tk.Menu(root, tearoff=0)
    menu3 = tk.Menu(root, tearoff=0)

    dropdown1 = tk.OptionMenu(root, selected_option1, *options1)
    dropdown2 = tk.OptionMenu(root, selected_option2, *options2)
    dropdown3 = tk.OptionMenu(root, selected_option3, *options3)

    dropdown1["menu"] = menu1
    dropdown2["menu"] = menu2
    dropdown3["menu"] = menu3

    # Bind events to dropdowns to handle selection behavior
    dropdown1.bind("<Button-1>", lambda event: toggle_menu(menu1, options1, selected_option1))
    dropdown2.bind("<Button-1>", lambda event: toggle_menu(menu2, options2, selected_option2))
    dropdown3.bind("<Button-1>", lambda event: toggle_menu(menu3, options3, selected_option3))

    # Create confirm button
    apstiprinat_poga = tk.Button(root, text="Confirm", command=apstiprinat)

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
sportaveidsgui()