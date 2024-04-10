#PALAVRA DO JOGO
secreto = 'perfume'
digitadas = []
chances = 3
#ENUNCIADO DO JOGO
print('-=' *20)
print ('Jogo da forca em Python')
print('-=' *20)
#sistema para pergunta
while True:
     letra = str(input('Digite uma letra'))
#sistema para evitar trapaça
     if len(letra)> 1:
         print('Erro, Não vale digitar mais de uma letra') 
         continue
#lista de digitadas
     digitadas.append(letra)
#sistema logico
#variavel
     secreto_temporario = '' 
     for letra_secreta in secreto:
        if letra_secreta in digitadas:
         secreto_temporario += letra_secreta
     else:
         secreto_temporario += '*'
#checar se a variavel secreto e igual a palavra
         if secreto_temporario == secreto:
             print (f'Você venceu e escapou da forca!{secreto}')
             break
         else:
             print(f'palavra secreta esta assim:{secreto_temporario}')
#contador de chances
         if letra not in secreto:
               chances -= 1
         if chances <=0:
#condição perdeu
                 print ('Você perdeu!')
                 break
#quantia de chances
                 print (f'Você tem{chances}chances') 
                 print()
                 
                 