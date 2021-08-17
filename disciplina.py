import tkinter as tk
from tkinter import messagebox

class Disciplina:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

class LimiteConsultaDisciplina(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta disciplina")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameCod.pack()
        self.labelCod = tk.Label(self.frameCod,text="Código disciplina: ")
        self.labelCod.pack(side="left")

        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

      
class CtrlDisciplina():       
    def __init__(self):
        self.listaDisciplinas = [
            Disciplina('COM220', 'Programação OO'),
            Disciplina('COM222', 'Programação Web'),
            Disciplina('COM111', 'Estruturas de Dados')
        ]

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def getCodigo2(self):
        for disc in self.listaDisciplinas:
            return disc.getCodigo()

    def insereDisciplinas(self):
        self.limiteIns = LimiteInsereDisciplinas(self) 

    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
        self.limiteLista = LimiteMostraDisciplinas(str)

    def consultaDisciplinas(self):
        self.limiteIns = LimiteConsultaDisciplina(self)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        disciplina = Disciplina(nroMatric, nome)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def consultaHandler(self, event):
        codDisciplina = self.limiteIns.inputCod.get()
        confirma = 0

        for disc in self.listaDisciplinas:
            if codDisciplina == disc.getCodigo():
                str = 'Código. -- Nome\n'
                str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n' 
                self.limiteLista = LimiteMostraDisciplinas(str)
                confirma = 1
            
        if confirma == 0:
            self.limiteIns.mostraJanela('Erro', 'Disciplina não cadastrada no sistema')

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    