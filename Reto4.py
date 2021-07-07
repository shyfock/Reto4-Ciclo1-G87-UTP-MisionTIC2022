from datos import d

def estudio(d:dict,codDep:str,codRes:int):
    if codRes == 1:
        Ans = Codigo1(codDep)
        return Ans
    elif codRes == 2:
        Ans = Codigo2(codDep)
        return Ans
    elif codRes == 3:
        Ans = ALS_MaxPR(Codigo3(codDep)[0], Codigo3(codDep)[1])
        return Ans
    return f'Código Errado'

def Codigo1(codDep:str):
    minTL = Max_Min(codDep)['Latencias'][0]
    maxPR = Max_Min(codDep)['Rendimientos'][1]
    AppMinTL = list(d[codDep])[minTL]['App']
    AppMaxPR = list(d[codDep])[maxPR]['App']
    Par1 = (list(d[codDep])[minTL]['LP'],list(d[codDep])[minTL]['SGBD'])
    Par2 = (list(d[codDep])[maxPR]['LP'],list(d[codDep])[maxPR]['SGBD'])
    return (AppMinTL, AppMaxPR, Par1, Par2)
    
def Codigo2(codDep:str):
    maxTL = Max_Min(codDep)['Latencias'][1]
    minPR = Max_Min(codDep)['Rendimientos'][0]
    Par1 = (list(d[codDep])[maxTL]['App'],list(d[codDep])[minPR]['App'])
    Par2 = (list(d[codDep])[maxTL]['LP'],list(d[codDep])[maxTL]['SGBD'])
    Par3 = (list(d[codDep])[minPR]['LP'],list(d[codDep])[minPR]['SGBD'])
    return [Par1, Par2, Par3]

def ALS_MaxPR(cod1:str, cod2:str):
    minTL = Max_Min(cod1)['Latencias'][0]
    AppMinTL = d[cod1][minTL]['App']
    LPMinTL = d[cod1][minTL]['LP']
    SGBDMinTL = d[cod1][minTL]['SGBD']
    maxPR = Max_Min(cod2)['Rendimientos'][1]
    AppMaxPR = d[cod2][maxPR]['App']
    LPMaxPR = d[cod2][maxPR]['LP']
    SGBDMaxPR = d[cod2][maxPR]['SGBD']
    return [(AppMinTL, LPMinTL, SGBDMinTL), (AppMaxPR, LPMaxPR, SGBDMaxPR)]

def Max_Min(codDep:str):
    latenList = [int(d[codDep][i]['Latencia']) for i in range(len(d[codDep]))]
    rendList = [float(d[codDep][i]['Rendimiento']) for i in range(len(d[codDep]))]
    minTL = latenList.index(min(latenList))
    maxTL = latenList.index(max(latenList))
    minPR = rendList.index(min(rendList))
    maxPR = rendList.index(max(rendList))
    return {'Latencias': (minTL, maxTL), 'Rendimientos': (minPR, maxPR)}

def Codigo3(codDep:str):
    LL1 = []
    LL2 = []
    ListDep = list(d.keys())
    ListDep.remove(codDep)
    ListIndMinTL = [list(map(Max_Min,ListDep))[i]['Latencias'][0] for i in range(len(ListDep))]
    ListIndMaxPR = [list(map(Max_Min,ListDep))[i]['Rendimientos'][1] for i in range(len(ListDep))]
    DepMinTL = list(zip(ListDep, ListIndMinTL, ListIndMaxPR))
    for i in DepMinTL:
        LL1.append(d[i[0]][i[1]]['Latencia'])
        LL2.append(d[i[0]][i[2]]['Rendimiento'])
    MinTL = DepMinTL[LL1.index(min(LL1))][0]
    MaxPR = DepMinTL[LL2.index(max(LL2))][0]
    return [MinTL, MaxPR]

print(estudio(d, "IDI09", 2))