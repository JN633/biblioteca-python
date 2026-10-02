import sqlite3

def cadastrar_livro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")

    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO livros (titulo, autor)
        VALUES (?, ?) 
        """, (titulo, autor))

    conexao.commit()
    conexao.close()

    print("Livro cadastrado com sucesso!")



def listar_livros():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    conexao.close()

    for livro in livros:
        print(livro)

        
    conexao.close()



def excluir_livros():
    id_livro = int(input("Digite o ID do livro que deseja excluir: "))

    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

    conexao.commit()
    conexao.close()

    print("Livro excluido com sucesso!")


