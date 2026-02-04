"""
APLIKASAUN DESKTOP - VALIDADOR AUTOMATA TIMOR-LESTE
Autor: Asshy, Yopi & Abilio
Materia: Automata - Semester VI
Instituto: IPDC

Aplikasaun ne'e valida:
1. Númeru Pares (DFA)
2. Kode Bináriu (DFA)
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
from datetime import datetime

# ============================================================================
# KLASE DFA - Númeru Pares
# ============================================================================

class DFANumeruPares:
    """Deterministic Finite Automaton ba deteta númeru pares"""
    
    def __init__(self):
        self.estado_atual = 'par'
        self.historiku = []
    
    def reset(self):
        """Reset ba estadu inisiál"""
        self.estado_atual = 'par'
        self.historiku.clear()
    
    def transisaun(self, digitu):
        """Aplika funsaun transisaun"""
        estado_anterior = self.estado_atual
        
        if digitu in '02468':
            self.estado_atual = 'par'
        elif digitu in '13579':
            self.estado_atual = 'ímpar'
        else:
            raise ValueError(f"Dígitu inválidu: {digitu}")
        
        self.historiku.append({
            'digitu': digitu,
            'estado_anterior': estado_anterior,
            'estado_foun': self.estado_atual
        })
        
        return self.estado_atual
    
    def prosesa(self, numero):
        """Prosesa string númeru kompletu"""
        self.reset()
        
        if not numero:
            return True, "String mamuk konsidera par"
        
        for digitu in numero:
            if not digitu.isdigit():
                raise ValueError(f"Input la'ós númeru: {numero}")
            self.transisaun(digitu)
        
        resultado = self.estado_atual == 'par'
        return resultado, f"Dígitu ikus: {numero[-1]}"

# ============================================================================
# KLASE DFA - Kode Bináriu
# ============================================================================

class DFAKodeBinariu:
    """Deterministic Finite Automaton ba valida kode bináriu"""
    
    def __init__(self):
        self.estado_atual = 'start'
        self.historiku = []
    
    def reset(self):
        """Reset ba estadu inisiál"""
        self.estado_atual = 'start'
        self.historiku.clear()
    
    def transisaun(self, karakter):
        """Aplika funsaun transisaun"""
        estado_anterior = self.estado_atual
        
        if self.estado_atual == 'rejeita':
            pass  # Trap state
        elif karakter in '01':
            self.estado_atual = 'válidu'
        else:
            self.estado_atual = 'rejeita'
        
        self.historiku.append({
            'karakter': karakter,
            'estado_anterior': estado_anterior,
            'estado_foun': self.estado_atual
        })
        
        return self.estado_atual
    
    def prosesa(self, kode):
        """Prosesa string kode kompletu"""
        self.reset()
        
        if not kode:
            return False, "String mamuk la válidu"
        
        for karakter in kode:
            self.transisaun(karakter)
            if self.estado_atual == 'rejeita':
                return False, f"Karakter inválidu: '{karakter}'"
        
        resultado = self.estado_atual == 'válidu'
        return resultado, f"Total bit: {len(kode)}"

# ============================================================================
# KLASE APLIKASAUN PRINSIPAL
# ============================================================================

class AplicasaunValidadorAutomata:
    """Aplikasaun Desktop ba Validador Automata"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Validador Automata - Timor-Leste")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Inisializa DFA
        self.dfa_pares = DFANumeruPares()
        self.dfa_binariu = DFAKodeBinariu()
        
        # Konfigura tema kór
        self.cor_primaria = "#2C3E50"
        self.cor_sekundaria = "#3498DB"
        self.cor_susesu = "#27AE60"
        self.cor_error = "#E74C3C"
        self.cor_background = "#ECF0F1"
        
        # Kria interface
        self.kria_interface()
        
    def kria_interface(self):
        """Kria interface usuario kompletu"""
        
        # Header
        self.kria_header()
        
        # Notebook (Tabs)
        self.kria_tabs()
        
        # Footer
        self.kria_footer()
    
    def kria_header(self):
        """Kria header aplikasaun"""
        header_frame = tk.Frame(self.root, bg=self.cor_primaria, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Títulu
        titulo = tk.Label(
            header_frame,
            text="🤖 VALIDADOR AUTOMATA",
            font=("Arial", 24, "bold"),
            bg=self.cor_primaria,
            fg="white"
        )
        titulo.pack(pady=10)
        
        # Subtítulu
        subtitulo = tk.Label(
            header_frame,
            text="Finite State Automata | Timor-Leste 🇹🇱",
            font=("Arial", 10),
            bg=self.cor_primaria,
            fg="#BDC3C7"
        )
        subtitulo.pack()
    
    def kria_tabs(self):
        """Kria tabs ba kada validador"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Númeru Pares
        self.tab_pares = tk.Frame(self.notebook, bg=self.cor_background)
        self.notebook.add(self.tab_pares, text="  📊 Númeru Pares  ")
        self.kria_tab_pares()
        
        # Tab 2: Kode Bináriu
        self.tab_binariu = tk.Frame(self.notebook, bg=self.cor_background)
        self.notebook.add(self.tab_binariu, text="  💻 Kode Bináriu  ")
        self.kria_tab_binariu()
        
        # Tab 3: Kona-ba
        self.tab_kona = tk.Frame(self.notebook, bg=self.cor_background)
        self.notebook.add(self.tab_kona, text="  ℹ️ Kona-ba  ")
        self.kria_tab_kona()
    
    def kria_tab_pares(self):
        """Kria interface ba validador númeru pares"""
        
        # Frame Input
        input_frame = tk.LabelFrame(
            self.tab_pares,
            text="Input Númeru",
            font=("Arial", 12, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            input_frame,
            text="Hakerek númeru (ezemplu: 71901006):",
            font=("Arial", 10),
            bg=self.cor_background
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        self.entry_pares = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=40
        )
        self.entry_pares.pack(padx=10, pady=5)
        
        # Buttaun Valida
        btn_valida_pares = tk.Button(
            input_frame,
            text="🔍 VALIDA NÚMERU",
            font=("Arial", 12, "bold"),
            bg=self.cor_sekundaria,
            fg="white",
            command=self.valida_pares,
            cursor="hand2",
            relief=tk.RAISED,
            borderwidth=3
        )
        btn_valida_pares.pack(pady=10)
        
        # Frame Rezultadu
        resultado_frame = tk.LabelFrame(
            self.tab_pares,
            text="Rezultadu",
            font=("Arial", 12, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        resultado_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.label_resultado_pares = tk.Label(
            resultado_frame,
            text="Hein rezultadu...",
            font=("Arial", 16, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        self.label_resultado_pares.pack(pady=20)
        
        # Frame Historiku
        historiku_frame = tk.LabelFrame(
            self.tab_pares,
            text="Historiku Transisaun DFA",
            font=("Arial", 10, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        historiku_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.text_historiku_pares = scrolledtext.ScrolledText(
            historiku_frame,
            font=("Courier", 10),
            height=10,
            wrap=tk.WORD
        )
        self.text_historiku_pares.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def kria_tab_binariu(self):
        """Kria interface ba validador kode bináriu"""
        
        # Frame Input
        input_frame = tk.LabelFrame(
            self.tab_binariu,
            text="Input Kode Bináriu",
            font=("Arial", 12, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            input_frame,
            text="Hakerek kode bináriu (ezemplu: 101010):",
            font=("Arial", 10),
            bg=self.cor_background
        ).pack(anchor=tk.W, padx=10, pady=5)
        
        self.entry_binariu = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=40
        )
        self.entry_binariu.pack(padx=10, pady=5)
        
        # Buttaun Valida
        btn_valida_binariu = tk.Button(
            input_frame,
            text="🔍 VALIDA KODE",
            font=("Arial", 12, "bold"),
            bg=self.cor_sekundaria,
            fg="white",
            command=self.valida_binariu,
            cursor="hand2",
            relief=tk.RAISED,
            borderwidth=3
        )
        btn_valida_binariu.pack(pady=10)
        
        # Frame Rezultadu
        resultado_frame = tk.LabelFrame(
            self.tab_binariu,
            text="Rezultadu",
            font=("Arial", 12, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        resultado_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.label_resultado_binariu = tk.Label(
            resultado_frame,
            text="Hein rezultadu...",
            font=("Arial", 16, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        self.label_resultado_binariu.pack(pady=20)
        
        # Frame Historiku
        historiku_frame = tk.LabelFrame(
            self.tab_binariu,
            text="Historiku Transisaun DFA",
            font=("Arial", 10, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        )
        historiku_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.text_historiku_binariu = scrolledtext.ScrolledText(
            historiku_frame,
            font=("Courier", 10),
            height=10,
            wrap=tk.WORD
        )
        self.text_historiku_binariu.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def kria_tab_kona(self):
        """Kria tab informasaun kona-ba aplikasaun"""
        
        # Frame Konteúdu
        content_frame = tk.Frame(self.tab_kona, bg=self.cor_background)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Títulu
        tk.Label(
            content_frame,
            text=" Kona-ba Aplikasaun",
            font=("Arial", 18, "bold"),
            bg=self.cor_background,
            fg=self.cor_primaria
        ).pack(pady=10)
        
        # Informasaun
        info_text = """
        VALIDADOR AUTOMATA TIMOR-LESTE
        
         Materia: Automata (Semester VI)
         Estudante: Asshy, Yopi & Abilio
         Instituto: IPDC
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        📖 DESKRISAUN
        Aplikasaun ne'e implementa Deterministic Finite Automaton (DFA)
        ba valida rua tipu input:
        
        1️⃣  NÚMERU PARES
           • Deteta se númeru ida mak par ka ímpar
           • Bazeia ba dígitu ikus
           • Kompleksidade: O(n) tempu, O(1) espasu
        
        2️⃣  KODE BINÁRIU
           • Valida se string kontein só 0 no 1
           • Rejeita karakter seluk
           • Kompleksidade: O(n) tempu, O(1) espasu
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        🛠️ TEKNOLOJIA
        • Python 3.9+
        • Tkinter (GUI)
        • DFA Theory (Automata)
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        📅 Tinan: 2025-2026
        🇹🇱 Timor-Leste
        """
        
        tk.Label(
            content_frame,
            text=info_text,
            font=("Courier", 10),
            bg=self.cor_background,
            fg=self.cor_primaria,
            justify=tk.LEFT
        ).pack(pady=10)
    
    def kria_footer(self):
        """Kria footer aplikasaun"""
        footer_frame = tk.Frame(self.root, bg=self.cor_primaria, height=40)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        footer_text = "© 2025-2026 | YOPI ABILIO ASSHY | IPDC - Timor-Leste 🇹🇱"
        tk.Label(
            footer_frame,
            text=footer_text,
            font=("Arial", 9),
            bg=self.cor_primaria,
            fg="white"
        ).pack(pady=10)
    
    def valida_pares(self):
        """Valida númeru pares"""
        input_text = self.entry_pares.get().strip()
        
        if not input_text:
            messagebox.showwarning("Input Mamuk", "Por favor hakerek númeru ida!")
            return
        
        try:
            # Prosesa ho DFA
            start_time = time.time()
            resultado, info = self.dfa_pares.prosesa(input_text)
            end_time = time.time()
            tempo_prosesa = (end_time - start_time) * 1000  # millisegundas
            
            # Hatudu rezultadu
            if resultado:
                self.label_resultado_pares.config(
                    text=f"✅ NÚMERU PAR",
                    fg=self.cor_susesu
                )
            else:
                self.label_resultado_pares.config(
                    text=f"❌ NÚMERU ÍMPAR",
                    fg=self.cor_error
                )
            
            # Hatudu historiku
            self.hatudu_historiku_pares(input_text, resultado, info, tempo_prosesa)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def hatudu_historiku_pares(self, input_text, resultado, info, tempo):
        """Hatudu historiku transisaun DFA Númeru Pares"""
        self.text_historiku_pares.delete(1.0, tk.END)
        
        historiku_text = f"""
╔══════════════════════════════════════════════════════════╗
║           HISTORIKU TRANSISAUN DFA - NÚMERU PARES        ║
╚══════════════════════════════════════════════════════════╝

📥 INPUT: {input_text}
{"✅ REZULTADU: PAR" if resultado else "❌ REZULTADU: ÍMPAR"}
ℹ️  INFO: {info}
⏱️  TEMPU PROSESA: {tempo:.4f} ms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASU-PASU TRANSISAUN:

"""
        
        for i, step in enumerate(self.dfa_pares.historiku, 1):
            historiku_text += f"Pasu {i}:\n"
            historiku_text += f"  Dígitu: '{step['digitu']}'\n"
            historiku_text += f"  Estadu Anterior: [{step['estado_anterior']}]\n"
            historiku_text += f"  Estadu Foun: [{step['estado_foun']}]\n"
            historiku_text += f"  {'─' * 50}\n"
        
        historiku_text += f"\n🎯 ESTADU FINAL: [{self.dfa_pares.estado_atual.upper()}]\n"
        
        self.text_historiku_pares.insert(1.0, historiku_text)
    
    def valida_binariu(self):
        """Valida kode bináriu"""
        input_text = self.entry_binariu.get().strip()
        
        if not input_text:
            messagebox.showwarning("Input Mamuk", "Por favor hakerek kode bináriu ida!")
            return
        
        try:
            # Prosesa ho DFA
            start_time = time.time()
            resultado, info = self.dfa_binariu.prosesa(input_text)
            end_time = time.time()
            tempo_prosesa = (end_time - start_time) * 1000
            
            # Hatudu rezultadu
            if resultado:
                self.label_resultado_binariu.config(
                    text=f"✅ KODE VÁLIDU",
                    fg=self.cor_susesu
                )
            else:
                self.label_resultado_binariu.config(
                    text=f"❌ KODE INVÁLIDU",
                    fg=self.cor_error
                )
            
            # Hatudu historiku
            self.hatudu_historiku_binariu(input_text, resultado, info, tempo_prosesa)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def hatudu_historiku_binariu(self, input_text, resultado, info, tempo):
        """Hatudu historiku transisaun DFA Kode Bináriu"""
        self.text_historiku_binariu.delete(1.0, tk.END)
        
        historiku_text = f"""
╔══════════════════════════════════════════════════════════╗
║        HISTORIKU TRANSISAUN DFA - KODE BINÁRIU           ║
╚══════════════════════════════════════════════════════════╝

📥 INPUT: {input_text}
{"✅ REZULTADU: VÁLIDU" if resultado else "❌ REZULTADU: INVÁLIDU"}
ℹ️  INFO: {info}
⏱️  TEMPU PROSESA: {tempo:.4f} ms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASU-PASU TRANSISAUN:

"""
        
        for i, step in enumerate(self.dfa_binariu.historiku, 1):
            historiku_text += f"Pasu {i}:\n"
            historiku_text += f"  Karakter: '{step['karakter']}'\n"
            historiku_text += f"  Estadu Anterior: [{step['estado_anterior']}]\n"
            historiku_text += f"  Estadu Foun: [{step['estado_foun']}]\n"
            historiku_text += f"  {'─' * 50}\n"
            
            if step['estado_foun'] == 'rejeita':
                historiku_text += f"  ⚠️  REJEITA! Prosesa para iha ne'e.\n"
                break
        
        historiku_text += f"\n🎯 ESTADU FINAL: [{self.dfa_binariu.estado_atual.upper()}]\n"
        
        self.text_historiku_binariu.insert(1.0, historiku_text)

# ============================================================================
# PROGRAMA PRINSIPAL
# ============================================================================

def main():
    """Funsaun main atu hahu aplikasaun"""
    root = tk.Tk()
    app = AplicasaunValidadorAutomata(root)
    root.mainloop()

if __name__ == "__main__":
    main()
