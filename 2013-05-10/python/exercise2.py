from pyplasm import *

# FUNZIONI DI SUPPORTO
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

def bezierS1(controlpoints):
	return BEZIER(S1)(controlpoints)

def bezierS2(f):
	return BEZIER(S2)(f)


def bezierMappata_1D(controlpoints):
	return MAP(bezierS1(controlpoints))(INTERVALS(1)(32))

def bezierMappata_2D(functions):
	return MAP(BEZIER(S2)(functions))(dom2D)

def scambia(elemento):
	return [S1(elemento),S3(elemento),S2(elemento)]

def invertiXZ(array):
	return AA(scambia)(array)

def scambiaYZ(elemento):
	return [S3(elemento),S2(elemento),S1(elemento)]

def invertiYZ(array):
	return AA(scambiaYZ)(array)


#PIANO XY

p1 = [[7.73, 1.68], [6.55, 1.68], [6.58, 2.3], [6.68, 2.47]]
p1Bez = bezierMappata_1D(p1);

p2 = [[8.89, 3.43], [8.27, 3.2], [6.95, 2.99], [6.68, 2.47]]
p2Bez = bezierMappata_1D(p2);

p3 = [[8.89, 3.43], [10.46, 3.76], [10.93, 3.44], [11.81, 2.83]]
p3Bez = bezierMappata_1D(p3);

p4 = [[14.25, 1.9], [14.38, 2.59], [12.31, 2.84], [11.81, 2.83]]
p4Bez = bezierMappata_1D(p4);

p5 = [[14.25, 1.9], [14.02, 1.52], [13.6, 1.62], [13.1, 1.59]]
p5Bez = bezierMappata_1D(p5);

p6 = [[11.81, 1.62], [11.55, 2.56], [13.29, 2.98], [13.1, 1.59]]
p6Bez = bezierMappata_1D(p6);

p7 = [[11.81, 1.62], [10.18, 1.66], [9.69, 1.65], [9.12, 1.56]]
p7Bez = bezierMappata_1D(p7);

p8 = [[7.73, 1.68], [7.95, 2.98], [9.24, 2.61], [9.12, 1.56]]
p8Bez = bezierMappata_1D(p8)

xy = STRUCT([p1Bez,p2Bez,p3Bez,p4Bez,p5Bez,p6Bez, p7Bez,p8Bez])
xy = T([1,2])([-10.03,-2.58])(xy)

# PIANO XZ

y1 = [[7.85, 0.29,0], [6.64, 0.65,0], [6.72, 0.68,0], [6.63, 1.9,0]]
y1 = invertiXZ(y1)
y1Bez = bezierMappata_1D(y1)

y2 = [[7.85, 3.39,0], [6.47, 2.99,0], [6.73, 2.74,0], [6.63, 1.9,0]]
y2 = invertiXZ(y2)
y2Bez = bezierMappata_1D(y2)

y3 = [[7.85, 3.39,0], [8.66, 3.32,0], [11.18, 3.28,0], [12.93, 3.29,0]]
y3 = invertiXZ(y3)
y3Bez = bezierMappata_1D(y3)

y4 = [[14.26, 1.81,0], [14.06, 2.44,0], [14.32, 3.12,0], [12.93, 3.29,0]]
y4 = invertiXZ(y4)
y4Bez = bezierMappata_1D(y4)

y5 = [[14.26, 1.81,0], [13.91, 0.31,0], [13.71, 0.56,0], [12.83, 0.37,0]]
y5 = invertiXZ(y5)
y5Bez = bezierMappata_1D(y5)

y6 = [[7.85, 0.29,0], [9.52, 0.33,0], [11.33, 0.41,0], [12.83, 0.37,0]]
y6 = invertiXZ(y6)
y6Bez = bezierMappata_1D(y6)

xz = STRUCT([y1Bez,y2Bez,y3Bez,y4Bez,y5Bez,y6Bez])
xz = T([1,3])([-10.1,-1.8])(xz)

# PIANO YZ

x1 = [[11.11, 1.62,0], [10.64, 2.94,0], [11.2, 2.69,0], [11.24, 2.82,0]]
x1 = invertiYZ(x1)
x1Bez = bezierMappata_1D(x1)

x2 = [[12.53, 3.57,0], [11.33, 3.52,0], [11.53, 3.43,0], [11.24, 2.82,0]]
x2 = invertiYZ(x2)
x2Bez = bezierMappata_1D(x2)

x3 = [[12.53, 3.57,0], [13.23, 3.53,0], [13.44, 3.6,0], [13.69, 2.79,0]]
x3 = invertiYZ(x3)
x3Bez = bezierMappata_1D(x3)

x4 = [[13.85, 1.61,0], [14.04, 1.97,0], [14.21, 2.79,0], [13.69, 2.79,0]]
x4 = invertiYZ(x4)
x4Bez = bezierMappata_1D(x4)

x5 = [[13.85, 1.61,0], [13.09, 1.64,0], [12.4, 1.59,0], [11.11, 1.62,0]]
x5 = invertiYZ(x5)
x5Bez = bezierMappata_1D(x5)

yz = STRUCT([x1Bez,x2Bez,x3Bez,x4Bez,x5Bez])
yz = T([2,3])([-2.58,-12.48])(yz)

s = STRUCT([xy,xz,yz])

VIEW(s)










