#!/usr/bin/python
# -*- coding: utf-8 -*-

'''This example shows usage of clumpTemplate() and replaceByClumps().'''

#define material for all bodies:
id_Mat=O.materials.append(FrictMat(young=1e7,poisson=0.3,density=1000,frictionAngle=1))
Mat=O.materials[id_Mat]

#define engines:
O.engines=[
	ForceResetter(),
	InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Box_Aabb()]),
	InteractionLoop(
		[Ig2_Sphere_Sphere_ScGeom(),Ig2_Box_Sphere_ScGeom()],
		[Ip2_FrictMat_FrictMat_FrictPhys()],
		[Law2_ScGeom_FrictPhys_CundallStrack()]
	),
	NewtonIntegrator(damping=0.7,gravity=[0,0,-10])
]


from yade import qt
qt.Controller()
qt.View()

#create a box:
id_box = O.bodies.append(utils.box((0,0,0),(2,2,.1),fixed=True,material=Mat))

#create assembly of spheres:
sp=pack.SpherePack()
sp.makeCloud(minCorner=(-1.5,-1.5,.1),maxCorner=(1.5,1.5,2),rMean=.2,rRelFuzz=.5,num=100,periodic=False)
O.bodies.append([utils.sphere(c,r,material=Mat) for c,r in sp])

print len(sp),' particles generated.'


#### show how to use makeClumpTemplate():


#dyad:
relRadList1 = [1,1]
relPosList1 = [[1,0,0],[-1,0,0]]

#peanut:
relRadList2 = [.5,1,.5]
relPosList2 = [[1,0,0],[0,0,0],[-1,0,0]]

#stick:
relRadList3 = [1,1,1,1,1]
relPosList3 = [[0,1,0],[0,2,0],[0,3,0],[0,4,0],[0,5,0]]

templates= []
templates.append(utils.clumpTemplate(relRadii=relRadList1,relPositions=relPosList1))
templates.append(utils.clumpTemplate(relRadii=relRadList2,relPositions=relPosList2))
templates.append(utils.clumpTemplate(relRadii=relRadList3,relPositions=relPosList3))


#### show how to use replaceByClumps():


#replace by 50% dyads, 30% peanuts and 10% sticks:
O.bodies.replaceByClumps(templates,[.5,.3,.1])

O.dt=1e-6

#NOTE, that after replacing some overlaps may occur.
#So after replacing calm() function may be helpful:
if 0:
	print '\nPlease wait a minute ...\n'
	O.engines=O.engines+[PyRunner(iterPeriod=10000,command='calm()',label='calmRunner')]
	O.run(1000000,True)
	calmRunner.dead=True

print '\nPress Play button ... '
                
