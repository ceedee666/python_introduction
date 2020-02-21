# Anleitung zur Installation von Nbgrader
- Jupyterhub einrichten:
  - Um The littlest Jupyterhub einzurichten über Amazon Web Services einfach dieses Tutorial genau befolgen: https://tljh.jupyter.org/en/latest/install/amazon.html
- Nbgrader installieren:
  - das Terminal öffnen (oben rechts new -> terminal)
  - sudo -E pip install -U nbgrader
  - sudo -E jupyter nbextension install --py nbgrader --overwrite
  - sudo -E jupyter nbextension enable --py nbgrader 
  - sudo -E jupyter serverextension enable --py nbgrader
- Die Assignment-Funktion für Studenten aktivieren:
  - sudo jupyter nbextension enable --sys-prefix assignment_list/main --section=tree
  - sudo jupyter serverextension enable --sys-prefix nbgrader.server_extensions.assignment_list
  - sudo jupyter nbextension enable --sys-prefix validate_assignment/main --section=tree
  - sudo jupyter serverextension enable --sys-prefix nbgrader.server_extensions.validate_assignment
- Den Austauschordner anlegen
  - über das Terminal in den Ordner srv navigieren (2x „cd ..“ um in den übergeordneten Ordner zu gelangen. Dann „cd srv“)
  - dort den Ordner „nbgrader“ anlegen (sudo mkdir nbgrader)
  - in diesen navigieren (cd nbgrader)
  - dort den Ordner „exchange“ anlegen (sudo mkdir exchange)
  - allen Nutzern die Zugriffsrechte auf diesen Ordner geben (sudo chmod ugo+rw exchange)
- nbgrader_config.py erstellen:
  - navigiere im terminal zu ~/.jupyter
  - erstelle die Datei als Admin (sudo nano nbgrader_config.py) mit folgendem Inhalt: <br>
    `c = get_config()`<br>
    `c.CourseDirectory.root = '/home/jupyter-adminname/kursname'`
  - Editor verlassen mit strg+x, speichern mit y und enter
  - erstelle einen leeren Ordner "migrated" (sudo mkdir migrated)
  - erteile Zugriffsrechte auf den Ordner "migrated" (sudo chmod ugo+rw migrated)
- Den Kursordner anlegen
  - nbgrader quickstart *kursname*
  - den Ordner "ps1" und den Header löschen. So dass "source" leer ist
- Nbgrader_config.py anpassen im Kursordner
  - Über das normale Interface in den Ordner navigieren
  - Die Datei nbgrader_config.py ändern: <br>
          `c = get_config()`<br>
          `c.CourseDirectory.course_id = "kursname"`<br>
          `c.CourseDirectory.db_assignments = [dict(name="aufgabenname"),`<br>
                                              `(name="aufgabenname2")]`<br>
          `c.CourseDirectory.db_students = [dict(id="jupyter-Studentenkürzel"),`<br>
                                           `(id="jupyter-Studentenkürzel2")]`<br>
- Instanz rebooten über AWS (rechtsklick auf Instanz -> Instance State -> Reboot)
----                                      
                                   
### Studenten hinzufügen
- Den Formgrader öffnen
- "Manage Students" -> "Add new student..."
- bei der "Student ID" **unbedingt darauf achten** "jupyter-" vor das Studentenkürzel zu schreiben
- Alternativ zu diesen ersten drei Schritten um einzelne Studenten hinzuzufügen, kann man eine CSV-Datei importieren:
  - Dazu eine CSV Datei in folgendem Format hochladen: <br>
    `id,last_name,first_name,email`<br>
    `ab1234s,Buerger,Anton,anton.buerger@alumni.fh-aachen.de`<br>
    `mm4321s,Mustermann,Max,max.mustermann@alumni.fh-aachen.de`<br>
    
*Die folgenden Schritte müssen **zusätzlich** erledigt werden:*
- Im Kursordner in der "nbgrader_config.py" den Studenten auch hinzufügen, wieder mit "jupyter-" vor dem Studentenkürzel
- Das Control Panel öffnen (oben rechts)
- "Admin" -> Add Users" (Hier darauf achten nur das Studentenkürzel in das Feld zu schreiben. Kein "jupyter-" oder sonstige Angaben)
----
### Aufgaben hinzufügen
- Zunächst darauf achten, dass die Notebooks für nbGrader lesbar sind:
  - Innerhalb des Notebooks "View" -> "Cell Toolbar" -> "Create Assignment" auswählen
  - Dann für jede Zelle bestimmen was mit dem Inhalt geschieht (rechts oben in der jeweiligen Zelle im Dropdown-Menü):
    - Read only -> Der Student kann die Zelle nicht bearbeiten (sinnvoll für Aufgabenstellungen)
    - Autograded answer -> Innerhalb dieses Feldes soll die Aufgabe bearbeitet werden
    - Autograder tests -> In dieser Zelle befindet sich ein oder mehrere Tests für das Programm 
- Den Formgrader öffnen
- "Add new assignment"
- Namen und Abgabedatum (optional) eingeben 
- Bei der neu erstellten Aufgabe auf den Namen klicken um in den Ordner zu gelangen
- Die Datei dort hochladen
- Im Kursordner in der "nbgrader_config.py" die Aufgabe hinzufügen
- Im Formgrader den "generate assignment"-Button anklicken

- Zur veröffentlichung den "Release"-Button anklicken
- Zum einholen der bearbeiteten Notebooks den "Collect"-Button anklicken
- Zur automatischen Bewertung: Terminal öffnen -> sudo nbgrader autograde aufgabenname
----
### Als Student Jupyterhub nutzen
- Bei erstmaligem anmelden mittels Studentenkürzel, legt der Student selbst das Passwort fest
- Über den Reiter Assignments gelangt man zu den zu erledigenden Aufgaben
- Mittels fetch kann man diese auf den eigenen Account einholen
- Dann einfach online bearbeiten und per submit absenden
----
#### nützliche Unix Befehle:
- ls -> Ordner und Dateien anzeigen
- ll -> Write, Read, Execute Berechtigungen anzeigen
- sudo -> Befehl als admin ausführen
- mkdir -> Ordner anlegen
- nano -> Datei anlegen und beschreiben mit Editor
- less -> Dateiinhalt anzeigen
- rm -> löschen
- rm -r -> rekursiv löschen (für Ordner)
- cd -> zu Ordner wechseln
- cd .. -> Ordner verlassen
- sudo journalctl -u jupyterhub -> Logfiles des Jupyterhub einsehen
- sudo journalctl -u jupyter-*Username*  -> Logfiles eines Users einsehen
  - in Logfiles mit Pfeiltasten navigieren, beenden mit "!"
- Sollten nbgrader Befehle (auf der Webseite nachzulesen) nicht funktionieren, probiere: source .profile
