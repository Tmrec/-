#!/usr/bin/env python2
# coding:utf-8

import os
from matplotlib import pyplot as plt  
import numpy as np
import shutil
from matplotlib import animation
#from scipy import interpolate
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'C:\WINDOWS\Fonts\YuGothic.ttf', size=14)


if "property" =="property":
    startTime       = 0 #default= 1
    number_of_T     = 500 #default = 1
    name0_list      = ["a=0","","","","","","","","","","","","","","",""]
    color_list      = ["green","blue","red","orange","yellow","black","black","black","black","black","black"]
    ct_ylim         = "off"#[-1.5,2]  #"off"#
    cl_ylim         = [-1,2] #"off"
    cd_ylim         = "off"
    grid            = False
    transParent     = True
    line0           = "off"
    xaxis           = "$\it{t}$"
    legendFont      = 15

    if "no needed"=="no needed":
        cl_xlim         = [0,number_of_T]
        ct_xlim         = [0,number_of_T]
        title0          = "" #"Ellipticval Move with Pitching"
        #moveption
        movefolderName  = "s0.5000" #プロットを動かしたいファイル文字
        movePlotNumber  = [2,3] #一番目は0,2番目が1
        pictureNow      = "off" #wpictureNow!にgifが保存される
    
def Moveplot(xList,ctList,ctList2,figName,axName,saveFigname,colorP,colorP2,gifName):
    ims = []
    ims2= []
    for i in range(len(xList)):
        p = axName.plot(xList[i], ctList[i], color = colorP, marker = 'o', markersize = 15)
        p2 = axName.plot(xList[i], ctList2[i], color = colorP2, marker = 'o', markersize = 15)
        ims.append(p+p2)

    ani = animation.ArtistAnimation(figName, ims, interval=100)  #ArtistAnimationでアニメーションを作成する。
    
    ani.save("./0_fig_using/"+root_dir_name+"/"+saveFigname+gifName,writer='imagemagick', dpi = 300)  #gifで保存
    if pictureNow =="on":
        ani.save("wpictureNow!"+gifName,writer='imagemagick', dpi = 300)  #gifで保存

