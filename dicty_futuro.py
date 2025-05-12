import tkinter as tk
from tkinter import messagebox

produtos = []

def adicionar_produto():
    nome = entry_nome.get()
    try:
        preco = float(entry_preco.get())
    except ValueError:
        messagebox.showerror("Erro", "Preço inválido. Digite um número.")
        return

    if nome == "":
        messagebox.showerror("Erro", "O nome do produto não pode estar vazio.")
        return

    produto = {
        "ID": len(produtos),
        "Nome": nome,
        "preço": preco
    }

    produtos.append(produto)
    messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)

def ver_produtos():
    if not produtos:
        messagebox.showinfo("Nenhum produto", "Nenhum produto foi cadastrado ainda.")
        return

    janela_lista = tk.Toplevel(root)
    janela_lista.title("Produtos Cadastrados")

    texto = tk.Text(janela_lista, width=40, height=15)
    texto.pack(padx=10, pady=10)

    for p in produtos:
        texto.insert(tk.END, f"ID: {p['ID']}\n")
        texto.insert(tk.END, f"Nome: {p['Nome']}\n")
        texto.insert(tk.END, f"Preço: R$ {p['preço']:.2f}\n\n")

# Janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")

tk.Label(root, text="Nome do Produto:").pack()
entry_nome = tk.Entry(root, width=30)
entry_nome.pack(pady=5)

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root, width=30)
entry_preco.pack(pady=5)

tk.Button(root, text="Cadastrar Produto", command=adicionar_produto).pack(pady=10)
tk.Button(root, text="Ver Produtos Cadastrados", command=ver_produtos).pack(pady=5)

root.mainloop()
