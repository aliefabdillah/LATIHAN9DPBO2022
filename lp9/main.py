from re import I
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 30, 900, "s/d Desember 2022"))
hunians.append(Rumah("Gustavo Fring", 5, 2, 210, 1300, "Permanent"))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 10, 900, "s/d Oktober 2022", "320428", "12-02-2001", "Laki-Laki", "Guru"))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 120, 1300, "Permanent"))

# Tkinter Declaration
root = Tk()
root.title("Latihan Praktikum DPBO - 2003623 ; Alief Muhammad Abdillah")

def details(index):
    # frame Detail
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # frame data residen
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # display data 
    d_pemilik = Label(d_frame, text="Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=1, column=0, sticky="w")
    if hunians[index].get_jenis() != "Indekos":
        d_jmlh_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=2, column=0, sticky="w")
    d_document = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=3, column=0, sticky="w")
    d_luasBangunan = Label(d_frame, text="LuasBangunan: " + hunians[index].get_luasBangunan(), anchor="w").grid(row=4, column=0, sticky="w")
    d_listrik = Label(d_frame, text="Kapasitas Listrik: " + hunians[index].get_listrik(), anchor="w").grid(row=5, column=0, sticky="w")
    d_status = Label(d_frame, text="Status: " + hunians[index].get_status(), anchor="w").grid(row=6, column=0, sticky="w")

    # frame penghuni kos
    if hunians[index].get_jenis() == "Indekos":
        d_penghuni = Label(d_frame, text="\nDATA PENGHUNI\n---------------------\n" + hunians[index].getDataPenghuni(), justify= LEFT).grid(row=7, column=0, sticky="w")



    # back to main page function
    def back():
        top.destroy()

    # frame for button
    opts_detail = LabelFrame(top, padx=10, pady=10)
    opts_detail.pack(padx=10, pady=10)

    # back button
    button_back = Button (opts_detail, text = "Back", command = back, activebackground="blue")
    button_back.grid(row=0, column=0)

    # exit button 
    button_exit = Button(opts_detail, text="Exit", command=root.quit, activebackground="red")
    button_exit.grid(row=0, column=1)

# Main Frame    
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# button Frame
opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

#button add
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)
# Button exit
b_exit = Button(opts, text="Exit", command=root.quit, activebackground="red")
b_exit.grid(row=0, column=1)

# display Data
for index, h in enumerate(hunians):
    # column number
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # column jenis hunian
    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # column nama pemilik/penghuni hunian
    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # detail button
    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
