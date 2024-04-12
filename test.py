import tkinter as tk

products = ["A","B","C","D"]

operation = [["aX","aY"],
             ["bX","bY"],
             ["cX","cY"],
             ["dX","dY"]]

room =[[["axP","axQ"], ["ayP","ayQ"]],
       [["bxP","bxQ"], ["byP","byQ"]],
       [["cxP","cxQ"], ["cyP","cyQ"]],
       [["dxP","dxQ"], ["dyP","dyQ"]]]

root = tk.Tk()
canvas = tk.Canvas(root, height=1000, width= 1000, bg="white")
canvas.pack()

tkvar = tk.StringVar(root)
tkvar.set('Product')

tkvar2 = tk.StringVar(root)
tkvar2.set('Operation')

tkvar3 = tk.StringVar(root)
tkvar3.set('Room')

def on_product_change(product):
    print("Chosen product", product)

    i = products.index(product)

    # update popupMenu2
    menu = popupMenu2['menu']
    menu.delete(0, 'end')
    for op in operation[i]:
        menu.add_command(label=op, command=tk._setit(tkvar2, op, on_operation_change))
    tkvar2.set('Operation')

    # clear popupMenu3
    popupMenu3['menu'].delete(0, 'end')
    tkvar3.set('Room')

def on_operation_change(op):
    print("Chosen operation", op)

    i = products.index(tkvar.get())
    j = operation[i].index(op)

    # update popupMenu3
    menu = popupMenu3['menu']
    menu.delete(0, 'end')
    for item in room[i][j]:
        menu.add_command(label=item, command=tk._setit(tkvar3, item, on_room_change))
    tkvar3.set('Room')

def on_room_change(room):
    print("Chosen room", room)

exit_button = Button(root, text="Exit", command=root.destroy) 
exit_button.pack(pady=20) 

popupMenu1 = tk.OptionMenu(canvas, tkvar, *products, command=on_product_change)
popupMenu1.pack()

popupMenu2 = tk.OptionMenu(canvas, tkvar2, [])
popupMenu2.pack()

popupMenu3 = tk.OptionMenu(canvas, tkvar3, [])
popupMenu3.pack()

root.mainloop()