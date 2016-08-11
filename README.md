Temperature dependence of Josephson junction critical current based on KO-I and KO-II equations 
==============

Named after the British physicist Brian Josephson [1], Josephson junctions are a subset of weak links; a family of structures that display the Josephson effect. Such structures have an important application in voltage standards [2], quantum-mechanical circuits, such as Superconducting QUantum Interference Devices (SQUIDs) [3], superconducting qubits [4], and RSFQ digital electronics [5]. Different examples of Josephson junctions are shown in Figure below.

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/410811/junctions-eps-converted-to.pdf" width="300" title="Different types of structures where the Josephson effect can take place. (a) tunnel junction, for example, S-I-S sandwich. All others are dif- ferent weak links (structures with direct non-tunnel-type conductivity): (b) sandwich, (c) proximity effect bridge, (d) ion implanted bridge, (e) Dayem bridge, (f) variable thickness bridge, (g) point contact, (h) blob type junction. S = Superconducting, S’ = superconducting with reduced critical parameters, SE = semiconductor (usually highly doped), N = normal metal and I = Insulator. Adapted from Likharev [6]">

The python code desrcibed in this repiository solves the temerpature dependednt equtions of that descbie the behavoiur of the criticla temeprature of long and short weak links for material with differeing ctirtical temerpre 

KO (I) 
--------------
- The first case (denoted as (KO-I)) [2] applies to dirty or short weak links and is given as:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/411536/eq1.pdf" width="600">

where &#948; and the the n<sup>th</sup> Matsubara &#295;&#969; frequency are respectively given as:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/411548/eq2.pdf" width=600>
n is a positive integer

Taking the maximum of the resulting plot of I<sub>s</sub>(&phi;)R<sub>N<\sub> the phase &phi; and plotting this results in the overall temerpature dependent plot for the critical current of the weak link. Plotting the resulting I<sub>s</sub>(&phi;) RN as a function of the phase for a typical short weak link results in Figure 1.15, where the critical current I<sub>c</sub> is taken as the maximum value of the function.

KO (II) 
--------------

The second case(KO-II) [50] applies to clean or long weak links and gives:
<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/411802/eq3.pdf" width="600">

