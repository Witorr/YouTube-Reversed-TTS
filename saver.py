from fpdf import FPDF
import os

class TextSaver:
    @staticmethod
    def salvar(texto, nome_arquivo="resumo"):
        caminho = os.path.join("resultados", f"{nome_arquivo}.txt")
        os.makedirs("resultados", exist_ok=True)
        
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)
        return caminho

class PDFSaver(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_font("Arial", size=12)
    
    @staticmethod
    def salvar(texto, nome_arquivo="resumo"):
        caminho = os.path.join("resultados", f"{nome_arquivo}.pdf")
        os.makedirs("resultados", exist_ok=True)
        
        pdf = PDFSaver()
        pdf.multi_cell(0, 10, txt=texto)
        pdf.output(caminho)
        return caminho