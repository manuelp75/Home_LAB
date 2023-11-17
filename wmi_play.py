import wmi
c = wmi.WMI()
process_watcher = c.Win32_Process.watch_for("creation")
while True:
    new_process = process_watcher()
    print(new_process.Caption)