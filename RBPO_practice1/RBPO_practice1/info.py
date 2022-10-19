import wmi
class Info:
    def showInfo(self):
        c = wmi.WMI()
        for d in c.Win32_LogicalDisk():
            freeSpace = round(int(d.FreeSpace) / 1024 / 1024 / 1024)
            size = round(int(d.Size) / 1024 / 1024 / 1024)
            return f"Название: {d.Caption} \nСвободное пространство: {freeSpace} GB \nОбъем диска: {size} GB \nТип: {d.DriveType} \nМетка: {d.VolumeName}"