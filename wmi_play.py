import wmi  #prerequisite : pip install wmi
c = wmi.WMI() #connessione al repository WMI locale
#c = wmi.WMI("remote machine hostname", user=r"remote machine hostname\user", password="inserisci la password") 
# #... leva il commento al codice 'c =WMI.....'per usare lo script su una macchina remote. 
# nb. se si usa un administrator di dominio si ha pieno controsllo su tutti gli host della rete
process_watcher = c.Win32_Process.watch_for("creation") 
while True:
    new_process = process_watcher()
    print(new_process.Caption)
#lancia lo script e monitora la creazione dei processi...
#doc: https://github.com/tjguk/wmi/blob/master/docs/tutorial.rst
