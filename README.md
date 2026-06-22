# First-Prosthetic-Arm
This is a very simple prosthetic arms, that can currently do only simple movement by code.

## Overview:
This project is a simple low-cost prosthetic hand designed to demonstrate finger movement using a Raspberry Pi. The hand is mechanically simple, requiring only a small number of moving parts while still being capable of performing basic finger motions.

At its current stage, the fingers are controlled directly through programmed commands. Future versions of the project will incorporate EMG sensors, allowing the hand to respond to muscle signals from the user.

The goal of this project is to create an accessible and easy to build prosthetic hand that can serve as a foundaion for more advanced prosthetic technologies.

## Features:
  Individual finger movment through software conrol
  Raspberry Pi-based control system
  Simple mechanical design with few moving pars
  Modular design for future upgrades
  Expandable to EMG based control

## How it Works:
The prosthetic hand is controlled by by a Raspberry Pi running Python code.

When the program is executed, the Raspberry Pi sends commands to the motors that control the fingers. Different code sequences can be used to create different hand movements such as opening, closing, or gripping motions.

Currently, all movement is controlled through software(micropython code). The hand does not yet interpret muscle signals or user intent automatically.

## How to Use:
  Connect the electronic and motors according to the wiring schemetic picture.
  Upload the provided Python code to the Raspberry Pi for simple movement, or use your own.
  Power on the Raspberry Pi
  Run the control program
  The fingers will move according to the programmed commands,
  Modify the code to create new movement patterns or gestures.

## Why I Made This:
I created this project because I wanted to combine my interest in biology and engineering. Prosthetics are a perfect example of how technology can be used to improve people's lives by restoring lost functionality. As we all are aware that there are many companies who make Prosthetic hands currently. But all of them work based on the user inputs either given by EMG. My goal is to see if we can bring in value to the human kind by adding some Artificial intelligence to the Prosthetic hand which none of the current prosthetic hands in the market have. This is my ultimate goal out of this project.

I was particularly interested in building a project that involved both hardware and programming while also relating to the human body. Designing a prosthetic hand allowed me to explore concepts from biomechanics, robotics, and medicine in a hand on way.

My goal was to create a simple design that demonstrates the fundamentals of a prosthetic tech while leaving room of future improvments such as EMG-based control and more natural movement.

## Overview

This guide explains how to assemble the simple robotic prosthetic hand. The hand uses 3D-printed finger parts, servo motors, screws, rubber bands, jumper wires, and a Raspberry Pi Pico to move the fingers through programmed code.

## Parts Needed

* 3D-printed palm
* 3D-printed finger segments

  * Pinky base, middle, and tip pieces
  * Ring base, middle, and tip pieces
  * Middle finger base, middle, and tip pieces
  * Pointer/index finger base, middle, and tip pieces
  * Thumb base and tip pieces
* 4 SG90 micro servos
* 1 MG996R servo
* Raspberry Pi Pico
* Servo board or mounting plate
* Jumper wires
* Small rubber bands
* M3 screws, nuts, and washers
* Optional M4 screws for larger hinge holes
* Budget soldering kit
* Screwdriver
* Pliers
* Optional 3.2 mm drill bit if M3 holes are too tight

## Important Notes Before Assembly

Do not fully tighten the hinge screws at first. The finger joints need to rotate freely. If the screws are too tight, the fingers will become stiff and the servos may not move them properly.

Most screw holes are close to 3 mm in diameter, so M3 screws are the best choice for most joints and mounts. Some larger hinge holes may fit M4 screws, but M3 screws with washers may still work depending on how the parts fit.

Do not power all servos directly from the Raspberry Pi Pico. Servos should use an external 5V power source. The Raspberry Pi Pico and servo power supply must share a common ground.

## Step 1: Prepare the Printed Parts

Lay out all of the 3D-printed parts before assembly.

## Step 2: Assemble Each Finger

Start with one finger at a time.

For each regular finger, connect the pieces in this order:

1. Base finger segment
2. Middle finger segment
3. Tip finger segment

Line up the hinge holes between the parts. Insert an M3 screw through the hinge. Add a washer if needed, then secure it with a nut. Tighten the nut only enough to hold the pieces together while still allowing the joint to rotate.

Repeat this process for the pinky, ring, middle, and pointer/index fingers.

## Step 3: Assemble the Thumb

The thumb has fewer segments than the other fingers. Connect the thumb base piece to the thumb tip piece using the hinge holes.

Insert an M3 screw through the hinge and secure it with a nut. Keep the joint loose enough so the thumb can rotate smoothly.

## Step 4: Attach the Fingers to the Palm

Place each assembled finger into its correct position on the palm:

