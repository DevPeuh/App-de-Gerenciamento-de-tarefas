import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


class AppListaTarefa:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title('Aplicativo de Lista de tarefas')
        self.raiz.geometry('500x400')

        self.tarefas = []

        #estilo
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Helvetica', 20, 'bold'), foreground='#333')
        self.style.configure('TButton', font=('Helvetica', 10), padding=5)
        self.style.configure('TEntry', font=('Helvetica', 10), padding=5)

        #header
        cabecalho = ttk.Frame(raiz)
        cabecalho.pack(pady=10)

        cabecalho_rotulo = ttk.Label(cabecalho, text='Lista de afazeres', style='Header.TLabel')
        cabecalho_rotulo.pack()

        #entrada
        quadro_tarefa = ttk.Frame(raiz)
        quadro_tarefa.pack(pady=10)

        self.entrada_de_tarefa = ttk.Entry(quadro_tarefa, width=40)
        self.entrada_de_tarefa.grid(row=0, column=0, padx=5, pady=5)

        opcoes_prioridade = ['baixo', 'Médio', 'alto']
        self.prioridade_var = tk.StringVar(raiz)
        self.prioridade_var.set(opcoes_prioridade[0])

        self.menu = ttk.OptionMenu(quadro_tarefa, self.prioridade_var, *opcoes_prioridade)
        self.menu.grid(row=0, column=2, padx=5, pady=5)

        self.entrada_data_vencimento = ttk.Entry(quadro_tarefa, width=15)
        self.entrada_data_vencimento.grid(row=0, column=3, padx=5, pady=5)
        self.entrada_data_vencimento.insert(0, datetime.now().strftime('%d-%m-%Y'))

        add_botao = ttk.Button(quadro_tarefa, text="Adicionar Tarefa", command=self.AdicionarTarefa)
        add_botao.grid(row=0, column=4, padx=5, pady=5)

        # Lista tarefas
        self.caixa_de_tarefas = tk.Listbox(raiz, width=60, height=15, font=('Helvetica', 10))
        self.caixa_de_tarefas.pack(pady=20)

        # ações de tarefas
        quadro_de_acoes = ttk.Frame(raiz)
        quadro_de_acoes.pack()

        botao_completo = ttk.Button(quadro_de_acoes, text='Tarefa Completa', command=self.tarefa_concluida)
        botao_completo.grid(row=0, column=0, padx=5, pady=5)

        deletar_botao = ttk.Button(quadro_de_acoes, text='Deletar Tarefa', command=self.deletar_tarefa)
        deletar_botao.grid(row=0, column=1, padx=5, pady=5)

    def AdicionarTarefa(self):
        tarefa = self.entrada_de_tarefa.get()
        prioridade = self.prioridade_var.get()
        data_de_vencimento = self.entrada_data_vencimento.get()

        if tarefa:
            self.tarefas.append({'tarefa': tarefa, 'prioridade': prioridade, "data_de_vencimento": data_de_vencimento, 'concluido': False})
            self.atualizar_tarefas()
            self.limpar_campo_entrada()
        else:
            messagebox.showwarning('AVISO', 'Por favor insira uma tarefa!')

    def atualizar_tarefas(self):
        self.caixa_de_tarefas.delete(0, tk.END)
        for i, tarefa in enumerate(self.tarefas, start=1):
            informacao_tarefa = f'{i}. {tarefa["tarefa"]} - Prioridade: {tarefa["prioridade"]} - Data de Vencimento: {tarefa["data_de_vencimento"]}'
            if tarefa['concluido']:
                informacao_tarefa += ' (concluido)'
            self.caixa_de_tarefas.insert(tk.END, informacao_tarefa)

    def limpar_campo_entrada(self):
        self.entrada_de_tarefa.delete(0, tk.END)
        self.entrada_data_vencimento.delete(0, tk.END)
        self.entrada_data_vencimento.insert(0, datetime.now().strftime('%d-%m-%Y'))

    def deletar_tarefa(self):
        tarefa_selecionada = self.caixa_de_tarefas.curselection()
        if tarefa_selecionada:
            for i in tarefa_selecionada:
                del self.tarefas[i]
            self.atualizar_tarefas()
        else:
            messagebox.showwarning('AVISO', 'Por favor selecione uma tarefa para deletar!')

    def tarefa_concluida(self):
        tarefa_selecionada = self.caixa_de_tarefas.curselection()
        if tarefa_selecionada:
            for i in tarefa_selecionada:
                self.tarefas[i]['concluido'] = True
            self.atualizar_tarefas()
        else:
            messagebox.showwarning('AVISO', 'Por favor selecione uma tarefa para marcar como concluída!')


def principal():
    raiz = tk.Tk()
    app = AppListaTarefa(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    principal()
