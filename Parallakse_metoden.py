
import numpy as np


# Egentlig_radius_af_Jupiter = 71492 # km

# målte_radius_af_jupiter = 51.8

# Vinkel_mellem_sol_og_jord =  4.5526*(2*np.pi/360)

# io_midten = 42.28

# skygge_midten = 21.76 

# Radius_ved_omløb = 51.8


def afstands_måler(Radius_planet,Målte_radius,Radius_omløb, Vinkel_sol_jord, Io_midtpunkt, Skygge_midtpunkt, samme_side = False):
    
    Vinkel_sol_jord = Vinkel_sol_jord*(2*np.pi/360)
    
    Radius_i_km = Radius_planet*(Radius_omløb/Målte_radius)
    
    
    Vinkel_mellem_io_og_midte = np.arcsin(Io_midtpunkt/Radius_omløb) 
    
    
    Vinkel_mellem_skygge_og_midte = np.arcsin(Skygge_midtpunkt/Radius_omløb)
    
    Indre_vinkel_øverst = Vinkel_mellem_io_og_midte
    
    indre_vinkel_nederst = Vinkel_mellem_skygge_og_midte+Vinkel_sol_jord
    
    Afstand_mellem_io_og_jupiter = (Radius_i_km/Vinkel_sol_jord)*(np.sin(Indre_vinkel_øverst)+np.sin(indre_vinkel_nederst))
    
    if samme_side:
        Vinkel_sol_jord = np.abs(Vinkel_sol_jord)
        
        indre_vinkel_nederst = np.abs(-Vinkel_mellem_skygge_og_midte+Vinkel_sol_jord)
        
        Afstand_mellem_io_og_jupiter = (Radius_i_km/Vinkel_sol_jord)*np.abs(np.sin(Indre_vinkel_øverst)-np.sin(indre_vinkel_nederst))
        
    
    
    return print(f"Den målte afstand mellem Io og jupiter: {Afstand_mellem_io_og_jupiter:.2f} Km")
  
# samme_side = True
# afstands_måler(Egentlig_radius_af_Jupiter,målte_radius_af_jupiter,Radius_ved_omløb,Vinkel_mellem_sol_og_jord,io_midten,skygge_midten,samme_side)