import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
import subprocess
import os
import socket
import sys
import ipaddress

def scanFunc():
    ip = a1.get()
    start = b1.get()
    end = c1.get()

    if ip == "":
        var = tk.messagebox.showinfo("Port Scanner", "Enter valid to IP")
        return

    elif start == "":
        var = tk.messagebox.showinfo("Port Scanner", "Enter valid Start Port")
        return

    elif end == "":
        var = tk.messagebox.showinfo("Port Scanner", "Enter valid End Port")
        return

    #ip = ipaddress.ip_address(ip)
    start = int(start)
    end = int(end)

    #print(ip,start,end)

    try:
        textData = ""
        for port in range(start,end+1):  
            #print(port,"   ",ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            #print(port,result)
            if result == 0:
                print(port," is OPEN")
                textData = str(port) + " is OPEN" + "\n"
                content.insert(tk.INSERT, textData)
            sock.close()
        print("Done")
    
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')

    except socket.error:
        print("Couldn't connect to server")




window = tk.Tk()
window.title("Welcome to Port Scanner")
window.geometry("600x450")
window.configure(background="grey")

a = tk.Label(window, text="IP: ").grid(row=0, column=0)
b = tk.Label(window, text="Start Port: ").grid(row=1, column=0)
c = tk.Label(window, text="End Port: ").grid(row=2, column=0)

a1 = tk.Entry(window, width="51")
a1.grid(row=0, column=1)
b1 = tk.Entry(window, width="51")
b1.grid(row=1, column=1)
c1=tk.Entry(window, width="51")
c1.grid(row=2, column=1)

tk.Button(
    window, text="Scan", highlightbackground="#3E4149", command=scanFunc
).place(relx=0.5, rely=0.30, anchor=tk.CENTER)


content = ScrolledText(window, width=45, height=15, selectborderwidth=2)
content.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.mainloop()