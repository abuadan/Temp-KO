Temperature dependence of Josephson junction critical current based on KO-I and KO-II equations 
==============

Named after the British physicist Brian Josephson [1], Josephson junctions are a subset of weak links; a family of structures that display the Josephson effect. Such structures have an important application in voltage standards [2], quantum-mechanical circuits, such as Superconducting QUantum Interference Devices (SQUIDs) [3], superconducting qubits [4], and RSFQ digital electronics [5]. Different examples of Josephson junctions are shown in Figure below.

<p><img align="..." src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/410811/junctions-eps-converted-to.pdf" width="300" title="Different types of structures where the Josephson effect can take place. (a) tunnel junction, for example, S-I-S sandwich. All others are dif- ferent weak links (structures with direct non-tunnel-type conductivity): (b) sandwich, (c) proximity effect bridge, (d) ion implanted bridge, (e) Dayem bridge, (f) variable thickness bridge, (g) point contact, (h) blob type junction. S = Superconducting, S’ = superconducting with reduced critical parameters, SE = semiconductor (usually highly doped), N = normal metal and I = Insulator. Adapted from Likharev [6]"></p>

To understand the unique and important features of Josephson junctions, it's first necessary to understand the basic concepts and features of superconductivity. Whenever you cool many metals and alloys to very low temperatures (kelvin and millikelvin temperatures), a phase transition occurs. At this "critical temperature, (T<sub>c</sub>)" the metal goes from what is known as the normal state, where it has electrical resistance, to the superconducting state, where there is essentially no resistance to the flow of direct electrical current, the resistance returns when either the temperature is brought back above the critical temperature or the current through the device is higher than a critical current I<sub>c</sub>. As such evaluating the performance of Josephson junctions is determined by the parameters;
- Critical Temperature T<sub>c</sub>
- Operating temperature T
- Critical current I<sub>c</sub>
- Normal State Resistance R<sub>N</sub>

Hence determining the critical current of different weak links is an important step in modelling Joesphson junctions. In 1975 and 1977, Kulik and Omelyanchuk developed a set of equations that model the effect of temperature on I<sub>c</sub> of different weak links.

KO (I) and KO (II)
--------------
- The first case (denoted as (KO-I)) [6] applies to dirty or short weak links and is given as:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/417966/eq1.pdf" width="600">

where &#948;, the n<sup>th</sup> Matsubara frequency &#295;&#969; and &#916; are respectively given as:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/417964/eq2.pdf" width=700>

where n is a positive integer and &#916;<sub>o</sub> = 3.528k<sub>B</sub>T<sub>c</sub>. Plotting the resulting I<sub>c</sub>(&phi;)R<sub>N</sub> as a function of the phase for a typical short weak link results in Figure below, where the critical current I<sub>c</sub> is taken as the maximum value of the function. 

<p><img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/414991/current_phase-eps-converted-to.pdf" width="400" title="I<sub>s</sub>(&phi;) relationship for a typical short Nb weak link produced from the KO(I) equations, I<sub>s</sub>(&phi;) tends from a sinusoidal to a non-sinusoidal relation as T&rarr;0. I<sub>c</sub> is taken as the maximum value of the function"></p>

- The second case(KO-II) [7] applies to clean or long weak links and gives:

<img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/417962/eq3.pdf" width="600">

Plotting the I<sub>c</sub>(&phi;)R<sub>N</sub> in this region gives the behaviour shown below;

<p><img src="https://github.com/abuadan/Temperature-Dependance-of-Josephson-Junctions-based-on-KOI-II-/files/415091/current_phase1-eps-converted-to.pdf" width = "400" title="I<sub>c</sub>(&phi;) relationship for a typical long/clean weak link produced from the KO(II) equations, as with the KO(I) theory, I<sub>c</sub>(&phi;) tends from a sinusoidal to a non-sinusoidal relation as T&rarr;0."></p>

Considering the maximum of both the KO (I) and KO (II) equations, a graphical representation of the the temperature dependence of I<sub>c</sub> can be produced for each case. The Python code in this repository illustrates this final step and produces a graph of I<sub>c</sub> as a fucntion of temperature.

References
============================
1. J. B. D., Supercurrents through barriers, Adv. Phys. 14, 419 (1965).
2. J. Kohlmann and R. Behr, Development of Josephson voltage standards, Superconductivity—Theory and Applications p. 239 (2011).
3. B. N. Taylor, W. H. Parker, D. N. Langenberg and A. Denenstein, On the use of the ac Josephson effect to maintain standards of electromotive force, Metrologia 3, 89 (1967).
4. G. P. Antonio Barone, Physics and Applications of the Josephson Effect, Physics and Applications of the Josephson Effect (1982).
5. S. Anders, European roadmap on superconductive electronics status and perspectives, Physica 470, 2079 (2010).
6. K. K. Likharev, Superconducting weak links, Rev. Mod. Phys. 51, 101–159 (1979).
7. K. K. Likharev, Dynamics of Josephson Junctions and Circuits, Dynamics of Joseph- son Junctions and Circuits p. 614 (1986).


