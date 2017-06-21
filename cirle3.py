import pygame
import math

pygame.init()


black = (0,0,0)
white = (254/2,254/2,254/2)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)

x_border = 1200
y_border = 1000

game = pygame.display.set_mode((x_border,y_border))
pygame.display.set_caption("Circle")

clock = pygame.time.Clock()

gameExit = False

fps = 60

radius = 150
x_circle = x_border/2
y_circle = 3*y_border/4

x_rod = x_circle 
y_rod = y_circle + radius

font = pygame.font.SysFont(None, 25)
def msg(msgs,color,x,y):
	screen_text=font.render(msgs,True,color)
	game.blit(screen_text,[x,y])

piston_width = 20*4
piston_height = 25*2
clearance = 20

connecting_rod = 2*radius + radius/2

speed = 1
theta = 0

stroke = 1
stroke_name = ["","Intake","Compression","Power","Exhaust"]

x_corner = x_circle - piston_width/2 - clearance/2
y_corner = y_circle - 3*radius - radius/2

while not gameExit:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				speed += 1
			elif event.key == pygame.K_DOWN:
				speed -= 1
				if speed < 10:
					speed = 10
	if theta > 630 or theta < 90:
		stroke = 1
	elif theta > 90 and theta < 270:
		stroke = 2
	elif theta > 270 and theta < 450:
		stroke = 3
	elif theta > 450 and theta < 630:
		stroke = 4

	x_rod = radius*math.cos(math.radians(theta)) + x_circle
	y_rod = radius*math.sin(math.radians(theta)) + y_circle

	game.fill(white)

	msg(`theta`,blue,700,400)
	msg(stroke_name[stroke],blue,700,420)

	pygame.draw.circle(game,red,(x_circle,y_circle),radius,0) 
	pygame.draw.line(game,black,(x_circle,y_circle),(x_rod,y_rod),2) 
	pygame.draw.rect(game,blue,[x_circle - piston_width/2 - clearance/2 , y_circle - 3*radius - radius/2,piston_width+clearance,2*radius+piston_height]) #cylinder

	connecting_rod_x = abs(x_circle - x_rod)
	connecting_rod_y = math.sqrt(connecting_rod**2 - connecting_rod_x**2)

	render_connecting_rod_y = y_rod - connecting_rod_y

	pygame.draw.rect(game,black,[x_circle - piston_width/2, render_connecting_rod_y , piston_width,piston_height]) #piston

	pygame.draw.line(game,black,(x_rod , y_rod),(x_circle,render_connecting_rod_y + piston_height),2) # connnecting rod

	pygame.draw.rect(game,yellow,[x_corner,y_corner , piston_width+clearance, render_connecting_rod_y - y_corner  ])#area sweeped

	pygame.draw.circle(game,(0,0,255),(int(x_rod),int(y_rod)),10,0)

	pygame.display.update()
	clock.tick(fps)


	# power stroke effect
	# if stroke == 3:
	# 	theta += speed*2
	# else:
	# 	theta += speed

	theta += speed
	if theta >= 720:
		theta = 0