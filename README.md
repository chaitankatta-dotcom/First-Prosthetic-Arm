# First-Prosthetic-Arm
This is a very simple prosthetic arms, that can currently do only simple movement by code.

Overview:
This project is a simple low-cost prosthtic hand designed to demonstrate fingermovement using a Raspberry Pi. The hand is mechanically simple, requiring only a small number of moving pars while still being capable of performing basic finger motions.

At its current stage, the fingers are conrolled directly through programmed commands. Future versions of he project will incorporate EMG sensors, allowing the hand o respong to muscle signals from the user.

The goal of this project was to create an accessible and easy to build prosthetic hand that can serve as a foundaion for more advanced prosthetic technologies.

Features:
  Individual finger movmen through software conrol
  Raspberry Pi-based control system
  Simple mechanical design with few moving pars
  Modular design for future upgrades
  Expandable to EMG based control

How it Works:
The prosthetic hand is controlledby by a Raspberry Pi running Python code.

When the program is executed, he Raspberry Pi sends commands to the motors that control the fingers. Different code sequences can be usedto create diffferent hand movements such as opening, closing, or gripping motions.

Currently, all movement is controlled through software(micropython code). The handdoes not yet interpret muscle signals or user intent automatically.

How to Use:
  Connect the electronic and motors according to the wiring schemetic picture.
  Upload the provided Python code to the Raspberry Pi for simple movement, or use your own.
  Power on the Raspberry Pi
  Run the control program
  The fingerswill move according to the programmed commands,
  Modify the code to create new movement patterns or gestures.

Why I Made This
I createdthis project because I wanted to combine my interes in biology and engineering. Prosthetics are a perfect example of how technology can be used to improve people's lives by restoring lost functionality.

I was particularly interested in building a project that involved both hardware and programming while also relating to the human body. Designing a prosthetic hand allowed me to explore concepts from biomechanics, robotics, and medicine in a hand on way.

My goal was to create a simple design that demonstrates the fundamentals of a prosthetic tech while leaving room of future improvments such as EMG-based control and ore natural movement.

