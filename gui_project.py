import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk() # dia bikin objek namanya window
window.configure(bg='white') #.configure(something) , configure itu kalo di kelas2 bilangnya ' method' buat ubah sesuatu
window.geometry("400x400")
window.resizable(False,False) # gaiso diubah2 x dan y nya
window.title("Hitung Price Bond")


# buat frame input
input_frame = ttk.Frame(window)
#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen-komponen
#1. label face value
Face_Value = ttk.Label(input_frame,text="Nilai Face Value")
Face_Value.pack(padx=10,fill="x",expand=True)
# entry guyss 
F_string = tk.StringVar()
Face_Value_entry = ttk.Entry(input_frame,textvariable=F_string) # F ini nangkap nilai yang ditulis user
Face_Value_entry.pack(padx=10,fill="x",expand=True)

#2. label yield rate
yield_rate = ttk.Label(input_frame,text="Persentase Yield Rate")
yield_rate.pack(padx=10,fill="x",expand=True)
# entry guyss 
i_string = tk.StringVar()
yield_rate_entry = ttk.Entry(input_frame,textvariable=i_string) 
yield_rate_entry.pack(padx=10,fill="x",expand=True)

#3. label coupon rate
coupon_rate = ttk.Label(input_frame,text="Persentase coupon rate")
coupon_rate.pack(padx=10,fill="x",expand=True)
# entry guyss 
r_string = tk.StringVar()
coupon_rate_entry = ttk.Entry(input_frame,textvariable=r_string) 
coupon_rate_entry.pack(padx=10,fill="x",expand=True)

#4. label redemption value
redemption_value = ttk.Label(input_frame,text="Nilai Redemption Value")
redemption_value.pack(padx=10,fill="x",expand=True)
# entry guyss 
C_string = tk.StringVar()
redemption_value_entry = ttk.Entry(input_frame,textvariable=C_string) 
redemption_value_entry.pack(padx=10,fill="x",expand=True)

#5. label tahun
brp_tahun = ttk.Label(input_frame,text="Berapa Tahun")
brp_tahun.pack(padx=10,fill="x",expand=True)
# entry guyss 
t_string = tk.StringVar()
brp_tahun_entry = ttk.Entry(input_frame,textvariable=t_string) 
brp_tahun_entry.pack(padx=10,fill="x",expand=True)

# 6. tombol buat pilih frekuensi pembayaran pakai radiobutton  ( ben iso pilih salah satu aja)
freq_val = tk.IntVar(value=1) # pakek default annually aj yeahh

ttk.Radiobutton(input_frame, text="Annually", variable=freq_val, value=1).pack(side="top",anchor="w")
ttk.Radiobutton(input_frame, text="Semiannually", variable=freq_val, value=2).pack(side="top",anchor="w")
ttk.Radiobutton(input_frame, text="Quarterly", variable=freq_val, value=4).pack(side="top",anchor="w")
ttk.Radiobutton(input_frame, text="Monthly", variable=freq_val, value=12).pack(side="top",anchor="w")

#function tombol click
def tombol_click():
    try:
        # karena di awal pakenya stringvar,jadiya string, ubah ke float dulu
        F = float(F_string.get())
        i_nominal = float(i_string.get())/100
        r_nominal = float(r_string.get())/100
        t = float(t_string.get())
        C = float(C_string.get())
        m = freq_val.get()

        #penyesuaian i , r dan n
        n = t * m
        i = i_nominal / m
        r = r_nominal/m

        #hitung diskonto (v)
        v = 1/(1+i)

        # hitung anuitas
        a = (1 - (v**n))/i

        P = F*r*a + C*(v**n) # rumus price bond
        hasil = f"harga bond dengan face value {F} adalah ${P:.2f}"
        messagebox.showinfo("Hasil Perhitungan", hasil)

    except ValueError:
        # Muncul kalo user input huruf atau ada kotak yang kosong
        messagebox.showerror("Error Input", "Pastikan semua kolom diisi dengan angka!")
    
    except ZeroDivisionError:
        # Jaga-jaga kalau user isi Yield Rate pake angka 0
        messagebox.showerror("Error Matematika", "Yield rate tidak boleh 0!")

tombol_hitung = ttk.Button(input_frame,text="Hitung!",command=tombol_click)
tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)


window.mainloop()