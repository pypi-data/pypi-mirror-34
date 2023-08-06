[![Build Status](https://travis-ci.org/USGS-Astrogeology/PySAT_Point_Spectra_GUI.svg?branch=dev)](https://travis-ci.org/USGS-Astrogeology/PySAT_Point_Spectra_GUI)
[![Coverage Status](https://coveralls.io/repos/github/Kelvinrr/PySAT_Point_Spectra_GUI/badge.svg?branch=master)](https://coveralls.io/github/Kelvinrr/PySAT_Point_Spectra_GUI?branch=master)
[![Join the chat at https://gitter.im/USGS-Astrogeology/PySAT](https://badges.gitter.im/USGS-Astrogeology/PySAT.svg)](https://gitter.im/USGS-Astrogeology/PySAT?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


## Installation


### 1. Fresh install of Miniconda (Skip to step 2 if you have Anaconda/Miniconda)

Install <a href="https://conda.io/miniconda.html">Miniconda</a>

\*Note for Windows: If you have previous versions of Python on your system, it may make it difficult for Anaconda/Miniconda to use the command `conda`. If this is the case, you have two options:
1. You can choose to uninstall previous versions of Python using <a href ="https://www.iobit.com/en/advanceduninstaller.php?">IObit Uninstaller</a><br>
2. If uninstalling previous version of Python is not an option, you can do a <a href="https://www.anaconda.com/download/">full Anaconda install</a> and then use the Anaconda Prompt that gets installed with it to execute the following commands.

### 2. Download the environment file (right click the link and save)

[Environment.yml](https://raw.githubusercontent.com/USGS-Astrogeology/PySAT_Point_Spectra_GUI/master/environment.yml)

### 3. Open a terminal (on Windows, use the Anaconda prompt or `cmd`, not Powershell) in the directory where you saved the file and type:

```bash
conda --v # this will give you your version, make sure it is 4 or greater, if not use the below command
conda install conda=4  # SKIP THIS LINE ON WINDOWS
conda env create -n point_spectra_gui -f environment.yml
source activate point_spectra_gui  # omit the `source` on Windows
```

### 4. Done! How to use point_spectra_gui

```bash
source activate point_spectra_gui  # omit the `source` on Windows
point_spectra_gui
```

### 5. Optional. Run program with a script

If you'd like to be able to run our program without having to retype **4** out, simply copy the below text into notepad, and then save it as point_spectra_gui.bat

```
call activate point_spectra_gui
point_spectra_gui
```

### 6. Update an existing installation

If you already have an earlier version of the PySAT Point Spectra GUI installed as described above and you want to wipe it and update to the latest version, just do:

```bash
conda env remove -n point_spectra_gui
```
And then follow the instructions above to install a fresh version.

# Bugs

## Run into bugs or features that are missing? Let us know by reporting an issue!

# PYSAT UI
![PYSAT splash](./images/splash.png)  

- The UI's backend is designed and created in Python with the QT framework


## Control Flow

![FlowChart](./images/Flowchart.png)

- The user begins by starting \_\_main\_\_.py.
- \_\_main\_\_.py will load MainWindow.py which in turn will load the splash screen and all necessary UI pieces
- MainWindow.py displays the mainframe in which the UI's submodules will be loaded into
- MainWindow.py will then foward control to each submodule of focus
- Each of the submodules build the collective UI library
- Each submodule also contains all the necessary functions that will interact with Anaconda and PYSAT
- The PYSAT and Anaconda libraries will then do the necessary data manipulations
- The values are then returned back up to the Submodule which in turn is returned back to MainWindow which will then deal with changed data

# Walkthrough (with images)

## 1. Fresh install of Miniconda (Skip to step 2 if you have Anaconda/Miniconda)

![982f2828-0d23-4dac-b84c-5808d47cd3ae](https://user-images.githubusercontent.com/11879769/32648152-ce130f7c-c5b1-11e7-954a-f580ff64f331.gif)

## 2. Download the environment file (right click the link and save)

![dc336619-0412-4d4d-959d-dd4d83d863f8](https://user-images.githubusercontent.com/11879769/32661238-613f2386-c5e3-11e7-9e24-05bebb9ba8f7.gif)

## 3. Open a terminal (on Windows, `cmd`, not Powershell) in the directory where you saved the file and type:

![55096025-e378-4728-ba89-9ed1a5bcf24b](https://user-images.githubusercontent.com/11879769/32648500-3a948580-c5b3-11e7-86e9-cabf56827f1e.gif)

## 4. Done! How to use point_spectra_gui

![0f5329a7-1e09-49f2-8971-6e503b25f648](https://user-images.githubusercontent.com/11879769/32648596-ccd5ffa0-c5b3-11e7-9c38-44a5e4ad9ca1.gif)
