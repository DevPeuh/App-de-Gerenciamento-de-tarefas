import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class AppListaTarefa:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title('Aplicativo de Lista de Tarefas')
        self.raiz.geometry('500x400')

        self.tarefas = []

        self.configurar_estilo()
        self.criar_widgets()

    def configurar_estilo(self):
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Helvetica', 20, 'bold'), foreground='#333')
        self.style.configure('TButton', font=('Helvetica', 10), padding=5)
        self.style.configure('TEntry', font=('Helvetica', 10), padding=5)

    def criar_widgets(self):
        # Header
        cabecalho = ttk.Frame(self.raiz)
        cabecalho.pack(pady=10)
        cabecalho_rotulo = ttk.Label(cabecalho, text='Lista de Afazeres', style='Header.TLabel')
        cabecalho_rotulo.pack()

        # Entrada de Tarefa
        quadro_tarefa = ttk.Frame(self.raiz)
        quadro_tarefa.pack(pady=10)
        self.entrada_de_tarefa = ttk.Entry(quadro_tarefa, width=40)
        self.entrada_de_tarefa.grid(row=0, column=0, padx=5, pady=5)

        opcoes_prioridade = ['Baixo', 'Médio', 'Alto']
        self.prioridade_var = tk.StringVar(self.raiz)
        self.prioridade_var.set(opcoes_prioridade[0])
        self.menu = ttk.OptionMenu(quadro_tarefa, self.prioridade_var, *opcoes_prioridade)
        self.menu.grid(row=0, column=1, padx=5, pady=5)

        self.entrada_data_vencimento = ttk.Entry(quadro_tarefa, width=15)
        self.entrada_data_vencimento.grid(row=0, column=2, padx=5, pady=5)
        self.entrada_data_vencimento.insert(0, datetime.now().strftime('%d-%m-%Y'))

        add_botao = ttk.Button(quadro_tarefa, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        add_botao.grid(row=0, column=3, padx=5, pady=5)

        # Lista de Tarefas
        self.caixa_de_tarefas = tk.Listbox(self.raiz, width=60, height=15, font=('Helvetica', 10))
        self.caixa_de_tarefas.pack(pady=20)

        # Ações de Tarefas
        quadro_de_acoes = ttk.Frame(self.raiz)
        quadro_de_acoes.pack()
        botao_completo = ttk.Button(quadro_de_acoes, text='Tarefa Completa', command=self.tarefa_concluida)
        botao_completo.grid(row=0, column=0, padx=5, pady=5)
        deletar_botao = ttk.Button(quadro_de_acoes, text='Deletar Tarefa', command=self.deletar_tarefa)
        deletar_botao.grid(row=0, column=1, padx=5, pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_de_tarefa.get()
        prioridade = self.prioridade_var.get()
        data_de_vencimento = self.entrada_data_vencimento.get()

        if tarefa and self.validar_data(data_de_vencimento):
            self.tarefas.append({'tarefa': tarefa, 'prioridade': prioridade, 'data_de_vencimento': data_de_vencimento, 'concluido': False})
            self.atualizar_tarefas()
            self.limpar_campo_entrada()
        else:
            messagebox.showwarning('AVISO', 'Por favor insira uma tarefa válida e uma data de vencimento válida!')

    def validar_data(self, data_texto):
        try:
            datetime.strptime(data_texto, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def atualizar_tarefas(self):
        self.caixa_de_tarefas.delete(0, tk.END)
        for i, tarefa in enumerate(self.tarefas, start=1):
            informacao_tarefa = f'{i}. {tarefa["tarefa"]} - Prioridade: {tarefa["prioridade"]} - Data de Vencimento: {tarefa["data_de_vencimento"]}'
            if tarefa['concluido']:
                informacao_tarefa += ' (concluído)'
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
