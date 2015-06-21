import matplotlib.pylab as plt
import numpy as np
import scipy as sci
import pandas as pd
from collections import defaultdict
import math
b=[]
c = []
Tc = 9.2
k= 1.3806488*10**-23
e = 1.60217657*10**-19
Rn_ohm = []
Temp_ = []
b =[]
c=[]
for Rn in range(2, 7, 1):
    Rn = 1*Rn
    #print Rn
    d0 = 1.78*k*Tc
    names = ['T', 'KO-I', 'KO-II', 'AB']
    results = pd.read_table('/Users/abu_adan/Code_and_JSIM/Python_Code/Final_results_for_thertical_Ic_values.csv', sep=',',names=names)
    T = results['T']
    KOI = results['KO-I']
    KOII = results['KO-II']
    AB = results['AB']
    Temp = T*Tc
    Temp_.append(Temp)
    Ic = (KOI*(d0/e))/Rn
    Rn_ohm.append(Ic)
    print len(Ic)
    #out_file ='/Users/abu_adan/PhD/MacOs/Python Code/Thertical_Rn_from_KO-II/therotical_Ic_at_Rn='+str(Rn)+'ohm.csv'
    #np.savetxt(out_file, np.c_[Temp, Ic], delimiter=",", fmt='%10.8f')
    plt.plot(Temp, Ic, '--o',linewidth=1.75, label='$R_n$= '+str(Rn)+'ohm')
    plt.legend(loc='best', frameon=False)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(-8,-9))
    plt.ylabel('I$_c$ / A', fontsize=14)
    plt.xlabel('T / K', fontsize=14)
    from collections import OrderedDict
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.show()
    del Rn_ohm[:]
plt.savefig('diff_Rn.png', dpi=500)