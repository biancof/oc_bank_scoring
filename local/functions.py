# Version 1.1 (July 12th, 2023)
# Version 1.2 (July 21th, 2023)

# Import packages
import os, shutil
import time, datetime
from contextlib import contextmanager

# Set starting time of a given process (time to be used in calc_time, print_time and script_exec_time functions; see below)
def set_start():
    return time.time()

# Raturns a calculated time interval (needs a starting time set by set_start function; see above)
def calc_time(start_time, r=0):
    end_time = time.time()
    ela_time = round(end_time - start_time, r)
    return ela_time

# Prints (or returns) he result of a process, including its duration (needs either a duration time calculated by calc_time funtion, or a starting time set by set_start function; see above)
def print_time(text, start_time=None, ela_time=None, r=0, label='[ela_time]', print_res=True):
    if(ela_time==None):
        ela_time = calc_time(start_time, r)
    ela_time_str = str(ela_time)
    res = text.replace(label, ela_time_str)
    if(print_res):
        print(res)
    else:
        return res

# Prints (or return) the script execution duration (needs a starting time set by set_start function; see above)
def script_exec_time(start_time, ela_time=None, r=0, label='[ela_time]', print_res=True):
    txt = f"Time elapsed to execute the script: {label} sec."
    res = print_time(text=txt, start_time=start_time, ela_time=ela_time, r=r, label=label, print_res=False)
    if(print_res):
        print(res)
    else:
        return res

# Returns the current date + time in a customizable format (default: 00/00/0000 00:00:00)
def get_date_time(dt_format="%d/%m/%Y %H:%M:%S"):
    dt = datetime.datetime.now()
    dt_str = dt.strftime(dt_format)
    return dt_str

# Timer function from https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/script
@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} - done in {:.0f}s".format(title, time.time() - t0))

# Prints (or returns in form of string) the shape of a given dataframe
def print_shape(df, desc=None, print_res=True):
    if(desc!=None):
        desc = f"({desc}) "
    n_rows, n_cols = df.shape
    res = f"The dataframe {desc}contains {n_rows} rows and {n_cols} columns."
    if(print_res):
        print(res)
    else:
        return res

# Makes a folder empty (if it is not)
def empty_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
# Print version of the package
print("Local functions: version 1.2 (July 20th, 2023)")
  
