import sys
import os
import zipfile


def main():
    """Main function."""
    try:
        print(command_line())
    except Exception as e:
        print(f"An error occurred: {e}")


def zip_file(file_name):
    """Zip the given file."""
    if not os.path.exists(file_name):
        return f"Error: File '{file_name}' not found."

    zip_file_name = os.path.splitext(file_name)[0] + ".zip"
    with zipfile.ZipFile(
        zip_file_name, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6
    ) as zipf:
        zipf.write(file_name, os.path.basename(file_name))
    return f"{file_name} has been zipped as {zip_file_name}"


def unzip_file(zip_file_name):
    """Unzip the given file."""
    if not os.path.exists(zip_file_name):
        return f"Error: Zip file '{zip_file_name}' not found."

    with zipfile.ZipFile(zip_file_name, "r") as zipf:
        zipf.extractall(os.path.splitext(zip_file_name)[0])
    return f"{zip_file_name} has been unzipped."


def usage_instruction():
    """Display usage instruction."""
    return "Usage: python project.py [-z | --zip | -u | --unzip] file_name"


def command_line():
    """Handle command line arguments."""
    if len(sys.argv) != 3:
        return usage_instruction()

    if sys.argv[1] in ["-z", "--zip"]:
        return zip_file(sys.argv[2])
    elif sys.argv[1] in ["-u", "--unzip"]:
        return unzip_file(sys.argv[2])
    else:
        return usage_instruction()


if __name__ == "__main__":
    main()
