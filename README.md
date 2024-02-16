# ZIPPY
### Description
This is **_Zippy_**! A command-line tool designed to simplify the process of zipping and unzipping files. It provides an easy-to-use interface for compressing files into zip archives and extracting files from existing zip archives.
### Motivation
Zipping and unzipping files is a common task in software development, data management, and everyday computer use. However, performing these tasks manually can be tedious and error-prone, especially when dealing with large numbers of files or complex directory structures.

**_Zippy_** aims to streamline this process by providing a simple command-line interface that allows users to zip and unzip files with ease. Whether you need to package files for distribution, reduce storage space, or organize your files more efficiently, **_Zippy_** is here to help.

### Quick Start
To get started with **_Zippy_**, use the command-line interface to zip or unzip files as needed:
```
python project.py [-z | --zip] file_to_zip.ext
python project.py [-u | --unzip] file_to_unzip.zip
```
That's it! You're now ready to start zipping and unzipping files with **_Zippy_**.

### Usage
**_Zippy_** consists of two main files:

- project.py: This file contains the core functionality of the Zippy tool. It defines functions for zipping and unzipping files, as well as handling command-line arguments and displaying usage instructions.

- test_project.py: This file contains unit tests for the functions defined in project.py. It ensures that the zipping, unzipping, and usage instruction functions behave as expected under various scenarios.
