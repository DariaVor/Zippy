import os
import zipfile
from project import zip_file, unzip_file, usage_instruction


def test_zip_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test file content")

    # Assert that the file was zipped successfully
    assert "has been zipped as" in zip_file(test_file)

    # Check if zip file exists
    assert os.path.exists(test_file.with_suffix(".zip"))


def test_unzip_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test file content")

    # Create a test zip file
    test_zip_file = tmp_path / "test.zip"
    with zipfile.ZipFile(test_zip_file, "w") as zf:
        zf.write(test_file, arcname=test_file.name)

    # Assert that the file was unzipped successfully
    assert "has been unzipped" in unzip_file(test_zip_file)

    # Check if unzipped file exists
    assert os.path.exists(tmp_path / "test.txt")


def test_usage_instruction():
    # Check if usage instruction is a non-empty string
    assert (
        "Usage: python project.py [-z | --zip | -u | --unzip] file_name"
        in usage_instruction()
    )
