import json
import time
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

def notificar(titulo, mensagem):

    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(titulo, mensagem)

    root.destroy()


def carregar_nfs():
    with open("banco.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def verificar_nfs():

    nfs = carregar_nfs()
    hoje = datetime.today()
    mes_atual = hoje.strftime("%Y-%m")

    for nf in nfs:

        empresa = nf["empresa"]
        descricao = nf["descricao"]
        dia_vencimento = nf["dia_vencimento"]
        ultimo_lancamento = nf.get("ultimo_lancamento")

        vencimento = datetime(hoje.year, hoje.month, dia_vencimento)

        alerta_15 = vencimento - timedelta(days=15)

        ultimo_dia = vencimento.replace(day=1) - timedelta(days=1)

        print("Empresa:", empresa)
        print("Vencimento:", vencimento)
        print("Alerta 15 dias:", alerta_15)
        print("Último dia:", ultimo_dia)
        print("-------------")

        if ultimo_lancamento != mes_atual:

            if hoje.date() == alerta_15.date():

                notificar(
                    "NF pode ser lançada",
                    f"A NF de {descricao} ({empresa}) já pode ser lançada."
                )

            if hoje.date() == ultimo_dia.date():

                notificar(
                    "Último dia para lançar",
                    f"Hoje é o último dia para lançar {descricao}."
                )


print("Sistema rodando...")

while True:

    verificar_nfs()

    time.sleep(43200)
