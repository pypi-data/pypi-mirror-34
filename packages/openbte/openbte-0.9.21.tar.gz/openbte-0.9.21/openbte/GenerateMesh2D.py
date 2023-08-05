from __future__ import print_function
import xml.etree.ElementTree as ET
import os,sys
import numpy as np
import random
import math
from matplotlib.pylab import *
import pyclipper
from pyclipper import *
import subprocess
from shapely.ops import cascaded_union
from shapely.geometry import Point
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon
import shapely

def get_loop(points,lines):


 return loop



def line_exists_ordered(l,lines):

 for n,line in enumerate(lines) :
  if (line[0] == l[0] and line[1] == l[1]) :
   return n
  if (line[0] == l[1] and line[1] == l[0]) :
   return -n

 return 0 
     

def line_exists(l,lines):

 for n,line in enumerate(lines) :
   if (line[1] == l[0] and line[2] == l[1]) or (line[1] == l[1] and line[2] == l[0]) :
     return line
 return 0

def point_exists(p,points):

 delta = 1e-2
 for n,point in enumerate(points) :
   if abs(point[0] - p[0]) < delta and abs(point[1] - p[1])< delta :
     return n

 return -1


def get_line_from_points(p1,p2,all_lines,points):

 #Get indexes
 for t,p in enumerate(points):
  if p == p1 :
   t1 = t 
  if p == p2 :
   t2 = t 


 for t,l in enumerate(all_lines):
  if (t1 == l[1] and t2 == l[2]) :  
   line = [l[0],t1,t2]
   break
  if (t2 == l[1] and t1 == l[2])  :
   line = [l[0],t2,t1]
   break


 return line


def rev_rotate(l,n):
    return l[-n:] + l[:-n]


def rotate(l,n):
    return l[n:] + l[:n]


def GetSampleList(output_dir) :
   tmp =  glob.glob(output_dir + '/*.json')
   index = 0
   if len(tmp) > 0:
    for n in range(len(tmp)) :
     tmp2 = tmp[n].split('/')
     tmp3 = tmp2[-1].split('.')
     tmp4 = tmp3[0].split('_') 
     index = max([int(tmp4[1]),index])
    index +=1


   return index

 

def plot_region(region):

   for n in range(len(region)) :
    n1 = n
    n2 = (n+1)%len(region)
    plot([region[n1][0],region[n2][0]],[region[n1][1],region[n2][1]],color='black')
   xlim([-3,3])
   ylim([-3,3])

def FindPeriodic(control,others,points,lines):

    
     
 delta = 1e-3   
 p1c = points[lines[control][0]]
 p2c = points[lines[control][1]]
 for n in range(len(others)):
   p1 = points[lines[others[n]][0]]
   p2 = points[lines[others[n]][1]]
   #Positive  
   pd1 = [p1c[0]-p1[0],p1c[1]-p1[1]]  
   pd2 = [p2c[0]-p2[0],p2c[1]-p2[1]]  
   if abs(pd1[0] - pd2[0]) < delta and abs(pd1[1] - pd2[1]) <delta :
     return others[n]
   
   #Negative  
   pd1 = [p1c[0]-p2[0],p1c[1]-p2[1]]   
   pd2 = [p2c[0]-p1[0],p2c[1]-p1[1]]   
   if abs(pd1[0] - pd2[0])<delta and abs(pd1[1] - pd2[1])<delta :
     return -others[n]


 #If no periodic line has been found
 print("NO PERIODIC LINES HAS BEEN FOUND")
 quit()
 
def LineOrdering(lines) :

  new_lines = []
  new_lines.append(lines[0])
  check = np.ones(len(lines))
  check[0] = 0
  n_check = 0 
  while len(lines) > len(new_lines) :
   n_check +=1 
   line = new_lines[len( new_lines)-1]
   for k in range(len(lines)):
    if check[k] == 1:
     if lines[k][1] == line[2]  :
      check[k] = 0
      new_lines.append([lines[k][0],lines[k][1],lines[k][2]])
      break;
     if lines[k][2] == line[2]  :
      check[k] = 0
      new_lines.append([-lines[k][0],lines[k][2],lines[k][1]])
      break;
   if n_check > len(lines) :
    print('CANNOT FIND A ORDERED LOOP')
    print(lines)
    quit()
  return new_lines



