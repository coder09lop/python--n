import random

print("benvenuto nell softmint 2.0")
print("qual è il tuo nome?")
nomeutente = input()
print("quanti anni hai")
anniutente = input()
if anniutente > '11':
    print("ok entra")
    print("ok procediamo")
    print("ok inserisci il nomeutente")
    nome = input()
    print("ok ora inserisci la password")
    passworditente = input()
    print("ok ora ricordati il codice che ti diamo")
    print("il codice è")
    listacodici = ('2317')
    print(random.choice(listacodici))
    print("cerca di non perdere il codice perchè non è recuperabile")
    print("qual è il codice?")
    code = input()
    if code == '2317':
        print("ok giusto")
    else:
        print("errato")
    print("ora sei collegato alla rete dell softmint con ip:")
    ipsoftmint = ('192.89.00', '192.88.3253', '192.87.2317', '192.67.8978')
    print(random.choice(ipsoftmint))
    print("ora che è connesso può uscire digitando 'esci' o collegarsi a un altro server con 'connect")
    uscitadisconnessione = input()
    if uscitadisconnessione == 'connect':
        print("ok ora si connettera a")
        listaserver = ('193.7.48.103', '110.55.68.5', '137.240.46.77', '108.57.69.23', '64.174.73.74', '81.1.30.251')
        print(random.choice(listaserver))
        print("premi 'esci' per uscire")
        uscita = input()
    else:
        print("esco")
else:
    print("non puoi entrare")
# 64.174.73.74 è pericoloso anche 192.67.8978 è pericoloso
    



    
