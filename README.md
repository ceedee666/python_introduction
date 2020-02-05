# About
This repository contains a number of [Jupyter](https://jupyter.org/) notebooks. These notbooks
provide an introduction to programming in Python.

The focus of the matrial are students with 
little or none previous programmin experience, especially in non-technical courses of study. 
To support these students in learning the complex skill of programming, the
[Four Components Instructional Design (4C/ID)](http://www.tensteps.info/) method was used to create the material.

The notebooks are organised as in a directory structure in ascending complexity. Each dictionay contains an 
notebook explaning the topic as well as *hotwo-notebook* that summarises the most important aspects. 
Furthermore, there is an exercises folder that contains exercises according to the 4C/ID model. In the 
exercises folder there is allways an index file linking to all the available exercises. As an example consider the
topic [conditionals](/notebooks/30_conditionals). The folder contains the following files:

- [conditionals.ipynb](/notebooks/30_conditionals/conditionals.ipynb): The introduction to the topic (i.e. the lecture)
- [conditionals_howto.ipynb](/notebooks/30_conditionals/conditionals_howto.ipynb): the howto 
- [exercises](/notebooks/30_conditionals/exercises): a folder containing all the exercises for the topic
    - [00_conditional_exercises.ipynd](/notebooks/30_conditionals/exercises/00_conditional_exercises.ipynd): the index file for the exercises. 

All the exercises contain unittests. These test can be used by the students to check their solutions. The unit test have been created using 
[nose](https://nose.readthedocs.io/en/latest/). Futhermore, all the exercises contain the annotations required by 
[nbgrader](https://nbgrader.readthedocs.io/en/stable/).

# Todos
- After the first semester teaching whith these notebooks it became clear that some of the exercises require some rework. Currently, the explanation of the task is not always clear enough.
- Translate the notebooks and exercises.
# Acknowledgements 
The work on this material has been supported by 

- The SQSL-Project of the FH Aachen: https://www.fh-aachen.de/en/hochschule/projekt-sqsl/
- The [Stifterverband](https://www.stifterverband.org/) in the context of a *Senior-Fellowship für Innovationen in der digitalen Hochschullehre*: https://www.stifterverband.org/digital-lehrfellows-nrw/2019/drumm
