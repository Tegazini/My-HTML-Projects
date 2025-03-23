
'''Geologic Time'''
import sys
print("***GEOLOGIC TIME CALCULATOR***")

eons = {'Phanerozoic':'Below 542Ma',
        'Proterozoic':'2500-542Ma',
        'Archean':'4000-2500Ma',
        'Hadean':'4600-4000Ma'
        }
eras = {'Eoarchean':'4000-3600Ma',
        'Paleoarchean':'3600-3200Ma',
        'Mesoarchean':'3200-2800Ma',
        'Neoarchean':'2800-2500Ma',
        'Paleoproterozoic':'2500-1600Ma',
        'Mesoproterozoic':'1600-1000Ma',
        'Neoproterozoic':'1000-542Ma',
        'Paleozoic':'542-251Ma',
        'Mesozoic':'251-65.5Ma',
        'Cenozoic':'Below 65.5Ma',
        
        }
periods = {'Siderian':'2500-2300Ma',
           'Rhyacian':'2300-2050Ma',
           'Orosirian':'2050-1800Ma',
           'Statherian':'1800-1600Ma',
           'Calymmian':'1600-1400My',
           'Ecstacian':'1400-1200Ma',
           'Stenian':'1200-1000Ma',
           'Tonian':'1000-720Ma',
           'Cryogenian':'720-635Ma',
           'Ediacaran':'635-542Ma',
           'Cambrian':'542-488Ma',
           'Ordovician':'488-444Ma',
           'Silurian':'444-416Ma',
           'Devonian':'416-359Ma',
           'Carboniferous':'359-299Ma',
           'Permian':'299-251Ma',
           'Triassic':'251-199.6Ma',
           'Jurassic':'199.6-145.5Ma',
           'Cretacious':'145.5-65.5Ma',
           'Tertiary':'65.5-2.6Ma',
           'Quarternary':'Below 2.6Ma'
           }
initializing = 0

