#!env python
import os
import sys

classes_dir = os.path.join(os.path.dirname(__file__), '..', 'classes')
node_name = sys.argv[1]
print(open(os.path.join(classes_dir, node_name)+'.yaml').read())
