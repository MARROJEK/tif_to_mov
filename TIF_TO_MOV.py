import os
import re
import cv2
import threading
import psutil
import tempfile
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import base64

base64_icon = "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"


def create_temp_icon_file(base64_data):
    """Creates a temporary icon file from a Base64 string"""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.ico')
    temp_file.write(base64.b64decode(base64_data))
    temp_file.close()
    return temp_file.name


num_threads = min(psutil.cpu_count(logical=True), 8)

current_progress = 0


def process_frame(filename, input_folder, scale_factor):
    """Function to process a single frame"""
    frame = cv2.imread(os.path.join(input_folder, filename))
    if frame is not None:
        new_width = int(frame.shape[1] / scale_factor)
        new_height = int(frame.shape[0] / scale_factor)
        resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        return resized_frame
    return None


def sum_of_numbers_in_filename(filename):
    """Sums all the numbers in the filename"""
    numbers = re.findall(r'\d+', filename)
    return sum(int(num) for num in numbers)


def create_csv_file(tiff_files, output_folder, csv_filename):
    """Creates a CSV file with TIFF filenames and their numeric values"""
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Sum of Numbers in Filename"])
        for filename in tiff_files:
            sum_value = sum_of_numbers_in_filename(filename)
            writer.writerow([filename, sum_value])
    print(f"CSV file has been created: {csv_filename}")


def process_segment(segment, input_folder, scale_factor, fps, video_name, progress_callback):
    """Processes a single segment of frames"""
    segment_file_list = sorted(segment, key=lambda f: sum_of_numbers_in_filename(f))
    with tempfile.NamedTemporaryFile(suffix='.mov', delete=False) as temp_file:
        output_file = temp_file.name

    # Load the first frame to get the dimensions
    first_frame = cv2.imread(os.path.join(input_folder, segment_file_list[0]))
    if first_frame is None:
        print(f"Error loading the first frame in the folder: {input_folder}.")
        return

    new_width = int(first_frame.shape[1] / scale_factor)
    new_height = int(first_frame.shape[0] / scale_factor)

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Changed codec for MOV
    video = cv2.VideoWriter(output_file, fourcc, fps, (new_width, new_height))

    # Processing frames
    total_frames = len(segment_file_list)
    for idx, filename in enumerate(segment_file_list):
        frame = process_frame(filename, input_folder, scale_factor)
        if frame is not None:
            video.write(frame)
        progress_callback(idx + 1, total_frames, video_name)  # Passing the video name

    video.release()
    print(f"Video segment has been created: {output_file}")
    return output_file


