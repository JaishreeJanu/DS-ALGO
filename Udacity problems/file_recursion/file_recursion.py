import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name ending with suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_c_files = []
    contents = os.listdir(path)

    for content in contents:
        nextpath = os.path.join(path,content)

        if os.path.isdir(nextpath):
            list_c_files = list_c_files + find_files(suffix,nextpath)
        elif content.endswith(suffix):
            list_c_files.append(nextpath)

    return list_c_files


path = os.getcwd()+'/testdir/'
print("Path of .c files \n", find_files('.c',path))
'''
Output:
Path of .c files 
['/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/subdir3/subsubdir1/b.c',
'/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/subdir5/a.c',
'/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/subdir1/a.c',
'/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/t1.c']
'''

print("Path of .py files \n", find_files('.py',path))
'''
Output:
Path of .py files 
[]
'''

print("Path of .gitkeep files \n", find_files('.gitkeep',path))
'''
Output:
Path of .gitkeep files 
 ['/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/subdir2/.gitkeep',
'/home/jaishree/Data-structures-and-algorithms/Udacity problems/file_recursion/testdir/subdir4/.gitkeep']
'''
