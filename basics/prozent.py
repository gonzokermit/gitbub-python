import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry("400x600")
root.configure(background="#a32cc4")
root.title("Prozent Rechner")

def reset_entries():
    entry_g.delete(0,"end")
    entry_p.delete(0,"end")
    label_ergebnis_prozentWert["text"] = ""
    label_ergebnis_gesamtWert["text"] = ""

#Funktion ohne TKINTER
#def prozentWert():
#
#    g = float(input("Grundwert: "))
#    p = float(input("Prozentsatz: "))
#
#    pw = p * g / 100
#    gesamtWert = g + pw
#
#    print("{} % von {} sind {}".format(p,g,(round(pw,2))))
#    print("{} + {} sind {}".format(g,(round(pw,2)),(round(gesamtWert,2))))

def prozentWert():
    try:
        g = float(entry_g.get())
        p = float(entry_p.get())
        
        pw = p * g / 100
        gesamtWert = g + pw

        label_ergebnis_prozentWert["text"] = "{} % von {} sind {}".format(p,g,(round(pw,2)))
        label_ergebnis_gesamtWert["text"] = "{} + {} sind {}".format(g,(round(pw,2)),(round(gesamtWert,2)))
    except ValueError:
        tkinter.messagebox.showerror(root, message="Not a valid number!")

# Create GUI
# label widget Ueberschrift
label_header = tkinter.Label(root, text="Prozent Rechner", bg="#a32cc4", fg="#ffffff",
                             font=("arial",25,"bold"))
label_header.pack(pady=15)

# label widget Ueberschrift Grundwert -> g
label_g = tkinter.Label(root, text="Grundwert", bg="#a32cc4", fg="#ffffff", 
                        font=("arial",15,"bold"))
label_g.pack(pady=15)

# entry text widget Eingabe Grundwert -> g
entry_g = tkinter.Entry(root, justify="center", font=("arial",17,"bold"))
entry_g.pack()

# label widget Ueberschrift Prozentsatz -> p
label_p = tkinter.Label(root, text="Prozentsatz", bg="#a32cc4", fg="#ffffff",
                        font=("arial",15,"bold"))
label_p.pack(pady=15)

# entry text widget Eingabe Prozentsatz -> p
entry_p = tkinter.Entry(root, justify="center", font=("arial",17,"bold"))
entry_p.pack()

# button widget berechnen
button_berechnen = tkinter.Button(root, text="Berechnen", bg="#ff0157", fg="#ffffff",
                                  font=("arial",10,"bold"), command=prozentWert)
button_berechnen.pack(pady=15)
 
# button widget reset_entries
button_reset_entries = tkinter.Button(root, text="Eingabe loeschen", bg="#ff0157", fg="#ffffff",
                                      font=("arial",10,"bold"), command=reset_entries)
button_reset_entries.pack(pady=10)

#button widget closeWindow
button_closeWindow = tkinter.Button(root, text="Programm beenden", bg="#ff0157", fg="#ffffff",
                                    font=("arial",10,"bold"), command=root.destroy)
button_closeWindow.pack(pady=15)

# label widget Ergebnis Prozentwert -> pw
label_ergebnis_prozentWert = tkinter.Label(root, text="Ergebnis", bg="#a32cc4", fg="#ffffff",
                                           font=("arial",17,"bold"))
label_ergebnis_prozentWert.pack(pady=15)

# label widget Ergebnis Neuer Gesamtwert -> neuerWert
label_ergebnis_gesamtWert = tkinter.Label(root, text="Gesamtwert", bg="#a32cc4", fg="#ffffff",
                                          font=("arial",17,"bold"))
label_ergebnis_gesamtWert.pack(pady=10)

root.mainloop()