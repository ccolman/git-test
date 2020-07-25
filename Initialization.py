#!/usr/bin/python2

import random
from dijkstar import Graph, find_path

def solve(Pnodes, Nodenum, VNodenum, VNFnum, VNF, SFCnum, Source, Destination, SFCname, Latency, SVNFnumber, SVNF, c, Q, v, suit):
    solution = [[0 for o in range(SVNFnumber[k])] for k in range(SFCnum)]

    Pnodes_before = [[0 for feature in range(3)] for i in range(VNodenum)]
    for i in range(VNodenum):
        Pnodes_before[i][0] = Pnodes[i].get('PCPU')
        Pnodes_before[i][1] = Pnodes[i].get('Pbw')
        Pnodes_before[i][2] = Pnodes[i].get('Poeo')
    Pnodes_used = [[0 for feature in range(3)] for i in range(VNodenum)]
#THIS IS A TEST OF GIT
    #Generate Initial Solutions for the Latency Minimization
    for i in range(VNodenum):
        Pnodes_used[i][0] = Pnodes_before[i][0]
        Pnodes_used[i][1] = Pnodes_before[i][1]
        Pnodes_used[i][2] = Pnodes_before[i][2]
    for k in range(SFCnum):
        for o in range(SVNFnumber[k]):
            for a in range(VNFnum):
                if (VNF[a]['Name'] == SVNF[k][o]):
                    if (Pnodes_used[Source[k]][0] > VNF[a]['FCPU']*v[k][o]) and (Pnodes_used[Source[k]][1] > VNF[a]['Fbw']*v[k][o]) and (Pnodes_used[Source[k]][2] > VNF[a]['Foeo']*v[k][o]) and (suit[Source[k]][k][o] == 1):
                        solution[k][o] = Source[k]
                        Pnodes_used[Source[k]][0] = Pnodes_used[Source[k]][0] - VNF[a].get('FCPU')*v[k][o]
                        Pnodes_used[Source[k]][1] = Pnodes_used[Source[k]][1] - VNF[a].get('Fbw')*v[k][o]
                        Pnodes_used[Source[k]][2] = Pnodes_used[Source[k]][2] - VNF[a].get('Foeo')*v[k][o]
                    elif (Pnodes_used[Destination[k]][0] > VNF[a]['FCPU']*v[k][o]) and (Pnodes_used[Destination[k]][1] > VNF[a]['Fbw']*v[k][o]) and (Pnodes_used[Destination[k]][2] > VNF[a]['Foeo']*v[k][o]) and (suit[Destination[k]][k][o] == 1):
                        solution[k][o] = Destination[k]
                        Pnodes_used[Destination[k]][0] = Pnodes_used[Destination[k]][0] - VNF[a].get('FCPU')*v[k][o]
                        Pnodes_used[Destination[k]][1] = Pnodes_used[Destination[k]][1] - VNF[a].get('Fbw')*v[k][o]
                        Pnodes_used[Destination[k]][2] = Pnodes_used[Destination[k]][2] - VNF[a].get('Foeo')*v[k][o]
                    elif (Pnodes_used[2][0] > VNF[a]['FCPU']*v[k][o]) and (Pnodes_used[2][1] > VNF[a]['Fbw']*v[k][o]) and (Pnodes_used[2][2] > VNF[a]['Foeo']*v[k][o]) and (suit[2][k][o] == 1):
                        solution[k][o] = 2
                        Pnodes_used[2][0] = Pnodes_used[2][0] - VNF[a].get('FCPU')*v[k][o]
                        Pnodes_used[2][1] = Pnodes_used[2][1] - VNF[a].get('Fbw')*v[k][o]
                        Pnodes_used[2][2] = Pnodes_used[2][2] - VNF[a].get('Foeo')*v[k][o]
                    elif (Pnodes_used[3][0] > VNF[a]['FCPU']*v[k][o]) and (Pnodes_used[3][1] > VNF[a]['Fbw']*v[k][o]) and (Pnodes_used[3][2] > VNF[a]['Foeo']*v[k][o]) and (suit[3][k][o] == 1):
                        solution[k][o] = 3
                        Pnodes_used[3][0] = Pnodes_used[3][0] - VNF[a].get('FCPU')*v[k][o]
                        Pnodes_used[3][1] = Pnodes_used[3][1] - VNF[a].get('Fbw')*v[k][o]
                        Pnodes_used[3][2] = Pnodes_used[3][2] - VNF[a].get('Foeo')*v[k][o]

    return solution, Pnodes_used

