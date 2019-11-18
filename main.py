
def del_expansions(directory, expansions):
    for filename in os.listdir(directory):
        for expansion in expansions:
            if filename.endswith(expansion):
                os.remove(directory + filename)

def remove_old_files(directory):
    for filename in os.listdir(directory):
        if os.path.getmtime(os.path.join(directory, filename)) < time.time() - 7 * 86400:
            if os.path.isfile(os.path.join(directory, filename)):
                os.remove(os.path.join(directory, filename))

def files_sort(directory):
    for filename in os.listdir(directory):
        if "6001000149_" and "_РайпоБежаницы-" in filename:
            if ".rnp" in filename:
                os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename)
            else:
                os.rename(directory + filename, directory + 'Пушгоры_МСЗ/' + filename + 'горячий_хлеб.rnp')
        elif "6027108130" and "_Д" in filename:
            os.rename(directory + filename, directory + 'Дива_Плюс/' + filename)
        elif "6027149513" and "_УТ" in filename:
            os.rename(directory + filename, directory + 'Дитрейд/' + filename)
        elif "6027173812" and "_5ГК" in filename:
            os.rename(directory + filename, directory + 'Мега_Холод/' + filename)
        elif "7802548281_РЛ" in filename:
            os.rename(directory + filename, directory + 'Региональная_Логистика/' + filename)
        elif "7811215747_ГЛ" in filename:
            os.rename(directory + filename, directory + 'Глобал_Лоджистикс/' + filename)
        elif "532111776395_" in filename:
            os.rename(directory + filename, directory + 'Пр._Никоноров/' + filename)


if __name__ == "__main__":
    import os, time
    directory = r'//RAIPO_MAIN/Mail_Exchange/'
    expansions = ['-1.rnp','(1).rnp', '.txt', '.png', '.jpg', '.JPG', '.xls', '.html', '.pdf', '.xlsx',
                  '.ppt', '.doc', '.zip', '.eml', '.xml', '.docx', '.rar', '.gif', '.odt', '.ods', '.DOC']
    del_expansions(directory, expansions)
    remove_old_files(directory)
    files_sort(directory)

