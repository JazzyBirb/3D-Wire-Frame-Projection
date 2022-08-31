from cmath import cos, sin
import numpy as n
import turtle
import time
import trimesh

Model = trimesh.load("C:\\Users\\34758\\Downloads\\34553_20mm_Cube\\files\\20mm_cube.stl")

screen = turtle.Screen()
pen = turtle.Turtle()
pen.ht()
screen.tracer(False)

deg = 0
def rot_mtx(deg,vector,mtx):
    if vector == 'x':
        return n.dot(n.matrix([[1,0,0],[0,cos(deg),-sin(deg)],[0,sin(deg),cos(deg)]]),mtx)
    if vector == 'y':
        return n.dot(n.matrix([[cos(deg),0,sin(deg)],[0,1,0],[-sin(deg),0,cos(deg)]]),mtx)
    if vector == 'z':
        return n.dot(n.matrix([[cos(deg),-sin(deg),0],[sin(deg),cos(deg),0],[0,0,1]]),mtx)

def proj_mtx(mtx):
     return n.dot(n.matrix([[1,0,0],[0,1,0]]),mtx)

def trans_mtx(x,y,z,mtx):
    mtx = n.vstack([mtx,n.matrix([[1]])])
    mtx = n.dot(n.matrix([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]),mtx)
    return n.delete(mtx,1,0)

def scal_mtx(x,y,z,mtx):
    mtx = n.vstack([mtx,n.matrix([[1]])])
    mtx = n.dot(n.matrix([[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]]),mtx)
    return n.delete(mtx,1,0)

vertices = []
edges = Model.vertices[Model.edges_unique]

for i in Model.vertices:
    vertices.append(n.matrix(i))

while True:
    deg+=0.1
    for i in edges:
        p13Dcoords = rot_mtx(0,'x',n.matrix(i[0]).reshape(3,1))
        p13Dcoords = rot_mtx(deg,'y',p13Dcoords.reshape(3,1))
        p13Dcoords = rot_mtx(deg,'z',p13Dcoords.reshape(3,1))
        p23Dcoords = rot_mtx(0,'x',n.matrix(i[1]).reshape(3,1))
        p23Dcoords = rot_mtx(deg,'y',p23Dcoords.reshape(3,1))
        p23Dcoords = rot_mtx(deg,'z',p23Dcoords.reshape(3,1))
        p13Dcoords = scal_mtx(1,1,1,p13Dcoords)
        p23Dcoords = scal_mtx(1,1,1,p23Dcoords)
        x1 = int(proj_mtx(p13Dcoords.real.reshape((3,1)))[0][0])*10
        y1 = int(proj_mtx(p13Dcoords.real.reshape((3,1)))[1][0])*10
        x2 = int(proj_mtx(p23Dcoords.real.reshape((3,1)))[0][0])*10
        y2 = int(proj_mtx(p23Dcoords.real.reshape((3,1)))[1][0])*10
        pen.goto(x1,y1)
        pen.pendown()
        pen.dot(10)
        pen.goto(x2,y2)
        pen.dot(10)
        pen.penup()
    screen.update()
    time.sleep(0.05)
    pen.clear()



#external libraries: Trimesh, Numpy
#btw please do not render stl files with a a high number of vertices and edges. 
#This renderer is a piece of garbage and unoptimized. 
#Usually OpenGL and Vulkan are used to render 3D projections. 
#I just made this to get  a better understanding of 3D projections.
