[Setup]
AppName=Exam Kiosk
AppVersion=1.0
DefaultDirName={pf}\ExamKiosk
DefaultGroupName=Exam Kiosk
OutputDir=installer
OutputBaseFilename=ExamKiosk_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\ExamKiosk\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Exam Kiosk"; Filename: "{app}\ExamKiosk.exe"
Name: "{commondesktop}\Exam Kiosk"; Filename: "{app}\ExamKiosk.exe"

[Run]
Filename: "{app}\ExamKiosk.exe"; Description: "Launch Exam Kiosk"; Flags: postinstall nowait
