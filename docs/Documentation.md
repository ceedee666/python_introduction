# Installation guide for NbGrader on Jupyterhub
- Installing Jupyterhub:
  - to install The littlest Jupyterhub using Amazon Web Services follow this tutorial step by step: https://tljh.jupyter.org/en/latest/install/amazon.html
- Installing NbGrader:
  - open the terminal (upper right: new -> terminal)
  - sudo -E pip install -U nbgrader
  - sudo -E jupyter nbextension install --py nbgrader --overwrite
  - sudo -E jupyter nbextension enable --py nbgrader 
  - sudo -E jupyter serverextension enable --py nbgrader
- Activating the Assignment-function for students
  - sudo jupyter nbextension enable --sys-prefix assignment_list/main --section=tree
  - sudo jupyter serverextension enable --sys-prefix nbgrader.server_extensions.assignment_list
  - sudo jupyter nbextension enable --sys-prefix validate_assignment/main --section=tree
  - sudo jupyter serverextension enable --sys-prefix nbgrader.server_extensions.validate_assignment
- Preparing the Exchange Directory:
  - using the terminal, navigate into the srv directory (2x "cd .." to get into the superior directory. Then "cd srv")
  - create the directory "nbgrader" (sudo mkdir nbgrader)
  - navigate into the newly created directory (cd nbgrader)
  - create the "exchange" directory (sudo mkdir exchange)
  - give everyone access to this directory (sudo chmod ugo+rw exchange)
- Creating the nbgrader_config.py:
  - navigate to ~/.jupyter using the terminal
  - create the file (sudo nano nbgrader_config.py) with following content: <br>
    `c = get_config()`<br>
    `c.CourseDirectory.root = '/home/jupyter-adminname/kursname'`
  - exit the editor using strg+x, save by pressing y and enter
  - create an empty diretory "migrated" (sudo mkdir migrated)
  - give everyone access to this directory (sudo chmod ugo+rw migrated)
- Create the course directory
  - nbgrader quickstart coursename
  - delete the directory "ps1" and the header, to make sure "source" is empty.
- Modify nbgrader_config.py in the course directory
  - navigate into the course directory using the normal interface
  - modify the file nbgrader_config.py: <br>
          `c = get_config()`<br>
          `c.CourseDirectory.course_id = "coursename"`<br>
          `c.CourseDirectory.db_assignments = [dict(name="assignmentname1"),`<br>
                                              `(name="assignmentname2")]`<br>
          `c.CourseDirectory.db_students = [dict(id="jupyter-studentname1"),`<br>
                                           `(id="jupyter-studentname2")]`<br>
- reboot the instance on AWS (right click on Instance -> Instance State -> Reboot)
----                                      
                         
### Adding students
- open the formgrader
- "Manage Students" -> "Add new student..."
- **Make sure to write "jupyter-" in front of the students name**
- Alternatively to these first steps for adding a single student, you can also import a CSV-File:
  - Upload a CSV-File in this format: <br>
    `id,last_name,first_name,email`<br>
    `ab1234s,Buerger,Anton,anton.buerger@alumni.fh-aachen.de`<br>
    `mm4321s,Mustermann,Max,max.mustermann@alumni.fh-aachen.de`<br>
  - import it using the terminal (nbgrader db student import filename)
    
*Die folgenden Schritte müssen **zusätzlich** erledigt werden:*
*The following steps have to be taken **additionally**:*
- Adding the student in the "nbgrader_config.py" that is located in the coursefolder. Again make sure to put "jupyter-" in front of the students name
- Open the control panel (upper right)
- "Admin" -> Add Users" (In here only write the students names. No "jupyter-" or other information)
----
### Adding assignments
- At first make sure, that your notebooks are readable for NbGrader:
  - inside of the notebooks click on "View" -> "Cell Toolbar" -> "Create Assignment"
  - Then choose what every cell does (upper right in the according cell using the drop-down menu):
    - Read only -> The student can not edit the cell (useful for task formulations)
    - Autograded answer -> The solution has to be written in this cell
    - Autograder tests -> Inside of this cell, there are testcases to check the correctness of ones solution
- Open the formgrader
- "Add new assignment"
- Choose a name and due-date (optional)
- Click on the newly created assignment to access its directory
- Upload your file here
- Go to the "nbgrader_config.py" inside of the course folder and add the assignment
- click on the "generate assignment" button, that you can find in the formgrader

- To release the assignment for all students, click on the "release"-button
- To collect the solutions click on the "collect"-button
- to automatically grade the solutions: open the terminal -> sudo nbgrader autograde assignmentname
----
### Using NbGrader as a student
- When logging in for the first time, you can define your own password
- When logged in you can access all assignments using the assignments tab
- Clicking on fetch, you can fetch any of those assignments onto your account to work on them
- You can then work on assignments online in the browser or download the assignments to work on them offline
- When work is done, click on submit to submit the notebook.
----
