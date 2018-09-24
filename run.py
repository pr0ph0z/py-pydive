from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'DistinctionBias.pdf'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile("DistinctionBias.pdf") # Set content of the file from given string.
file1.Upload()