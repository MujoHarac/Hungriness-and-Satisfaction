import random
# zemun_kiklop = [{'hrana': 'Gyros 700g' , 'cena': 800 , 'koeficijent': 1.9},
#                 {'hrana': 'Kiklop hamburger 300g' , 'cena': 590 , 'koeficijent': 1.4},
#                 {'hrana': 'Kebab rolls 225g' , 'cena': 550, 'koeficijent': 1.3},
#                 {'hrana': 'Pancakes(eurokrem,banana,plazma)' , 'cena': 390 , 'koeficijent': 1.2}
#                 ]
# for i in zemun_kiklop:
#     print(i['hrana'])
# k = input('ime hrane: ')
# for i in zemun_kiklop:
#     if k in i['hrana']:
# ##        print(i['cena'])  
#


tags = {'broad': {'meat': (1,2), 'vegetable': (2, 1), 'sweet': (3,1), 'sandwich':(4,1)},
         'specific': {'eggs': (4,1), 'bun': (5,1)}}

# #print(tags['broad'])
# for i in tags:
#     print(tags[i])
#     for j in tags[i]:
#         print(j,tags[i][j][0])

# call = 'asd'

# brick = ['12', '23', '23', call, '23']
# index = brick.index(call)
# print(index)


distance_between_places_using_main_roud = (
                            (('start_1','roud'), 100),
                            (('start_2','roud'), 50),
                            (('Zemun','roud'), 200),
                            (('Vracar','roud'), 150),
                            (('Novi Beograd', 'roud'), 300),
                            (('Zvezdara','roud'), 350),
                            (('Vozdovac','roud'), 450),
                            (('Grocka','roud'), 200),
                            )

distance_between_places_that_are_connected = (
                            (('Vracar','Zvezdara'), 200),
                            (('Zemun','Novi Beograd'), 50),

                                            )

for i in distance_between_places_that_are_connected:
    print(i[0])

print(random.choice(tags['broad']['meat']))

print(round(1/40))