from info import Info
from txtfile import TxtFile
from xmlfile import XMLFile
from jsonfile import JsonFile
from ziparchive import ZipArchive
import PySimpleGUI as gui

class DrawWindows:
    def drawWindowInfo(self):
        info = Info()
        layoutInfo = [ [gui.Text('Info:\n' + info.showInfo(), font='Arial 12')],
                       [gui.Button('Return in main menu')] ]
        infoWindow = gui.Window('Info', layoutInfo, size = (350, 200), element_justification='c')

        while True:
            event, values = infoWindow.read()
            if event == 'Return in main menu':
                infoWindow.close()
                self.drawStartWindow()
            if event == gui.WIN_CLOSED:
                break
        infoWindow.close()

    def drawWindowTxt(self):
        txt = TxtFile()
        layoutTxt = [ [gui.Text('Enter file name: '), gui.Input(key = '-FileName-'), gui.Text('.txt')],
                      [gui.Text('Enter some text: '), gui.Input(key = '-Text-')],
                      [gui.Button('Add'), gui.Button('Read'), gui.Button('Remove')], 
                      [gui.Text('Text: '), gui.Output(size = (60, 10), key = '-TextOutput-')],
                      [gui.Button('Return in main menu')] ]
        txtWindow = gui.Window('Info', layoutTxt, size = (500, 400), element_justification='c')

        while True:
            event, values = txtWindow.read()
            if event == 'Add':
                if(values['-FileName-'] == '' or values['-Text-'] == ''):
                    gui.popup('You should to fill all the fields')
                else:
                    txt.createFile(values['-FileName-'], values['-Text-'])
                    gui.popup('Data appended successfully')
            if event == 'Read':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(txt.readFile(values['-FileName-']) == 'Error'):
                        gui.popup('Sorry, the file ' + values['-FileName-'] + '.txt' + ' does not exist')
                    else:
                        output = txtWindow['-TextOutput-']
                        output.Update(txt.readFile(values['-FileName-']))
            if event == 'Remove':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(txt.removeFile(values['-FileName-']) == False):
                       gui.popup('Sorry, the file ' + values['-FileName-'] + '.txt' + ' does not exist')
                    else:
                        gui.popup('File deleted successfully')
            if event == 'Return in main menu':
                txtWindow.close()
                self.drawStartWindow()
            if event == gui.WIN_CLOSED:
                break
        txtWindow.close()

    def drawWindowXml(self):
        xml = XMLFile()
        layoutXml = [ [gui.Text('Enter file name: '), gui.Input(key = '-FileName-'), gui.Text('.xml')],
                      [gui.Text('Enter new data: ')],
                      [gui.Text('Enter recipe name: '), gui.Input(key = '-Name-')],
                      [gui.Text('Enter recipe category: '), gui.Input(key = '-Category-')],
                      [gui.Text('Enter recipe main ingredient: '), gui.Input(key = '-Ingredient-')], 
                      [gui.Button('Add'), gui.Button('Read'), gui.Button('Remove')], 
                      [gui.Text('Xml: '), gui.Output(size = (60, 10), key = '-TextOutput-')],
                      [gui.Button('Return in main menu')] ]
        xmlWindow = gui.Window('XML', layoutXml, size = (500, 400), element_justification='c')

        while True:
            event, values = xmlWindow.read()
            if event == 'Add':
                if(values['-FileName-'] == '' or values['-Name-'] == '' or values['-Category-'] == '' or values['-Ingredient-'] == ''):
                    gui.popup('You should to fill all the fields')
                else:
                    xml.writeXml(values['-FileName-'], values['-Name-'], values['-Category-'], values['-Ingredient-'])
                    gui.popup('Data appended successfully')
            if event == 'Read':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(xml.readXml(values['-FileName-']) == 'Error'):
                        gui.popup('Sorry, the file ' + values['-FileName-'] + '.xml' + ' does not exist')
                    else:
                        output = xmlWindow['-TextOutput-']
                        output.Update(xml.readXml(values['-FileName-']))
            if event == 'Remove':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(xml.removeXml(values['-FileName-']) == False):
                       gui.popup('Sorry, the file ' + values['-FileName-'] + '.xml' + ' does not exist')
                    else:
                        gui.popup('File deleted successfully')
            if event == 'Return in main menu':
                xmlWindow.close()
                self.drawStartWindow()
            if event == gui.WIN_CLOSED:
                break
        xmlWindow.close()

    def drawWindowJson(self):
        json = JsonFile()
        layoutJson = [ [gui.Text('Enter file name: '), gui.Input(key = '-FileName-'), gui.Text('.json')],
                      [gui.Text('Enter new data: ')],
                      [gui.Text('Enter recipe name: '), gui.Input(key = '-Name-')],
                      [gui.Text('Enter recipe category: '), gui.Input(key = '-Category-')],
                      [gui.Text('Enter recipe main ingredient: '), gui.Input(key = '-Ingredient-')], 
                      [gui.Button('Add'), gui.Button('Read'), gui.Button('Remove')], 
                      [gui.Text('Json: '), gui.Output(size = (60, 10), key = '-TextOutput-')],
                      [gui.Button('Return in main menu')] ]
        jsonWindow = gui.Window('XML', layoutJson, size = (500, 400), element_justification='c')

        while True:
            event, values = jsonWindow.read()
            if event == 'Add':
                if(values['-FileName-'] == '' or values['-Name-'] == '' or values['-Category-'] == '' or values['-Ingredient-'] == ''):
                    gui.popup('You should to fill all the fields')
                else:
                    json.writeJson(values['-FileName-'], values['-Name-'], values['-Category-'], values['-Ingredient-'])
                    gui.popup('Data appended successfully')
            if event == 'Read':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(json.readJson(values['-FileName-']) == 'Error'):
                        gui.popup('Sorry, the file ' + values['-FileName-'] + '.json' + ' does not exist')
                    else:
                        output = jsonWindow['-TextOutput-']
                        output.Update(json.readJson(values['-FileName-']))
            if event == 'Remove':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    if(json.removeJson(values['-FileName-']) == False):
                       gui.popup('Sorry, the file ' + values['-FileName-'] + '.json' + ' does not exist')
                    else:
                        gui.popup('File deleted successfully')
            if event == 'Return in main menu':
                jsonWindow.close()
                self.drawStartWindow()
            if event == gui.WIN_CLOSED:
                break
        jsonWindow.close()

    def drawWindowZip(self):
        zipArch = ZipArchive()
        layoutZip = [  [gui.Text('Enter archive name: '), gui.Input(key = '-ArchiveName-', size = (20, 1)), gui.Text('.zip'), gui.Button('Create')],
                       [gui.Text('Choose file for zip: '), gui.Input(key = '-FileName-', size = (20, 1), change_submits=True), gui.FileBrowse()],
                       [gui.Button('Zip'), gui.Button('Unzip'), gui.Button('Remove')],
                       [gui.Button('Return in main menu')] ]
        zipWindow = gui.Window('Info', layoutZip, size = (500, 200), element_justification='c')

        while True:
            event, values = zipWindow.read()
            if event == 'Create':
                if(values['-ArchiveName-'] == ''):
                    gui.popup('You should to fill archive name')
                else:
                    z = zipArch.createFile(values['-ArchiveName-'])
                    gui.popup('Archive created successfully')
            if event == 'Zip':
                if(values['-FileName-'] == ''):
                    gui.popup('You should to fill file name')
                else:
                    zipWindow['-FileName-'].update('')
                    z = zipArch.createFile(values['-ArchiveName-'])
                    write = zipArch.writeFile(values['-FileName-'], z)
                    if write == 'Error':
                        gui.popup('Sorry, the file ' + values['-FileName-'] + ' does not exist')
                    else:
                        gui.popup('File appended to archive successfully. Info about files in archive: ', write)
            if event == 'Unzip':
                if(values['-FileName-'] == '' and values['-ArciveName-'] == ''):
                    gui.popup('You should to fill all fields')
                else:
                    read = zipArch.readFile(values['-ArchiveName-'], values['-FileName-'])
                    if read == 'Error':
                        gui.popup('Sorry, the file does not exist')
                    else:
                        gui.popup('File extracted from archive successfully. Info about files from archive: ', read)
            if event == 'Remove':
                if(values['-FileName-'] == '' and values['-ArchiveName-'] == ''):
                    gui.popup('You should to fill all fields')
                else:
                    remove = zipArch.removeFiles(values['-ArchiveName-'], values['-FileName-'])
                    if remove == 'Error':
                        gui.popup('Sorry, the file does not exist')
                    else:
                        gui.popup('Files deleted successfully')
            if event == 'Return in main menu':
                zipWindow.close()
                self.drawStartWindow()
            if event == gui.WIN_CLOSED:
                break
        zipWindow.close()

    def drawStartWindow(self):
        gui.theme('DarkGreen')
        layoutButtons =[ [gui.Button('Check Info', size=(100, 1))],
                  [gui.Button('TXT File', size=(100, 1))],
                  [gui.Button('XML File', size=(100, 1))],
                  [gui.Button('JSON File', size=(100, 1))],
                  [gui.Button('ZIP Archive', size=(100, 1))] ]

        startWindow = gui.Window('Start Window', layoutButtons, size=(250, 180), element_justification='c')

        while True:
            event, values = startWindow.read()

            if event == 'Check Info' :
                startWindow.close()
                self.drawWindowInfo()

            if event == 'TXT File' :
                startWindow.close()
                self.drawWindowTxt()

            if event == 'XML File' :
                startWindow.close()
                self.drawWindowXml()

            if event == 'JSON File' :
                startWindow.close()
                self.drawWindowJson()

            if event == 'ZIP Archive' :
                startWindow.close()
                self.drawWindowZip()

            if event == gui.WIN_CLOSED :
                break