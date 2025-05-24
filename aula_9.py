import tkinter as tk
from tkinter import messagebox, PhotoImage

def calcular_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura) / 100  # Converte altura de cm para m
        imc = peso / (altura ** 2)
        return round(imc, 2)
    except ValueError:
        return None

def mostrar_imc():
    peso = entrada_peso.get()
    altura = entrada_altura.get()
    imc = calcular_imc(peso, altura)
    if imc:
        messagebox.showinfo("Resultado do IMC", f"Seu IMC é: {imc}")
        exibir_imagem_imc(imc)
    else:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos para peso e altura.")

def exibir_imagem_imc(imc):
    if imc < 18.5:
        caminho_imagem = "bmi1.gif"  # Substitua pelo caminho da sua imagem de baixo peso
    elif 18.5 <= imc < 24.9:
        caminho_imagem = "bmi2.gif"  # Substitua pelo caminho da sua imagem de peso normal
    elif 25 <= imc < 29.9:
        caminho_imagem = "bmi3.gif"  # Substitua pelo caminho da sua imagem de sobrepeso
    else:
        caminho_imagem = "bmi4.gif"  # Substitua pelo caminho da sua imagem de obesidade

    try:
        img = PhotoImage(file=caminho_imagem)
        label_imagem.config(image=img)
        label_imagem.image = img
    except Exception as e:
        messagebox.showerror("Erro de Imagem", f"Erro ao carregar a imagem: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Cria e posiciona os rótulos, entradas e botão
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack()

entrada_peso = tk.Entry(root)
entrada_peso.pack()

label_altura = tk.Label(root, text="Altura (cm):")
label_altura.pack()

entrada_altura = tk.Entry(root)
entrada_altura.pack()

botao_calcular = tk.Button(root, text="Calcular IMC", command=mostrar_imc)
botao_calcular.pack()

label_imagem = tk.Label(root, text="")
label_imagem.pack()

# Executa a aplicação
root.mainloop()
