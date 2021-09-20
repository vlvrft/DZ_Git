import os

ROOT = os.path.dirname(__file__)
project_name = 'my_project'
paths = [os.path.join(project_name, 'settings'),
         os.path.join(project_name, 'mainapp')
         os.path.join(project_name, 'adminapp')
         os.path.join(project_name, 'authapp')]
for path1 in paths:
    os.makedirs(os.path.join(ROOT, path1), exist_ok=True)
