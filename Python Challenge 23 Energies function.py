#A function to calculate and print the three energies, kinetic, potential and mecanical.

def energies(m, v, h):
    g = 9.81
    Ec = 0.5*m*v**2
    Ep = m*g*h
    Em = Ec + Ep
    print("Kinetic energy: {} J".format(Ec))
    print("Potential energy: {} J".format(Ep))
    print("Mecanical energy: {} J".format(Em))


#energies(0.1, 2, 10)    