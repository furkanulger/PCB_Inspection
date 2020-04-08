# Optical-Inspection-of-PCBs

This project is intended to execute optical inspection for bare, assembled boards and solder joints based on template and defective board image comparison.
By editing relevant parts and changing segmentation parameters according to which yields the best in your case you can inspect your defective board based on template board image in JPEG format or there are some board image pairs available to test in BOARD LIBRARY  file to instantiate the procedure.
Please refer to the research paper for more information.
https://ieeexplore.ieee.org/document/8936659

## Installation

### Anaconda

#### Windows

- Open up an anaconda prompt
- Create a new environment called `pcb` with `python3.6`
	- `conda create -n pcb python=3.6`
- Switch to the new environment
	- `conda activate pcb`
- Install qt4
	- Download the relevant pyqt4 wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)
	- Download PyQt4‑4.11.4‑cp36‑cp36m‑win_amd64.whl if 64 bit or otherwise
	- Go to download folder
	- Build and install the wheel
		- for example: `pip install PyQt4‑4.11.4‑cp36‑cp36m‑win_amd64.whl` if it is 64 bit one
- Install other packages
	- `pip install opencv-python==3.2.0.8 matplotlib numpy pytesseract imutils`
- Install Tesseract
	- Download [this](https://excellmedia.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe) (Or go to [here](https://sourceforge.net/projects/tesseract-ocr-alt/files/) and download the required version)
	- Install it with default settings

## Run

- `python InspectonGUI.py`



