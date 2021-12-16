"""
This program approximately re-synchronizes the srt file if the subtitle is not synchronized
with the movie. This program will create a new file with adjusted time.

This program can be run with the following command:
    python Main.py directory operation milliseconds
    where,
    Main.py     : refers to this program
    directory   : directory of the srt file
    operation   : {prev or next} prev is to delay and next is to speed up
    milliseconds    : total duration you would like to delay or speed up

Example 1, If you want to delay the srt file for 5 seconds (5000 in milliseconds), then
    python Main.py D://your directory//file.srt prev 5000

Example 2, If you want to speed up the srt files for 3 seconds (3000 in milliseconds), then
    python Main.py D://your directory//file.srt next 3000
"""

import sys
import re
import datetime


def accept_arguments():
    """
    This method accepts the parameters from the user - srt file directory, {prev, next}, duration (seconds).
    """
    try:
        return sys.argv[1], sys.argv[2], sys.argv[3]
    except:
        print("You failed to provide arguments!")
        sys.exit()


def check_arguments(file_directory, operation, duration):
    """
    This function checks the passed arguments.
    :param file_directory: the directory of the srt file
    :param operation: subtraction or addition operation
    :param duration: total seconds to be subtracted or added
    """
    try:
        file_directory = str(file_directory)
        duration = int(duration)
        operation = str(operation)
        if operation in ["prev", "next"]:
            return True
    except ValueError:
        return False


def load_file(file_directory):
    """
    This function loads the srt data from given file.
    :param file_directory: the directory of the srt file
    :return: data
    """
    file = open(file_directory, "r", encoding="utf8")
    data = file.read()
    return data


def find_timestamps(data):
    """
    This function finds all timestamps in the data loaded from srt file.
    :param data: data loaded from srt file
    :return: list of timestamps pairs
    """
    pattern = "[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2},[0-9]{1,3} --> [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2},[0-9]{1,3}"
    timestamps = re.findall(pattern, data)
    return timestamps


def adjust_timestamps(timestamps, operation, duration):
    """
    This function adjusts the timestamps by adding or subtracting duration (in milliseconds).
    :param timestamps: a list of timestamps extracted from the srt file
    :param operation: the user input operation (prev, next)
    :param duration: total duration in seconds to be added or subtracted
    :return: a list of newly adjusted timestamps
    """
    new_timestamps = list()  # to store the newly adjusted timestamps
    for timestamp_pair in timestamps:
        # temp list
        temp_list = list()  # to store the newly adjusted timestamp pair temporarily
        # extract start and end
        result = re.findall("[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2},[0-9]{1,3}", timestamp_pair)
        for t in result:
            # Format string t into datetime
            old_timestamp = datetime.datetime.strptime(t, "%H:%M:%S,%f")
            # Add or subtract duration from that timestamp
            if operation == "next":
                new_timestamp = (old_timestamp + datetime.timedelta(milliseconds=int(duration))).time()
            else:
                new_timestamp = (old_timestamp - datetime.timedelta(milliseconds=int(duration))).time()
            # Format to defined format (HH:MM:SS,MS)
            temp = new_timestamp.strftime("%H")+":"+new_timestamp.strftime("%M")+":"+new_timestamp.strftime("%S")+","+new_timestamp.strftime("%f")[:3]
            temp_list.append(temp)
        new_timestamps.append(" --> ".join(temp_list))
    return new_timestamps


def replace_timestamps(data, old_timestamp, new_timestamp):
    """
    This function replaces the old timestamps with new timestamps.
    :param data: data loaded from srt file
    :param old_timestamp: a list of old timestamp pairs (start --> end)
    :param new_timestamp: a list of new timestamp pairs (start --> end)
    :return: data updated
    """
    for old, new in zip(old_timestamp, new_timestamp):
        data = data.replace(old, new)
    return data


def write_file(file_directory, data):
    """
    This function writes updated data into a new file.
    :param file_directory: the directory of input srt file
    :param data: data updated with new timestamps
    """
    dir, name = file_directory[0:file_directory.rindex("/")+1], file_directory[file_directory.rindex("/")+1:]
    file = open(dir+"new_"+name, "w", encoding="utf8")
    file.write(data)
    # Print result
    print("#### Your new file is ready. ###")


def main():
    """
    This function runs first.
    """

    # Accept arguments.
    file_directory, operation, duration = accept_arguments()

    # Check arguments
    if not check_arguments(file_directory, operation, duration):
        print("Try again!!")
        sys.exit()

    # Load str file
    data = load_file(file_directory)

    # Search timestamps
    timestamps = find_timestamps(data)

    # Adjust timestamps
    new_timestamps = adjust_timestamps(timestamps, operation, duration)

    # Replace timestamps
    new_data = replace_timestamps(data, timestamps, new_timestamps)

    # Replace file data
    write_file(file_directory, new_data)


if __name__ == '__main__':
    main()
