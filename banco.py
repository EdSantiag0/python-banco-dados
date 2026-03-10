import sqlite3

def conectar():
  conexao = sqlite3.connect("loja.db")
  return conexao