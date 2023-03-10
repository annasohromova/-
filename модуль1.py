def Lisa_andmed(i:list,p:list):
    """Kirjeldus 
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def Kustutamine(i:list,p:list):
    """ Определение индекса человека и удаляние его
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p 

def Suurim_palk(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def Väiksem_palk(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def Sorteerimine(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    v=int(input("palk 1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi
                    abi=i[j] 
                    i[j]=p[k] 
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi
                    abi=i[j] 
                    i[j]=p[k] 
                    i[k]=abi

    return i,p


def Vordses_palgad(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid: #1200, n=2; 750, n=2
        n=p.count(palk)
        k=-1 #------
        print(f"(palk) saavad kätte järgmised inimesed: ")
        for j in range(n):
            k=p.index(palk,k+1)#---------
            nimi=i[k]
            print(nimi)
