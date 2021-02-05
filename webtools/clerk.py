# clerk.py
# A utility file used to deal with files and folders

import csv
import os
import glob
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import codehsinator.page as site
import codehsinator.config as config
from codehsinator.locators import MainPageLocators, CoursePageLocators, StudentPageLocators
from selenium import webdriver

working_dir = Path.cwd()



def file_exists(filename):
    filename = Path(filename)
    return filename.exists()


def get_path_list(path):
    """ creates a list of all parts to a path - OS agnostically"""
    # convert path to OS-specific format
    path = Path(path)
    # convert path to string with / slashes
    path = path.as_posix()
    return path.split('/')


def get_full_path_string(path):
    """path must be a relative path starting from working directory """
    full_path = working_dir
    p_list = get_path_list(path)
    for i in p_list:
        full_path = full_path / i
    return full_path


def write_csv_file(filename, data_list):
    # Build filename
    try:
        with open(filename, "w", newline='') as output:
            writer = csv.writer(output)
            writer.writerows(data_list)
    except:
        with open(filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(data_list)


def get_list_from_file(filename):
    data = []
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    except:
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    return data


def get_all_file_paths(directory):
    """ returns all file paths within a directory relative to project directory path """
    # initializing empty file paths list
    file_paths = []
    directory = Path(directory)
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            # Path(filepath) converts to a OS-specific path
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def archive_files(dir_path):
    """ Compresses all files from dir_path into zip """
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H%M%S")
    filename = 'data/archives/{}-{}-{}_{}-archive.zip'.format(
        year, month, day, time)
    # directory = Path(dir_path)

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(dir_path)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(filename, 'w') as zip:
        # writing each file one by one
        # adding an attempt to write into a folder called "archives"
        for file in file_paths:
            file = Path(file)
            zip.write(file)
    return filename


def create_pretest_list(browser):
    file_name = browser.title + "pretest.csv"
    # Create initial list with headers (title, then row headers)
    file_list = [[file_name],
                 ["Student Name", "Score"], ]
    # GET list of students in the class
    student_list = browser.get_student_names()
    # Open each student page and get their pretest score
    for name in student_list:
        browser.open_student_page(name)
        # set score to 0, then, if we can get the completed module
        score = '0'
        try:
            # get the first module div
            first_module = browser.get_elements(
                StudentPageLocators.MODULE_CONTAINERS)[0]
            # Make sure it's the pretest module
            if "Unit 0" not in first_module.text:
                continue
            # get the right-hand div with the percentage
            right_div = first_module.find_element_by_class_name(
                'module-info-right')
            # get the text from the right_div
            result = right_div.text
            # if we haven't raised an exception, then student completed it
            if '100' in result:
                score = '15'
            else:
                score = '0'
        except:
            score = '0'
        # Change name to sortable name
        name = get_sortable_name(name)
        # Append name and score to next row
        file_list.append([name, score])
        # Go back to get next student
        browser.back()
    # End loop - sort list
    file_list.sort()
    # Go back to course page
    browser.back()
    return file_list


def get_sortable_name(name):
    # split the names and take first and last of the names (in case there are spaces)
    names = name.split(" ")
    first = names[0]
    last = names[-1]
    return last + '_' + first


def sort_students(unsorted):
    sorted_names = []
    for i in unsorted:
        sorted_names.append(get_sortable_name(i))
    return sorted_names


def insert_course_title(title, data_list):
    data_list[0][1] = title


def extract_element_title(el):
    try:
        my_string = el.text.split('\n', 1)
    except:
        my_string = el.split('\n', 1)
    return my_string[0]


if __name__ == "__main__":
    print(working_dir)
    data_file_paths = get_all_file_paths("data")
    print(data_file_paths)

    # Test create_pretest_csv

    browser = site.MainPage(webdriver)
    browser.launch(config.CODEHS_MAIN)
    browser.set_course_titles()
    course_link = browser.get_course_link('Programming 1 Spring 2020 Python')
    browser.launch(course_link)
    unsorted = browser.get_student_names()
    sorted_names = sort_students(unsorted)
    print(sorted_names)
    pretest_list = create_pretest_list(browser)
    print(pretest_list)
    archive_files("data/sample")
