Dad = {'Ming': 'haibo',
       'Xing': 'Liang',
       'age' : '49',
       'city' : 'Huaibei',
       }

Mom = {'Ming': 'wen',
       'Xing': 'Yang',
       'age' : '46',
       'city' : 'Huaibei',
       }

Gf = {'Ming': 'yang',
       'Xing': 'Jin',
       'age' : '23',
       'city' : 'Beijing',
       }

people = [Dad,Mom,Gf]

for ren in people:
    for key,value in ren.items():
        print('Key:' + key)
        print('Value:' + value)
    print('\n')