import random


print("benvenuto nell ip server creator")
print("qui creerai il tuo server per accedere hai file di stato")
print("qui inserisci un codice da 6 cifre")
pin = input()
print("ora il tuo ip sara")
ips = ('192.839.838', '192.909.87', '89787.09', 'error 404', 'cracking server')
print(random.choice(ips))
print("per uscire digita 'esci'")
uscita = input()