* Pinky on the outside edge
* Ring finger next to the pinky
* Middle finger in the center
* Pointer/index finger next to the thumb side
* Thumb on the side of the palm

Line up the base hinge holes of each finger with the matching holes on the palm. Insert screws through the hinge points and secure them with nuts.

## Step 5: Mount the Servos

Mount the SG90 servos into the servo slots or servo board area. These servos control the smaller finger movements.

Use small screws to secure the servos in place. If the servo mounting holes are around 3 mm, use M3 screws. If the holes are smaller, use the screws that came with the servos.

Mount the MG996R servo in the larger servo position. This servo is stronger and should be used for a larger movement, such as wrist, palm, or thumb motion depending on your design.

Make sure all servo horns can rotate without hitting the palm or finger parts.

## Step 6: Connect the Rubber Bands

Attach small rubber bands to the fingers so they help return the fingers to their open position.

## Step 7: Connect Servos to Fingers

Connect each servo horn to its matching finger using string, wire, or linkage depending on your design.

Before attaching the servo horn permanently, center the servo using code. This prevents the finger from starting in the wrong position.

## Step 8: Wire the Electronics

Each servo has three wires:

* Red wire: 5V power
* Brown or black wire: Ground
* Orange, yellow, or white wire: Signal

Suggested Raspberry Pi Pico signal pins:

* SG90 servo 1: GP11
* SG90 servo 2: GP12
* SG90 servo 3: GP13
* SG90 servo 4: GP14
* MG996R servo: GP15

Connect all servo ground wires to the external power supply ground. Also connect the Raspberry Pi Pico ground to the same ground. This is called a common ground.

Use an external 5V power source for the servos. Do not power all the servos from the Pico’s 3.3V pin.

## Step 9: Upload Test Code

Upload simple servo test code to the Raspberry Pi Pico.

Test one servo at a time first. Make sure each servo moves correctly before testing all fingers together.

## Credits

Blender, Onshape and finally Thank you so much to all my Friends & Mentors

## Pictures
<img width="1405" height="631" alt="Screenshot 2026-06-22 134310" src="https://github.com/user-attachments/assets/6ef3d566-6400-479e-895f-128de2bfcbde" />
<img width="1052" height="836" alt="Screenshot 2026-06-22 134258" src="https://github.com/user-attachments/assets/3a94bc90-f0e8-49b5-bd7c-9ef480b85ffc" />
<img width="960" height="600" alt="Wiring Picture" src="https://github.com/user-attachments/assets/d34898ba-22b8-4ba3-adb9-ff9f30fe9a67" />

## BOM

Item,Description,Quantity,Unit Cost (USD),Total Cost (USD),Link
SG90 Servo,SG90 9g micro servo motor,4,2.75,10.98,https://www.amazon.com/Micro-Miuzei-Servos-Arduino-Airplane/dp/B0FGQ432JP
MG996R Servo,MG996R metal gear high torque servo,1,4.99,4.99,https://www.waveshare.com/mg996r-servo.htm
Jumper Wires,Raspberry Pi/Arduino jumper wire pack,1,5.99,5.99,https://vilros.com/products/jumper-wires
Raspberry Pi Pico,Raspberry Pi Pico microcontroller board,1,3.99,3.99,https://www.microcenter.com/product/661033/raspberry-pi-pico-microcontroller-development-board
Budget Soldering Kit,Basic soldering iron kit for connecting wires/electronics,1,10.99,10.99,https://www.walmart.com/ip/Soldering-Iron-Kit-Electric-60W-110V-Adjustable-Temperature-Soldering-Gun-Welding-Tools-5pcs-Replacement-Tips-and-Solder-Wire-Tube-Basic/5744425180
Small Rubber Bands,Small rubber bands for finger return tension or elastic movement,1,4.99,4.99,https://www.amazon.com/s?k=small+rubber+bands
M3 Screw Assortment Kit,M3 screws/bolts with nuts and washers for most finger and palm holes,1,8.99,8.99,https://www.amazon.com/s?k=M3+screw+assortment+kit+nuts+washers
M4 Screws,Optional M4 screws for larger hinge holes around 4 mm diameter,1,6.99,6.99,https://www.amazon.com/s?k=M4+screws+nuts+washers
TOTAL,,,,57.91,[Untitled spreadsheet - prosthetic_hand_BOM (1).csv](https://github.com/user-attachments/files/29216812/Untitled.spreadsheet.-.prosthetic_hand_BOM.1.csv)

## Zine

<img width="1410" height="2000" alt="Low Cost Prosthetic Hand" src="https://github.com/user-attachments/assets/41b5b1fd-5be5-4baa-a698-b03f192f8a9a" />
