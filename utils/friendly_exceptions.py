""" This module contains functions to provide 
    beginner-friendly error messages for exceptions."""

def msg(e):
    """ This function returns some explanations to typically
        exceptions encountered by beginners. In particular some
        hints on how to remove the root cause is given"""

    if type(e).__name__ == "NameError":
        return "Es wurde eine Exception vom Type {} ausgelöst.\nStellen Sie sicher, dass die Namen der von Ihnen verwendeten Funktionen korrekt sind.\nEvtl. müssen Sie die Zelle, in der Ihre Funktion definert ist, neu ausführen.".format(type(e).__name__)

    elif type(e).__name__ == "UnboundLocalError":
        return "Es wurde eine Exception vom Type {} ausgelöst.\nStellen Sie sicher, dass alle Variable vor ihrer Verwendung korrekt initialisiert werden.".format(type(e).__name__)

    elif type(e).__name__ == "NotImplementedError":
        return "Bitte entfernen Sie die Zeile \"raise NotImplementedError()\" aus Ihrer Lösung."
    else:
        return "Eine Exception vom Typ {} ist aufgetreten.\nDie Ursache hier war: {}".format(type(e).__name__, str(e))
