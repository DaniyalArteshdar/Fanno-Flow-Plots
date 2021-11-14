# Coded Daniyal Arteshdar - Fanno Flow

import matplotlib.pylab as plt
import numpy as np

# Initioal Conditions

Gama=1.4
R=8.314472
Mach1 =  np.linspace(0, 4)

# Equations for Fanno Flow

P_Pstar=(((1+Gama)/(2+(Gama-1)*(Mach1**2)))**0.5)*(1/Mach1)
P0_P0star=((2+(Gama-1)*(Mach1**2))/(Gama+1))**((Gama+1)/(2**(Gama-1)))
t_tstar=1/((2+(Gama-1)*(Mach1**2))/(Gama+1))
Ro_Rostar=(1/Mach1)*((((2+(Gama-1)*(Mach1**2))/(Gama+1)))**0.5)
flstar_D=((1-Mach1**2)/(Gama*(Mach1**2)))+((Gama+1)/(2*Gama))*np.log(((Gama+1)*Mach1**2)/(2+(Gama-1)*(Mach1**2)))
S_Sstar_R= -1 * np.log((1/Mach1)*((2/(Gama+1))*(1+((Gama-1)*Mach1)/2))**((Gama+1)/(2*Gama-2)))

# Codes for plotting

plt.plot(Mach1,P_Pstar, label='P/P*')
plt.plot(Mach1,P0_P0star, label='P0/P0*')
plt.plot(Mach1,t_tstar, label='t/t*')
plt.plot(Mach1,Ro_Rostar, label='ρ/ρ*')
plt.plot(Mach1,flstar_D, label='Fl*/D')
plt.plot(Mach1,S_Sstar_R, label='(S-S*)/R')

plt.xlabel('Mach Number')
plt.ylabel('Ratio')
plt.title('Fanno Flow - Daniyal Arteshdar')
plt.ylim(0,5)
plt.legend()
plt.grid()
plt.show()

# The Outputs of Data

print("** The proportion of P/P* based on Mach Numbers **\n", P_Pstar, "\n")
print("** The proportion of P0/P0* based on Mach Numbers **\n", P0_P0star, "\n")
print("** The proportion of t/t* based on Mach Numbers **\n", t_tstar, "\n")
print("** The proportion of ρ/ρ* based on Mach Numbers **\n", Ro_Rostar, "\n")
print("** The proportion of Fl*/D based on Mach Numbers **\n", flstar_D, "\n")
print("** The proportion of S_Sstar_R based on Mach Numbers **\n", S_Sstar_R, "\n")
