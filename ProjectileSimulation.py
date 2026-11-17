from vpython import *

scene = canvas(width=1920, height=1080, title="Projectile Simulation\n") #To enlargen simulation's display
ground = box(pos = vector(0, 0, 0), size = vector(10, 0.1, 1), color = color.red)
ball1 = sphere(pos = vector(0, 0, 0), radius = 0.2, color = color.white)
ball2 = sphere(pos = vector(0, 0, 0), radius = 0.2, color = color.blue)
ball3 = sphere(pos = vector(0, 0, 0), radius = 0.2, color = color.cyan)

g1 = vector(0, -9.81, 0)
g2 = vector(0, -1.62, 0)
g3 = vector(0, -3.71, 0)

v0 = 15 #Group 2 velocity
angle = 15 #Angle variable to easily manipulate angle for the 5 trials (15, 30, 45, 60, 75)
theta = angle * pi / 180

#cos(theta)
#sin(theta)

ball1.m = 1
ball1.v = vector(v0 * (cos(theta)), v0 * (sin(theta)), 0)

ball2.m = 1
ball2.v = vector(v0 * (cos(theta)), v0 * (sin(theta)), 0)

ball3.m = 1
ball3.v = vector(v0 * (cos(theta)), v0 * (sin(theta)), 0)

t1 = 0
t2 = 0
t3 = 0
dt = 0.01

attach_trail(ball1)
attach_trail(ball2)
attach_trail(ball3)

while ball1.pos.y >= 0:
    rate(50)
    F = ball1.m * g1
    ball1.v = ball1.v + (F / ball1.m) * dt
    ball1.pos = ball1.pos + ball1.v * dt / ball1.m
    t1 = t1+dt

while ball2.pos.y >= 0:
    rate(50)
    F = ball2.m * g2
    ball2.v = ball2.v + (F / ball2.m) * dt
    ball2.pos = ball2.pos + ball2.v * dt / ball2.m
    t2 = t2+dt

while ball3.pos.y >= 0:
    rate(50)
    F = ball3.m * g3
    ball3.v = ball3.v + (F / ball3.m) * dt
    ball3.pos = ball3.pos + ball3.v * dt / ball3.m
    t3 = t3+dt


print('Time of flight of ball1 = ', t1, ' s')
print('Final position ball1 = ', ball1.pos, ' m')

print('Time of flight of ball2 = ', t2, ' s')
print('Final position ball2 = ', ball2.pos, ' m')

print('Time of flight of ball3 = ', t3, ' s')
print('Final position ball3 = ', ball3.pos, ' m')

while True: #To keep the browser tab open.
    rate(10)