from tkinter import * #importa a biblioteca que cria a janela

def JanelaSolo():#janela para o jogo solo  
    janelaSolo = Tk()
    janelaSolo.geometry('500x500')
    janelaSolo.title('Jogo da forca: Solo') 
    
    
    janelaSolo.mainloop()
    
def JanelaGrupo():#janela para jogo em grupo 
    
    janelaGrupo = Tk()
    janelaGrupo.geometry('500x500')
    janelaGrupo.title('Jogo da forca: Grupo') 
    texto_Palavra = Label(janelaGrupo, text="Digite a palavra secreta:")
    texto_Palavra.grid(column=0, row = 0)
    entrada_palavra = Entry(janelaGrupo)
    entrada_palavra.grid(column=1, row=0)
    
    janelaGrupo.mainloop() 
 



janela1 = Tk() #inicia a janela principal
janela1.geometry('500x300') #tamanho da janela ao iniciar
janela1.title("Jogo da forca-Inicio") #nome da janela 
janela1.grid()#faz o texto dentro da janela 
texto_bemVindo = Label(janela1, text="Bem vindo ao jogo da forca!")
texto_bemVindo.grid(column=0, row=0)
texto_bemVindo2 = Label (janela1, text="Qual tipo de jogo deseja? ")
texto_bemVindo2.grid(column=0, row=1) 

#botão para selecionar o tipo de jogo
botaoSolo = Button(janela1, text="Jogo Solo", command= JanelaSolo )
botaoSolo.grid(column=0, row=5)
botaoGrupo = Button(janela1, text="Jogo em grupo", command= JanelaGrupo )
botaoGrupo.grid(column=5, row=5) 

janela1.mainloop()
#loop que mantem a janela aberta 

    
    