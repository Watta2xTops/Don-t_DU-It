import turtle
import time
import random

#================== Global Variables ========================
#Kph, Lives, Difficulty initial
Kph = 20
lives = 1
difficulty = 0
player_file = "C:/Users/Gavin/IT-L Summative/score.txt"
time_save = 0
#================== Turtle Objects ==========================
wn = turtle.Screen()
wn.title("Don't DU-It")
wn.bgcolor("#46753e")
wn.bgpic('gifs/background.gif')
wn.setup(width= 800, height=600)
wn.tracer(0)#Shuts all screen updates

wn.register_shape('C:/Users/Gavin/IT-L Summative/gifs/RedCar.gif')
wn.register_shape('C:/Users/Gavin/IT-L Summative/gifs/Bluecar.gif')
wn.register_shape('C:/Users/Gavin/IT-L Summative/gifs/Tree.gif')
wn.register_shape('C:/Users/Gavin/IT-L Summative/gifs/rock.gif')
wn.register_shape('C:/Users/Gavin/IT-L Summative/gifs/bottle.gif')

# Kph display
pen= turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.write('Kph: {} Lives:{}'.format(Kph, lives), align='center', font=('ByteBounce.ttf',16,'bold'))

# Timer
start_time = time.time()  # Record the starting time

def display_timer():
    elapsed_time = int(time.time() - start_time)
    # Format the elapsed time into minutes and seconds
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    timer_str = "Time: {:02d}:{:02d}".format(minutes, seconds)
    timer_pen.clear()  # Clear the previous timer display
    timer_pen.write(timer_str, align='center', font=('ByteBounce.ttf', 16, 'normal'))

# Create a turtle for the timer display
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.color('white')
timer_pen.penup()
timer_pen.goto(-300, 260)  # Position the timer display
display_timer()  # Display the initial timer

#add the player
player = turtle.Turtle()
player.speed(1)
player.shape('C:/Users/Gavin/IT-L Summative/gifs/RedCar.gif')
player.setheading(90)
player.color("white")
player.penup()# Makes sure no line is drawn
player.goto(0,-250)# sets player position
player.direction = 'stop'

# List of bottle
bottles = []# N. of objects
#add points as coins
for b in range(2):
    bottle = turtle.Turtle()
    bottle.speed(1)# This speed is a function; how fast it is drawn
    bottle.shape('C:/Users/Gavin/IT-L Summative/gifs/bottle.gif')
    bottle.color('yellow')
    bottle.penup()
    bottle.goto(100,250)
    bottle.speed= 5# This speed is a variable; for speed of object
    bottles.append(bottle)

#List for obstacles
obstacles = []
#add obstacles
for o in range(4):
    obstacle = turtle.Turtle()
    obstacle.speed(1)
    obstacle.shape('C:/Users/Gavin/IT-L Summative/gifs/Bluecar.gif')
    obstacle.setheading(90)
    obstacle.color('blue')
    obstacle.penup()
    obstacle.goto(-100,250)
    obstacle.obstacle_speed = random.randint(3 + difficulty ,5 + difficulty)
    obstacles.append(obstacle)

# List for objects
objects1=[]
objects2=[]
#adding background objects:
for t in range(4):
    #Trees
    object1 = turtle.Turtle()
    object1.speed(1)
    object1.shape('C:/Users/Gavin/IT-L Summative/gifs/Tree.gif')
    object1.setheading(90)
    object1.penup()
    object1.obj1_speed = 4 + difficulty
    x1 = random.choice([random.randint(-600, -250), random.randint(250, 600)])  # Random x-coordinate selection
    y1 = 250
    object1.goto(x1 , y1)
    objects1.append(object1)

    #rocks
    object2 = turtle.Turtle()
    object2.speed(1)
    object2.shape('C:/Users/Gavin/IT-L Summative/gifs/rock.gif')
    object2.setheading(90)
    object2.penup()
    object2.obj2_speed = 4 + difficulty
    x2 = random.choice([random.randint(-600, -250), random.randint(250, 600)])  # Random x-coordinate selection
    y2 = 250
    object2.goto(300, 250)
    objects2.append(object2)

#Score pen
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color('white')

# Message pen
penalty_pen = turtle.Turtle()
penalty_pen.hideturtle()
penalty_pen.color('red')
penalty_pen.penup()
penalty_pen.goto(0, -200)

#================================== Controls ============================================
# Function
def goLeft():
    player.direction ='left'

def goRight():
    player.direction='right'

def goStop():
    player.direction='stop'
#Keyboard Binding
wn.listen()
wn.onkeypress(goLeft, "Left")
wn.onkeypress(goLeft, 'a')
wn.onkeypress(goRight, "Right")
wn.onkeypress(goRight, 'd')
wn.onkeypress(goStop, 'Up')
wn.onkeypress(goStop, 'w')
#====================================File==========================================
# Scores
def get_scores():
    with open(player_file, "r") as file:
        for i, line in enumerate(file, start=1):
            kph, time_survived = line.strip().split(",")
            score_pen.write(f'{i}. {kph} {time_survived}', align='center', font=('Arial', 12, 'normal'))
            score_pen.goto(300, score_pen.ycor() - 20)

