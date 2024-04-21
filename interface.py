from tkinter import *
import tkinter as tk
from models.pessoa import Pessoa
from models.recibo import Recibo

class ReciboApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gerador de Recibo")
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.texto_nome_recibo = Label(self, text="Digite o nome do recibo")
        self.local_nome_recibo = Entry(self)
        self.valor_recibo = Label(self, text="Valor do recibo")
        self.local_valor_recibo = Entry(self)
        self.nome_cliente = Label(self, text="Cliente")
        self.local_nome_cliente = Entry(self)
        self.documento_cliente = Label(self, text="CPF/CNPJ")
        self.local_documento_cliente = Entry(self)
        self.nome_emitente = Label(self, text="Emitente")
        self.local_nome_emitente = Entry(self)
        self.documento_emitente = Label(self, text="CPF/CNPJ")
        self.local_documento_emitente = Entry(self)
        self.referencia_recibo = Label(self, text="Referência do recibo")
        self.local_referencia_recibo = Text(self, height=5, width=30)
        self.data_recibo = Label(self, text="Data do recibo")
        self.local_data_recibo = Entry(self)
        self.cidade_recibo = Label(self, text="Cidade")
        self.local_cidade_recibo = Entry(self)
        self.estado_recibo = Label(self, text="Estado")
        self.local_estado_recibo = Entry(self)
        self.botao_gerar_recibo = Button(self, text="Gerar recibo", command=self.gerar_recibo)

        self.texto_nome_recibo.grid(column=0, row=0)  # da para referenciar o excel nisso aqui
        self.local_nome_recibo.grid(column=1, row=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.valor_recibo.grid(column=0, row=1)
        self.local_valor_recibo.grid(column=1, row=1, padx=5, pady=5, columnspan=2, sticky="ew")
        self.nome_cliente.grid(column=0, row=2, columnspan=2, sticky='ew')
        self.local_nome_cliente.grid(column=0, row=3, padx=5, pady=5, columnspan=2, sticky='ew')
        self.documento_cliente.grid(column=2, row=2, columnspan=2, sticky='ew')
        self.local_documento_cliente.grid(column=2, row=3, padx=5, pady=5, columnspan=2, sticky='ew')
        self.nome_emitente.grid(column=0, row=4, columnspan=2, sticky='ew')
        self.local_nome_emitente.grid(column=0, row=5, padx=5, pady=5, columnspan=2, sticky='ew')
        self.documento_emitente.grid(column=2, row=4, columnspan=2, sticky='ew')
        self.local_documento_emitente.grid(column=2, row=5, padx=5, pady=5, columnspan=2, sticky='ew')
        self.referencia_recibo.grid(column=0, row=6, columnspan=3, sticky='ew')
        self.local_referencia_recibo.grid(column=0, row=7, columnspan=3, padx=5, pady=5, sticky='ew')
        self.data_recibo.grid(column=0, row=8)
        self.local_data_recibo.grid(column=0, row=9, padx=(10, 10), pady=5, sticky='ew')
        self.cidade_recibo.grid(column=1, row=8)
        self.local_cidade_recibo.grid(column=1, row=9, padx=(10, 10), pady=5)
        self.estado_recibo.grid(column=2, row=8)
        self.local_estado_recibo.grid(column=2, row=9, padx=(10, 10), pady=5)
        self.botao_gerar_recibo.grid(column=0, row=10, padx=5, pady=5, columnspan=3, sticky='ew')


    def gerar_recibo(self):
        try:
            user_nome_recibo = self.local_nome_recibo.get()
            user_valor_recibo_str = self.local_valor_recibo.get()
            if user_valor_recibo_str.strip() == "":
                raise(ValueError("Erro ao inserir valor de recibo"))

            user_valor_recibo = float(user_valor_recibo_str)
            user_nome_cliente = self.local_nome_cliente.get()
            user_documento_cliente = self.local_documento_cliente.get()
            user_nome_emitente = self.local_nome_emitente.get()
            user_documento_emitente = self.local_documento_emitente.get()
            user_referencia_recibo = self.local_referencia_recibo.get("1.0", "end-1c")
            user_cidade_recibo = self.local_cidade_recibo.get()
            user_estado_recibo = self.local_estado_recibo.get()
            user_data_recibo = self.local_data_recibo.get()

            pagador = Pessoa(user_nome_cliente, user_documento_cliente)
            recebedor = Pessoa(user_nome_emitente, user_documento_emitente)

            recibo = Recibo(pagador, recebedor, user_nome_recibo, user_valor_recibo, user_referencia_recibo, user_data_recibo, user_cidade_recibo, user_estado_recibo)

            recibo.criar_recibo()
        except ValueError as e:
            print(f"Erro: {e}")
