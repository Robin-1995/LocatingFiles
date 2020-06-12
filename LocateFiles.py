import os
def find_files(suffix, path):

    """
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    while True:
        try:
            directories = os.listdir(path)
            break
        except OSError as e:
            print(f"OSError: {e}")
            return

    paths = list()
    for item in directories:
        new_path = os.path.join(path, item)

        if os.path.isfile(new_path):    # <-- check whether new_path a file
            if new_path.endswith(str(suffix)):  # <-- append to ouput if new_path ends with suffix
                paths.append(new_path)

        else:
            sub_dir = find_files(suffix, new_path)  # <-- if not a file, it must be a directory, call find_files on the new path
            for item in sub_dir:
                paths.append(item)

    return paths


# # Test Case 1 - valid path and suffix
# path = os.getcwd()
# test1 = find_files(".c",path)
# print(test1) #<-- return list of all paths which contains a file that ends with the ".c"
#
#
#
# #Test Case 3 - invalid path
# path3 = r""
# test3 = find_files(".c", path3)
# print(test3) # <-- Raise an OSError since path is invalid and return none
#
# #Test Case 4 - valid path, no suffix
# path4 = os.getcwd()
# test4 = find_files("", path4) # <-- return all files under path
# print(test4)
#
# #Test Case 5 - valid path, non-string suffix
# path4 = os.getcwd()
# test4 = find_files(1, path4) # <-- returns empty list (suffix is converted to string in the function)
# print(test4)