def merge_video_segments(segments, output_file):
    """Merges video segments into a single video file"""
    # Assuming all segments have the same dimensions and fps
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    first_segment = cv2.VideoCapture(segments[0])
    fps = first_segment.get(cv2.CAP_PROP_FPS)
    width = int(first_segment.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(first_segment.get(cv2.CAP_PROP_FRAME_HEIGHT))
    first_segment.release()

    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for segment in segments:
        cap = cv2.VideoCapture(segment)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            video.write(frame)
        cap.release()

    video.release()
    print(f"Final video has been created: {output_file}")


def get_parent_folder_names(directory):
    """Get a string containing the names of parent folders of the given directory"""
    parent_names = []
    while True:
        directory, folder = os.path.split(directory)
        if folder:
            parent_names.append(folder)
        else:
            break
    return '_'.join(reversed(parent_names))


def get_base_folder_name(directory):
    """Get the base folder name from the full directory path."""
    return os.path.basename(directory)


def get_relative_path(base_folder, current_folder):
    """Get the relative path from the base folder to the current folder."""
    return os.path.relpath(current_folder, base_folder)


def process_folder(input_folder, output_folder, fps, scale_factor, progress_callback):
    """Processes a single folder or a parent folder with subfolders"""

    def process_directory(directory):
        """Recursively processes the folder and its subfolders"""
        segments = []
        for root, dirs, files in os.walk(directory):
            tiff_files = [f for f in files if f.endswith(".tif")]
            if tiff_files:
                # Split the files into segments
                segment_size = len(tiff_files) // num_threads + (len(tiff_files) % num_threads > 0)
                segments = [tiff_files[i:i + segment_size] for i in range(0, len(tiff_files), segment_size)]

                # Process segments in parallel
                temp_files = []
                threads = []
                update_status(f"Processing files in {directory}...")
                reset_progress_bar()
                for i, segment in enumerate(segments):
                    # Compute the relative path from the base folder
                    relative_path = get_relative_path(input_folder, root)
                    video_name = f"{base_folder_name}_{relative_path.replace(os.sep, '_')}_resized_{scale_factor}x_video.mov"
                    thread = threading.Thread(target=lambda seg=segment, path=relative_path: temp_files.append(
                        process_segment(seg, root, scale_factor, fps, video_name,
                                        lambda current, total, name: progress_callback(current, total, name))
                    ))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()  # Wait for all segments to finish processing

                # After processing the segments, merge the segments
                final_output_file = os.path.join(output_folder,
                                                 f"{base_folder_name}_{relative_path.replace(os.sep, '_')}_resized_{scale_factor}x_video.mov")
                merge_video_segments(temp_files, final_output_file)

                # Removing temporary files
                for temp_file in temp_files:
                    os.remove(temp_file)

    if os.path.isdir(input_folder):
        base_folder_name = get_base_folder_name(input_folder)
        process_directory(input_folder)
    else:
        # If the specified folder is not a directory, treat it as a folder with TIFFs
        base_folder_name = get_base_folder_name(os.path.dirname(input_folder))
        tiff_files = [f for f in os.listdir(input_folder) if f.endswith(".tif")]
        if tiff_files:
            output_file = os.path.join(output_folder, f"{base_folder_name}_resized_{scale_factor}x_output_video.mov")
            update_status(f"Processing files in {input_folder}...")
            reset_progress_bar()
            temp_file = process_segment(tiff_files, input_folder, scale_factor, fps, base_folder_name,
                                        lambda current, total, name: update_progress_bar(current, len(tiff_files),
                                                                                         name))
            merge_video_segments([temp_file], output_file)
            os.remove(temp_file)
            update_status(f"Completed processing {base_folder_name}")


def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_folder_var.set(folder_path)


def open_about_dialog():
    about_window = tk.Toplevel(window)
    about_window.title("About Authors")
    about_window.geometry("700x500")  # Adjust the size as needed

    icon_path = create_temp_icon_file(base64_icon)

    about_window.iconbitmap(icon_path)

    about_text = """
    About the Authors

    If you find this tool useful, please consider citing our work:

    Marcin Rojek  
    Lead Statistician, Programmer, Poland  
    Medical University of Silesia
    Department of Histology and Cell Pathology  
    (https://www.researchgate.net/profile/Marcin-Rojek-3)

    Piotr Lewandowski  
    Physician, Histology Specialist  
    Medical University of Silesia
    Department of Histology and Cell Pathology  
    (https://www.researchgate.net/profile/Piotr-Lewandowski-4)

    Filip Patryk Pietryga  
    Independent Programmer  

    Professor Romuald Wojnicz  
    Project Supervisor, Head of Department  
    Medical University of Silesia
    Department of Histology and Cell Pathology 
    (https://histologia-zabrze.sum.edu.pl/)

    Project website:
    https://github.com/MARROJEK/TIF_to_MOV

    Your citation helps recognize our work and supports further research.
    """

    # Create a Frame to contain the Text widget and Scrollbar
    frame = tk.Frame(about_window)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a Scrollbar and add it to the right side of the Frame
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Text widget for displaying the text with a vertical scrollbar
    text_widget = tk.Text(frame, wrap=tk.WORD, height=20, width=70, padx=10, pady=10, yscrollcommand=scrollbar.set)
    text_widget.insert(tk.END, about_text)
    text_widget.config(state=tk.DISABLED)  # Make it read-only
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configure the Scrollbar to work with the Text widget
    scrollbar.config(command=text_widget.yview)

    # Add a Close button
    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=10)


def open_output_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_var.set(folder_path)


def validate_fps_input(value_if_allowed):
    if value_if_allowed.isdigit():
        if value_if_allowed == "0":
            messagebox.showerror("Invalid Input", "FPS cannot be zero. Please enter a positive number.")
            return False
        return True
    elif value_if_allowed == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number for FPS.")
        return False


def update_progress_bar(current, total, video_name):
    """Updates the progress bar"""
    global current_progress
    progress = (current / total) * 100
    if progress > current_progress:
        current_progress = progress
        progress_var.set(progress)
        if progress >= 100:
            update_status(f"Saving {video_name}...")

    window.update_idletasks()