def makeFigure(fontSize,style,root_dir_name,k_list,s_list,number_of_data,test_fig,freq,alphaU_list,comparedata,k,s):
    #listの初期条件
    if "list"=="list":
        s_list =[]
        k_list =[]
        name_list=[]

        
        x_list_all=[]
        x_list_allt=[]


        cd_list_all=[]
        cl_list_all=[]
        ct_list_all=[]

        cd_list_allt=[]
        cl_list_allt=[]
        ct_list_allt=[]


        clMean_list=[]
        ctMean_list=[]

        index = 0
        count = 1

    #k s name list------------
    if "k_s_list"=="k_s_list":
        path = "./" + root_dir_name
        file_list = os.listdir(path) 
        for f in file_list:
            if "s" in f:
                s_list.append(f)
        path2 = "./" + root_dir_name +"/"+s_list[0]
        file_list2 = os.listdir(path2)     
        for f2 in file_list2:
            if "k" in f2:
                k_list.append(f2)


        a_list =[]
        for a in alphaU_list:
            a_list.append(np.radians(a))
        alphaU_list = a_list
        if number_of_data > len(alphaU_list):
            print("out of index alphaU_list")



        if  k != "" and s !="":
            print("Choose k or s")
            exit()

        elif k == "" and s =="":
            print("Choose k or s")
            exit()

        elif k != "":
            if len(s_list) < number_of_data:
                number_of_data = len(s_list)
            title =k
            name_list = s_list
            k_list.clear()
            for i in range(number_of_data):
                k_list.append(k)
            saveFigname = k

        elif s != "": 
            if len(k_list) < number_of_data:
                number_of_data = len(k_list)
            title = s
            name_list = k_list
            s_list.clear()
            for i in range(number_of_data):
                s_list.append(s)
            saveFigname = s

    #open data------------
    if "openData"=="openData":
        f_list =[]
        for i in range(number_of_data):
            f = open(root_dir_name+"/"+s_list[i]+"/"+k_list[i]+'/postProcessing/forceCoeffs/0/forceCoeffs.dat','rt') 
            f_list.append(f)

    #calculate------------
    if "calculate"=="calculate":
        omega = freq*np.pi*2
        for i in range(number_of_data):
            count = 1
            index =0
            if "list"=="list":           
                x_list=[]
                cd_list=[]
                cl_list=[]
                ct_list=[]
                x_list_t=[]
                cd_list_t=[]
                cl_list_t=[]
                ct_list_t=[]

            for line in f_list[i]:
                data = line[:-1].split()
                if data[0] != "#":
                    if float(data[0]) +0.0001 >= startTime/freq:
                        xdata = float(data[0])
                        t = float(data[0])
                        deg = alphaU_list[i]
                        
                        if round(float(data[0]),4) < (startTime+number_of_T)/freq:
                            cdData = float(data[2])
                            clData = float(data[3])
                            cdActual = cdData*np.cos(deg)+clData*np.sin(deg)
                            clActual = -cdData*np.sin(deg)+clData*np.cos(deg)
                            x_list.append(xdata*freq-startTime)
                            cd_list.append(cdActual)
                            cl_list.append(clActual)
                            ct_list.append(-cdActual)
                            if test_fig == 1:
                                x_list_t.append(xdata*freq-1)
                                cd_list_t.append(cdActual)
                                cl_list_t.append(clActual)
                                ct_list_t.append(-cdActual)


                    if round(float(data[0]),4) >= (startTime+number_of_T)/freq:
                        t = xdata
                        cdData = float(data[2])
                        clData = float(data[3])
                        cdActual = cdData*np.cos(deg)+clData*np.sin(deg)
                        clActual = -cdData*np.sin(deg)+clData*np.cos(deg)
                        cdMean = (cdActual + cd_list[index]* count)/(count+1)
                        clMean = (clActual + cl_list[index] * count)/(count+1)
                        cd_list[index] = cdMean
                        cl_list[index] = clMean
                        ct_list[index] = -cdMean
                        index += 1
                        if index == len(cd_list):
                            index = 0
                            count += 1   

            x_list_all.append(x_list)
            cd_list_all.append(cd_list)
            cl_list_all.append(cl_list)
            ct_list_all.append(ct_list)
            if test_fig == 1:
                x_list_allt.append(x_list_t)
                cd_list_allt.append(cd_list_t)
                cl_list_allt.append(cl_list_t)
                ct_list_allt.append(ct_list_t)

    #output----------------
    if "output"=="output":
        ###---------------------------print

        if os.path.exists("./0_fig_using/"+root_dir_name) != True:
            os.makedirs("./0_fig_using/"+root_dir_name)

        if os.path.exists("./0_fig_using/"+root_dir_name+"/"+saveFigname) == False:
            os.makedirs("./0_fig_using/"+root_dir_name+"/"+saveFigname)
            
        if "print"=="print":

            for i in range(number_of_data):
                force = open("./0_fig_using/"+root_dir_name+"/"+saveFigname+"/forceData", 'w', encoding='UTF-8')
                force.write(                          
                name_list[i]+'\n'+"ct : " + str(round(np.mean(ct_list_all[i]),3))+" cl : " + str(round(np.mean(cl_list_all[i]),4))	+'\n'
                )
                clMean_list.append(np.mean(cl_list_all[i]))
                ctMean_list.append(np.mean(ct_list_all[i]))

            Mean_list =[]
            Mean_list.append(clMean_list)
            Mean_list.append(ctMean_list)

            force.close()

            print("-----test------------")
            print("test1(100 100 100 100 100)" )
            for i in range(number_of_data):
                print(str(i)+":"+str(len(x_list_all[i])))

        if name0_list[0] != "":
            name_list = name0_list

        title = title0
        ###---------------------------cl
        if "clPlot"=="clPlot":
            fig,ax = plt.subplots(figsize=(8, 6))
            for i in range(number_of_data): 
                plt.plot(x_list_all[i], cl_list_all[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])

                if test_fig==1:
                    for i in range(number_of_data):
                        fig = plt.figure(figsize=(8, 6))
                        plt.plot(x_list_allt[i], cl_list_allt[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])

            if line0 =="on":
                plt.plot([0,50],[0,0],'-',color='#000000',lw=1)
            plt.xlabel(xaxis,fontsize = fontSizelabal)
            plt.ylabel('$\it{C_l}$',fontsize = fontSizelabal)
            plt.title(title)
            plt.legend(fontsize=legendFont)
            plt.xticks(fontsize=fontSize) 
            plt.yticks(fontsize=fontSize) 
            plt.grid(grid) 
            plt.xlim(cl_xlim)
            if cl_ylim != "off":
                plt.ylim(cl_ylim)

            if movefolderName in saveFigname:
                Moveplot(x_list_all[0],cl_list_all[movePlotNumber[0]],cl_list_all[movePlotNumber[1]],fig,ax,saveFigname,color_list[movePlotNumber[0]],color_list[movePlotNumber[1]],"/Cl.gif")
                #Moveplot(x_list,ct_list_3,fig3,ax2,saveFigname,'red')
                #Moveplot(x_list,ct_list_5,fig3,ax3,saveFigname,'black')

            fig.savefig("./0_fig_using/"+root_dir_name+"/"+saveFigname+"/compareCl.png",transparent=transParent)

        ###---------------------------cd
        if "cdPlot" =="cdPlot":
            fig2 = plt.figure(figsize=(8, 6))
            for i in range(number_of_data):    
                plt.plot(x_list_all[i], cd_list_all[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])
            

                if test_fig==1:
                    for i in range(number_of_data):
                        fig = plt.figure(figsize=(8, 6))
                        plt.plot(x_list_allt[i], cd_list_allt[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])

            if line0 =="on":
                plt.plot([0,50],[0,0],'-',color='#000000',lw=1)


            plt.xlabel(xaxis,fontsize = fontSizelabal)
            plt.ylabel('$\it{C_d}$',fontsize = fontSizelabal)
            plt.title(title)
            plt.legend(fontsize=legendFont)
            plt.xticks(fontsize=fontSize) 
            plt.yticks(fontsize=fontSize) 
            plt.grid(grid)
            plt.xlim(cl_xlim)
            if cd_ylim != "off":
                plt.ylim(cd_ylim)
                

            fig2.savefig("./0_fig_using/"+root_dir_name+"/"+saveFigname+"/compareCd.png",transparent=transParent)
            

        ###---------------------------ct
        if "ctPlot" =="ctPlot": 
            fig3,ax1 = plt.subplots(figsize=(8, 6))
            
            for i in range(number_of_data):
                plt.plot(x_list_all[i], ct_list_all[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])

                if test_fig==1:
                    for i in range(number_of_data):
                        fig = plt.figure(figsize=(8, 6))
                        plt.plot(x_list_allt[i], ct_list_allt[i],style,color=color_list[i],linewidth=4.0, label=name_list[i])

            if line0 =="on":
                plt.plot([0,50],[0,0],'-',color='#000000',lw=1)

            plt.xlabel(xaxis,fontsize = fontSizelabal)
            plt.ylabel('$\it{C_t}$',fontsize = fontSizelabal)
            plt.title(title)
            plt.legend(fontsize=legendFont)
            plt.xticks(fontsize=fontSize) 
            plt.yticks(fontsize=fontSize) 
            plt.grid(grid)
            plt.xlim(ct_xlim)
            if ct_ylim != "off":
                plt.ylim(ct_ylim)
            if movefolderName in saveFigname:
                Moveplot(x_list_all[0],ct_list_all[movePlotNumber[0]],ct_list_all[movePlotNumber[1]],fig3,ax1,saveFigname,color_list[movePlotNumber[0]],color_list[movePlotNumber[1]],"/Ct.gif")
                #Moveplot(x_list,ct_list_3,fig3,ax2,saveFigname,'red')
                #Moveplot(x_list,ct_list_5,fig3,ax3,saveFigname,'black')
            else:
                fig3.savefig("./0_fig_using/"+root_dir_name+"/"+saveFigname+"/compareCt.png",transparent=transParent)

            if pictureNow =="yon":    
                fig.savefig("wpictureNow!/compareCl.png",transparent=transParent)
                fig2.savefig("wpictureNow!/compareCd.png",transparent=transParent)
                fig3.savefig("wpictureNow!/compareCt.png",transparent=transParent)


    return Mean_list

