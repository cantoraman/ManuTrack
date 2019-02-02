## Manufacturing Job Tracker

This project is aimed to provide an interface for job tracking in a manufacturing plant environment.

### Proto Persona:

Who: A CAD specialist working in a screw conveyor manufacturing plant.
 
What: She wants to send job orders from her terminal in her office to a downstairs terminal where the manufacturing takes place.
Orders are similar to these:
- send sheet metals to laser cutting
- get the ring sheets and scrap metal from the laser cutters
- send the ring sheets to hydrolic press
- bend the rings into screw flights according to the specs
- fit and weld the screw sheets to the shaft
- ship the finished product

Manufacturing workers should follow these directives and provide feedback to the design team

### User Journey:
- Editing, deleting old jobs and creating new jobs should only be done by the designers (general CRUD)
- Manufacturers can tick a job as "in progress" or "done" on their terminals
- Manufacturers can flag a job as 'problematic' and provide feedback to designers through a form
- Every action must be logged in a file and stamped with the server time
- Completed jobs should be moved to a different section on the list


### Future Extensions:
- Users may download action logs of their desired time frames in PDF format 
- System must let different designers and workers login to the system and let logged actions be in their names
- Designers may upload technical drawings and attach these to the jobs

### To Install:
1) [Directive]
2) [Directive]

### Tech:
- Python
- Django