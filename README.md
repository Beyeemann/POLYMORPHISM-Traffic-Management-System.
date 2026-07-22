# Smart Traffic Management System

## Project Description

This project is a Python implementation of a Smart Traffic Management System designed to demonstrate the use of polymorphism in Object-Oriented Programming. Different traffic devices inherit from a common parent class and provide their own implementation of the activate() method.

The application shows how multiple objects can be treated uniformly while producing different behaviors.

## Purpose

The project was developed to:

- Understand the concept of inheritance.
- Demonstrate method overriding.
- Illustrate runtime polymorphism.
- Show how object-oriented design improves code flexibility and maintainability.

## System Design

TrafficDevice
│
├── TrafficLight
├── SpeedCamera
├── PedestrianSignal
└── EmergencySiren
## Components

### TrafficDevice
The base class that defines the general behavior shared by all traffic devices through the activate() method.

### TrafficLight
Simulates a traffic light changing to green to control vehicle movement.

### SpeedCamera
Simulates monitoring road traffic and detecting speeding vehicles.

### PedestrianSignal
Represents a pedestrian crossing signal that safely manages pedestrian movement.

### EmergencySiren
Simulates an emergency alert system that warns drivers to give way to emergency vehicles.

## Project Features

- Object-oriented design using inheritance.
- Method overriding for specialized device behavior.
- Polymorphism through a shared activate() method.
- Stores different traffic devices in one collection.
- Activates every device using a single loop.
- Easily extendable with additional traffic device classes.

## Technologies

- Python 3
- Object-Oriented Programming (OOP)

## Example Execution

Traffic Light: Green light is ON.
Speed Camera: Capturing speeding vehicles.
Pedestrian Signal: Walk sign is ON.
Emergency Siren: Emergency vehicle approaching!
## Learning Outcomes

Through this project, the following OOP concepts are demonstrated:

- Creating classes and objects
- Inheritance
- Method overriding
- Runtime polymorphism
- Code reusability

## Conclusion

This project provides a practical example of how polymorphism enables different objects to respond to the same method call in unique ways. The design also makes it simple to introduce new traffic devices without changing the existing activation process.

## Author

Acquah Patrick

## Repository

POLYMORPHISM-Traffic-Management-System
