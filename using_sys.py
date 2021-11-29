import sys # we now have access to aspeects of the platform we are runnnig upon
print(sys.version, sys.version_info)
# print(sys.path) # where will python look for imports
print(sys.platform)
print(sys.base_prefix)

# we can pass in systetm arguments when we invoke a python module
# NB run this as follows:
# python using_sys.py athlone ie
print( sys.argv[1], sys.argv[2] ) # careful - sys.argv[0] is always the name of the module