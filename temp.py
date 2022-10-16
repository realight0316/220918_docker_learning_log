import os
import pandas as pd

def a_data_to_csv(file, filename):
    result = pd.DataFrame({'host':[], 'up':[], 'down':[]})
    i = 0
    temp = pd.DataFrame({'host':[], 'up':[], 'down':[]})
    for f in file:
        f = f.split()
        if f[0] == 'Host:':
            i = 0
            temp.at[0, 'host'] = f[1]
            result = pd.concat([result, temp], ignore_index=True)
            temp = pd.DataFrame({'host':[], 'up':[], 'down':[]})
        elif i == 1:
            temp.at[0, 'up'] = f[0][-5:]
        else:
            temp.at[0, 'down'] = f[0][-5:]
            i += 1
    print(result)
    return result.to_csv(f'./csv/{filename[:-4]}.csv', index=False)
        

def b_data_to_csv(file, filename):
    result = pd.DataFrame({'host':[], 'up':[], 'down':[]})
    temp = pd.DataFrame({'host':[], 'up':[], 'down':[]})
    for f in file:
        f = f.split()
        if 'PARAM' in f[0]:
            temp.at[0, 'host'] = f[1]
        elif 'INFO' == f[1] and 'DOWNLOAD' in f[3]:
            temp.at[0, 'down'] = f[5][:-1]
        elif 'INFO' == f[1] and 'UPLOAD' in f[3]:
            temp.at[0, 'up'] = f[5][:-1]
            result = pd.concat([result, temp], ignore_index=True)
            temp = pd.DataFrame({'host':[], 'up':[], 'down':[]})
    print(result)
    return result.to_csv(f'./csv/{filename[:-4]}.csv', index=False)

for filename in os.listdir('./log'):
    with open(f'./log/{filename}', 'r+') as file:
        if 'AAA' in filename:
            print('A')
            benchbee_to_csv(file, filename)
        else:
            print('B')
            softfusion_to_csv(file, filename)