while initializing != 1:
    try:
    
        print("Enter 1 to terminate and ANY NUMBER to continue.")
        initializing = int(input())
        if initializing == 1:
            print("CALCULATOR TERMINATED!!!")
            print("GOODBYE!")
            sys.exit()

        
        else:

            def geologic_time(age = float(input('Enter age in miilions of years:\n'))):
                if age > 4000 and age <=4600:
                    Eon = 'Hadean'
                    Era = 'Unknown'
                    Period = 'Unknown'
                    Epoch = 'Unknown'
                    Age = 'Unknown'
                    print('Eon=' + Eon, 'Era=' + Era, 'Period=' + Period, 'Epoch=' + Epoch, 'Age=' + Age, sep='\n')

                elif age > 2500 and age <= 4000:
                    Eon = 'Archean'
                    if age >3600 and age <= 4000:
                        Era = 'Eoarchian'
                    elif age > 3200 and age <= 3600:
                        Era = 'Paleoarchean'
                    elif age >2800 and age <= 3200:
                        Era = 'Mesoarchean'
                    elif age >2500 and age <= 2800:
                        Era = 'Neoarchean'
                    Period = 'Unknown'
                    Epoch = 'Unknown'
                    Age = 'Unknown'
                    print('Eon=' + Eon, 'Era=' + Era, 'Period=' + Period, 'Epoch=' + Epoch, 'Age=' + Age, sep='\n')

                elif age >= 542 and age <= 2500:
                    Eon = 'Proterozoic'
                    if age >=1600 and age <= 2500:
                        Era = 'Paleoproterozoic'
                        if age >=2300 and age <= 2500:
                            Period = 'Siderian'
                        elif age >=2050 and age <= 2300:
                            Period = 'Rhyacian'
                        elif age >=1800 and age <= 2050:
                            Period = 'Orosirian'
                        elif age >= 1600 and age <= 1800:
                            Period = 'Statherian'
                    elif age >= 1000 and age <= 1600:
                        Era = 'Mesoproterozoic'
                        if age >=1400 and age <= 1600:
                            Period = 'Calymmian'
                        elif age >=1200 and age <= 1400:
                            Period = 'Ecstacian'
                        elif age >=1000 and age <= 1200:
                            Period = 'Stenian'
                    elif age >=542 and age <= 1000:
                        Era = 'Neoproterozoic'
                        if age >=720 and age <= 1000:
                            Period = 'Tonian'
                        elif age >=635 and age <= 720:
                            Period = 'Cryogenian'
                        elif age >542 and age <= 635:
                            Period = 'Ediacaran'
                    Epoch = 'Unknown'
                    Age = 'Unknown'
                    print('Eon=' + Eon, 'Era=' + Era, 'Period=' + Period, 'Epoch=' + Epoch, 'Age=' + Age, sep='\n')
                elif age < 542:
                    Eon = 'Phanerozoic'
                    if age >=251 and age <542:
                        Era = 'Paleozoic'
                        if age >=488 and age < 542:
                            Period = 'Cambrian'
                            if age >=521 and age <542:
                                Epoch = 'Terreneuvian'
                                if age >=529 and age <542:
                                    Age = 'Fortunian'
                                elif age >=521 and age <=529:
                                    Age = 'Age 2'
                            elif age >=509 and age <=521:
                                Epoch = 'Epoch 2'
                                if age >=514 and age <=521:
                                    Age = 'Age 3'
                                elif age >=509 and age <=514:
                                    Age = 'Age 4'
                            elif age >=497 and age <=509:
                                Epoch = 'Epoch 3'
                                if age >=504.5 and age <=509:
                                    Age = 'Age 5'
                                elif age >= 500.5 and age <=504.5:
                                    Age = 'Drumian'
                                elif age >=497 and age <=500.5:
                                    Age = 'Guzhangian'
                            elif age >=488 and age <=497:
                                Epoch = 'Furongian'
                                if age >=494 and age <= 497:
                                    Age = 'Paibian'
                                elif age >=489.5 and age <=494:
                                    Age = 'Jiangshanian'
                                elif age >=488 and age <=489.5:
                                    Age = 'Age 10'
                        elif age >= 444 and age <= 488:
                            Period = 'Ordovician'
                            if age >=470 and age <=488:
                                Epoch = 'Early Ordovician'
                                if age >=477.7 and age <=488:
                                    Age = 'Tremadocian'
                                elif age >=470 and age <=477.7:
                                    Age = 'Floian'
                            elif age >=458.4 and age <=470:
                                Epoch = 'Middle Ordovician'
                                if age >=467.3 and age <=470:
                                    Age = 'Dapingian'
                                elif age >=458.4 and age <=467.3:
                                    Age = 'Darriwilian'
                            elif age >=444 and age <=458.4:
                                Epoch = 'Late Ordovician'
                                if age >=453 and age <=458.4:
                                    Age = 'Sandbian'
                                elif age >=445.2 and age <=453:
                                    Age = 'Katian'
                                elif age >=444 and age <=445.2:
                                    Age = 'Hirnantian'
                        elif age >= 416 and age <444:
                            Period = 'Silurian'
                            if age >=433.4 and age <444:
                                Epoch = 'Llandovery'
                                if age >=440.8 and age <=444:
                                    Age = 'Rhuddanian'
                                elif age >=438.5 and age <=440.8:
                                    Age = 'Aeronian'
                                elif age >=433.4 and age <=438.5:
                                    Age = 'Telychian'
                            elif age >=427.4 and age <=433.4:
                                Epoch = 'Wenlock'
                                if age >=430.5 and age <=433.4:
                                    Age = 'Sheinwoodian'
                                elif age >=427.4 and age <=430.5:
                                    Age = 'Homerian'
                            elif age >=423 and age <=427.4:
                                Epoch = 'Ludlow'
                                if age >=425.6 and age <=427.4:
                                    Age = 'Gorstian'
                                elif age >=423 and age <=425.6:
                                    Age = 'Ludfordian'
                            elif age >=416 and age <=423:
                                Epoch = 'Pridoli'
                                Age = 'Unspecified'
                        elif age >= 359 and age <=416:
                            Period = 'Devonian'
                            if age >=393.3 and age <=416:
                                Epoch = 'Early Devonian'
                                if age >=410.8 and age <=416:
                                    Age = 'Lochkovian'
                                elif age >=407.6 and age <=410.8:
                                    Age = 'Pragian'
                                elif age >=393.3 and age <=407.6:
                                    Age = 'Emsian'
                            elif age >=382.7 and age <=393.3:
                                Epoch = 'Middle Devonian'
                                if age >=387.7 and age <=393.3:
                                    Age = 'Eifelian'
                                elif age >=382.7 and age <=387.7:
                                    Age = 'Givetian'
                            elif age >=359 and age <=382.7:
                                Epoch = 'Late Devonian'
                                if age >=372.2 and age <=382.7:
                                    Age = 'Frasnian'
                                elif age >=359 and age <=372.2:
                                    Age = 'Famennian'
                        elif age >= 324 and age < 359:
                            Period = 'Carboniferous(Mississippian)'
                            if age >=346.7 and age <359:
                                Epoch = 'Early Mississippian'
                                Age = 'Tournaisian'
                            elif age >=330.9 and age <=346.7:
                                Epoch = 'Middle Mississippian'
                                Age = 'Visean'
                            elif age >324 and age <=330.9:
                                Epoch = 'Late Mississippian'
                                Age = 'Serpukhovian'
                        elif age >= 299 and age < 324:
                            Period = 'Carboniferous(Pennsylvanian)'
                            if age >=315.2 and age <324:
                                Epoch = 'Early Pennsylvanian'
                                Age = 'Bashkirian'
                            elif age >=307 and age <=315.2:
                                Epoch = 'Middle Pennsylvanian'
                                Age = 'Moscovian'
                            elif age >=299 and age <=307:
                                Epoch = 'Late Pennsylvanian'
                                if age >=303.7 and age <=307:
                                    Age = 'Kasimovian'
                                elif age >=299 and age <=303.7:
                                    Age = 'Gzhelian'
                        elif age >= 251 and age <= 299:
                            Period = 'Permian'
                            if age >=272.95 and age <=299:
                                Epoch = 'Cisuralian'
                                if age >=295 and age <=299:
                                    Age = 'Asselian'
                                elif age >=290.1 and age <=295:
                                    Age = 'Sakmarian'
                                elif age >=283.5 and age <=290.1:
                                    Age = 'Artinskian'
                                elif age >=272.95 and age <=283.5:
                                    Age = 'Kungurian'
                            elif age >=259.1 and age <=272.95:
                                Epoch = 'Guadalupian'
                                if age >=268.8 and age <=272.95:
                                    Age = 'Roadian'
                                elif age >=265.1 and age <=268.8:
                                    Age = 'Wordian'
                                elif age >= 259.1 and age <= 265.1:
                                    Age = 'Capitanian'
                            elif age >=251 and age <=259.1:
                                Epoch = 'Lopingian'
                                if age >=254.14 and age <=259.1:
                                    Age = 'Wuchiapingian'
                                elif age >=251 and age <=254.14:
                                    Age = 'Changhsingian'
                    elif age >=65.5 and age <=251:
                        Era = 'Mesozoic'
                        if age >=201.3 and age <=251:
                            Period = 'Triassic'
                            if age >=247.2 and age <=251:
                                Epoch = 'Early Triassic'
                                if age >=250 and age <=251:
                                    Age = 'Induan'
                                elif age >=247.2 and age <=250:
                                    Age = 'Olenekian'
                            elif age >=237 and age<=247.2:
                                Epoch = 'Middle Triassic'
                                if age >=242 and age <=247.2:
                                    Age = 'Anisian'
                                elif age >=237 and age <=242:
                                    Age = 'Ladinian'
                            elif age >=201.3 and age <=237:
                                Epoch = 'Late Triassic'
                                if age >=227 and age <=237:
                                    Age = 'Carnian'
                                elif age >=208.5 and age <=227:
                                    Age = 'Norian'
                                elif age >=201.3 and age <=208.5:
                                    Age = 'Rhaetian'
                        elif age >=145.5 and age <=201.3:
                            Period = 'Jurassic'
                            if age >=174.1 and age <=201.3:
                                Epoch = 'Early Jurassic'
                                if age >=199.3 and age <=201.3:
                                    Age = 'Hettangian'
                                elif age >=190.8 and age <=199.3:
                                    Age = 'Sinemurian'
                                elif age >=182.7 and age <=190.8:
                                    Age = 'Pliensbachian'
                                elif age >=174.1 and age <=182.7:
                                    Age = 'Toarcian'
                            elif age >=163.5 and age <=174.1:
                                Epoch = 'Middle Jurassic'
                                if age >=170.3 and age <=174.1:
                                    Age = 'Aalenian'
                                elif age >=168.3 and age <=170.3:
                                    Age = 'Bajocian'
                                elif age >=166.1 and age <=168.3:
                                    Age = 'Bathonian'
                                elif age >=163.5 and age <=166.1:
                                    Age = 'Callovian'
                            elif age >=145.5 and age <=163.5:
                                Epoch = 'Late Jurassic'
                                if age >=157.3 and age <=163.5:
                                    Age = 'Oxfordian'
                                elif age >=152.1 and age <=157.3:
                                    Age = 'Kimmeridgian'
                                elif age >=145.5 and age <=152.1:
                                    Age = 'Tithonian'
                        elif age >=65.5 and age <=145.5:
                            Period = 'Cretaceous'
                            if age >=100.5 and age <=145.5:
                                Epoch = 'Early Cretaceous'
                                if age >= 139.8 and age <=145.5:
                                    Age = 'Berriasian'
                                elif age >=132.9 and age <=139.8:
                                    Age = 'Valanginian'
                                elif age >=129.4 and age <=132.9:
                                    Age = 'Hauterivian'
                                elif age >=125 and age <=129.4:
                                    Age = 'Barremian'
                                elif age >=113 and age <=125:
                                    Age = 'Aptian'
                                elif age >=100.5 and age <=113:
                                    Age = 'Albian'
                            elif age >=65.5 and age <= 100.5:
                                Epoch = 'Late Cretaceous'
                                if age >=93.9 and age <=100.5:
                                    Age = 'Cenomanian'
                                elif age >=89.8 and age <=93.9:
                                    Age = 'Turonian'
                                elif age >=86.3 and age <=89.8:
                                    Age = 'Coniacian'
                                elif age >=83.6 and age <=86.3:
                                    Age = 'Santonian'
                                elif age >=72.1 and age <=83.6:
                                    Age = 'Campanian'
                                elif age >=65.5 and age <=72.1:
                                    Age = 'Maastrichtian'
                    elif age < 65.5:
                        Era = 'Cenozoic'
                        if age >=23.03 and age < 65.5:
                            Period = 'Tertiary(Paleogene)'
                            if age >=56 and age <65.5:
                                Epoch = 'Paleocene'
                                if age >=61.6 and age <65.5:
                                    Age = 'Danian'
                                elif age >= 59.2 and age <=61.6:
                                    Age = 'Selandian'
                                elif age >=56 and age <=59.2:
                                    Age = 'Thanetian'
                            elif age >=33.9 and age <=56:
                                Epoch = 'Eocene'
                                if age >=47.8 and age <=56:
                                    Age = 'Ypresian'
                                elif age >=41.2 and age <=47.8:
                                    Age = 'Lutetian'
                                elif age >=37.8 and age <=41.2:
                                    Age = 'Bartonian'
                                elif age >=33.9 and age <=37.8:
                                    Age = 'Priabonian'
                            elif age >=23.03 and age <=33.9:
                                Epoch = 'Oligocene'
                                if age >=27.82 and age <=33.9:
                                    Age = 'Rupelian'
                                elif age >=23.03 and age <=27.82:
                                    Age = 'Chattian'
                        elif age >=2.6 and age <=23.03:
                            Period = 'Tertiary(Neogene)'
                            if age >=5.33 and age <=23.03:
                                Epoch = 'Miocene'
                                if age >=20.44 and age <=23.03:
                                    Age = 'Aquitanian'
                                elif age >=15.97 and age <=20.44:
                                    Age = 'Burdigalian'
                                elif age >=13.82 and age <=15.97:
                                    Age = 'Langhian'
                                elif age >=11.63 and age <=13.82:
                                    Age = 'Serravallian'
                                elif age >=7.246 and age <=11.63:
                                    Age = 'Tortonian'
                                elif age >=5.33 and age <=7.246:
                                    Age = 'Messinian'
                            elif age >=2.6 and age <=5.33:
                                Epoch = 'Pliocene'
                                if age >=3.6 and age <=5.33:
                                    Age = 'Zanclean'
                                elif age >=2.6 and age <=3.6:
                                    Age = 'Piacenzian'
                        elif age < 2.6:
                            Period = 'Quarternary'
                            if age >=0.012 and age <2.6:
                                Epoch = 'Pleistocene'
                                if age >= 1.8 and age <2.6:
                                    Age = 'Gelasian'
                                elif age >=0.012 and age <=1.8:
                                    Age = 'Calabrian'
                            elif age <0.012:
                                Epoch = 'Holocene'
                                Age = 'Recent'
        
                    print('Eon=' + Eon, 'Era=' + Era, 'Period=' + Period, 'Epoch=' + Epoch, 'Age=' + Age, sep='\n')
        
                else:
                    print('The age inputed is out of range. \nThe earth is 4.6Billion years old!!!')
            geologic_time()                   
        
    except ValueError:
        print('Invalid Input!')
    continue
