# If you use this software in your publications, we kindly ask you to consider citing this work.

This is an editable Python file. To download the executable, check here: [(https://drive.google.com/drive/folders/1TjpILuU1iJKzM-O5ONXmrXlGx29T_HsG?usp=sharing)] or contact the author.



# TIFF to MOV Converter
=====================

**TIFF to MOV Converter** is a Python-based tool for converting TIFF images into MOV video files. It supports image resizing and allows you to specify the frames per second (FPS) for the output video. The tool features a user-friendly graphical interface built with Tkinter.

Features
--------
- Convert single or multiple TIFF image folders to MOV video files
- Resize images before conversion
- Specify FPS for the output video
- Process TIFF files in nested directories
- User-friendly GUI with progress updates


### Prerequisites
To run the Python script directly, ensure you have Python 3.x installed. 


Usage
-----
### Running the Application
- **Executable Version**: Double-click the `.exe` file to launch the application.
- **Python Script**: Run the script from the command line:
    python TIF_TO_MOV.py

### Configuring the Application
1. **Select Parent Folder**:
    - Click the "Browse" button next to "Select parent folder".
    - Choose a folder containing TIFF images. The tool will process TIFF files in this folder and its subfolders.

2. **Select Output Folder**:
    - Click the "Browse" button next to "Select output folder".
    - Specify the folder where the resulting MOV files will be saved.

3. **Scale Factor**:
    - Choose the scaling factor for the images from the dropdown menu (e.g., 1x, 2x, 4x).

4. **FPS**:
    - Enter the desired frames per second (FPS) for the output video. Ensure the FPS value is greater than 0.

5. **Start Processing**:
    - Click the "Create MOV" button to begin the conversion process. The progress will be displayed in the GUI, and the status will be updated accordingly.

File Naming Convention
----------------------
### Single Folder Processing
If processing a single folder, the MOV file will be named using the base name of the selected folder. Example:
- **Input Folder**: C:\Images\MyTiffFolder
- **Output MOV File**: MyTiffFolder_resized_2x_video.mov

### Multiple Folder Processing
If processing a parent folder containing subfolders, each subfolder's MOV file will include the base name of the parent folder and the relative path of the subfolder. Example:
- **Parent Folder**: C:\Images\ParentFolder
- **Subfolder**: Subfolder1
- **Output MOV File**: ParentFolder_Subfolder1_resized_2x_video.mov

Example
-------
1. **Folder Structure**:
    C:\Images\
    ├── FolderA\
    │   ├── image1.tif
    │   └── image2.tif
    └── FolderB\
        ├── image3.tif
        └── image4.tif

2. **Processing Result**:
    Two MOV files will be created:
    - FolderA_resized_2x_video.mov
    - FolderB_resized_2x_video.mov

Contact the Authors
-------------------
For support or inquiries, please contact:
- **Marcin Rojek**
  Lead Statistician, Programmer, Poland
  Medical University of Silesia
  Department of Histology and Cell Pathology
  [ResearchGate Profile](https://www.researchgate.net/profile/Marcin-Rojek-3)

- **Piotr Lewandowski**
  Physician, Histology Specialist
  Medical University of Silesia
  Department of Histology and Cell Pathology
  [ResearchGate Profile](https://www.researchgate.net/profile/Piotr-Lewandowski-4)

- **Filip Patryk Pietryga**
  Independent Programmer

- **Professor Romuald Wojnicz**
  Project Supervisor, Head of Department
  Medical University of Silesia
  Department of Histology and Cell Pathology
  [Department Website](https://histologia-zabrze.sum.edu.pl/)

License
-------
This project is licensed under the GNU 3.0 License. 

Acknowledgments
---------------
- Tkinter for the GUI framework
- OpenCV for image processing and video creation
- psutil for CPU count