def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area




def already_included(all_points,new_point): 

 for n,p in enumerate(all_points):
  d = np.linalg.norm(np.array(p)-np.array(new_point))
  if d < 1e-2:
   return n

 return -1


def regularize_polygons(polygons):


 #cut redundant points
 new_poly = []
 for poly in polygons:
  N = len(poly)
  tmp = []
  for n in range(N):
   p1 = poly[n]
   p2 = poly[(n+1)%(N-1)]
   if np.linalg.norm(np.array(p1)-np.array(p2)) >1e-4:
    tmp.append(p1)  
  new_poly.append(tmp)


 #eliminate useless points
 #cut redundant points
 #new_poly2 = []
 #for poly in new_poly:
 # poly.append(poly[-1])
 # N = len(poly)
 # tmp = []
 # for n in range(N):
 #  p1 = np.array(poly[(n-1)%N])
 #  p2 = np.array(poly[n])
 #  p3 = np.array(poly[(n+1)%N])
   
 #  l1 = (p2-p1)/np.linalg.norm(p2-p1)
 #  l2 = (p3-p2)/np.linalg.norm(p3-p2)
 #  print(np.linalg.norm(cross(l1,l2)))
#    tmp.append(p1)  
#   else:
#    print('ggg')
 # new_poly2.append(tmp)


 return new_poly

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def prune(solution):


 #Eliminate unnecessary points---
 tmp = []
 for region in solution:
  points = []   
  for p,point in enumerate(region):
   if p > 0:   
    if already_included([points[-1]],point) == -1:
     points.append(point)
   else:  
    points.append(point)
  tmp.append(points)


 polygons = []
 for n,region in enumerate(tmp):

  area = PolyArea(np.array(region)[:,0],np.array(region)[:,1]) 
  if area > 1e-2:
   points = []  

   for p,new_point in enumerate(region):
    tmp = already_included(points,new_point)
    if not tmp == -1 and not tmp == len(points)-1:
     polygons.append(points[tmp:len(points)])
     del points[tmp+1:len(points)]
    if not (not tmp == -1 and tmp == len(points)-1):
     points.append(new_point)
   polygons.append(points)


 #for poly in polygons:
 # poly.append(poly[0])
 # x = np.array(poly)[:,0]
 # y = np.array(poly)[:,1]
 # plot(x,y)
 # show()

 return polygons
 

def plot_region(dd,color='r'):

 dd.append(dd[0])    
 dd = np.array(dd)
 x = dd[:,0]
 y = dd[:,1]
 plot(x,y,color=color)
 axis('equal')
 axis('off')
 xlim([-30,30])
 ylim([-30,30])


def create_line_list(pp,points,lines,store,mesh_ext):

   p_list = []
   for p in pp: 
    tmp = already_included(points,p)
    if tmp == -1:
     points.append(p)   
     store.write( 'Point('+str(len(points)-1) +') = {' + str(p[0]) +','+ str(p[1])+',0,'+ str(mesh_ext) +'};\n')
     p_list.append(len(points)-1)
    else: 
     p_list.append(tmp)


   line_list = []
   for l in range(len(p_list)):
    p1 = p_list[l] 
    p2 = p_list[(l+1)%len(p_list)]
    tmp = line_exists_ordered([p1,p2],lines)

    if tmp == 0 : #craete line
     lines.append([p1,p2])   
     store.write( 'Line('+str(len(lines)-1) +') = {' + str(p1) +','+ str(p2)+'};\n')
     line_list.append(len(lines)-1)
    else: 
     line_list.append(tmp)

    #print(' ')
    #print(p1)
    #print(p2)
    #print(tmp)
    #print(line_list)
    #print(lines[abs(line_list[-1])])

   #quit()
   return line_list


