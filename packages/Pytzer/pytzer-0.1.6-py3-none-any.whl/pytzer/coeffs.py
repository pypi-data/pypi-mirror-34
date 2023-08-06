import autograd.numpy as np
from autograd.extend import primitive, defvjp
from .constants import Patm_bar

#%%############################################################################
# === ZERO FUNCTIONS ==========================================================

def bC_zero(T):
    
    b0    = np.zeros_like(T)
    b1    = np.zeros_like(T)
    b2    = np.zeros_like(T)
    C0    = np.zeros_like(T)
    C1    = np.zeros_like(T)
    alph1 = np.full_like(T,-9)
    alph2 = np.full_like(T,-9)
    omega = np.full_like(T,-9)
    valid = T > 0
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

def theta_zero(T):
    
    theta = np.zeros_like(T)
    valid = T > 0
    
    return theta, valid

def psi_zero(T):
    
    psi   = np.zeros_like(T)
    valid = T > 0
    
    return psi, valid

# === ZERO FUNCTIONS ==========================================================
###############################################################################

#%%############################################################################
# === JESS VALUES =============================================================
    
# --- bC: calcium chloride ----------------------------------------------------
    
@primitive
def b0_Ca_Cl_JESS(T):
    return np.full_like(T,0.319270074367523, dtype='float64') # AC 298.15 K
def b0_Ca_Cl_JESS_vjp(ans,T):
    return lambda g: g * np.float_(0.000203132018214092) # HA 298.15 K
defvjp(b0_Ca_Cl_JESS,b0_Ca_Cl_JESS_vjp)

@primitive
def b1_Ca_Cl_JESS(T):
    return np.full_like(T,1.56483352184295, dtype='float64') # AC 298.15 K
def b1_Ca_Cl_JESS_vjp(ans,T):
    return lambda g: g * np.float_(0.00305774295702577) # HA 298.15 K
defvjp(b1_Ca_Cl_JESS,b1_Ca_Cl_JESS_vjp)

@primitive
def Cphi_Ca_Cl_JESS(T):
    return np.full_like(T,-0.000792843929957598, dtype='float64') # AC 298.15 K
def Cphi_Ca_Cl_JESS_vjp(ans,T):
    return lambda g: g * np.float_(-0.000161954856594093) # HA 298.15 K
defvjp(Cphi_Ca_Cl_JESS,Cphi_Ca_Cl_JESS_vjp)

def bC_Ca_Cl_JESS(T):
    
    b0 = b0_Ca_Cl_JESS(T)
    b1 = b1_Ca_Cl_JESS(T)
    b2 = np.zeros_like(T)
    
    Cphi = Cphi_Ca_Cl_JESS(T)
    
    zCa   = np.float_(+2)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zCa*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 297.65, T <= 298.65)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# === JESS VALUES =============================================================
###############################################################################

#%%############################################################################
# === DE LIMA & PITZER 1983 ===================================================

# --- bC: magnesium chloride --------------------------------------------------

def bC_Mg_Cl_dLP83(T):
    
    # dLP83 Eq. (11)
    
    b0   = 5.93915e-7 * T**2 \
         - 9.31654e-4 * T    \
         + 0.576066
        
    b1   = 2.60169e-5 * T**2 \
         - 1.09438e-2 * T    \
         + 2.60135
        
    b2 = np.zeros_like(T)
    
    Cphi = 3.01823e-7 * T**2 \
         - 2.89125e-4 * T    \
         + 6.57867e-2
    
    zMg   = np.float_(+2)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zMg*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# === DE LIMA & PITZER 1983 ===================================================
###############################################################################
    
#%%############################################################################
# === PALABAN & PITZER 1987 ===================================================

# Note that there are two Palaban & Pitzer (1987)'s: one compiling a suite of
#  electrolytes (PP87ii), and one just for NaOH (PP87i).
# There are also a bunch of Phutela & Pitzer papers in similar years, so will
#  need to take care with naming conventions!

# --- bC: sodium hydroxide ----------------------------------------------------

def PP87i_eqNaOH(T,a):
    
    P = Patm_bar
    
    return a[0]                 \
         + a[1]  * P            \
         + a[2]  / T            \
         + a[3]  * P / T        \
         + a[4]  * np.log(T)    \
         + a[5]  * T            \
         + a[6]  * T * P        \
         + a[7]  * T**2         \
         + a[8]  * T**2 * P     \
         + a[9]  / (T-227.)     \
         + a[10] / (647.-T)     \
         + a[11] * P / (647.-T)

