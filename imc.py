print(30*'-')
print('| CALCUlO IMC')
print(30*'-')
nome=input('| Diga seu nome: ')
altura= float(input('| Digite sua altura: '))
peso=float(input('| Digite seu peso: '))
print(30*'-')
IMC= peso/ (altura**2)

print('Seu IMC é:', round(IMC,2))

if IMC<= 18.5:
    print(f'| AVISO:{nome},tome cuidado você está abaixo do peso!!!)')
    print(f'| RECOMENDAÇÂO: Procure um médico ;)')

elif IMC<= 24.9:
    print(f'| AVISO:{nome}!!! Você está com o peso normal!!')
    print(f'| RECOMENDAÇÂO: Continue assim!')

elif IMC<= 29.9:
    print(f'| AVISO:{nome}, você está com sobrepeso')
    print(f'| RECOMENDAÇÂO:Tome cuidado!')

elif IMC<= 34.9:
    print(f'| AVISO:{nome}, está com obesidade grau 1')
    print(f'| RECOMENDAÇÂO: Vai pra academia!')

elif IMC<= 39.9:
    print(f'| AVISO:{nome},você está com obesidade grau 2')
    print(f'| RECOMENDAÇÂO: Seu caso é grave!! Procure um médico.')

else:
    print(f'| AVISO: Meu Deus,{nome}, seu caso é gravissímo!! Você esta com obesidade grau 3')
    print(f'|RECOMENDAÇÂO:Faça dieta, procure um médicoe e faça exércicios físicos.Por favorrrrr!!!')


