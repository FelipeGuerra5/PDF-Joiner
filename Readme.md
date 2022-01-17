# This project is made to be transformed in a ".exe" extension file.
- When executed it joins all ".pdf" extension files in the folder in one single file.
- They are order by ASCII Value of Character.
- The name of the new file is "PDF Join by Guerra"
- <a id="raw-url" href="https://github.com/FelipeGuerra5/PDF-Joiner/raw/main/PDF%20joiner%202.0.zip">Download .zip FILE</a>
- P.S. for convenience I hid all file, except the .exe file.

# Run it
- Download the ".zip" file
- After extraction insert your .pdf files in the folder and execute the .exe file.

# Do it yourself
- Copy the py code and save it. <a id="raw-url" href="https://github.com/FelipeGuerra5/PDF-Joiner/blob/main/PDF%20joiner%202.0.py">Download .py FILE</a>
- Create a virtual ambient in the folder the file on.
- On Anaconda prompt:

```commandline
    conda create -n [name of venv] python=[version]
    conda activate [name of venv] 
``` 
      
- With venv activated:

```commandline
    pip install pdfrw
    pip install glob
    pip install pyinstaller 
    pyinstaller -w "Name of the file.py"
```

- Three folders are going be created in your folder
  - _pycache_
  - dist
  - build
- On dist folder you have your the executable and all that it needs to run.
- For convenience I hid all but the .exe file. 

# Motivation
- This project was made to help me in my previous job were hundreds of pdf extension file needed to be joined together.