def bC_Na_OH_PP87i(T):
    
    b0    = PP87i_eqNaOH(T,
                         np.float_([ 2.7682478e+2,
                                    -2.8131778e-3,
                                    -7.3755443e+3,
                                     3.7012540e-1,
                                    -4.9359970e+1,
                                     1.0945106e-1,
                                     7.1788733e-6,
                                    -4.0218506e-5,
                                    -5.8847404e-9,
                                     1.1931122e-1,
                                     2.4824963e00,
                                    -4.8217410e-3]))
    
    b1    = PP87i_eqNaOH(T,
                         np.float_([ 4.6286977e+2,
                                     0           ,
                                    -1.0294181e+4,
                                     0           ,
                                    -8.5960581e+1,
                                     2.3905969e-1,
                                     0           ,
                                    -1.0795894e-4,
                                     0           ,
                                     0           ,
                                     0           ,
                                     0           ]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = PP87i_eqNaOH(T,
                         np.float_([-1.66868970e+01,
                                     4.05347780e-04,
                                     4.53649610e+02,
                                    -5.17140170e-02,
                                     2.96807720e000,
                                    -6.51616670e-03,
                                    -1.05530373e-06,
                                     2.37657860e-06,
                                     8.98934050e-10,
                                    -6.89238990e-01,
                                    -8.11562860e-02,
                                     0             ]))
    
    zNa   = np.float_(+1)
    zOH   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zNa*zOH)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: magnesium chloride --------------------------------------------------

def bC_Mg_Cl_PP87i(T):
    
    b0,b1,b2,_,C1,alph1,alph2,omega,_ = bC_Mg_Cl_dLP83(T)
    
    Cphi = 2.41831e-7 * T**2 \
         - 2.49949e-4 * T    \
         + 5.95320e-2
    
    zMg   = np.float_(+2)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zMg*zCl)))
       
    valid = np.logical_and(T >= 298.15, T <= 473.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# === PALABAN & PITZER 1987 ===================================================
###############################################################################
    
#%%############################################################################
# === SIMONSON ET AL 1987 =====================================================

def SRRJ87_eq7(T,a):
    
    Tr = np.float_(298.15) 
    return a[0]                      \
         + a[1] * 1e-3 * (T - Tr)    \
         + a[2] * 1e-5 * (T - Tr)**2

# --- bC: potassium chloride --------------------------------------------------
    
def bC_K_Cl_SRRJ87(T):
    
    # Coefficients from SRRJ87 Table III
    
    b0   = SRRJ87_eq7(T,np.float_([ 0.0481,
                                    0.592 ,
                                   -0.562 ]))
    
    b1   = SRRJ87_eq7(T,np.float_([ 0.2188,
                                    1.500 ,
                                   -1.085 ]))
    
    b2 = np.zeros_like(T)
    
    Cphi = SRRJ87_eq7(T,np.float_([-0.790 ,
                                   -0.639 ,
                                    0.613 ]))
    
    zK    = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zK*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: sodium chloride -----------------------------------------------------
    
def bC_Na_Cl_SRRJ87(T):
    
    # Coefficients from SRRJ87 Table III
    
    b0   = SRRJ87_eq7(T,np.float_([ 0.0754,
                                    0.792 ,
                                   -0.935 ]))
    
    b1   = SRRJ87_eq7(T,np.float_([ 0.2770,
                                    1.006 ,
                                   -0.756 ]))
    
    b2 = np.zeros_like(T)
    
    Cphi = SRRJ87_eq7(T,np.float_([ 1.40  ,
                                   -1.20  ,
                                    1.15  ]))
    
    zNa   = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zNa*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: potassium borate ----------------------------------------------------
    
def bC_K_BOH4_SRRJ87(T):
    
    # Coefficients from SRRJ87 Table III
    
    b0   = SRRJ87_eq7(T,np.float_([  0.1469,
                                     2.881 ,
                                     0     ]))
    
    b1   = SRRJ87_eq7(T,np.float_([- 0.0989,
                                   - 6.876 ,
                                     0     ]))
    
    b2 = np.zeros_like(T)
    
    Cphi = SRRJ87_eq7(T,np.float_([-56.43  ,
                                   - 9.56  ,
                                     0     ]))
    
    zK    = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zK*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: sodium borate ----------------------------------------------------------------
    
def bC_Na_BOH4_SRRJ87(T):
    
    # Coefficients from SRRJ87 Table III
    
    b0   = SRRJ87_eq7(T,np.float_([- 0.0510,
                                     5.264 ,
                                     0     ]))
    
    b1   = SRRJ87_eq7(T,np.float_([  0.0961,
                                   -10.68  ,
                                     0     ]))
    
    b2 = np.zeros_like(T)
    
    Cphi = SRRJ87_eq7(T,np.float_([ 14.98  ,
                                   -15.7   ,
                                     0     ]))
    
    zNa   = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zNa*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- theta: borate chloride --------------------------------------------------
    
def theta_BOH4_Cl_SRRJ87(T):
    
    # Coefficient from SRRJ87 Table III
    
    theta = np.full_like(T,-0.056, dtype='float64')
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return theta, valid

# --- psi: potassium borate chloride ------------------------------------------
    
def psi_K_BOH4_Cl_SRRJ87(T):
    
    psi   = np.zeros_like(T)
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return psi, valid

# --- psi: sodium borate chloride ---------------------------------------------
    
def psi_Na_BOH4_Cl_SRRJ87(T):
    
    # Coefficient from SRRJ87 Table III
    
    psi   = np.full_like(T,-0.019, dtype='float64')
    
    valid = np.logical_and(T >= 278.15, T <= 328.15)
    
    return psi, valid

# === SIMONSON ET AL 1987 =====================================================    
###############################################################################

#%%############################################################################
# === MOLLER 1988 =============================================================

def M88_eq13(T,a):
    
    return a[0]             \
         + a[1] * T         \
         + a[2] / T         \
         + a[3] * np.log(T) \
         + a[4] / (T-263.)  \
         + a[5] * T**2      \
         + a[6] / (680.-T)  \
         + a[7] / (T-227.)

# --- Debye-Hueckel slope -----------------------------------------------------

def Aosm_M88(T):
    
    Aosm  = M88_eq13(T,
                     np.float_([ 3.36901532e-1,
                                -6.32100430e-4,
                                 9.14252359e00,
                                -1.35143986e-2,
                                 2.26089488e-3,
                                 1.92118597e-6,
                                 4.52586464e+1,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 573.15)
    
    return Aosm, valid

# --- bC: calcium chloride ----------------------------------------------------

@primitive
def b0_Ca_Cl_M88(T):
    return M88_eq13(T,
                    np.float_([-9.41895832e+1,
                               -4.04750026e-2,
                                2.34550368e+3,
                                1.70912300e+1,
                               -9.22885841e-1,
                                1.51488122e-5,
                               -1.39082000e00,
                                0            ]))
defvjp(b0_Ca_Cl_M88,b0_Ca_Cl_JESS_vjp)

@primitive
def b1_Ca_Cl_M88(T):
    return M88_eq13(T,
                    np.float_([ 3.47870000e00,
                               -1.54170000e-2,
                                0            ,
                                0            ,
                                0            ,
                                3.17910000e-5,
                                0            ,
                                0            ]))
defvjp(b1_Ca_Cl_M88,b1_Ca_Cl_JESS_vjp)

@primitive
def Cphi_Ca_Cl_M88(T):
    return M88_eq13(T,
                    np.float_([-3.03578731e+1,
                               -1.36264728e-2,
                                7.64582238e+2,
                                5.50458061e00,
                               -3.27377782e-1,
                                5.69405869e-6,
                               -5.36231106e-1,
                                0            ]))
defvjp(Cphi_Ca_Cl_M88,Cphi_Ca_Cl_JESS_vjp)

def bC_Ca_Cl_M88(T):
    
    b0    = b0_Ca_Cl_M88(T) 
    b1    = b1_Ca_Cl_M88(T)
    b2    = np.zeros_like(T)
    
    Cphi  = Cphi_Ca_Cl_M88(T)
    zCa   = np.float_(+2)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zCa*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: calcium sulfate -----------------------------------------------------

def bC_Ca_SO4_M88(T):
    
    b0    = np.full_like(T,0.15, dtype='float64')
    
    b1    = np.full_like(T,3.00, dtype='float64')
    
    b2    = M88_eq13(T,
                     np.float_([-1.29399287e+2,
                                 4.00431027e-1,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    C0    = np.zeros_like(T)
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(1.4)
    alph2 = np.float_(12)
    omega = -9
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: sodium chloride -----------------------------------------------------

def bC_Na_Cl_M88(T):
    
    b0    = M88_eq13(T,
                     np.float_([ 1.43783204e+1,
                                 5.60767406e-3,
                                -4.22185236e+2,
                                -2.51226677e00,
                                 0            ,
                                -2.61718135e-6,
                                 4.43854508e00,
                                -1.70502337e00]))
    
    b1    = M88_eq13(T,
                     np.float_([-4.83060685e-1,
                                 1.40677479e-3,
                                 1.19311989e+2,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                -4.23433299e00]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = M88_eq13(T,
                     np.float_([-1.00588714e-1,
                                -1.80529413e-5,
                                 8.61185543e00,
                                 1.24880954e-2,
                                 0            ,
                                 3.41172108e-8,
                                 6.83040995e-2,
                                 2.93922611e-1]))
    
    zNa   = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zNa*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 273.15, T <= 573.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: sodium sulfate ------------------------------------------------------

def bC_Na_SO4_M88(T):
    
    b0    = M88_eq13(T,
                     np.float_([ 8.16920027e+1,
                                 3.01104957e-2,
                                -2.32193726e+3,
                                -1.43780207e+1,
                                -6.66496111e-1,
                                -1.03923656e-5,
                                 0            ,
                                 0            ]))
    
    b1    = M88_eq13(T,
                     np.float_([ 1.00463018e+3,
                                 5.77453682e-1,
                                -2.18434467e+4,
                                -1.89110656e+2,
                                -2.03550548e-1,
                                -3.23949532e-4,
                                 1.46772243e+3,
                                 0            ]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = M88_eq13(T,
                     np.float_([-8.07816886e+1,
                                -3.54521126e-2,
                                 2.02438830e+3,
                                 1.46197730e+1,
                                -9.16974740e-2,
                                 1.43946005e-5,
                                -2.42272049e00,
                                 0            ]))
    
    zNa   = np.float_(+1)
    zSO4  = np.float_(-2)
    C0    = Cphi / (2 * np.sqrt(np.abs(zNa*zSO4)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 273.15, T <= 573.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- theta: calcium sodium ---------------------------------------------------
    
def theta_Ca_Na_M88(T):
    
    theta = np.full_like(T,0.05, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return theta, valid

# --- theta: chloride sulfate -------------------------------------------------
    
def theta_Cl_SO4_M88(T):
    
    theta = np.full_like(T,0.07, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 423.15)
    
    return theta, valid

# --- psi: calcium sodium chloride --------------------------------------------
    
def psi_Ca_Na_Cl_M88(T):
    
    psi = np.full_like(T,-0.003, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return psi, valid

# --- psi: calcium sodium sulfate ---------------------------------------------
    
def psi_Ca_Na_SO4_M88(T):
    
    psi = np.full_like(T,-0.012, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return psi, valid

# --- psi: calcium chloride sulfate -------------------------------------------
    
def psi_Ca_Cl_SO4_M88(T):
    
    psi = np.full_like(T,-0.018, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return psi, valid

# --- psi: sodium chloride sulfate --------------------------------------------
    
def psi_Na_Cl_SO4_M88(T):
    
    psi = np.full_like(T,-0.009, dtype='float64')
    
    valid = np.logical_and(T >= 298.15, T <= 423.15)
    
    return psi, valid

# --- dissociation: water -----------------------------------------------------
    
def dissoc_H2O_M88(T):
    
    lnKw  = M88_eq13(T,
                     np.float_([ 1.04031130e+3,
                                 4.86092851e-1,
                                -3.26224352e+4,
                                -1.90877133e+2,
                                -5.35204850e-1,
                                -2.32009393e-4,
                                 5.20549183e+1,
                                 0            ]))
    
    valid = np.logical_and(T >= 298.15, T <= 523.15)
    
    return np.exp(lnKw), valid

# === MOLLER 1988 =============================================================
###############################################################################

#%%############################################################################
# === GREENBERG & MOLLER 1989 =================================================
    
# --- inherit from M88 --------------------------------------------------------
    
GM89_eq3 = M88_eq13

# --- bC: calcium chloride ----------------------------------------------------

@primitive
def Cphi_Ca_Cl_GM89(T):
    return GM89_eq3(T,
                    np.float_([ 1.93056024e+1,
                                9.77090932e-3,
                               -4.28383748e+2,
                               -3.57996343e00,
                                8.82068538e-2,
                               -4.62270238e-6,
                                9.91113465e00,
                                0            ]))
defvjp(Cphi_Ca_Cl_GM89,Cphi_Ca_Cl_JESS_vjp)

def bC_Ca_Cl_GM89(T):
    
    b0,b1,b2,_,C1,alph1,alph2,omega,valid = bC_Ca_Cl_M88(T)
    
    Cphi  = Cphi_Ca_Cl_GM89(T)
    
    zCa   = np.float_(+2)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zCa*zCl)))
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: potassium chloride --------------------------------------------------

def bC_K_Cl_GM89(T):
    
    b0    = GM89_eq3(T,
                     np.float_([ 2.67375563e+1,
                                 1.00721050e-2,
                                -7.58485453e+2,
                                -4.70624175e00,
                                 0            ,
                                -3.75994338e-6,
                                 0            ,
                                 0            ]))
    
    b1    = GM89_eq3(T,
                     np.float_([-7.41559626e00,
                                 0            ,
                                 3.22892989e+2,
                                 1.16438557e00,
                                 0            ,
                                 0            ,
                                 0            ,
                                -5.94578140e00]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = GM89_eq3(T,
                     np.float_([-3.30531334e00,
                                -1.29807848e-3,
                                 9.12712100e+1,
                                 5.86450181e-1,
                                 0            ,
                                 4.95713573e-7,
                                 0            ,
                                 0            ]))
    
    zK    = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zK*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: potassium sulfate ---------------------------------------------------

def bC_K_SO4_GM89(T):
    
    b0    = GM89_eq3(T,
                     np.float_([ 4.07908797e+1,
                                 8.26906675e-3,
                                -1.41842998e+3,
                                -6.74728848e00,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    b1    = GM89_eq3(T,
                     np.float_([-1.31669651e+1,
                                 2.35793239e-2,
                                 2.06712594e+3,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = np.full_like(T,-0.0188, dtype='float64')
    
    zK    = np.float_(+1)
    zSO4  = np.float_(-2)
    C0    = Cphi / (2 * np.sqrt(np.abs(zK*zSO4)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- theta: calcium potassium ------------------------------------------------

def theta_Ca_K_GM89(T):
    
    theta = np.full_like(T,0.1156, dtype='float64')
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return theta, valid

# --- theta: potassium sodium -------------------------------------------------
    
def theta_K_Na_GM89(T):
    
    theta = GM89_eq3(T,
                     np.float_([-5.02312111e-2,
                                 0            ,
                                 1.40213141e+1,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return theta, valid

# --- psi: calcium potassium chloride -----------------------------------------
    
def psi_Ca_K_Cl_GM89(T):
    
    psi   = GM89_eq3(T,
                     np.float_([ 4.76278977e-2,
                                 0            ,
                                -2.70770507e+1,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return psi, valid

# --- psi: calcium potassium sulfate ------------------------------------------

def psi_Ca_K_SO4_GM89(T):
    
    theta = np.zeros_like(T)
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return theta, valid

# --- psi: potassium sodium chloride ------------------------------------------
    
def psi_K_Na_Cl_GM89(T):
    
    psi   = GM89_eq3(T,
                     np.float_([ 1.34211308e-2,
                                 0            ,
                                -5.10212917e00,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return psi, valid

# --- psi: potassium sodium sulfate -------------------------------------------
    
def psi_K_Na_SO4_GM89(T):
    
    psi   = GM89_eq3(T,
                     np.float_([ 3.48115174e-2,
                                 0            ,
                                -8.21656777e00,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 423.15)
    
    return psi, valid

# --- psi: potassium chloride sulfate -----------------------------------------
    
def psi_K_Cl_SO4_GM89(T):
    
    psi   = GM89_eq3(T,
                     np.float_([-2.12481475e-1,
                                 2.84698333e-4,
                                 3.75619614e+1,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ,
                                 0            ]))
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return psi, valid

# === GREENBERG & MOLLER 1989 =================================================
###############################################################################

#%%############################################################################
# === ARCHER 1992 =============================================================
    
# Set up p/T function
def A92ii_eq36(T,p,a):
    
    # a[5] and a[6] multipliers corrected for typos in A92ii
    
    return  a[ 0]                               \
          + a[ 1] * 10**-3 * T                  \
          + a[ 2] * 4e-6 * T**2                 \
          + a[ 3] * 1 / (T - 200)               \
          + a[ 4] * 1 / T                       \
          + a[ 5] * 100 / (T - 200)**2          \
          + a[ 6] * 200 / T**2                  \
          + a[ 7] * 8e-9 * T**3                 \
          + a[ 8] * 1 / (650 - T)**0.5          \
          + a[ 9] * 10**-5 * p                  \
          + a[10] * 2e-4 * p / (T - 225)        \
          + a[11] * 100 * p / (650 - T)**3      \
          + a[12] * 2e-8 * p * T                \
          + a[13] * 2e-4 * p / (650 - T)        \
          + a[14] * 10**-7 * p**2               \
          + a[15] * 2e-6 * p**2 / (T - 225)     \
          + a[16] * p**2 / (650 - T)**3         \
          + a[17] * 2e-10 * p**2 * T            \
          + a[18] * 4e-13 * p**2 * T**2         \
          + a[19] * 0.04 * p / (T - 225)**2     \
          + a[20] * 4e-11 * p * T**2            \
          + a[21] * 2e-8 * p**3 / (T - 225)     \
          + a[22] * 0.01 * p**3 / (650 - T)**3  \
          + a[23] * 200 / (650 - T)**3

# --- bC: sodium chloride -----------------------------------------------------

def bC_Na_Cl_A92ii(T):

    # Pressure can be varied
    p = np.float_(0.101325) # MPa

    # Coefficients from A92ii Table 2
    
    b0 = A92ii_eq36(T,p,np.float_([ \
              0.242408292826506,
              0,
            - 0.162683350691532,
              1.38092472558595,
              0,
              0,
            -67.2829389568145,
              0,
              0.625057580755179,
            -21.2229227815693,
             81.8424235648693,
            - 1.59406444547912,
              0,
              0,
             28.6950512789644,
            -44.3370250373270,
              1.92540008303069,
            -32.7614200872551,
              0,
              0,
             30.9810098813807,
              2.46955572958185,
            - 0.725462987197141,
             10.1525038212526   ]))

    b1 = A92ii_eq36(T,p,np.float_([ \
            - 1.90196616618343,
              5.45706235080812,
              0,
            -40.5376417191367,
              0,
              0,
              4.85065273169753  * 1e2,
            - 0.661657744698137,
              0,
              0,
              2.42206192927009  * 1e2,
              0,
            -99.0388993875343,
              0,
              0,
            -59.5815563506284,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0                  ]))

    b2 = np.zeros_like(T)

    C0 = A92ii_eq36(T,p,np.float_([ \
              0,
            - 0.0412678780636594,
              0.0193288071168756,
            - 0.338020294958017,      # typo in A92ii
              0,
              0.0426735015911910,
              4.14522615601883,
            - 0.00296587329276653,
              0,
              1.39697497853107,
            - 3.80140519885645,
              0.06622025084,          # typo in A92ii - "Rard's letter"
              0,
            -16.8888941636379,
            - 2.49300473562086,
              3.14339757137651,
              0,
              2.79586652877114,
              0,
              0,
              0,
              0,
              0,
            - 0.502708980699711   ]))

    C1 = A92ii_eq36(T,p,np.float_([ \
              0.788987974218570,
            - 3.67121085194744,
              1.12604294979204,
              0,
              0,
            -10.1089172644722,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
             16.6503495528290      ]))

    # Alpha and omega values
    alph1 = np.float_(2)
    alph2 = -9
    omega = np.float_(2.5)

    # Validity range
    valid = np.logical_and(T >= 250, T <= 600)
    valid = np.logical_and(valid, p <= 100)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# === ARCHER 1992 =============================================================           
###############################################################################

#%%############################################################################
# === CAMPBELL ET AL 1993 =====================================================

# --- inherit from M88 --------------------------------------------------------
    
CMR93_eq31 = M88_eq13

# --- bC: hydrogen chloride ---------------------------------------------------

def bC_H_Cl_CMR93(T):
    
    b0    = CMR93_eq31(T,
                       np.float_([   1.2859     ,
                                  -  1.1197e-3  ,
                                  -142.5877     ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ]))
    
    b1    = CMR93_eq31(T,
                       np.float_([-  4.4474     ,
                                     8.425698e-3,
                                   665.7882     ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ]))
    
    b2    = np.zeros_like(T)
    
    Cphi  = CMR93_eq31(T,
                       np.float_([-  0.305156   ,
                                     5.16e-4    ,
                                    45.52154    ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ,
                                     0          ]))
    
    zH    = np.float_(+1)
    zCl   = np.float_(-1)
    C0    = Cphi / (2 * np.sqrt(np.abs(zH*zCl)))
    
    C1    = np.zeros_like(T)
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- theta: hydrogen potassium -----------------------------------------------

def theta_H_K_CMR93(T):
    
    theta = np.float_(0.005) - np.float_(0.0002275) * T
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return theta, valid

# --- theta: hydrogen sodium --------------------------------------------------

def theta_H_Na_CMR93(T):
    
    theta = np.float_(0.0342) - np.float_(0.000209) * T
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return theta, valid

# --- psi: hydrogen potassium chloride ----------------------------------------

def psi_H_K_Cl_CMR93(T):
    
    psi   = np.zeros_like(T)
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return psi, valid

# --- psi: hydrogen sodium chloride -------------------------------------------

def psi_H_Na_Cl_CMR93(T):
    
    psi   = np.zeros_like(T)
    
    valid = np.logical_and(T >= 273.15, T <= 523.15)
    
    return psi, valid

# === CAMPBELL ET AL 1993 =====================================================
###############################################################################

#%%############################################################################
# === CLEGG ET AL 1994 ========================================================    

# --- Debye-Hueckel slope -----------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOT AUTOGRAD-ABLE due to updating Tmx
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Aosm_CRP94(T): # CRP94 Appendix II

    # Transform temperature
    T = T.ravel()
    X = (2 * T - 373.15 - 234.15) / (373.15 - 234.15)

    # Set coefficients - CRP94 Table 11
    a_Aosm = np.float_( \
             [ 0.797256081240 / 2,
               0.573389669896e-1,
               0.977632177788e-3,
               0.489973732417e-2,
              -0.313151784342e-2,
               0.179145971002e-2,
              -0.920584241844e-3,
               0.443862726879e-3,
              -0.203661129991e-3,
               0.900924147948e-4,
              -0.388189392385e-4,
               0.164245088592e-4,
              -0.686031972567e-5,
               0.283455806377e-5,
              -0.115641433004e-5,
               0.461489672579e-6,
              -0.177069754948e-6,
               0.612464488231e-7,
              -0.175689013085e-7])

    # Set up T matrix - CRP94 Eq. (AII2)
    Tmx = np.full((np.size(T),np.size(a_Aosm)),1.)
    Tmx[:,1] = X
    for C in range(2,np.size(a_Aosm)):
        Tmx[:,C] = 2 * X * Tmx[:,C-1] - Tmx[:,C-2]

    # Solve for Aosm (CRP94 E.AII1)
    Aosm = np.matmul(Tmx,a_Aosm)

    # Validity range
    valid = np.logical_and(T >= 234.15, T <= 373.15)

    return Aosm, valid

# --- betas and Cs ------------------------------------------------------------

CRP94_Tr = np.float_(328.15) # K

def CRP94_eq24(T,q):
    return q[0] + 1e-3 *                 \
        ( (T-CRP94_Tr)    * q[1]         \
        + (T-CRP94_Tr)**2 * q[2] / 2.    \
        + (T-CRP94_Tr)**3 * q[3] / 6.)

# --- bC: hydrogen bisulfate --------------------------------------------------

def bC_H_HSO4_CRP94(T):

    # Evaluate coefficients, parameters from CRP94 Table 6
    b0 = CRP94_eq24(T,
                    np.float_([  0.227784933   ,
                               - 3.78667718    ,
                               - 0.124645729   ,
                               - 0.00235747806 ]))
    
    b1 = CRP94_eq24(T,
                    np.float_([  0.372293409   ,
                                 1.50          ,
                                 0.207494846   ,
                                 0.00448526492 ]))  
    
    b2    = np.zeros_like(T)
    
    C0 = CRP94_eq24(T,
                    np.float_([- 0.00280032520 ,
                                 0.216200279   ,
                                 0.0101500824  ,
                                 0.000208682230]))
    
    C1 = CRP94_eq24(T,
                    np.float_([- 0.025         ,
                                18.1728946     ,
                                 0.382383535   ,
                                 0.0025        ]))
    
    alph1 = np.float_(2)
    alph2 = -9
    omega = np.float_(2.5)

    valid = np.logical_and(T >= 273.15, T <= 328.15)

    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- bC: hydrogen sulfate ----------------------------------------------------

def bC_H_SO4_CRP94(T):

    # Evaluate coefficients, parameters from CRP94 Table 6
    b0 = CRP94_eq24(T,
                    np.float_([  0.0348925351  ,
                                 4.97207803    ,
                                 0.317555182   ,
                                 0.00822580341 ]))
    
    b1 = CRP94_eq24(T,
                    np.float_([- 1.06641231    ,
                               -74.6840429     ,
                               - 2.26268944    ,
                               - 0.0352968547  ]))
    
    b2    = np.zeros_like(T)
    
    C0 = CRP94_eq24(T,
                    np.float_([  0.00764778951 ,
                               - 0.314698817   ,
                               - 0.0211926525  ,
                               - 0.000586708222]))
    
    C1 = CRP94_eq24(T,
                    np.float_([  0.0           ,
                               - 0.176776695   ,
                               - 0.731035345   ,
                                 0.0           ]))

    alph1 = 2 - 1842.843 * (1/T - 1/298.15)
    alph2 = -9
    omega = np.float_(2.5)

    valid = np.logical_and(T >= 273.15, T <= 328.15)

    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# --- theta: bisulfate sulfate ------------------------------------------------
    
def theta_HSO4_SO4_CRP94(T):
    
    theta = np.zeros_like(T)
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return theta, valid

# --- psi: hydrogen bisulfate sulfate -----------------------------------------
    
def psi_H_HSO4_SO4_CRP94(T):
    
    psi   = np.zeros_like(T)
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return psi, valid

# --- dissociation: bisulfate -------------------------------------------------

def dissoc_HSO4_CRP94(T):
    
    valid = np.logical_and(T >= 273.15, T <= 328.15)
    
    return 10**(562.69486 - 102.5154 * np.log(T) \
        - 1.117033e-4 * T**2 + 0.2477538*T - 13273.75/T), valid

# === CLEGG ET AL 1994 ========================================================    
###############################################################################
    
#%%############################################################################
# === ARCHER 1999 =============================================================

def A99_eq22(T,a):

    Tref  = 298.15
    
    return   a[0]                        \
           + a[1] * (T - Tref)    * 1e-2 \
           + a[2] * (T - Tref)**2 * 1e-5 \
           + a[3] * 1e2 / (T - 225)      \
           + a[4] * 1e3 /  T             \
           + a[5] * 1e6 / (T - 225)**3

# --- bC: potassium chloride --------------------------------------------------

def bC_K_Cl_A99(T):

    # KCl T parameters from A99 Table 4
    b0 = A99_eq22(T,np.float_( \
           [ 0.413229483398493  ,
            -0.0870121476114027 ,
             0.101413736179231  ,
            -0.0199822538522801 ,
            -0.0998120581680816 ,
             0                  ]))

    b1 = A99_eq22(T,np.float_( \
           [ 0.206691413598171  ,
             0.102544606022162  ,
             0,
             0,
             0,
            -0.00188349608000903]))

    b2 = np.zeros_like(T)

    C0 = A99_eq22(T,np.float_( \
           [-0.00133515934994478,
             0,
             0,
             0.00234117693834228,
            -0.00075896583546707,
             0                  ]))

    C1 = np.zeros_like(T)

    # Alpha and omega values
    alph1 = np.float_(2)
    alph2 = -9
    omega = -9

    # Validity range
    valid = np.logical_and(T >= 260, T <= 420)
    
    return b0, b1, b2, C0, C1, alph1, alph2, omega, valid

# === ARCHER 1999 =============================================================    
###############################################################################

#%%############################################################################
# === UNPUBLISHED =============================================================

# --- DH lim.slope: osmotic coefficient ---------------------------------------
    
def Aosm_MPH(T):
    
    # Centre and scale temperature
    mu_T    = np.float_(318.15   )
    sigma_T = np.float_( 33.91165)
    Tn = (T - mu_T) / sigma_T
    
    # Define polynomial coefficients
    aosmi = np.float_( \
          [ 0.4062019   ,
            0.02712083  ,
            0.003647629 ,
            3.969679e-05,
            5.102238e-05,
           -7.672292e-05,
           -5.178963e-05,
            6.632046e-05,
            3.698934e-06,
           -9.619149e-06])

    # Evaluate AH
    Aosm =  aosmi[0]         \
          + aosmi[1] * Tn    \
          + aosmi[2] * Tn**2 \
          + aosmi[3] * Tn**3 \
          + aosmi[4] * Tn**4 \
          + aosmi[5] * Tn**5 \
          + aosmi[6] * Tn**6 \
          + aosmi[7] * Tn**7 \
          + aosmi[8] * Tn**8 \
          + aosmi[9] * Tn**9

    # Check temperature is in range
    valid = np.logical_and(T >= 263.15,T <= 373.15)

    return Aosm, valid

# --- DH lim. slope: app. molar heat capacity @ const. P ----------------------

def AC_MPH(T):
    
    # Centre and scale temperature
    mu_T    = np.float_(318.15   )
    sigma_T = np.float_( 33.91165)
    Tn = (T - mu_T) / sigma_T

    # Define polynomial coefficients
    aCi = np.float_( \
          [ 38.46378      ,
            10.58136      ,
             0.4002028    ,
             1.428966     ,
           - 1.022148     ,
             0.6230761    ,
           - 0.0006836758 ,
             0.00003146005,
           - 0.1415504    ,
             0.05742008   ])

    # Evaluate AH
    AC =  aCi[0]         \
        + aCi[1] * Tn    \
        + aCi[2] * Tn**2 \
        + aCi[3] * Tn**3 \
        + aCi[4] * Tn**4 \
        + aCi[5] * Tn**5 \
        + aCi[6] * Tn**6 \
        + aCi[7] * Tn**7 \
        + aCi[8] * Tn**8 \
        + aCi[9] * Tn**9

    # Check temperature is in range
    valid = np.logical_and(T >= 263.15,T <= 373.15)

    return AC, valid

# --- DH lim. slope: app. molar enthalpy --------------------------------------

@primitive
def AH_MPH(T):

    # Centre and scale temperature
    mu_T    = np.float_(318.15   )
    sigma_T = np.float_( 33.91165)
    Tn = (T - mu_T) / sigma_T

    # Define polynomial coefficients
    aHi = np.float_( \
          [ 2.693456    ,
            1.30448     ,
            0.1786872   ,
            0.004058462 ,
            0.01450615  ,
           -0.006302474 ,
            0.0008198109,
           -0.0003247116,
            0.001233857 ,
           -0.0004777861]) * 1e3

    # Evaluate AH
    AH =  aHi[0]         \
        + aHi[1] * Tn    \
        + aHi[2] * Tn**2 \
        + aHi[3] * Tn**3 \
        + aHi[4] * Tn**4 \
        + aHi[5] * Tn**5 \
        + aHi[6] * Tn**6 \
        + aHi[7] * Tn**7 \
        + aHi[8] * Tn**8 \
        + aHi[9] * Tn**9

# !!!!! NOTE !!!!!!!
# Needed to remove valid output to get primitive grad to work

#    # Check temperature is in range
#    valid = np.logical_and(T >= 263.15,T <= 373.15)

    return AH#, valid

# Set AC as AH's temperature derivative
def AH_vjp(ans,T):    
    return lambda g: g * AC_MPH(T)[0]
defvjp(AH_MPH,AH_vjp)

# === UNPUBLISHED =============================================================    
###############################################################################
                    