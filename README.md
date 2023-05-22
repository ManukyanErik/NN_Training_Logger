# Neural Network Training Logger

This project aims to facilitate the logging process for training neural network models and enables the sending of log messages via email. It provides a convenient mechanism for capturing and managing log messages at various log levels throughout the training process, ensuring effective monitoring and communication. It includes two code files: `logger.py` and `main.py`.

## Features

- Logging of training progress and metrics
- Email notification of log messages
- Adjustable log levels for different types of messages

## Getting Started

To use the logger in your own project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repo - url>
2. Import the Logger class from logger.py into your project:

   ```python
   from logger import Logger
3. Create an instance of the Logger class, providing the email sender and password as arguments: You should , enable 2-step verification for the email sender's account and generate an app password for the email password
   ```python
   logger = Logger(email_sender='your_email@gmail.com', email_password='your_email_password')
4. Add email recipients and their corresponding log levels using the add_email_receiver method:
   ```python
   logger.add_email_receiver("receiver1@example.com", 'INFO')
   logger.add_email_receiver("receiver2@example.com", 'DEBUG', 'WARNING')
5. Use the log method to send log messages at different log levels during the training process:
   ```python
   logger.log("Training started", log_level='INFO')
   logger.log(f'Epoch: {epoch}, Loss: {current_loss}, Accuracy: {current_accuracy}', "DEBUG")
   logger.log("Warning: Learning rate is too high!", log_level='WARNING')
6. Customize and run your neural network training code, using the logger to log important updates and metrics.

## Dependencies

*  Python 3.x
*  NumPy
*  TensorFlow
*  Keras

## File Descriptions

* logger.py: Contains the implementation of the Logger class, which handles logging and email notifications.
* main.py: An example usage of the Logger class, demonstrating how to train a neural network model and log the training progress.