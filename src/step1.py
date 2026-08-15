
import matplotlib.pyplot \
    as plt
import numpy as np
import scipy.io as sio






def generer_signal(freq_samp, duration, frequency, amplitude):
    time=np.linspace(0,duration,duration*freq_samp) #on echantillone le vecteur temps par la fréquence d'échantillonage
    n = len(frequency)
    sinusoid=[]
    for i in range(n):
        sinusoid.append(amplitude[i]*np.sin(2*np.pi*frequency[i]*time))
    signal=0
    for i in range(n):
        signal=signal+sinusoid[i]

    return signal,time

def calculer_fft(signal,freq_samp):
    freqs=np.fft.rfftfreq(len(signal),1/freq_samp)  #on utilise ici le pas temporelle
    spectre=np.fft.rfft(signal,norm="forward")
    amplitude_fft=2*np.abs(spectre)#on fait *2 a cause de la repartiton de l'énergie sur les 2 fréquences conjugués
    amplitude_fft[0]=amplitude_fft[0]/2
    if (len(signal) %2)==0 :
        amplitude_fft[-1]=amplitude_fft[-1]/2  #si le nombre élement de signal est Pair , il y 'a pas de répartition de l'amplitude sur les termes positifs et négatifs ( il y'a pas de miroir négatif ) pour le dernier terme ( fréquence de nyquist )
    return freqs, amplitude_fft

def tracer_spectre( freq_samp, amplitude_fft, title, freqs):
    plt.figure(figsize=(10,5))
    plt.plot(freqs,amplitude_fft)
    plt.xlim(0,freq_samp/2)
    plt.xlabel('frequence')
    plt.ylabel('amplitude de la transformee de fourier ')
    plt.title(title)
    plt.grid(True)




def tracer_signal(signal,time,title,duration):
    plt.figure(figsize=(10,4))
    plt.plot(time,signal)
    plt.xlabel('Time')
    plt.ylabel('Signal')
    plt.title(title)
    plt.grid(True)
    plt.savefig(r"C:\Users\amine\PycharmProjects\PythonProject\figures\graphic.png") #r veut "raw string" il ne consideren pas \U ou des trucs du genre comme des caractères spéciaux exemple  \n = retour à la ligne  \t = tabulation  \U = début d’un caractère Unicode spécial
    plt.show()







