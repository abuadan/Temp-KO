import math
import matplotlib.pylab as plt
import numpy as np
from collections import OrderedDict

'''
The code in this simualtions was desgined foir readbility over speed 
as such any increases in the value of M in the main() loop will result in 
a more accuraate simualtions but will increase the time required to complete 
'''
#Global Variables 
Tc = 9.3
k= 1.3806488*10**-23
e = 1.60217657*10**-19
#phi = math.asin(1)
x = []
y = []
z = []
g= []
f = []
Temp = []
D0 = 0

''' Calculate the delta of ... '''

def Delta(T):
	d0 = (math.pi/1.78)*k*Tc
	D0 = d0*(math.sqrt(1-(T**2/Tc**2)))
	return D0


''''' '''''

''''' '''''

def V0():
	d0 = (math.pi/1.78)*k*Tc
	V0 =(d0/e)
	return V0

''''' '''''

''''' '''''

def A_B(T):
    D =Delta(T)
    IabRn = ((math.pi*D)/(2*e)*math.tanh(D/(2*k*T)))
    return IabRn

''''' '''''

''''' '''''

def element_in_sum(T, n, phi):
    D = Delta(T)
    matsubara_frequency = (math.pi * k * T) * (2*n + 1)
    factor_d = math.sqrt((D**2 * math.cos(phi/2)**2) + matsubara_frequency**2)
    element = ((2 * D * math.cos(phi/2))/ factor_d) * math.atan((D * math.sin(phi/2))/factor_d)
    return element

def sum_elements(T, M, phi):
	X = list(np.arange(0,M,1))
	Y = [element_in_sum(T, n, phi) for n in X]
	return sum(Y)

def KO_1(M, T, phi):
	Iko1Rn = (2 * math.pi * k * T /e) * sum_elements(T, M, phi)
	return Iko1Rn

''''' '''''

''''' '''''

def KO_2(T, phi):
    D = Delta(T)
    Iko2Rn = (math.pi*D/e)*(math.sin(phi/2))*math.tanh(D*math.cos(phi/2)/(2*k*T))
    return Iko2Rn
 
''''' '''''

''''' '''''   

def main():
    for j in range(1,94):
        T = 0.1*j
	print T
	for i in range(0,315):
	   phi = 0.01*i
	   '''
	   As a first step when running this code start with a small value 
	   for M as larger values whilst accurate will take longer to run and complete 
	   In this example 26000 is the upper limit where the simualtion will compelete in under 3 hours 
	   with very accurate results.
	   
	   '''
	   result = KO_1(26800,T, phi) 
	   result_1 = KO_2(T, phi)
	   g.append(result)
	   f.append(result_1)
	   
	A = max(g);
	B = max(f);
	C = A_B(T)
	x.append(A/V0())
	y.append(B/V0())
	#print x
	del g[:]
	del f[:] 
	z.append(C/V0())
	Temp.append(T/Tc)
    plt.plot(Temp, x, '--bo', linewidth=1.5, label='KO-I')
    plt.plot(Temp, y,'--ro',  linewidth=1.5, label='KO-II')
    plt.plot(Temp, z, '--go', linewidth=1.5, label = 'AB')
    plt.legend(loc='best', frameon=False)
    plt.xlabel('T/T$_c$', fontsize=18)
    plt.ylabel(r'$\frac{V_c}{\Delta_{0}e}$', fontsize=22)
    plt.savefig('Final_results_for_thertical_Ic_values.png', dpi=500)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), frameon = False)
    plt.show()
#ArrayMain = []
#ArrayMain = np.column_stack((Temp,x,y,z)) 
#np.savetxt("Final_results_for_thertical_Ic_values.csv", ArrayMain, delimiter=",", fmt='%.9f')
main()
