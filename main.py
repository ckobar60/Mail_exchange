#!/usr/local/bin/python3.5m
#-*- coding: utf-8 -*-
def del_expansions(directory, expansions):
    for filename in os.listdir(directory):
        for expansion in expansions:
            if filename.endswith(expansion):
                os.remove(directory + filename)


def remove_old_files(directory):
    for dir in os.listdir(directory):
        dirs.append(directory + dir )
        for dir in dirs:
            path = str(dir)
            now = time.time()
            for filename in os.listdir(path):
                if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
                    if os.path.isfile(os.path.join(path, filename)):
                        os.remove(os.path.join(path, filename))
            

def files_sort(directory):
    for filename in os.listdir(directory):

        if "6001000149_" and "_РайпоБежаницы-Дедовичи" in filename:
            if ".rnp" in filename:
                os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename)
            else:
                os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename + '.rnp')
        
        elif "6001000149_" and "_РайпоБежаницы-склад" in filename:
            try:
                if ".rnp" in filename:
                    os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename)
                else:
                    os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename + '.rnp')
            except:
                os.remove(directory + filename)
                
        elif "6001000149_" and "_РайпоБежаницы" in filename:
            try:
                if ".rnp" in filename:
                    os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename)
                else:
                    os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename + 'горячий_хлеб.rnp')
            except:
                os.remove(directory + filename)

        elif "6027108130" and "_Д" in filename:
            try:
                os.rename(directory + filename, directory + 'Дива_Плюс/' + filename)
            except:
                os.remove(directory + filename)

        elif "6027149513" and "_УТ" in filename:
            try:
                os.rename(directory + filename, directory + 'Дитрейд/' + filename)
            except:
                os.remove(directory + filename)

        elif "6027173812" and "_5ГК" in filename:
            try:
                os.rename(directory + filename, directory + 'Мега_Холод/' + filename)
            except:
                os.remove(directory + filename)

        elif "7802548281_РЛ" in filename:
            try:
                os.rename(directory + filename, directory + 'Региональная_Логистика/' + filename)
            except:
                os.remove(directory + filename)

        elif "7811215747_ГЛ" in filename:
            try:
                os.rename(directory + filename, directory + 'Глобал_Лоджистикс/' + filename)
            except:
                os.remove(directory + filename)
        
        elif "532111776395_" in filename:
            try:    
                os.rename(directory + filename, directory + 'Пр._Никоноров/' + filename)
            except:
                os.remove(directory + filename)


if __name__ == "__main__":
    import os, time
    directory = r'/volume1/Mail_Exchange/'
    dirs=[]
    expansions = ['-1.rnp', '(1).rnp', '(2).rnp', '(3).rnp', '(4).rnp', '(5).rnp', '.txt', '.png', '.jpg', '.JPG', '.xls', '.html', '.pdf', '.xlsx',
                  '.ppt', '.doc', '.zip', '.eml', '.xml', '.docx', '.rar', '.gif', '.odt', '.ods', '.DOC']
    del_expansions(directory, expansions)
    files_sort(directory)
    remove_old_files(directory)