def display_scores():
    score_pen.clear()
    score_pen.penup()
    score_pen.goto(300, 260)
    score_pen.write('Score:', align='center', font=('Arial', 16, 'normal'))
    score_pen.goto(300, 230)
    get_scores()

def clear_file():
    with open(player_file, "w") as file:
        file.write("")

# Keyboard Binding for file
wn.onkeypress(clear_file, 'BackSpace')


def update_score(Kph, time_survived):
    with open(player_file, "a") as file:
        file.write(f"Speed: {Kph}, Time: {int(time_survived)}\n")
#=============================== Game ==============================================
#Main Game Loop
while True:
    time.sleep(0.01)
    wn.update()
    
    # Update the timer display
    display_timer()  
    display_scores()

    # move the player
    if player.direction == 'left':
        x = player.xcor()#Current coordinate of player
        x -= 3 + difficulty#Speed of player
        player.setx(x)
    
    if player.direction == 'right':
        x = player.xcor()#Current coordinate
        x += 3 + difficulty #Speed of player
        player.setx(x)
    
    #Setting Border Collisions
    if player.xcor() < -210:
        player.setx(-210)
    elif player.xcor() > 210:
        player.setx(210)

    # Move the bottles
    for bottle in bottles:    
        y = bottle.ycor()
        y -= bottle.speed
        bottle.sety(y)

        # If object out of screen
        if y < -300:
            x = random.randint(-200, 200)
            y = random.randint(300, 400)
            bottle.goto(x, y)

        # Check if collision with player
        if bottle.distance(player) < 20:
            x = random.randint(-200, 200)
            y = random.randint(300, 400)
            bottle.goto(x, y)
            Kph += 10
            pen.clear()
            pen.write('Kph:{}  Lives:{}'.format(Kph, lives), align='center', font=('ByteBounce.ttf',16,'bold'))
            difficulty += 1

    #Move Obstacles
    for obstacle in obstacles:    
        y = obstacle.ycor()
        y -= obstacle.obstacle_speed
        obstacle.sety(y)

        # If object out of screen
        if y < -300:
            x = random.randint(-200, 200)
            y = random.randint(300, 400)
            obstacle.goto(x, y)
            obstacle.obstacle_speed = random.randint(3 + difficulty, 5 + difficulty)  # Update obstacle speed

        # Check if collision with player
        if obstacle.distance(player) < 20:
            lives -= 1
            pen.clear()
            pen.write('Kph:{}  Lives:{}'.format(Kph, lives), align='center', font=('ByteBounce.ttf',16,'bold'))
            
            time.sleep(1)
            for obstacle in obstacles:
                obstacle.goto(random.randint(-200,200), random.randint(400, 800))# for some reason adding the y value fixes the lives counter
    
    # Moving objects 1 and 2
    for obj1 in objects1:    
        y = obj1.ycor()
        y -= obj1.obj1_speed
        obj1.sety(y)
        # If object out of screen
        if y < -300:
            x = random.choice([random.randint(-700, -300), random.randint(300, 700)])  # Random x-coordinate selection
            y = random.randint(300, 400)
            obj1.goto(x, y)
    for obj2 in objects2:    
        y = obj2.ycor()
        y -= obj2.obj2_speed
        obj2.sety(y)

        # If object out of screen
        if y < -300:
            x = random.choice([random.randint(-700, -300), random.randint(300, 700)])  # Random x-coordinate selection
            y = random.randint(300, 400)
            obj2.goto(x, y)
            
        #Game Over 
        if lives == 0:
            pen.clear
            pen.goto(0,0)
            pen.write("Game Over!", align='center', font=('ByteBounce.ttf',60,'bold'))
            pen.goto(0,260)
            # Displaying penalty messages
            penalty_pen.clear()
            penalty_pen.goto(0, -200)
            penalty_pen.write("Drunk Driving will be fined up to 500k and possible imprisonment", align='center', font=('ByteBounce.ttf', 15, 'bold'))
            penalty_pen.goto(0, -220)
            penalty_pen.write("Reckless Imprudence resulting to Homicide will result to imprisonment and suspension of license", align='center', font=('ByteBounce.ttf', 13, 'bold'))
            
            time_save = time.time() - start_time
            update_score(Kph, time_save)
            
            wn.update()
            time.sleep(10)
            Kph = 20
            lives = 1
            difficulty = 0
            start_time = time.time()
            pen.clear()
            penalty_pen.clear()
            pen.write('Kph: {} Lives {}'.format(Kph, lives), align='center', font=('ByteBounce.ttf',16,'bold'))

wn.exitonclick()