def reset_progress_bar():
    """Resets the progress bar"""
    global current_progress
    current_progress = 0
    progress_var.set(0)
    window.update_idletasks()


def update_status(message):
    """Updates the processing status"""
    status_label.config(text=message)
    window.update_idletasks()


def process_tiff_files():
    open_about_dialog()

    def task():
        input_folder = input_folder_var.get()
        output_folder = output_folder_var.get()
        fps = int(fps_var.get())
        scale_factor = int(scale_factor_var.get().replace('x', ''))

        # Disabling the GUI during processing
        start_button.config(state=tk.DISABLED)
        input_folder_entry.config(state=tk.DISABLED)
        output_folder_entry.config(state=tk.DISABLED)
        scale_factor_menu.config(state=tk.DISABLED)
        fps_entry.config(state=tk.DISABLED)

        # Resetting the progress bar before starting processing
        reset_progress_bar()

        # Setting the initial status
        update_status("Starting processing...")

        # Process the folder
        process_folder(input_folder, output_folder, fps, scale_factor,
                       lambda current, total, name: update_progress_bar(current, total, name))

        # Enabling the GUI after completion
        start_button.config(state=tk.NORMAL)
        input_folder_entry.config(state=tk.NORMAL)
        output_folder_entry.config(state=tk.NORMAL)
        scale_factor_menu.config(state=tk.NORMAL)
        fps_entry.config(state=tk.NORMAL)
        update_status("Processing complete")

    # Running the task in a separate thread
    processing_thread = threading.Thread(target=task)
    processing_thread.start()


def create_gui():
    icon_path = create_temp_icon_file(base64_icon)
    global window, progress_var, progress_bar, status_label, start_button
    global input_folder_var, output_folder_var, scale_factor_var, fps_var
    global input_folder_entry, output_folder_entry, scale_factor_menu, fps_entry

    window = tk.Tk()
    window.title("TIF to MOV Converter")
    window.resizable(False, False)
    window.iconbitmap(icon_path)
    # Global variables for the GUI

    # Create a menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Create the "Help" menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Cite Me", menu=help_menu)
    help_menu.add_command(label="About Authors", command=open_about_dialog)

    input_folder_var = tk.StringVar()
    output_folder_var = tk.StringVar()
    scale_factor_var = tk.StringVar(value="1x")
    fps_var = tk.StringVar(value="100")

    validate_fps = (window.register(validate_fps_input), '%P')

    # Selecting the parent folder
    tk.Label(window, text="Select parent folder:").grid(row=0, column=0, padx=5, pady=5)
    input_folder_entry = tk.Entry(window, textvariable=input_folder_var, width=50,
                                  state='readonly')  # Make it read-only
    input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=open_folder_dialog).grid(row=0, column=2, padx=5, pady=5)

    # Selecting the output folder
    tk.Label(window, text="Select output folder:").grid(row=1, column=0, padx=5, pady=5)
    output_folder_entry = tk.Entry(window, textvariable=output_folder_var, width=50,
                                   state='readonly')  # Make it read-only
    output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=open_output_folder_dialog).grid(row=1, column=2, padx=5, pady=5)

    # Selecting the scale factor
    tk.Label(window, text="Scale Factor:").grid(row=2, column=0, padx=5, pady=5)
    scale_factor_menu = tk.OptionMenu(window, scale_factor_var, "1x", "2x", "4x", "8x", "16x", "32x", "64x")
    scale_factor_menu.grid(row=2, column=1, padx=5, pady=5)

    # Entering FPS
    tk.Label(window, text="FPS:").grid(row=3, column=0, padx=5, pady=5)
    fps_entry = tk.Entry(window, textvariable=fps_var, validate='key', validatecommand=validate_fps)
    fps_entry.grid(row=3, column=1, padx=5, pady=5)

    # Button to start processing
    start_button = tk.Button(window, text="Create MOV", command=process_tiff_files)
    start_button.grid(row=4, column=1, padx=5, pady=10)

    # Progress bar
    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(window, variable=progress_var, maximum=100, length=400)
    progress_bar.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

    # Status label
    status_label = tk.Label(window, text="Waiting to start...")
    status_label.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

    window.mainloop()
    os.remove(icon_path)


create_gui()
