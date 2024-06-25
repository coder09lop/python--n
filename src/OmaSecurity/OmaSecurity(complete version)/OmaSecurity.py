import random


print("welcome to OmaSecurity what do you want to do?")
print("you are now in the standard plan the complete one coming soon")
print("digit '1' if you want to scan your pc if is there any virus '2' if you awnt to update your drivers")
chouce = input()
if chouce == '1':
    print("what type of scan do you want to do?")
    print("digit '1' if you want to do fast scan '2' if you want to do complete scan")
    scanning = input()
    if scanning == '1':
        print("ok scanning pc wait about 10 minutes")
        numero1 = ('sacn box 1 complete', 'sacn box 2 complete', 'sacn box 3 complete', 'sacn box 4 complete')
        for numero1 in range(1,100):
            print(numero1)
            print("scan complete digit 'exit' to shutdown the program")
            shut = input()
        
    else:
        print("press enter to star the scan")
        for sacn in range(10000000):
            print(sacn)
        print("scanning complete to exit digit 'exit'")
        ex = input()
else:
    print("Press Enter to scan drivers")
    Enter1 = input()
    for enter in range(10000000):
        print(enter)
    print("scan complete all drivers are updated")
    print("do you want to start the security drivers scan?")
    print("digit '1' if you want to start the security scan '2' if you want to exit")
    scan1 = input()
    if scan1 == '1':
        print("ok press enter to start")
        for press in range(1000000):
            print(press)
        print("now if you want you can tell us your reputazion")
        repu = input
    else:
        print("ciao")
    print("Digit 'exit' to exit")
    exit = input()