if "input" == "input":
    test_fig        = 0      
    number_of_data_s= 1
    number_of_data_k= 10
    freq            = 1
    TopFolder       = "corgate"#Data_only_PC1/
    root_dir_name   = "Re1000_1" #_mesh51000"
    alphaU_list     = [0,2,4,6,8,10,12,15,17,20,22,24]
    #alphaU_list     = [0,0,0,0,0]
    comparedata     = ""
    fontSize        = 15
    fontSizelabal   = 20
    style           = "-" #o -o --o
    if "no needed"=="no needed":
        TopFolder2       = ""#"elliptical_new"
        root_dir_name2  = "St_0.3_finemesh_T4_moreS"

    if "changeName" == "changeName":
        root_dir_name= TopFolder+"/"+root_dir_name
        root_dir_name2= TopFolder2+"/"+root_dir_name2
        root_dir_name_save = root_dir_name

if "calc"=="calc":  
    if "k_s_list"=="k_s_list":
        number_of_data  = number_of_data_s
        number_of_data2  = number_of_data_k
        s_list=[]
        k_list=[]
        path = "./" + root_dir_name
        file_list = os.listdir(path) 
        if len(file_list)<number_of_data_s:
            number_of_data_s = len(file_list) -1

        for f in file_list:
            if "s" in f:
                s_list.append(f)
        s_list = s_list[:number_of_data_s]

        
        path2 = "./" + root_dir_name +"/"+s_list[0]
        file_list2 = os.listdir(path2)    
        for f2 in file_list2:
            if "k" in f2:
                k_list.append(f2)
        k_list = k_list[:number_of_data_k]

    if "savelist"=="savelist":
        s_list_save =[]
        k_list_save =[]
        k_list_save2 =[]
        for ss in s_list:
            s_list_save.append(ss)

        for kk in k_list:
            k_list_save.append(kk)
            k_list_save2.append(kk)

    if "def_k"=="def_k":
        if len(s_list)<=number_of_data:
            number_of_data = len(s_list) 
        ctMean_list =[]
        clMean_list =[]

        for k in k_list:
            k_list=k_list_save
            s=""
            Mean_list = makeFigure(fontSize,style,root_dir_name,k_list,s_list,number_of_data,test_fig,freq,alphaU_list,comparedata,k,s)
            ctMean_list.append(Mean_list[1])
            clMean_list.append(Mean_list[0])
        ctMean_list_second =[]
        clMean_list_second =[]
        k_list=k_list_save
        print("----------------------------------------------------------")
        if TopFolder2 != "":
            root_dir_name = root_dir_name2
            for k in k_list:
                k_list=k_list_save
                s=""
                Mean_list_second = makeFigure(fontSize,style,root_dir_name,k_list,s_list,number_of_data,test_fig,freq,alphaU_list,comparedata,k,s)
                ctMean_list_second.append(Mean_list_second[1])
                clMean_list_second.append(Mean_list_second[0])
            root_dir_name = root_dir_name_save
            
    print("def_k ok")
    if "def_s"=="def_s":
        k_list  = k_list_save2
        if len(k_list)<=number_of_data2:
            number_of_data = len(k_list)
        ctMean2_list =[]
        clMean2_list =[]
        for s in s_list:
            s_list  = s_list_save
            k=""
            Mean_list = makeFigure(fontSize,style,root_dir_name,k_list,s_list,number_of_data,test_fig,freq,alphaU_list,comparedata,k,s)
            ctMean2_list.append(Mean_list[1])
            clMean2_list.append(Mean_list[0])

        ctMean2_list_second =[]
        clMean2_list_second =[]
        k_list  = k_list_save2
        if TopFolder2 != "":
            if "make_s_list"=="make_s_list":
                s_list_2=[]
                path = "./" + root_dir_name2
                file_list = os.listdir(path) 
                if len(file_list)<number_of_data_s:
                    number_of_data_s = len(file_list) -1

                for f in file_list:
                    if "s" in f:
                        s_list_2.append(f)
                s_list_2 = s_list_2[:number_of_data_s]
                s_list_save2 = s_list_2
            root_dir_name = root_dir_name2

            for s in s_list_2:
                s_list=s_list_save2
                k_list = k_list_save2
                k=""
                Mean_list_second = makeFigure(fontSize,style,root_dir_name2,k_list,s_list,number_of_data,test_fig,freq,alphaU_list,comparedata,k,s)
                ctMean2_list_second.append(Mean_list_second[1])
                clMean2_list_second.append(Mean_list_second[0])
            root_dir_name = root_dir_name_save   
    
    print("def_s ok")
    if "fig_k_s"=="fig_k_s":
        s0_list =[]       
        for s in s_list_save:
            s_int = s.split("_")[0][1:]
            s0_list.append(float(s_int))
        if TopFolder2 != "":
            s0_list2 =[]
            for s in s_list_save2:
                s_int = s.split("_")[0][1:]
                s0_list2.append(float(s_int))
        figMean = plt.figure(figsize=(8, 6))
        #figMean = interpolate.interpld(x,y,kind="cubic")
        if TopFolder2 != "":
            s0_list_both =[]
            ctMean_list_both =[]
                  
            for i in range(len(s0_list)-1):
                ctMean_list_0 =[]
                s0_list_both.append(s0_list[i])
                if i < len(s0_list):
                    s0_list_both.append(s0_list2[i])
                for v in range(len(s0_list)):
                    ctMean_list_0.append(ctMean_list[i][v])
                    if v < len(s0_list)-1:
                        ctMean_list_0.append(ctMean_list_second[i][v])
                ctMean_list_both.append(ctMean_list_0)
            s0_list_both.append(1)

        if name0_list[0]=="":
            name_list = k_list
        else:
            name_list = name0_list

        for i in range(len(ctMean_list)):
            if TopFolder2 != "":
                plt.plot(s0_list_both, ctMean_list_both[i],style,scale=4.0,linewidth=4.0,label=k_list_save[i],color=color_list[i])
            else:
                plt.plot(s0_list, ctMean_list[i],style,markersize=15.0,linewidth=4.0,label=name_list[i],color=color_list[i])
            #print(ctMean_list[i]+ctMean_list_second[i])
        plt.legend(fontsize=legendFont)
        plt.xticks(np.arange(0, 1.2, 0.25),fontsize=fontSize) 
        plt.yticks(fontsize=fontSize)
        if ct_ylim != "off":
            plt.ylim(ct_ylim)
        plt.xlabel('$\it{S}$',fontsize = fontSizelabal)
        plt.ylabel('$\it{C_t,mean}$',fontsize = fontSizelabal)
        figMean.savefig("./0_fig_using/"+root_dir_name+"/ctMean_s.png")

        s0_list =[]
        s0_list2 =[]

        for s in s_list_save:
            s_int = s.split("_")[0][1:]
            s0_list.append(float(s_int))
        if TopFolder2 != "":
            for s in s_list_save2:
                s_int = s.split("_")[0][1:]
                s0_list2.append(float(s_int))
        figMeanCl = plt.figure(figsize=(8, 6))
        s0_list_both =[]
        clMean_list_both =[]
        if TopFolder2 != "":
            for i in range(len(s0_list)-1):
                clMean_list_0 =[]
                s0_list_both.append(s0_list[i])
                if i < len(s0_list):
                    s0_list_both.append(s0_list2[i])
                for v in range(len(s0_list)):
                    clMean_list_0.append(clMean_list[i][v])
                    if v < len(s0_list)-1:
                        clMean_list_0.append(clMean_list_second[i][v])
                clMean_list_both.append(clMean_list_0)

            s0_list_both.append(1)

        if name0_list[0]=="":
            name_list = k_list
        else:
            name_list = name0_list

        for i in range(len(clMean_list)):
            #plt.plot(s0_list, clMean_list[i],style,linewidth=4.0,label=k_list_save[i])
            #plt.plot(s0_list2, clMean_list_second[i],style,linewidth=4.0,label=k_list_save[i])

            if TopFolder2 != "":
                plt.plot(s0_list_both, clMean_list_both[i],style,linewidth=4.0,label=k_list_save[i])
            else:
                plt.plot(s0_list, clMean_list[i],style,markersize=15.0,linewidth=4.0,label=name_list[i],color=color_list[i])
        plt.xticks(np.arange(0, 1.2, 0.25),fontsize=fontSize) 
        plt.yticks(fontsize=fontSize)
        plt.legend(fontsize=legendFont)
        plt.xlabel("$\it{S}$",fontsize = fontSizelabal)
        plt.ylabel('$\it{C_l,mean}$',fontsize = fontSizelabal)
        figMeanCl.savefig("./0_fig_using/"+root_dir_name+"/clMean_s.png")

        k0_list = []
        for k in k_list_save:
            k_int = k.split("_")[0][1:]
            k0_list.append(float(k_int))
        figMean1 = plt.figure(figsize=(8, 6))
        for i in range(len(ctMean2_list)):
            plt.plot(k0_list, ctMean2_list[i],style,linewidth=4.0,label=s_list_save[i])
        for i in range(len(ctMean2_list_second)):
            if TopFolder2 != "":
                plt.plot(k0_list, ctMean2_list_second[i],style,linewidth=4.0,label=s_list_save2[i])
        plt.legend(fontsize=legendFont)
        plt.xlabel('$\it{k}$',fontsize = fontSize)
        plt.ylabel('$\it{C_t}$',fontsize = fontSize)
        figMean1.savefig("./0_fig_using/"+root_dir_name+"/ctMean_k.png")

        k0_list = []
        for k in k_list_save:
            k_int = k.split("_")[0][1:]
            k0_list.append(float(k_int))
        figMeanCl1 = plt.figure(figsize=(8, 6))
        for i in range(len(clMean2_list)):
            plt.plot(k0_list, clMean2_list[i],style,markersize=15.0,linewidth=4.0,label=s_list_save[i])

        for i in range(len(clMean2_list_second)):
            if TopFolder2 != "":
                plt.plot(k0_list, clMean2_list_second[i],style,markersize=15.0,linewidth=4.0,label=s_list_save2[i])
            
        plt.legend(fontsize=legendFont)
        plt.xlabel('$\it{k}$',fontsize = fontSize)
        plt.ylabel('$\it{Cl_mean}$',fontsize = fontSize)
        figMeanCl1.savefig("./0_fig_using/"+root_dir_name+"/clMean_k.png")

    print("fig_k_s ok")
    if "sum"=="sum":
        k0_list = []
        for k in k_list_save:
            k_int = k.split("_")[0][1:]
            k0_list.append(float(k_int))
        figMeanCl1 = plt.figure(figsize=(8, 6))
        sum_Cl2_Ct2=[]
        for i in range(len(clMean2_list)):
            sum_Cl2_Ct2.append(ctMean2_list[i])
            sum_Cl2_Ct2.append(clMean2_list[i])
            sum_result = (np.sum(sum_Cl2_Ct2,axis=0))
            plt.plot(k0_list, sum_result,style,linewidth=4.0,label=s_list_save[i])
        plt.legend(fontsize=legendFont)
        plt.xlabel("k",fontsize = fontSize)
        plt.ylabel('Cl + Ct',fontsize = fontSize)
        figMeanCl1.savefig("./0_fig_using/"+root_dir_name+"/Cl+CtMean_k.png")

        
        s0_list =[]
        for s in s_list_save:
            s_int = s.split("_")[0][1:]
            s0_list.append(float(s_int))
        figMeanCl = plt.figure(figsize=(8, 6))
        sum_Cl_Ct=[]
        for i in range(len(clMean_list)):
            sum_Cl_Ct.append(ctMean_list[i])
            sum_Cl_Ct.append(clMean_list[i])
            sum_result = (np.sum(sum_Cl_Ct,axis=0))
            plt.plot(s0_list, sum_result,style,linewidth=4.0,label=k_list_save[i])
        plt.legend(fontsize=legendFont)
        plt.xlabel("S",fontsize = fontSize)
        plt.ylabel('Cl+Ct',fontsize = fontSize)
        figMeanCl.savefig("./0_fig_using/"+root_dir_name+"/Cl+CtMean_s.png")

print("end")