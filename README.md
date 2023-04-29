# Realistic-Projectiles
exploring realistic projectile mechanics using RK4 method of system of equations using python

Air resistance models attempt to model more realistic projectile behavior when the force of contact with the air contributes appreciably to the motion. While there are many specific air resistance models, all of them are based on the general assumptions that:

•The force of air resistance is directed exactly opposite the velocity.
•The force of air resistance is an increasing function of speed.
The system of differential equations for these models are (in vector form):

<img width="198" alt="Screen Shot 2023-04-28 at 6 10 51 PM" src="https://user-images.githubusercontent.com/121915438/235275021-91e259dd-28a7-48de-88f3-a6e2214ed473.png">



This project I wanted to address the following with data, generated graphs, and explanations:

1) The interdependence of the horizontal and vertical motion (i.e. that the horizontal and vertical motion are not independent)

2) The general shape of the trajectories, and how they appear to change based on initial speed and firing angle

3) How you will extract firing range from your program

4) The firing range as a function of firing angle for various fixed initial speeds (above and below terminal speed)

5) The firing range as a function of initial speed for various fixed firing angles

6) Firing on a infinite slope in high and low drag situations

7) Affects associated with incorporating lift



Findings:
1) Projectile motion is an object upon which the only force acting on the
system would be gravity (if ignoring wind resistance).
•The two components of projectile motion are horizontal and vertical
motion.
•Since perpindicular components of motion are not independent of eachother
they will not be dependent on
on eachother's motion. But, it will be dependent on the amount of air-time
to horizontal distance.

2) The general shape is shown to be a parabola, but upon observation of
many graphs, all have different distances with respect to the firing angle and initial velocities of each
projectile not forgetting the :air resistance: quadratic drag. By taking keen notice on fixed values of
initial velocity and variable firing angles it was discovered to me that this effect oddly resembles the
"envelope parabola". 
To elaborate: it appears from my data that above and below 45 degrees, we
begin to decrease our maximum attainable horizontal distance. As we go higher than 45 the shapes of the
parabola become more thin, which entails a higher verticle positon. As we go lower than 45 degrees the
parabola becomes more wide, which entails a lower verticle position. In both of these cases the horizontal
distance drops.

3) The way I extracted firing range from my program. Is after setting up
the definitions.
I setup an array for data to be collected from initial velocity and
initial positions. For every iteration
it will save a value for as long as y < 0 (to signify it hitting the
ground) in the array.
Upon setting up those values and setting up our constants. I then call for
the RK4 method to call
the functions I set earlier. Every valid data point is then appended to
the array of each category
and my program will spit out the last saved data point before hitting the
ground.

4)(sheet1)
![annotated-Project%202%20Exceldoc xlsx](https://user-images.githubusercontent.com/121915438/235274681-bdefb0f4-51f4-4e68-996a-4a6bba2dac65.jpg)


5)(sheet2)
![annotated-Project%202%20Exceldoc xlsx2](https://user-images.githubusercontent.com/121915438/235274685-288357c4-73d3-4a51-a919-8914a5ca110b.jpg)


**Infinite Slope**
6) I would extract the firing range by essentially modifying my code from
a different position (higher than zero) Then it would follow suit in the steps of [ 3) ] as we set new initial
conditions. (Sheet 2) on excel doc. To further elaborate. Since we're on an infinite slope, that gives us theparameter that there is a zero
change in the x direction. Which argues to us that the only thing that we
can modify in our code would be the initial height only. Therefore in the extension portion of the project I modified the program from Zero as the initial height then "60" as the new initial height. Relevant Imageary Attached as excel sheets + graphs.

**Incorporating Lift**
7)
-To incorporate lift into the projectile motion simulation, the lift coefficient (L)[LiftCoefficient] needs to be introduced as a parameter. The lift force acts perpendicular to the direction of the velocity and is proportional to the velocity and the lift coefficient.

-To determine optimal values for lift constants, we can run the simulation for different initial speeds and firing angles and observe the resulting trajectory of the projectile. By comparing the trajectories with and without lift, we can identify the lift coefficients that produce the desired trajectory. **[ X-axis (x-position), Y-axis(y-position) ]**

<img width="555" alt="Screen Shot 2023-04-28 at 8 11 39 PM" src="https://user-images.githubusercontent.com/121915438/235280908-3018d8db-d1c5-415b-9f91-48bac7faaea3.png">

-The lift force occurs due to the shape of the projectile. When the projectile moves through the air, the air flows around it. The shape of the projectile can cause the air to flow more quickly over the top surface than the bottom surface, creating a difference in air pressure that produces lift. This effect is known as Bernoulli's principle.

-The lift force can be used to manipulate the trajectory of the projectile, allowing it to travel farther or higher than it would with only gravity and air resistance acting upon it. However, the lift force can also cause the projectile to become unstable or to deviate from its intended path if not properly accounted for. 

<img width="635" alt="Screen Shot 2023-04-28 at 8 11 50 PM" src="https://user-images.githubusercontent.com/121915438/235280962-6747c6c9-b643-4430-9f3c-23f663477098.png">
<img width="720" alt="Screen Shot 2023-04-28 at 8 11 11 PM" src="https://user-images.githubusercontent.com/121915438/235281052-4082b538-e6d6-4fea-b4f2-9c50164bb9d8.png">


