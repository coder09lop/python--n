print("ciao benvenuto nell sistema centrale HackerBan")
print("come ti chiami?")
nome_anonimo = input()
print("domanda di sicurezza qunato fa 4*9?"+nome_anonimo)
ilinput = input()
if ilinput != "36":
    print("mi spiace non possiamo farti entrare prema 1 per uscire")
else:
    print("entri pure cosa vorrebbe fare? '1' esci '2' login '3' h4ck.exe")
entarata = input()
if entarata != "2":
    print("il codice è errato prema digiti 'esci' per uscire")
    print("arrivederci")
    uscita = input()

else:
    print("ok inserisca il codice")
    loginutente = input()
    if loginutente == "404":
    print("ok è il momento di loggare inserisca il nome utente")
    loginutente2 = input()