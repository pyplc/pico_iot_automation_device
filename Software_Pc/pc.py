# 720 x 1280 Pixel (309 ppi)

import tkinter as tk
import tkinter.ttk
import socket
import sys
import json

TITLE = "OnOff v0.0"
TITLE_ICO = "..."
TITLE_IMAGE = "title_image.gif"
MAIN_WIN_WIDTH = 720
MAIN_WIN_HEIGHT = 1280

var = {'Q1':'off', 'Q2':'off', 'Q3':'off', 'Q4':'off'}

class MainWindowFrame(object):
    def __init__(self, parent):
        self.parent = parent
        self.tk = tk

        # Taps
        self.note = tkinter.ttk.Notebook(parent.main_win)
        self.tab1 = tkinter.ttk.Frame(self.note)

        self.note.add(self.tab1, text="LED Steuern")

        self.note.grid(row=0, column=1, padx=0, pady=20, sticky="N")

        self.frame = tk.Frame(parent.main_win)
        self.frame.grid(row=0, column=0)

        self.frame2 = tk.Frame(parent.main_win, relief="ridge", borderwidth = 1)
        self.frame2.grid(row=0, column=1, pady=60, sticky="S" )

        # Titelbild & Icon
        # parent.main_win.iconbitmap(TITLE_ICO) # Für Windows
        #self.image = tk.PhotoImage(file="C:\Herbert\Hintergrund\Burg.png")
        #tk.Label(self.frame, image=self.image).pack()

        # Begrüßungstext
        #tk.Label(self.frame, text="...", font="Arial 20").grid()

        #TAP1 ###################################################################################
        # Denn Übung macht den Meister!
        # tk.Label(self.frame, text="Übung macht den Meister!",
        # font="Arial 10").grid()
        self.Anzeige1 = tk.Label(self.tab1, text="...", width=8, font=('Arial', 8))
        self.Anzeige1.grid(row=0)

        # Button Stempeln Tap1

        self.F1_B_on = tk.Button(self.tab1, text="ON",
                           width=15, command= self.parent.send_data_on_f1) #command=self.parent.do)
        self.F1_B_off = tk.Button(self.tab1, text="OFF",
                                    width=15, command= self.parent.send_data_off_f1)  # command=self.parent.do)
        
        self.F1_B_on.grid(row=1)
        self.F1_B_off.grid(row=2)
       

        #TAP2 ###################################################################################
        # Denn Übung macht den Meister!
        # tk.Label(self.frame, text="Übung macht den Meister!",
        # font="Arial 10").grid()
        self.Anzeige2 = tk.Label(self.tab1, text="...", width=8, font=('Arial', 8))
        self.Anzeige2.grid(row=3)

        # Button Stempeln Tap1

        self.F2_B_on = tk.Button(self.tab1, text="ON",
                           width=15, command= self.parent.send_data_on_f2) #command=self.parent.do)
        self.F2_B_off = tk.Button(self.tab1, text="OFF",
                                    width=15, command= self.parent.send_data_off_f2)  # command=self.parent.do)

        self.F2_B_on.grid(row=4)
        self.F2_B_off.grid(row=5)


        #TAP3 ###################################################################################
        # Denn Übung macht den Meister!
        # tk.Label(self.frame, text="Übung macht den Meister!",
        # font="Arial 10").grid()
        self.Anzeige3 = tk.Label(self.tab1, text="...", width=8, font=('Arial', 8))
        self.Anzeige3.grid(row=6)

        # Button Stempeln Tap1

        self.F3_B_on = tk.Button(self.tab1, text="ON",
                           width=15, command= self.parent.send_data_on_f3) #command=self.parent.do)
        self.F3_B_off = tk.Button(self.tab1, text="OFF",
                                    width=15, command= self.parent.send_data_off_f3)  # command=self.parent.do)

        self.F3_B_on.grid(row=7)
        self.F3_B_off.grid(row=8)
 

        #TAP4 ###################################################################################
        # Denn Übung macht den Meister!
        # tk.Label(self.frame, text="Übung macht den Meister!",
        # font="Arial 10").grid()
        self.Anzeige4 = tk.Label(self.tab1, text="...", width=8, font=('Arial', 8))
        self.Anzeige4.grid(row=9)

        # Button Stempeln Tap1

        self.F4_B_on = tk.Button(self.tab1, text="ON",
                           width=15, command= self.parent.send_data_on_f4) #command=self.parent.do)
        self.F4_B_off = tk.Button(self.tab1, text="OFF",
                                    width=15, command= self.parent.send_data_off_f4)  # command=self.parent.do)

        self.F4_B_on.grid(row=10)
        self.F4_B_off.grid(row=11)



