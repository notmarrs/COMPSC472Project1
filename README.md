# README for Process Manager Peoject COMPSC 472

This code is a Python application for managing processes through a graphical user interface (GUI) created using the Tkinter library. It provides functionalities to create, list, and terminate processes. Additionally, it simulates a producer-consumer scenario for each created process.

## Features

1. **Process Creation**: The application allows you to create a new process by specifying a command. The new process is created using the `subprocess.Popen` method.

2. **Process Listing**: You can list all running processes along with their details, such as Process ID (PID), associated command, the IDs of threads running within the process, and the queue size used for simulation.

3. **Process Termination**: The application provides the ability to terminate a running process by specifying its PID. This terminates the process and its associated threads.

## Logging

The application utilizes logging to record information about process creation and termination. Log entries are written to a file named "process_manager.log."

## Usage

1. **Creating a Process**: Enter a valid command in the "Enter a command" field and click the "Create Process" button. This will initiate the process and simulate a producer-consumer scenario for it.

2. **Listing Processes**: Click the "List Processes" button to see a list of all running processes, including their PIDs, associated commands, thread IDs, and queue sizes.

3. **Terminating a Process**: Enter the PID of the process you want to terminate in the "Enter PID to terminate" field and click the "Terminate Process" button. This will terminate the process and remove it from the list of running processes.

## Error Handling

The application provides error handling for various scenarios, such as invalid PIDs, failed process creation, and PID not found during termination.

## Dependencies

- Python 3.9
- Tkinter (Python GUI library)
- Multiprocessing and Threading for parallel execution
- Subprocess for creating and managing processes

## Running the Application

To run the application, execute the script containing the provided code. A GUI window will appear, allowing you to interact with the process manager.

## Author

This code was created by Fern

