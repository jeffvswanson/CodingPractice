# hydrocarbonMass.py
# A program which calculates the mass of a hydrocarbon molecule.
"""Write a program that computes the molecular weight of a carbohydrate (in
grams per mole) base on the number of hydrogen, carbon, and oxygen atoms in the
molecule. The grogram should prompt the user to enter the number of hydrogen
atoms, the number of carbon atoms, and the number of oxygen atoms. The
program then prints the total combined molecular weight of all the atoms based
on these individula atom weights:

Atom       Weight
        (grams/mole)
--------------------
  H        1.00794
  C        12.0107
  O        15/9994

    For example, the colecular weight of water (H2O) is:
    2(1.00794) + 15.9994 = 18.01528."""

import math

def main():

    h = 1.00794 # Mass of hydrogen (grams/mole)
    c = 12.0107 # Mass of carbon (grams/mole)
    o = 15.9994 # Mass of oxygen (grams/mole)
    mass = 0

    print("This program calculates the mass of a hydrocarbon molecule.")

    numH = int(input("Please enter the number of hydrogen atoms, H, in the molecule: "))
    numC = int(input("Please enter the number of carbon atoms, C, in the molecule: "))
    numO = int(input("Please enter the number of oxygen atoms, O, in the molecule: "))
    
    mass = numH * h + numC * c + numO * o

    print("The mass of the hydrocarbon molecule is {:.4f} grams/mole.".format(mass))

main()
