# ADM HW2 - Group 28

## Introduction
This repository represents the solutions for the second homework of the *ADM* course. The solution for each question is written in a separate file which can be recognized by its name. <br> 
The codes are developed by **Group #28** with the following members:<br>

Luca Mazzucco, 1997610<br>
Nemish Murawat, 2056142<br>
Giacomo Vittori, 1811571<br>
Sara Zeynalpour, 1997862<br>

The subject of this homework is 3 data sets collected from *Instagram* representing posts, profiles, and locations in three different *.csv* files. Considering the sheer volume of the data, all the solutions were developed on *AWS SageMaker*, over the *Jupyter Notebook* platform, and by using *Python* language.<br>
Here is the list of data sets used in this project which are already mounted on *AWS*:
- *Instagram* posts data: [instagram_posts.zip](https://adm2022.s3.amazonaws.com/instagram_posts.zip)
- *Instagram* profiles data: [instagram_profiles.zip](https://adm2022.s3.amazonaws.com/instagram_profiles.zip)
- *Instagram* locations data: [instagram_locations.zip](https://adm2022.s3.amazonaws.com/instagram_locations.zip)


## Contents
**Individual_Code_Files/RQ1 - RQ8** :<br> The solutions for RQ1 to RQ8, written in Python. <br>
Caveat: As mentioned before, these codes were developed on *AWS SageMaker*, therefor to run the .ipynb files without error, the needed datasets are addressed in *Data* folder like: '/home/ec2-user/SageMaker/Data/instagram_posts.csv'. <br>

**Individual_Code_Files/Bonus A,Bonus B,Bonus C**:<br> The solutions for all three bonus points. Again the same caveat is valid for these files as well. <br>

**CommandLine.sh** :<br> The solution to the command line question. It is developed on Linux so to run it over Windows, [Gawk](https://gnuwin32.sourceforge.net/packages/gawk.htm) needs to be installed. The output of this shell file is represented in the **Individual_Code_files/results.rar** file.

**Individual_Code_Files/AQ1,AQ2**:<br> Solutions for both algorithmic questions, written in notebooks. Both the needed codes and pseudocodes are written there. <br>

**Main.ipynb**:<br> This contains the combined Jupyter Notebooks for the all the questions[*RQ1-RQ8*,*BonusA-BonusB*,*AQ1-AQ2*]. In case of some discrepeancy please refer the individual notebooks present in the *Individual_Code_files* folder.

**pre_processing_posts.py,
pre_processing_profiles.py**:<br> These are the python functions used in some parts of the questions for pre-processing the data(dealing with NAN values and it's replacement). Again, this is not the standard adopted in the main.ipynb. Used when applicable.

