


circuit.cx(2,8)
circuit.cx(3,8)
circuit.cx(4,8)

circuit.cz(2,8)
circuit.cz(3,8)



alpha = pi / 2
beta =  pi / 2
gamma =  pi / 2


circuit.ry(alpha, 8)
circuit.rz(beta , 8)
circuit.ry(gamma , 8)


circuit.draw('mpl')