import cv2
import numpy as np
import matplotlib.pyplot as plt

def light_intensity_logger():
    # Open a connection to the webcam (0 represents the default camera)
    cap = cv2.VideoCapture(0)

    # Create a figure for plotting
    plt.ion()
    fig, ax = plt.subplots()
    intensity_values = []

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale for simplicity
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the average light intensity
        average_intensity = np.mean(gray_frame)

        # Append the intensity value to the list
        intensity_values.append(average_intensity)

        # Plot the intensity values
        ax.clear()
        ax.plot(intensity_values, label='Light Intensity')
        ax.axhline(y=150, color='r', linestyle='--', label='Threshold')

        ax.set_title('Light Intensity Logger')
        ax.set_xlabel('Frames')
        ax.set_ylabel('Intensity')
        ax.legend()

        # Display the plot
        plt.draw()
        plt.pause(0.01)

        # Display the frame with average intensity
        cv2.putText(frame, f'Avg Intensity: {average_intensity:.2f}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Light Intensity Logger', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Close the matplotlib plot
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    light_intensity_logger()
