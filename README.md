Temperature dependence of Josephson junction critical current based on KO-I and KO-II equations 
==============

Named after the British physicist Brian Josephson [1], Josephson junctions are a subset of weak links; a family of structures that display the Josephson effect. Such structures have an important application in voltage standards [2], quantum-mechanical circuits, such as Superconducting QUantum Interference De- vices (SQUIDs) [3], superconducting qubits [4], and RSFQ digital electronics [5]. Different examples of Josephson junctions are shown in Figure below.

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/410811/junctions-eps-converted-to.pdf" width="300" title="Different types of structures where the Josephson effect can take place. (a) tunnel junction, for example, S-I-S sandwich. All others are dif- ferent weak links (structures with direct non-tunnel-type conductivity): (b) sandwich, (c) proximity effect bridge, (d) ion implanted bridge, (e) Dayem bridge, (f) variable thickness bridge, (g) point contact, (h) blob type junction. S = Superconducting, S’ = superconducting with reduced critical parameters, SE = semiconductor (usually highly doped), N = normal metal and I = Insulator. Adapted from Likharev [6]">

The python code desrcibed in this repiository solves the temerpature dependednt equtions of that descbie the behavoiur of the criticla temeprature of long and short weak links for material with differeing ctirtical temerpre 

the KO(I)
--------------
- The first case (denoted as (KO-I)) [2] applies to dirty or short weak links and is given as:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/411536/eq1.pdf" width="600">

Is(φ)Rn = 2πkBT   2∆ cos(φ/2) arctan ∆ sin(φ/2) (1.55)
eω>0δ δ
where δ =  ∆2 cos2(φ/2) + ( ω)2 1and the nth Matsubara frequency  ω satisfies  ω = πkBT (2n + 1) where n is a positive integer. Plotting the resulting Is (φ) RN as a function of the phase for a typical short weak link results in Figure 1.15, where the critical current Ic is taken as the maximum value of the function.
