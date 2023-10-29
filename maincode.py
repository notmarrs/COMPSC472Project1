import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
import multiprocessing
import logging

# Configure logging
logging.basicConfig(filename='process_manager.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

processes = []  # Store information about running processes
process_lock = threading.Lock()  # Mutex for process synchronization

def producer_consumer(pid, queue):
    # Simulate a producer-consumer scenario
    for i in range(5):
        data = f"Data {i} produced by {pid}"
        logging.info(f"Process {pid} produced {data}")
        queue.put(data)

def create_process(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process_pid = process.pid
        process_queue = multiprocessing.Queue()

        with process_lock:
            processes.append({
                "pid": process_pid,
                "command": command,
                "threads": [],
                "queue": process_queue
            })

        logging.info(f"Process created with PID {process_pid}")

        # Create a thread to simulate producer-consumer for the new process
        producer_thread = threading.Thread(target=producer_consumer, args=(process_pid, process_queue))
        producer_thread.start()

    except Exception as e:
        error_msg = f"Error creating process: {str(e)}"
        logging.error(error_msg)
        messagebox.showerror("Error", error_msg)

    except Exception as e:
        error_msg = f"Error creating process: {str(e)}"
        logging.error(error_msg)
        messagebox.showerror("Error", error_msg)

def terminate_process(pid):
    try:
        with process_lock:
            for process in processes:
                if process["pid"] == pid:
                    for thread in process["threads"]:
                        thread.join()
                    process["queue"].close()
                    process["queue"].join_thread()
                    process["queue"].cancel_join_thread()
                    process["queue"].close()
                    process["queue"].join_thread()
                    process["queue"].cancel_join_thread()
                    processes.remove(process)  # Remove the process from the list
                    terminated_msg = f"Terminated process with PID {pid}"
                    logging.info(terminated_msg)
                    messagebox.showinfo("Process Terminated", terminated_msg)
                    return
            error_msg = f"Process with PID {pid} not found"
            logging.error(error_msg)
            messagebox.showerror("Error", error_msg)
    except Exception as e:
        error_msg = f"Error terminating process: {str(e)}"
        logging.error(error_msg)
        messagebox.showerror("Error", error_msg)

def create_thread_gui():
    command = command_entry.get()
    if command:
        try:
            create_process(command)
            messagebox.showinfo("Process Created", f"Created process with command: {command}")
        except Exception as e:
            error_msg = f"Error creating process: {str(e)}"
            logging.error(error_msg)
            messagebox.showerror("Error", error_msg)
    else:
        messagebox.showerror("Error", "Please enter a valid command.")

def list_processes():
    process_info = ""
    with process_lock:
        for process in processes:
            process_info += f"PID: {process['pid']}, Command: {process['command']}\n"
            process_info += f"Threads: {', '.join([str(thread.ident) for thread in process['threads']])}\n"
            process_info += f"Queue Size: {process['queue'].qsize()}\n"
    return process_info

def list_processes_gui():
    process_info = list_processes()
    if process_info:
        messagebox.showinfo("Running Processes", process_info)
    else:
        messagebox.showinfo("Running Processes", "No processes are running.")

def terminate_process_gui():
    pid_str = pid_entry.get()
    if pid_str:
        try:
            pid = int(pid_str)
            terminate_process(pid)
        except ValueError:
            messagebox.showerror("Error", "Invalid PID. Please enter a valid numeric PID.")
    else:
        messagebox.showerror("Error", "Please enter a PID to terminate.")

app = tk.Tk()
app.title("Process Manager GUI")

# Create Process
tk.Label(app, text="Enter a command:").pack()
command_entry = tk.Entry(app)
command_entry.pack()
create_process_button = tk.Button(app, text="Create Process", command=create_thread_gui)
create_process_button.pack()

# List Processes
list_processes_button = tk.Button(app, text="List Processes", command=list_processes_gui)
list_processes_button.pack()

# Terminate Process
tk.Label(app, text="Enter PID to terminate:").pack()
pid_entry = tk.Entry(app)
pid_entry.pack()
terminate_process_button = tk.Button(app, text="Terminate Process", command=terminate_process_gui)
terminate_process_button.pack()

app.mainloop()
