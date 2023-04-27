#importar as bibliotecas
from cProfile import label
from email import message
from email.mime import image
from pydoc import text
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from turtle import title, width
import database

#Criar nova janela
jan = Tk()
jan.title("DP Systems - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap("icons/LogoIcon.ico")


#.....Carregando as imagens....
logo = PhotoImage(file="icons/logo.png")


#...........Widgets.............
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=80)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=80)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=92)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=120)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=132)

def Login():

    #Pegando os Valores
    User = UserEntry.get()
    Password = PassEntry.get()

    database.cursor.execute("""
        SELECT * FROM Users
        WHERE (user = ? AND pass = ?)
    """, (User, Password))
    print("Selecionou")

    VerifyLogin = database.cursor.fetchone()
    try:
        if (User in VerifyLogin and Password in VerifyLogin):
            messagebox.showinfo(title="Access Info", message="Acesso confirmado. Bem-vindo(a)!")
    except:
        messagebox.showinfo(title="Access Info", message="Acesso negado. Usuário ou senha inválidos! Verifique se está cadastrado no sistema.")

#Botões
LoginButton = ttk.Button(RightFrame,text="Login", width=30, command=Login)
LoginButton.place(x=75, y=225)

def Register():
    #Remove os widgets do login
    LoginButton.place(x=601)
    RegisterButton.place(x=601)

    #Insere os widgets do registro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=37)
    NomeEntry.place(x=110, y=17)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=42)

    EmailEntry = ttk.Entry(RightFrame, width=37)
    EmailEntry.place(x=110, y=54)

    def RegisterToDataBase():
        #Pegando os Valores
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")
        else:
            database.cursor.execute("""
                INSERT INTO Users (name, email, user, pass) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            database.conn.commit()
            messagebox.showinfo(title="Register Info", message="Account created successfully")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=75, y=225)

    def BackToLogin():
        #Remove os widgets de Registro
        NomeLabel.place(x=601)
        NomeEntry.place(x=601)
        EmailLabel.place(x=601)
        EmailEntry.place(x=601)
        Register.place(x=601)
        Back.place(x=601)

        #Insere os widgets de Login
        LoginButton.place(x=75, y=225)
        RegisterButton.place(x=105, y=255)

    Back = ttk.Button(RightFrame, text="Login", width=20, command=BackToLogin)
    Back.place(x=105, y=255)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=105, y=255)


jan.mainloop()
