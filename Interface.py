import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class InterfaceUsuario:
    def __init__(self, processar_callback):
        self.janela = tk.Tk()
        self.janela.title("TTS Inverso")
        self.janela.geometry("500x200")
        self.processar_callback = processar_callback
        
        self.criar_widgets()
        self.janela.mainloop()

    def criar_widgets(self):
        # URL do YouTube
        ttk.Label(self.janela, text="URL do YouTube:").pack(pady=5)
        self.entrada_url = ttk.Entry(self.janela, width=50)
        self.entrada_url.pack(pady=5)

        # Botão de processamento
        self.botao_processar = ttk.Button(
            self.janela,
            text="Processar Vídeo",
            command=self.iniciar_processamento
        )
        self.botao_processar.pack(pady=10)

        # Barra de progresso
        self.barra_progresso = ttk.Progressbar(self.janela, mode='indeterminate')
        
        # Status
        self.status_label = ttk.Label(self.janela, text="")
        self.status_label.pack(pady=5)

    def iniciar_processamento(self):
        url = self.entrada_url.get()
        if not url:
            messagebox.showerror("Erro", "Insira uma URL válida!")
            return
        
        self.botao_processar.config(state='disabled')
        self.barra_progresso.pack(pady=5)
        self.barra_progresso.start()
        self.status_label.config(text="Processando...")
        
        try:
            self.processar_callback(url)
            messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
        finally:
            self.barra_progresso.stop()
            self.barra_progresso.pack_forget()
            self.botao_processar.config(state='normal')
            self.status_label.config(text="")