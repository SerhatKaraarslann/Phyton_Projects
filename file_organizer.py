import os
import shutil

def organize_files(directory_path):
    """
    Organisiert Dateien in einem gegebenen Verzeichnis basierend auf ihren Dateiendungen.
    
    Args:
        directory_path (str): Der Pfad zu dem Verzeichnis, das organisiert werden soll.
    """
    
    extensions = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'], # WebP hinzugefügt
        'documents': ['.pdf', '.docx', '.txt', '.odt', '.rtf', '.tex'], # Weitere Doku-Formate
        'videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'], # Weitere Video-Formate
        'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'], # Weitere Audio-Formate
        'archives': ['.zip', '.rar', '.tar', '.gz', '.7z'], # Weitere Archiv-Formate
        'scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'], # Shell-Skripte und CSS
        'spreadsheets': ['.xlsx', '.csv', '.ods'], # OpenDocument Spreadsheet
        'presentations': ['.pptx', '.key', '.odp'], # OpenDocument Presentation
        'code': ['.java', '.c', '.cpp', '.cs', '.php', '.go', '.rb', '.json', '.xml'], # Weitere Code-Formate
        'fonts': ['.ttf', '.otf', '.woff', '.woff2'], # Web-Fonts
        'miscellaneous': [] # Für alles, was nicht zugeordnet werden kann
    }

    if not os.path.isdir(directory_path):
        print(f"Fehler: Das Verzeichnis '{directory_path}' existiert nicht oder ist kein Verzeichnis.")
        return

    print(f"Starte die Organisation von Dateien in: '{directory_path}'")

    for filename in os.listdir(directory_path):
        source_path = os.path.join(directory_path, filename)

        # Überspringe Verzeichnisse
        if os.path.isdir(source_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower() # Endung in Kleinbuchstaben

        found_category = 'miscellaneous'
        for category, exts in extensions.items():
            if file_extension in exts:
                found_category = category
                break
        
        destination_folder = os.path.join(directory_path, found_category)
        
        # Erstelle den Zielordner, falls er noch nicht existiert
        try:
            os.makedirs(destination_folder, exist_ok=True)
        except OSError as e:
            print(f"Fehler beim Erstellen des Ordners '{destination_folder}': {e}")
            continue # Springe zur nächsten Datei, wenn Ordner nicht erstellt werden kann

        destination_path = os.path.join(destination_folder, filename)
        
        # Überprüfe, ob die Datei am Ziel bereits existiert und vermeide Überschreiben
        if os.path.exists(destination_path):
            print(f"Warnung: '{filename}' existiert bereits in '{found_category}/'. Überspringe.")
            continue

        try:
            shutil.move(source_path, destination_path)
            print(f"Verschoben: '{filename}' nach '{found_category}/'")
        except shutil.Error as e:
            print(f"Verschiebefehler für '{filename}': {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler beim Verschieben von '{filename}': {e}")

if __name__ == "__main__":
    # Standardmäßig das Downloads-Verzeichnis des Benutzers nehmen
    # Du könntest auch ein Argument für das Verzeichnis hinzufügen
    downloads_dir = os.path.expanduser('~/Downloads') 
    organize_files(downloads_dir)
    print("\nDateiorganisation abgeschlossen!")