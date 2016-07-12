
import regex


files_to_process = ['C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 CZ CZK.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 DEN DKK.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 MAR MAD.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 NOR NOK.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 PL PLN.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 RCIS countries.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 SWE SEK.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 SWI CHF.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 UK GBP.csv',
                    'C:/Work/Projects/WWPRT/Migration/zFix/LSCDx02062016 ZA ZAR.csv'
                    ]
folder = 'C:/Work/Projects/WWPRT/Migration/zFix/csv/'
pattern = regex.compile(pattern=r',$')
for file_name in files_to_process:
    file = open(file=file_name, mode='r')
    name = file.name.split('/')[-1]
    lines = file.readlines()
    new_lines = []
    for line in lines:
        new_line = pattern.sub(repl='', string=line)
        new_lines.append(new_line)
    new_file = open(file=folder + name, mode='w')
    for ln in new_lines:
        new_file.write(ln)
