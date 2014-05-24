
from Tkinter import *
from ampel import Ampel

import thread

class ClientUI:

    def __init__(self):
        self.ampel = Ampel('rot')
        self.fenster = Tk()
        self.fenster.geometry("600x200")
        #master.configure(background='red')
        self.userlabel=Label(self.fenster, text="User")
        self.userlabel.grid(row=0)
        self.user = Entry(self.fenster, width=70)
        self.user.grid(row=0, column=1)



        self.pwdlabel = Label(self.fenster, text="Password")
        self.pwdlabel.grid(row=1)
        self.pwd = Entry(self.fenster, width=70)
        self.pwd.grid(row=1, column=1)
        # Rahmen
        self.frameAmpel = Frame(master=self.fenster, background='darkgray')
        self.frameAmpel.place(x=500, y=20, width=40, height=100)
        # Label Rot-Licht
        self.labelRot = Label(master=self.frameAmpel, background='gray')
        self.labelRot.place(x=10, y=10, width=20, height=20)
        # Gelb-Licht
        self.labelGelb = Label(master=self.frameAmpel, background='gray')
        self.labelGelb.place(x=10, y=40, width=20, height=20)
        # Gruen-Licht
        self.labelGruen = Label(master=self.frameAmpel, background='gray')
        self.labelGruen.place(x=10, y=70, width=20, height=20)
        # Aktualisierung der Anzeige
        (lampeRot, lampeGelb, lampeGruen) = self.ampel.getLampen()
        self.anzeigeAktualisieren(lampeRot, lampeGelb, lampeGruen)
        self.buttonQuit = Button(self.fenster, text='Quit', command=self.fenster.quit)
        self.buttonQuit.grid(row=2, column=0, sticky=W, pady=1)
        self.buttonNext = Button(self.fenster, text='Next', command=self.Next)
        self.buttonNext.grid(row=2, column=1, sticky=W, pady=1)

        self.fenster.mainloop()



    def Next(self):
        #TODO:Abfrage ob man auf Schritt 2 zugreifen darf
        Label(self.fenster, text="Code").grid(row=0)
        self.buttonNext.destroy()


        eText = StringVar()
        self.code=Entry(self.fenster, state="readonly", textvariable=eText, width="70")
        self.code.grid(row=0, column=1)
        eText.set("...waiting for second password...")
        self.secondPW = Label(self.fenster, text="2. Password")
        self.secondPW.grid(row=1)
        self.secondPWEntry = Entry(self.fenster, width="70")
        self.secondPWEntry.grid(row=1, column=1)
        self.anzeigeAktualisieren(False, True, False)
        self.buttonLogin = Button(self.fenster, text='Send', command=self.Login)
        self.buttonLogin.grid(row=2, column=1, sticky=W, pady=1)
        self.userlabel.destroy()
        self.user.destroy()
        self.pwd.destroy()
        self.pwdlabel.destroy()


    def Login(self):
        #TODO:Abfrage, ob man eingeloggt ist
        self.anzeigeAktualisieren(False,False,True)


    def anzeigeAktualisieren(self,lampeRot, lampeGelb, lampeGruen):
        if lampeRot:
            self.labelRot.config(background='red')
        else:
            self.labelRot.config(background='gray')
        if lampeGelb:
            self.labelGelb.config(background='yellow')
        else:
            self.labelGelb.config(background='gray')
        if lampeGruen:
            self.labelGruen.config(background='green')
        else:
            self.labelGruen.config(background='gray')

clientUI = ClientUI()