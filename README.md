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

## Credits

Blender, Onshape and finally Thank you so much to all my Friends & Mentors

## Pictures
<img width="588" height="260" alt="Assembly 1" src="https://github.com/user-attachments/assets/066d7b47-3a4c-4c2e-b121-c9ca13ac0af2" />
<img width="449" height="385" alt="Assembly 2" src="https://github.com/user-attachments/assets/ae0964c0-1f5a-4b8f-871e-b33b8ddd5888" />
<img width="960" height="600" alt="Wiring Picture" src="https://github.com/user-attachments/assets/d34898ba-22b8-4ba3-adb9-ff9f30fe9a67" />
