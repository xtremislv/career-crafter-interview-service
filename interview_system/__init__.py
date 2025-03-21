import parselmouth
from parselmouth.praat import call, run_file
import glob
import pandas as pd
import numpy as np
import scipy
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os
import pickle
import cv2
import time
import math as m
import mediapipe as mp
import os
import uuid

def myspsyl(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[0]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        print ("number_ of_syllables=",z3)
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return; 

def mysppaus(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[1]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        print ("number_of_pauses=",z3)
        return z3
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return; 

def myspsr(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[2]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        print ("rate_of_speech=",z3,"# syllables/sec original duration")
        return z3
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return

def myspatc(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        print ("articulation_rate=",z3,"# syllables/sec speaking duration")
        return z3
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return

def myspst(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[4]) # will be the floating point number 8.3
        print ("speaking_duration=",z4,"# sec only speaking duration without pauses")
        return z4
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspod(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[5]) # will be the floating point number 8.3
        print ("original_duration=",z4,"# sec total speaking duration with pauses")
        return z4
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspbala(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[6]) # will be the floating point number 8.3
        print ("balance=",z4,"# ratio (speaking duration)/(original duration)")
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0mean(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[7]) # will be the floating point number 8.3
        print ("f0_mean=",z4,"# Hz global mean of fundamental frequency distribution")
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0sd(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[8]) # will be the floating point number 8.3
        print ("f0_SD=",z4,"# Hz global standard deviation of fundamental frequency distribution")
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0med(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[9]) # will be the floating point number 8.3
        print ("f0_MD=",z4,"# Hz global median of fundamental frequency distribution")
    except:
        z4=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0min(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[10]) # will be the integer number 10
        z4=float(z2[10]) # will be the floating point number 8.3
        print ("f0_min=",z3,"# Hz global minimum of fundamental frequency distribution")
    except:
        z3=0
        print ("Try again the sound of the audio was not clear") 
    return

def myspf0max(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[11]) # will be the integer number 10
        z4=float(z2[11]) # will be the floating point number 8.3
        print ("f0_max=",z3,"# Hz global maximum of fundamental frequency distribution")
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0q25(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[12]) # will be the integer number 10
        z4=float(z2[11]) # will be the floating point number 8.3
        print ("f0_quan25=",z3,"# Hz global 25th quantile of fundamental frequency distribution")
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return

def myspf0q75(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[13]) # will be the integer number 10
        z4=float(z2[11]) # will be the floating point number 8.3
        print ("f0_quan75=",z3,"# Hz global 75th quantile of fundamental frequency distribution")
    except:
        z3=0
        print ("Try again the sound of the audio was not clear")
    return

def mysptotal(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=np.array(z2)
        z4=np.array(z3)[np.newaxis]
        z5=z4.T
        dataset=pd.DataFrame({"number_ of_syllables":z5[0,:],"number_of_pauses":z5[1,:],"rate_of_speech":z5[2,:],"articulation_rate":z5[3,:],"speaking_duration":z5[4,:],
                          "original_duration":z5[5,:],"balance":z5[6,:],"f0_mean":z5[7,:],"f0_std":z5[8,:],"f0_median":z5[9,:],"f0_min":z5[10,:],"f0_max":z5[11,:],
                          "f0_quantile25":z5[12,:],"f0_quan75":z5[13,:]})
        # print (dataset.T)
        return dataset.T
    except:
        print ("Try again the sound of the audio was not clear")
    return

def mysppron(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[13]) # will be the integer number 10
        z4=float(z2[14]) # will be the floating point number 8.3
        db= binom.rvs(n=10,p=z4,size=10000)
        a=np.array(db)
        b=np.mean(a)*100/10
        print ("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
        return b
    except:
        print ("Try again the sound of the audio was not clear")
    return

def myspgend(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat" 
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=float(z2[8]) # will be the integer number 10
        z4=float(z2[7]) # will be the floating point number 8.3
        if z4<=114:
            g=101
            j=3.4
        elif z4>114 and z4<=135:
            g=128
            j=4.35
        elif z4>135 and z4<=163:
            g=142
            j=4.85
        elif z4>163 and z4<=197:
            g=182
            j=2.7
        elif z4>197 and z4<=226:
            g=213
            j=4.5
        elif z4>226:
            g=239
            j=5.3
        else:
            print("Voice not recognized")
            exit()
        def teset(a,b,c,d):
            d1=np.random.wald(a, 1, 1000)
            d2=np.random.wald(b,1,1000)
            d3=ks_2samp(d1, d2)
            c1=np.random.normal(a,c,1000)
            c2=np.random.normal(b,d,1000)
            c3=ttest_ind(c1,c2)
            y=([d3[0],d3[1],abs(c3[0]),c3[1]])
            return y
        nn=0
        mm=teset(g,j,z4,z3)
        while (mm[3]>0.05 and mm[0]>0.04 or nn<5):
            mm=teset(g,j,z4,z3)
            nn=nn+1
        nnn=nn
        if mm[3]<=0.09:
            mmm=mm[3]
        else:
            mmm=0.35
        if z4>97 and z4<=114:
            print("a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Male","No Emotion")
        elif z4>114 and z4<=135:
            print("a Male, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Male","Reading")
        elif z4>135 and z4<=163:
            print("a Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Male","speaking passionately")

        elif z4>163 and z4<=197:
            print("a female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Female","No Emotion")

        elif z4>197 and z4<=226:
            print("a female, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Female","Reading")

        elif z4>226 and z4<=245:
            print("a female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
            return ("Female","speaking passionately")

        else:
            print("Voice not recognized")
    except:
        print ("Try again the sound of the audio was not clear")

def myprosody(m,p):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"MLTRNL.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    outo=p+"/"+"dataset"+"/"+"datanewchi22.csv"
    outst=p+"/"+"dataset"+"/"+"datanewchi44.csv"
    outsy=p+"/"+"dataset"+"/"+"datanewchi33.csv"
    pa2=p+"/"+"dataset"+"/"+"stats.csv"
    pa7=p+"/"+"dataset"+"/"+"datanewchi44.csv" 
    result_array = np.empty((0, 100))
    files = glob.glob(path)
    result_array = np.empty((0, 27))
    objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
    z1=( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
    z3=z1.strip().split()
    z2=np.array([z3])
    result_array=np.append(result_array,[z3], axis=0)
    #print(z3)
    np.savetxt(outo,result_array, fmt='%s',delimiter=',')
    #Data and features analysis
    df = pd.read_csv(outo,
                     names = ['avepauseduratin','avelongpause','speakingtot','avenumberofwords','articulationrate','inpro','f1norm','mr','q25',
                              'q50','q75','std','fmax','fmin','vowelinx1','vowelinx2','formantmean','formantstd','nuofwrds','npause','ins',
							  'fillerratio','xx','xxx','totsco','xxban','speakingrate'],na_values='?')

    scoreMLdataset=df.drop(['xxx','xxban'], axis=1)
    scoreMLdataset.to_csv(outst, header=False,index = False)
    newMLdataset=df.drop(['avenumberofwords','f1norm','inpro','q25','q75','vowelinx1','nuofwrds','npause','xx','totsco','xxban','speakingrate','fillerratio'], axis=1)
    newMLdataset.to_csv(outsy, header=False,index = False)
    namess=nms = ['avepauseduratin','avelongpause','speakingtot','articulationrate','mr',
                              'q50','std','fmax','fmin','vowelinx2','formantmean','formantstd','ins',
							  'xxx']
    df1 = pd.read_csv(outsy, names = namess)    
    nsns=['average_syll_pause_duration','No._long_pause','speaking_time','ave_No._of_words_in_minutes','articulation_rate','No._words_in_minutes','formants_index','f0_index','f0_quantile_25_index',
                              'f0_quantile_50_index','f0_quantile_75_index','f0_std','f0_max','f0_min','No._detected_vowel','perc%._correct_vowel','(f2/f1)_mean','(f2/f1)_std',
                                'no._of_words','no._of_pauses','intonation_index',
				    '(voiced_syll_count)/(no_of_pause)','TOEFL_Scale_Score','Score_Shannon_index','speaking_rate']
    dataframe = pd.read_csv(pa2) 
    df55 = pd.read_csv(outst,names=nsns)
    dataframe=dataframe.values
    array = df55.values
    print("Compared to native speech, here are the prosodic features of your speech:")
    for i in range(25):
        sl0=dataframe[4:7:1,i+1]
        score = array[0,i]
        he=scipy.stats.percentileofscore(sl0, score, kind='strict')
        if he==0:
            he=25
            dfout = "%s:\t %f (%s)" %  (nsns[i],he,"% percentile ")
            print(dfout) 
        elif he>=25 and he<=75:
            dfout = "%s:\t %f (%s)" % (nsns[i],he,"% percentile ")
            print(dfout) 
        else:
           dfout = "%s:\t (%s)" % (nsns[i],":Out of Range")
           print(dfout) 

def myspp(bp,bg):
	sound=bg+"/"+"dataset"+"/"+"audioFiles"+"/"+bp+".wav"
	sourcerun=bg+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
	path=bg+"/"+"dataset"+"/"+"audioFiles"+"/"
	objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
	print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
	z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
	z2=z1.strip().split()
	z3=int(z2[13]) # will be the integer number 10
	z4=float(z2[14]) # will be the floating point number 8.3
	db= binom.rvs(n=10,p=z4,size=10000)
	a=np.array(db)
	b=np.mean(a)*100/10
	return b
    
def mysplev(m,p):
	import sys
	def my_except_hook(exctype, value, traceback):
		print('There has been an error in the system')
	sys.excepthook = my_except_hook
	import warnings
	if not sys.warnoptions:
		warnings.simplefilter("ignore")
	sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
	sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"MLTRNL.praat"
	path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
	pa1=p+"/"+"dataset"+"/"+"datanewchi23.csv"
	pa7=p+"/"+"dataset"+"/"+"datanewchi45.csv"
	pa5=p+"/"+"dataset"+"/"+"datanewchi34.csv"
	result_array = np.empty((0, 100))
	ph = sound
	files = glob.glob(ph)
	result_array = np.empty((0, 27))
	for soundi in files:
		objects= run_file(sourcerun, -20, 2, 0.3, "yes", soundi, path, 80, 400, 0.01, capture_output=True)
		#print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z3=z1.strip().split()
		z2=np.array([z3])
		result_array=np.append(result_array,[z3], axis=0)
		
	np.savetxt(pa1,result_array, fmt='%s',delimiter=',')
	#Data and features analysis 
	df = pd.read_csv(pa1, names = ['avepauseduratin','avelongpause','speakingtot','avenumberofwords','articulationrate','inpro','f1norm','mr','q25',
								  'q50','q75','std','fmax','fmin','vowelinx1','vowelinx2','formantmean','formantstd','nuofwrds','npause','ins',
								  'fillerratio','xx','xxx','totsco','xxban','speakingrate'],na_values='?')

	scoreMLdataset=df.drop(['xxx','xxban'], axis=1)
	scoreMLdataset.to_csv(pa7, header=False,index = False)
	newMLdataset=df.drop(['avenumberofwords','f1norm','inpro','q25','q75','vowelinx1','nuofwrds','npause','xx','totsco','xxban','speakingrate','fillerratio'], axis=1)
	newMLdataset.to_csv(pa5, header=False,index = False)
	namess=nms = ['avepauseduratin','avelongpause','speakingtot','articulationrate','mr',
								  'q50','std','fmax','fmin','vowelinx2','formantmean','formantstd','ins',
								  'xxx']
	df1 = pd.read_csv(pa5,
							names = namess)
	df33=df1.drop(['xxx'], axis=1)
	array = df33.values
	array=np.log(array)
	x = array[:,0:13]

    
	bp=m
	bg=p
	bi=myspp(bp,bg)
	if bi<85:
		input("Try again, unnatural-sounding speech detected. No further result. Press any key to exit.")
		exit()
	
	# filename=p+"/"+"dataset"+"/"+"essen"+"/"+"CART_model.sav"
	# model = pickle.load(open(filename, 'rb'))
	# predictions = model.predict(x)
	# print("58% accuracy    ",predictions)

	filename=p+"/"+"dataset"+"/"+"essen"+"/"+"KNN_model.sav"
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("65% accuracy    ",predictions)

	filename=p+"/"+"dataset"+"/"+"essen"+"/"+"LDA_model.sav"
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("70% accuracy    ",predictions)

	filename=p+"/"+"dataset"+"/"+"essen"+"/"+"LR_model.sav"
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("67% accuracy    ",predictions)

	filename=p+"/"+"dataset"+"/"+"essen"+"/"+"NB_model.sav"
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("64% accuracy    ",predictions)

	filename=p+"/"+"dataset"+"/"+"essen"+"/"+"SVN_model.sav"
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("63% accuracy    ",predictions)


def predict_pose(p):
  mp_pose = mp.solutions.pose
  good_frames = 0
  bad_frames = 0
  font = cv2.FONT_HERSHEY_SIMPLEX
  mp_holistic = mp.solutions.holistic
  blue = (255, 127, 0)
  red = (50, 50, 255)
  green = (127, 255, 0)
  dark_blue = (127, 20, 0)
  light_green = (127, 233, 100)
  yellow = (0, 255, 255)
  pink = (255, 0, 255)
  # Initialize mediapipe pose class.
  mp_pose = mp.solutions.pose
  # Initializing mediapipe drawing class, useful for annotation.
  mp_drawing = mp.solutions.drawing_utils
  BG_COLOR = (192, 192, 192) # gray
  images = []
  folder= p+'/dataset/videofile/input_files'
  with mp_pose.Pose(
      static_image_mode=True,
      model_complexity=2,
      enable_segmentation=True,
      min_detection_confidence=0.5) as pose:
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder,filename))
        if image is  None:
          break
        # file='/content/IMG_20240305_111352.jpg'
        # image = cv2.imread(file)
      # Get height and width.
        h, w = image.shape[:2]
      # Convert the BGR image to RGB.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

      # Process the image.
        keypoints = pose.process(image)

      # Convert the image back to BGR.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      # Use lm and lmPose as representative of the following methods.
        lm = keypoints.pose_landmarks
        lmPose = mp_pose.PoseLandmark

      # Acquire the landmark coordinates.
      # Once aligned properly, left or right should not be a concern.
      # Left shoulder.
        l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
        l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
      # Right shoulder
        r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
        r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
      # Left ear.
        l_ear_x = int(lm.landmark[lmPose.LEFT_EAR].x * w)
        l_ear_y = int(lm.landmark[lmPose.LEFT_EAR].y * h)

        r_ear_x = int(lm.landmark[lmPose.RIGHT_EAR].x * w)
        r_ear_y = int(lm.landmark[lmPose.RIGHT_EAR].y * h)
      # NOSE.
        l_nose_x = int(lm.landmark[lmPose.NOSE].x * w)
        l_nose_y = int(lm.landmark[lmPose.NOSE].y * h)
      # Calculate angles.
        l_neck_inclination = findAngle(l_shldr_x, l_shldr_y, l_ear_x, l_ear_y)
        l_bend_inclination = findAngle(l_nose_x, l_nose_y, l_shldr_x, l_shldr_y)
        r_neck_inclination = findAngle(r_shldr_x, r_shldr_y, r_ear_x, r_ear_y)
        r_bend_inclination = findAngle(l_nose_x, l_nose_y, r_shldr_x, r_shldr_y)
        shldr_inclination = findAngle(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)
      # Draw landmarks.
        cv2.circle(image, (l_shldr_x, l_shldr_y), 7, yellow, -1)
        cv2.circle(image, (r_shldr_x, r_shldr_y), 7, yellow, -1)
        cv2.circle(image, (l_ear_x, l_ear_y), 7, yellow, -1)
        cv2.circle(image, (r_ear_x, r_ear_y), 7, yellow, -1)
        mp_drawing.plot_landmarks(keypoints.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        z_nose=lm.landmark[lmPose.NOSE].z * w
        print(f'z: {lm.landmark[lmPose.NOSE].z * w}')
        if z_nose < -1100:
           cv2.putText(image, 'YOU ARE VERY CLOSER TO THE SCREEN', (10, 150), font, 0.9, red, 2)
           return('YOU ARE VERY CLOSER TO THE SCREEN')
        
      # Let's take y - coordinate of P3 100px above x1,  for display elegance.
      # Although we are taking y = 0 while calculating angle between P1,P2,P3.
        cv2.circle(image, (l_shldr_x, l_shldr_y - 100), 7, yellow, -1)
        cv2.circle(image, (r_shldr_x, r_shldr_y-100), 7, pink, -1)
        cv2.circle(image, (l_nose_x, l_nose_y), 7, yellow, -1)

      # Similarly, here we are taking y - coordinate 100px above x1. Note that
      # you can take any value for y, not necessarily 100 or 200 pixels.
        cv2.circle(image, (l_nose_x, l_nose_y - 100), 7, yellow, -1)

      # Put text, Posture and angle inclination.
      # Text string for display.
        angle_text_left = 'Neck_left : ' + str(int(l_neck_inclination)) + '  Bend_left : ' + str(int(l_bend_inclination))
        angle_text_right = 'Neck_right : ' + str(int(r_neck_inclination)) + '  Bend_right : ' + str(int(r_bend_inclination))
        angle_text_string = 'Neck : ' + str(int(l_neck_inclination+r_neck_inclination)) + '  Bend : ' + str(int(l_bend_inclination+r_bend_inclination))
        angle_text_shldr = 'Shoulder : ' + str(int(shldr_inclination))
        neck=l_neck_inclination+r_neck_inclination
        bend=l_bend_inclination+r_bend_inclination
        x_m_point = int((l_shldr_x +r_shldr_x )/2)
        y_m_point = int((l_shldr_y+r_shldr_y )/2)
            # Determine whether good posture or bad posture.
            # The threshold angles have been set based on intuition.
        if neck >= 50  and bend >=265:
           bad_frames = 0
           good_frames += 1# writing in a good frame posture
           cv2.putText(image, angle_text_string, (10, 30), font, 0.9, light_green, 2)
           cv2.putText(image, angle_text_left, (10, 60), font, 0.9, light_green, 2)
           cv2.putText(image, angle_text_right, (10, 90), font, 0.9, light_green, 2)
           cv2.putText(image, angle_text_shldr, (10, 120), font, 0.9, light_green, 2)
           cv2.putText(image, str(int(neck)), (l_shldr_x + 10, l_shldr_y), font, 0.9, light_green, 2)
           cv2.putText(image, str(int(bend)), (l_nose_x + 10, l_nose_y), font, 0.9, light_green, 2)

          # Join landmarks.
           cv2.line(image, (l_shldr_x, l_shldr_y), (l_ear_x, l_ear_y), green, 4)
           cv2.line(image, (l_shldr_x, l_shldr_y), (r_shldr_x, r_shldr_y), green, 4)
           cv2.line(image, (r_shldr_x, r_shldr_y), (r_ear_x, r_ear_y), green, 4)
           cv2.line(image, (l_shldr_x, l_shldr_y), (l_shldr_x, l_shldr_y - 100), green, 4)
           cv2.line(image, (r_shldr_x, r_shldr_y), (r_shldr_x, r_shldr_y - 100), green, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (l_shldr_x, l_shldr_y), green, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (r_shldr_x, r_shldr_y), green, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (l_nose_x, l_nose_y - 100), green, 4)
           cv2.line(image, (x_m_point,y_m_point), (l_nose_x, l_nose_y - 100), green, 4)

        else:
           good_frames = 0
           bad_frames += 1

           cv2.putText(image, angle_text_string, (10, 30), font, 0.9, red, 2)
           cv2.putText(image, angle_text_left, (10, 60), font, 0.9, red, 2)
           cv2.putText(image, angle_text_right, (10, 90), font, 0.9, red, 2)
           cv2.putText(image, angle_text_shldr, (10, 120), font, 0.9, red, 2)
           cv2.putText(image, str(int(neck)), (l_shldr_x + 10, l_shldr_y), font, 0.9, red, 2)
           cv2.putText(image, str(int(bend)), (l_nose_x + 10, l_nose_y), font, 0.9, red, 2)


          # Join landmarks.
           cv2.line(image, (l_shldr_x, l_shldr_y), (l_ear_x, l_ear_y), red, 4)
           cv2.line(image, (l_shldr_x, l_shldr_y), (r_shldr_x, r_shldr_y), red, 4)
           cv2.line(image, (r_shldr_x, r_shldr_y), (r_ear_x, r_ear_y), red, 4)
           cv2.line(image, (l_shldr_x, l_shldr_y), (l_shldr_x, l_shldr_y - 100), red, 4)
           cv2.line(image, (r_shldr_x, r_shldr_y), (r_shldr_x, r_shldr_y - 100), red, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (l_shldr_x, l_shldr_y), red, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (r_shldr_x, r_shldr_y),red, 4)
           cv2.line(image, (l_nose_x, l_nose_y), (l_nose_x, l_nose_y - 100), red, 4)
           cv2.line(image, (x_m_point,y_m_point), (l_nose_x, l_nose_y - 100), red, 4)
      # Calculate the time of remaining in a particular posture.
     # good_time = (1 / fps) * good_frames
     # bad_time =  (1 / fps) * bad_frames

      # Pose time.
        if good_frames > 0:
           time_string_good = 'Good Posture Time : ' + str(round(good_frames, 1)) + 's'
           cv2.putText(image, time_string_good, (10, h - 20), font, 0.9, green, 2)
        else:
           time_string_bad = 'Bad Posture Time : ' + str(round(bad_frames, 1)) + 's'
           cv2.putText(image, time_string_bad, (10, h - 20), font, 0.9, red, 2)

      # If you stay in bad posture for more than 3 minutes (180s) send an alert.
        if bad_frames > 0:
           sendWarning()
            # Write frames.
        annotated_image = image.copy()
        unique_filename = make_unique('fig1.png')
            # Draw segmentation on the image.
            # To improve segmentation around boundaries, consider applying a joint
            # bilateral filter to "results.segmentation_mask" with "image".
        cv2.imwrite(rf'{p}/dataset/videofile/output_files/{unique_filename}',annotated_image)
  print('finished')


def extract_frames(video_path, output_path):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return

    # Get video properties
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Initialize variables
    frame_count = 0
    current_time = 0

    while True:
        # Set the capture to the current frame
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
        
        # Read the next frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save the frame
        output_file = output_path + "/frame_" + str(frame_count) + ".jpg"
        cv2.imwrite(output_file, frame)

        # Move to the next frame
        frame_count += int(fps)

    # Release video capture
    video_capture.release()

def findDistance(x1, y1, x2, y2):
    dist = m.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

def findAngle(x1, y1, x2, y2):
    theta = m.acos((y2 -y1)*(-y1) / (m.sqrt((x2 - x1)**2 + (y2 - y1)**2) * y1))
    degree = int(180/m.pi)*theta
    return degree

def sendWarning():
    print('YOU ARE IN WRONG POSITION FOR LONG TIME')

def make_unique(filename):
    unique_id = uuid.uuid4()
    name, extension = os.path.splitext(filename)
    return f"{name}_{unique_id}{extension}"

def delete_files_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file and delete it
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error: {e}")