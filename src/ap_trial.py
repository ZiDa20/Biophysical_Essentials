import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set the window size and title
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Biphysical')

# Generate 500 evenly spaced time values
t = np.linspace(0, 5, 500)

# Generate the voltage values for the action potential
v = 60 * np.exp(-t / 0.5) * (np.sin(2 * np.pi * t / 0.5) + 1)

# Set the starting time and voltage
time = 0
voltage = v[0]

# Set the animation speed (in milliseconds per frame)
speed = 1

# Set the colors for the action potential and the background
color_ap = (255, 0, 0)  # Red
color_bg = (0, 0, 0)  # Black
# Set the number of repetitions
repetitions = 10

# Set the running flag to True
running = True

# Start the main loop
while running:
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(color_bg)

    # Calculate the current time and voltage
    time = (time + speed) % 500
    voltage = v[time]

    # Draw the action potential line
    pygame.draw.line(screen, color_ap, (0, height / 2), (width, height / 2), 3)
    for i in range(time):
        pygame.draw.line(screen, color_ap, (int(i / 500 * width), int((v[i] + 30) / 60 * height)),
                         (int((i + 1) / 500 * width), int((v[i + 1] + 30) / 60 * height)), 1)

    # Check if the maximum number of repetitions has been reached
    if time == 0:
        repetitions -= 1
        if repetitions == 0:
            running = False
           


    # Update the display
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