def create_loop(loops,line_list,store):

   #create external loop 
   strc = 'Line Loop(' + str(loops)+ ') = {'
   for n in range(len(line_list)):
    strc +=str(line_list[n])
    if n == len(line_list)-1:
     strc += '};\n'
    else:
     strc += ','
   store.write(strc)   

   return strc



def create_surface(ss,bulk_surface,store):


  strc = r'''Plane Surface(''' + str(bulk_surface) + ')= {'  
  for n,s in enumerate(ss):
   strc += str(s)
   if n == len(ss)-1:
     strc += '};\n'
   else:
     strc += ','
  store.write(strc)


def mesh(polygons,frame,argv):
 

  polygons = regularize_polygons(polygons)

  mesh_ext = argv['step']
  include_pores = argv.setdefault('include_pores',False)
  Frame = Polygon(frame)

  #CREATE BULK SURFACE------------------------------------
  store = open('mesh.geo', 'w+')
  points = []
  lines = []
  loops = 0
  ss = 0
  polypores = []
  for poly in polygons:
   thin = Polygon(poly).intersection(Frame)
   polypores.append(thin)
   #Points-------
   pp = list(thin.exterior.coords)[:-1]

   #for p in pp: 
   # points.append(p)   
   # store.write( 'Point('+str(len(points)-1) +') = {' + str(p[0]) +','+ str(p[1])+',0,'+ str(mesh_ext) +'};\n')

   #Lines--------
   #for n in range(len(pp)):
   # p1 = len(points) + n - len(pp)
   # p2 = len(points) + (n+1)%len(pp) - len(pp)
   # lines.append([p1,p2])   
   # store.write( 'Line('+str(len(lines)-1) +') = {' + str(p1) +','+ str(p2)+'};\n')
    
   #Line loops
   #loops += 1
   #strc = 'Line Loop(' + str(loops-1)+ ') = {'
   #for n in range(len(pp)):
   # strc +=str(len(lines)-len(pp)+n) 
   # if n == len(pp)-1:
   #  strc += '};\n'
   # else:
   #  strc += ','
   #store.write(strc)   

   #Pores surfaces--
   #ss +=1
   #strc = 'Plane Surface(' + str(ss-1)+ ') = {' + str(loops-1) + '};\n'
   #store.write(strc)   

   #plot_region(points)

  #show()
  #strc = r'''Physical Surface('Pores') = {'''  
  #for n in range(ss):
  # strc += str(n)
  # if n == ss-1:
  #   strc += '};\n'
  # else:
  #   strc += ','
  #store.write(strc)


  #Get boundary wall
  lx = frame[0][1]*2.0
  ly = frame[1][1]*2.0
  pore_wall = []
  delta = 1e-2
  #strc = r'''Physical Line('Boundary') = {'''  
  for l,line in enumerate(lines):
   p1 = points[line[0]]  
   p2 = points[line[1]]
   on_wall = True
   if abs(p1[0] + lx/2.0) < delta and abs(p2[0] + lx/2.0) < delta: on_wall=False
   if abs(p1[0] - lx/2.0) < delta and abs(p2[0] - lx/2.0) < delta: on_wall=False
   if abs(p1[1] - ly/2.0) < delta and abs(p2[1] - ly/2.0) < delta: on_wall=False
   if abs(p1[1] + ly/2.0) < delta and abs(p2[1] + ly/2.0) < delta: on_wall=False
   if on_wall:   
   # if len(pore_walls) > 0:   
   #  strc += ',' 
   # strc += str(l) 
    pore_wall.append(l)
  #strc += '};\n'
  #store.write(strc) 
  #-------------------------

  MP = MultiPolygon(polypores)

  #Create bulk surfacep
  bulk = Frame.difference(cascaded_union(MP))

  if not (isinstance(bulk, shapely.geometry.multipolygon.MultiPolygon)):
   bulk = [bulk]
  
  bulk_surface = []
  for region in bulk:

   pp = list(region.exterior.coords)[:-1]

   line_list = create_line_list(pp,points,lines,store,mesh_ext)


   loops +=1
   local_loops = [loops]
   create_loop(loops,line_list,store)


   internal_loops = []
   for interior in region.interiors:

    pp = list(interior.coords)[:-1]
    line_list = create_line_list(pp,points,lines,store,mesh_ext)
    loops +=1
    local_loops.append(loops)
    create_loop(loops,line_list,store)
   
   ss +=1
   bulk_surface.append(ss)
   create_surface(local_loops,ss,store)
  
  strc = r'''Physical Surface('Bulk') = {'''  
  for n,s in enumerate(bulk_surface):
   strc += str(s)
   if n == len(bulk_surface)-1:
     strc += '};\n'
   else:
     strc += ','
     
  store.write(strc)


  Minx= frame[0][0]
  Maxx= frame[2][0]
  Miny= frame[3][0]
  Maxy= frame[1][1]


  hot = []
  cold = []
  upper = [] 
  lower = [] 

  deltax = (Maxx-Minx)/1e5
  deltay = (Maxy-Miny)/1e5

  pore_wall = []
  for l,line in enumerate(lines):
   p1 = points[line[0]]
   p2 = points[line[1]]
   is_on_boundary = False
   if abs(p1[0] - Minx)<deltax and  abs(p2[0] - Minx)<deltax :
    hot.append(l)
    is_on_boundary = True
   if abs(p1[0] - Maxx)<deltax and  abs(p2[0] - Maxx)<deltax :
    cold.append(l)
    is_on_boundary = True
   if abs(p1[1] - Miny)<deltay and  abs(p2[1] - Miny)<deltay :
    lower.append(l)
    is_on_boundary = True
   if abs(p1[1] - Maxy)<deltay and  abs(p2[1] - Maxy)<deltay :
    upper.append(l)
    is_on_boundary = True
   if not is_on_boundary: 
    pore_wall.append(l)


  additional_boundary = []
  if argv.setdefault('Periodic',[True,True,True])[0]:
   strc = r'''Physical Line('Periodic_1') = {'''
   for n in range(len(hot)-1):
    strc += str(hot[n]) + ','
   strc += str(hot[-1]) + '};\n'
   store.write(strc)
  
   strc = r'''Physical Line('Periodic_2') = {'''
   for n in range(len(cold)-1):
    strc += str(cold[n]) + ','
   strc += str(cold[-1]) + '};\n'
   store.write(strc)
  else:
   for k in hot:
    additional_boundary.append(k)
   for k in cold:
    additional_boundary.append(k)

  if argv.setdefault('Periodic',[True,True,True])[1]:
   strc = r'''Physical Line('Periodic_3') = {'''
   for n in range(len(upper)-1):
    strc += str(upper[n]) + ','
   strc += str(upper[-1]) + '};\n'
   store.write(strc)

   strc = r'''Physical Line('Periodic_4') = {'''
   for n in range(len(lower)-1):
    strc += str(lower[n]) + ','
   strc += str(lower[-1]) + '};\n'
   store.write(strc)
  else:
   for k in lower:
    additional_boundary.append(k)
   for k in upper:
    additional_boundary.append(k)

  
  #Collect Wall
  boundary_surfaces = pore_wall + additional_boundary
  strc = r'''Physical Line('Boundary') = {''' 
  for r,region in enumerate(boundary_surfaces) :
   strc += str(region) 
   if r == len(boundary_surfaces)-1:
    strc += '};\n'
    store.write(strc)
   else :
    strc += ','


  for n in range(len(hot)):
   periodic = FindPeriodic(hot[n],cold,points,lines)
   strc = 'Periodic Line{' + str(hot[n]) + '}={' + str(periodic) + '};\n'
   store.write(strc)
  
  for n in range(len(lower)):
   periodic = FindPeriodic(lower[n],upper,points,lines)
   strc = 'Periodic Line{' + str(lower[n]) + '}={' + str(periodic) + '};\n'
   store.write(strc)
  
#-------------------------------------------------------
  store.close()
 

