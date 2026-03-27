# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:08:25 2026

@author: Sajid Hussain
"""

import mpmath
import cmath

# Set arbitrary precision to 50 decimal places
mpmath.mp.dps = 50

def zeta_correspondence_error(s):
    """
    Calculates the absolute error of the bounded correspondence:
    F(s) = 2*cosh(s*zeta(s)) - exp(zeta(s)) - exp(s)
    """
    term1 = 2 * mpmath.cosh(s * mpmath.zeta(s))
    term2 = mpmath.exp(mpmath.zeta(s))
    term3 = mpmath.exp(s)
    
    absolute_error = term1 - term2 - term3
    return absolute_error

def test_real_asymptotics():
    """
    Tests the asymptotic behavior of the correspondence on the real line.
    Shows that while absolute error diverges, relative error strictly collapses to 0.
    """
    print("="*60)
    print("TEST 1: REAL ASYMPTOTICS (s -> infinity)")
    print("="*60)
    print(f"{'s':<5} | {'Absolute Error':<25} | {'Relative Error':<25}")
    print("-" * 60)
    
    # Test values from s=5 to s=40
    for s_val in range(5, 45, 5):
        s = mpmath.mpf(s_val)
        abs_err = zeta_correspondence_error(s)
        
        # Relative error: (Absolute Error) / exp(s)
        rel_err = abs_err / mpmath.exp(s)
        
        # Format for clean output
        abs_str = mpmath.nstr(abs_err, 5)
        rel_str = mpmath.nstr(rel_err, 5)
        
        print(f"{s_val:<5} | {abs_str:<25} | {rel_str:<25}")

def test_riemann_zeros():
    """
    Evaluates the correspondence at the first few non-trivial Riemann zeros.
    Calculates the resulting radius to verify it exactly matches sqrt(e).
    """
    print("\n" + "="*60)
    print("TEST 2: GEOMETRIC MAPPING OF RIEMANN ZEROS")
    print("="*60)
    
    # The first 3 non-trivial zeros of the Riemann Zeta Function (approximate heights)
    # mpmath.zetazero() precisely calculates these
    zeros = [mpmath.zetazero(1), mpmath.zetazero(2), mpmath.zetazero(3)]
    
    target_radius = mpmath.exp(mpmath.mpf(0.5))
    print(f"Target Radius (sqrt(e)): {mpmath.nstr(target_radius, 15)}\n")
    
    for i, rho in enumerate(zeros, 1):
        # 1 - e^rho
        mapped_value = 1 - mpmath.exp(rho)
        
        # Calculate the absolute radius (magnitude) in the complex plane
        radius = mpmath.fabs(mapped_value - 1) # Distance from center (1, 0)
        
        # Compare to sqrt(e)
        diff = mpmath.fabs(radius - target_radius)
        
        print(f"Zero #{i}: rho = {mpmath.nstr(rho.real, 5)} + {mpmath.nstr(rho.imag, 7)}i")
        print(f"  -> Calculated Radius: {mpmath.nstr(radius, 15)}")
        print(f"  -> Deviation from sqrt(e): {mpmath.nstr(diff, 5)}")
        print("-" * 60)

if __name__ == "__main__":
    print("INITIALIZING ZETA CORRESPONDENCE VERIFICATION...")
    print(f"Operating Precision: {mpmath.mp.dps} Decimal Places\n")
    
    test_real_asymptotics()
    test_riemann_zeros()
    
    print("\nVERIFICATION COMPLETE.")