class Application(object):
    def __init__(self, main_win, title):
        self.main_win = main_win
        main_win.title(title)

        # Schliessung des Hauptfensters übder das 'x'-Symbol in der Titelleiste
        main_win.protocol("WM_DELETE_WINDOW", self.close_app)
        # Erstelle die Geometriedaten für ein zentriertes Hauptfenster
        geometry = self.center_win(main_win, MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT)
        # Zentrier das Hauptfenster
        #self.main_win.geometry("{}x{}+{}+{}".format(*geometry))
        self.main_win.geometry("220x450")
        # Erstelle den Inhalt des Hauptfensters
        self.main_window_frame = MainWindowFrame(self) # ertselle Objekt
        # Variablen für Zeichnen

        # Create a TCP/IP socket
        self.sock = socket.create_connection(('10.0.0.100', 10000))  # 'espressif' oder 'localhost'

    def center_win(self, window, width, height):
        xpos = int((window.winfo_screenwidth() - width) / 2)
        ypos = int((window.winfo_screenheight() - height) / 2)
        return width, height, xpos, ypos

    def close_app(self):
        # Here do something before apps shutdown
        print("Good Bye! ")
        print('closing socket')
        self.sock.close()
        self.main_win.withdraw()
        self.main_win.destroy()

    def send_data_on_f1(self):
        # Create a TCP/IP socket
        #self.sock = socket.create_connection(('10.0.0.100', 10000))  # 'espressif' oder 'localhost'
        try:
            # Send data
            global var
            var['Q1'] = 'on'
            str_json = json.dumps(var)
            #message = b'R1_on'
            message = bytes(str_json, 'utf-8')
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            # Anzeige was gestepelt wurde löschen
            self.main_window_frame.Anzeige1.config(text='R1 on')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(100)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('socket open')
            #self.sock.close()

    def send_data_on_f2(self):
        try:
            # Send data
            global var
            var['Q2'] = 'on'
            str_json = json.dumps(var)
            #message = b'R1_on'
            message = bytes(str_json, 'utf-8')
            #message = b'R2_on'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            # Anzeige was gestepelt wurde löschen
            self.main_window_frame.Anzeige2.config(text='R2 on')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('socket open')
            #sock.close()

    def send_data_on_f3(self):
        try:
            # Send data
            message = b'R3_on'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            # Anzeige was gestepelt wurde löschen
            self.main_window_frame.Anzeige3.config(text='R3 on')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('socket open')
            # sock.close()

    def send_data_on_f4(self):
        try:
            # Send data
            message = b'R4_on'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            # Anzeige was gestepelt wurde löschen
            self.main_window_frame.Anzeige4.config(text='R4 on')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('socket open')
            # sock.close()



    def send_data_off_f1(self):
        try:
            # Send data
            global var
            var['Q1'] = 'off'
            str_json = json.dumps(var)
            #message = b'R1_on'
            message = bytes(str_json, 'utf-8')
            #message = b'R1_off'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            self.main_window_frame.Anzeige1.config(text='R1 off')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('socket open')
            #sock.close()

    def send_data_off_f2(self):
        try:
            # Send data
            global var
            var['Q2'] = 'off'
            str_json = json.dumps(var)
            #message = b'R1_on'
            message = bytes(str_json, 'utf-8')
            #message = b'R1_off'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            self.main_window_frame.Anzeige2.config(text='R2 off')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('socket open')
            #sock.close()

    def send_data_off_f3(self):
        try:
            # Send data
            message = b'R3_off'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            self.main_window_frame.Anzeige3.config(text='R3 off')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('socket open')
            #sock.close()


    def send_data_off_f4(self):
        try:
            # Send data
            message = b'R4_off'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)
            self.main_window_frame.Anzeige4.config(text='R4 off')
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('socket open')
            #sock.close()


def main():
    main_win = tk.Tk()
    app = Application(main_win, TITLE)
    main_win.mainloop()

main()
