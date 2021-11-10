#!/usr/bin/env python2
# coding:utf-8
import os
from matplotlib import pyplot as plt  
import numpy as np
import shutil

#input------------------
if 'inputbase' == 'inputbase': 
    T                   = 500    #defolt 500
    alphaU_list         = [0]
    name_list0          = ["","","","",""]
    TopFolder           = "test_NACA0012"
    name_of_Root_folder = "Re10000"
    Re                  = 10000
    #20℃の時
    v                   = 15.12/1000000
    rho                 = 1.205

    if "no needed"=="no needed":
        f= 1
        c= 1
        ho_list= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        hwall = 0.01
        model ="kOmega"
        name_list=[]
        if name_list0[0]=="":
            for alphaU in alphaU_list:
                if alphaU <10:
                    name_list.append("a0"+str(alphaU))
                else:
                    name_list.append("a"+str(alphaU))
                    

        else:
            name_list = name_list0
        s_list= [0]
        #s_list= [0.125,0.375,0.625,0.875]
        k_list= [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
        npnp = 2
        n = "(2 1 1)"
        alpha0 = 0   #0 or 2.48


    if "blockMesh"=="blockMesh":
        zcell   = 180  #100
        xUcell  = 40  #40
        xMcell  = 40  #20
        xDcell  = 100  #60
        meshR   = 30   #30
        xMax    = 20    #20
        xDgrading=50
        zGgrading=50

#calculate------------------
if c != 0:
    name_of_Root_folder = TopFolder + "/"+ name_of_Root_folder
    u_list =[]
    nu_list =[]
    St_list =[]

    name_of_first_folder_list = s_list
    name_of_second_folder_list = k_list


    for k in k_list:
        if k != 0:
            u_list.append(Re*v/c)

    for i in range(len(u_list)):
        St_list.append(2*ho_list[i]*f/u_list[i])
        nu_list.append(v)
    omega=2*f*np.pi
    iterations = T/f
    writeEvery = 0.01/f

    number = int(len(name_of_Root_folder)-1)
    while os.path.exists(name_of_Root_folder) == True:
        name_of_Root_folder = name_of_Root_folder[:number]+str(int(name_of_Root_folder[number:])+1)

#output ---------------------
if "output"=="output":
    #if os.path.exists(dirname) == True:
    #    shutil.rmtree(dirname)
    #if folder=exist =>remove
    if os.path.exists(TopFolder) == False:
        os.mkdir(TopFolder)
    os.mkdir(name_of_Root_folder)
    count_st =0

    for i in range(len(s_list)):
        os.mkdir(name_of_Root_folder+"/s"+str(s_list[i]))
        #folder shutil.copytree
        #file shutil.copy
        shutil.copy("Mallrun",name_of_Root_folder+"/s"+str(s_list[i]))
        shutil.copy("Makemesh",name_of_Root_folder+"/s"+str(s_list[i]))
        f1 = open(name_of_Root_folder+"/s"+str(s_list[i])+'/Makemesh', 'a', encoding='UTF-8')
        f1.write( 
            "cd "+"k"+str(k_list[0])+"_"+name_list[0]+"\n"+"makeMesh\n"+"cd ..\n"
        )
        f1.close()


        for v in range(len(name_list)):
            f2 = open(name_of_Root_folder+"/s"+str(s_list[i])+'/Mallrun', 'a', encoding='UTF-8')
            f2.write( "cd "+"k"+str(k_list[v])+"_"+name_list[v]+"\n"+"simplefoam\n"+"cd ..\n")
            f2.close()
            f3 = open(name_of_Root_folder+"/s"+str(s_list[i])+'/Makemesh', 'a', encoding='UTF-8')
            if 0 < v:
                f3.write( 
                    "cp -r "+"k"+str(k_list[0])+"_"+name_list[0]+"/constant"+" k"+str(k_list[v])+"_"+name_list[v]+"\n"+"\n"
                    )
            f3.close()
            shutil.copytree('folder.orig', name_of_Root_folder+"/s"+str(s_list[i])+"/k"+str(k_list[v])+"_"+name_list[v])
            f = open(name_of_Root_folder+"/s"+str(s_list[i])+"/k"+str(k_list[v])+"_"+name_list[v]+'/initialConditions', 'a', encoding='UTF-8')
            if "f.write"=="f.write": 
                f.write(                        
                '\n'
                '	n	 '+	str( n )	+'	;	'	+'\n'
                '	np	 '+	str( npnp )	+'	;	'	+'\n'
                '	iterations	 '+	str( iterations	)	+'	;	'	+'\n'
                '	writeEvery	 '+	str(	writeEvery	)	+'	;	'	+'\n'
                '	alpha	 '+	str(	alphaU_list[v]	)	+'	;	'	+'\n'
                '	alpha0	 '+	str(	alpha0	)	+'	;	'	+'\n'
                '	chord	 '+	str(	c	)	+'	;	'	+'\n'
                '	CR	 '+	str(	''	)	+'	(0.25 0 0);	'	+'\n'
                '	pitch	 '+	str(	''	)	+'	(0 1 0);	'	+'\n'
                '	mach	 '+	str( u_list[v] )	+'	;	'	+'\n'
                '	Rair	 '+	str(	''	)	+' 287.05;	'	+'\n'
                '	gamma	 '+	str(	''	)	+'	1.4;	'	+'\n'
                '	Tref	 '+	str(	''	)	+'	293.15;	'	+'\n'
                '	muVal	 '+	str(	nu_list[v]	)	+'	;	'	+'\n'
                '	rhoVal	 '+	str(	rho	)	+'	;	'	+'\n'
                '	turbModel	 '+	str(	model	)	+'	;	'	+'\n'
                '	hWall	 '+	str(	hwall	)	+'	;	'	+'\n'
                '	omegaMotion	 '+	str(	omega	)	+'	;	'	+'\n'
                '	hlength	 '+	str(	ho_list[v]	)	+'	;	'	+'\n'
                '	wlength	 '+	str(	ho_list[v]*s_list[i]	)	+'	;	'	+'\n'
                )

            f.close()

            if "property.write"=="property.write": 
                propertyF = open(name_of_Root_folder+'/property', 'a', encoding='UTF-8')
                propertyF.write(                          
                '\n\n'+'	S_k_St	 '+	str( s_list[i] )+"_"+	str( k_list[v] )+"_"+	str( round(St_list[v],3) )	+'---------------	;	'	+'\n'
                '	zcell	 '+	str( zcell )	+'	;	'	+'\n'
                '	xUcell	 '+	str( xUcell )	+'	;	'	+'\n'
                '	xMcell	 '+	str( xMcell )	+'	;	'	+'\n'
                '	xDcell	 '+	str( xDcell )	+'	;	'	+'\n'
                '	xMin	 '+	str( -meshR )	+'	;	'	+'\n'
                '	xMax	 '+	str( xMax )	+'	;	'	+'\n'
                '	zMin	 '+	str( -(meshR+0.75) )	+'	;	'	+'\n'
                '	zMax	 '+	str( meshR-0.75 )	+'	;	'	+'\n'
                '	radiusH	 '+	str( meshR )	+'	;	'	+'\n'
                '	n	 '+	str( n )	+'	;	'	+'\n'
                '	np	 '+	str( npnp )	+'	;	'	+'\n'
                '	iterations	 '+	str( iterations	)	+'	;	'	+'\n'
                '	alpha	 '+	str(	alphaU_list[v]	)	+'	;	'	+'\n'
                '	alpha0	 '+	str(	alpha0	)	+'	;	'	+'\n'
                '	mach	 '+	str( u_list[v] )	+'	;	'	+'\n'
                '	muVal	 '+	str(	nu_list[v]	)	+'	;	'	+'\n'
                '	turbModel	 '+	str(	model	)	+'	;	'	+'\n'
                '	hWall	 '+	str(	hwall	)	+'	;	'	+'\n'
                '	omegaMotion	 '+	str(	omega	)	+'	;	'	+'\n'
                '	hlength	 '+	str(	ho_list[v]	)	+'	;	'	+'\n'
                '	wlength	 '+	str(	ho_list[v]*s_list[i]	)	+'	;	'	+'\n'
                )
                
                propertyF.close()