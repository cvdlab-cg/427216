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

def scalaRaggio(radius):
 	def prova(punto):
 		return [punto[0]*radius,punto[1]*radius,punto[2]]
 	return prova

def bezCircle(radius,z):
 	controlpoints = [[1,0,z],[1,1,z],[0,1.62,z],[-1.22,1.22,z],[-2,0,z],[-1.22,-1.22,z],[0,-1.63,z],[1,-1,z],[1,0,z]]
 	controlpoints = AA(scalaRaggio(radius))(controlpoints)
 	return BEZIER(S1)(controlpoints)

def scambia(elemento):
	return [S1(elemento),S3(elemento),S2(elemento)]

def invertiXZ(array):
	return AA(scambia)(array)

def scambiaYZ(elemento):
	return [S3(elemento),S2(elemento),S1(elemento)]

def invertiYZ(array):
	return AA(scambiaYZ)(array)

def wheel():
	c1 = bezCircle(1,0)
	c2 = bezCircle(1.2,0)
	c3 = bezCircle(1.5,0)


	# cCentro = bezCircle(1.8,0.5)


	c4 = bezCircle(1,1)
	c5 = bezCircle(1.2,1)
	c6 = bezCircle(1.5,1)

	cc1 = bezierMappata_2D([c1,c4])
	cc2 = bezierMappata_2D([c2,c5])
	cc3 = COLOR(BLACK)(bezierMappata_2D([c3,c6])) #cCentro,

	cc4 = COLOR(BLACK)(bezierMappata_2D([c2,c3]))
	cc5 = bezierMappata_2D([c1,c2])

	cc6 = bezierMappata_2D([c4,c5])
	cc7 = COLOR(BLACK)(bezierMappata_2D([c5,c6]))

	# PRIMO RAGGIO

	r1 = [[1,0.1,0], [-1,0.1,0]]
	r1 = BEZIER(S1)(r1)

	r1b = [[1,-0.1,0], [-1,-0.1,0]]
	r1b = BEZIER(S1)(r1b)

	r1r = [[1,0.1,1], [-1,0.1,1]]
	r1r = BEZIER(S1)(r1r)

	r1br = [[1,-0.1,1], [-1,-0.1,1]]
	r1br = BEZIER(S1)(r1br)

	r = bezierMappata_2D([r1b,r1])
	rr1 = bezierMappata_2D([r1br,r1r])

	m1 = bezierMappata_2D([r1,r1r])
	m2 = bezierMappata_2D([r1b,r1br])

	# SECONDO RAGGIO

	r2 = [[0.1,1,0], [0.1,-1,0]]
	r2 = BEZIER(S1)(r2)

	r2b = [[-0.1,1,0], [-0.1,-1,0]]
	r2b = BEZIER(S1)(r2b)

	r2r = [[0.1,1,1], [0.1,-1,1]]
	r2r = BEZIER(S1)(r2r)

	r2br = [[-0.1,1,1], [-0.1,-1,1]]
	r2br = BEZIER(S1)(r2br)

	rr2 = bezierMappata_2D([r2b,r2])
	rr2b = bezierMappata_2D([r2br,r2r])

	m3 = bezierMappata_2D([r2,r2r])
	m4 = bezierMappata_2D([r2b,r2br])

	# TERZO RAGGIO

	r3 = [[0.75,0.65,0], [-0.65,-0.75,0]]
	r3 = BEZIER(S1)(r3)

	r3b = [[0.65,0.75,0], [-0.75,-0.65,0]]
	r3b = BEZIER(S1)(r3b)

	r3r = [[0.75,0.65,1], [-0.65,-0.75,1]]
	r3r = BEZIER(S1)(r3r)

	r3br = [[0.65,0.75,1], [-0.75,-0.65,1]]
	r3br = BEZIER(S1)(r3br)

	rr3 = bezierMappata_2D([r3,r3b])
	rr3b = bezierMappata_2D([r3br,r3r])

	m5 = bezierMappata_2D([r3,r3r])
	m6 = bezierMappata_2D([r3b,r3br])

	# QUARTO RAGGIO

	r4 = [[-0.75,0.65,0], [0.65,-0.75,0]]
	r4 = BEZIER(S1)(r4)

	r4b = [[-0.65,0.75,0], [0.75,-0.65,0]]
	r4b = BEZIER(S1)(r4b)

	r4r = [[-0.75,0.65,1], [0.65,-0.75,1]]
	r4r = BEZIER(S1)(r4r)

	r4br = [[-0.65,0.75,1], [0.75,-0.65,1]]
	r4br = BEZIER(S1)(r4br)

	rr4 = bezierMappata_2D([r4,r4b])
	rr4b = bezierMappata_2D([r4br,r4r])

	m7 = bezierMappata_2D([r4,r4r])
	m8 = bezierMappata_2D([r4b,r4br])


	raggi = COLOR(BLACK)(STRUCT([r,rr1,m1,m2,rr2,rr2b,m3,m4,rr3,rr3b,m5,m6,rr4,rr4b,m7,m8]))
	return STRUCT([cc1,cc2,cc3,cc4,cc5,cc6,cc7,raggi])


def profile():
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

	return STRUCT([xy,xz,yz])

p = profile()
s1 = wheel()
s2 = wheel()
s3 = wheel()
s4 = wheel()

s1 = SCALE([1,2,3])([0.35,0.35,0.35])(s1)
s2 = SCALE([1,2,3])([0.35,0.35,0.35])(s2)
s3 = SCALE([1,2,3])([0.35,0.35,0.35])(s3)
s4 = SCALE([1,2,3])([0.35,0.35,0.35])(s4)

s1 = T([1,2,3])([2.38,-0.8,-1.6])(s1)
s2 = T([1,2,3])([2.38,-0.8,1.6])(s2)
s3 = T([1,2,3])([-1.60,-0.8,-1.6])(s3)
s4 = T([1,2,3])([-1.60,-0.8,1.6])(s4)

f = STRUCT([p,s1,s2,s3,s4])

VIEW(f)
