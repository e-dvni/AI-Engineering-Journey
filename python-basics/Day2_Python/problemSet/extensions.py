def fileType():
    audio = [".aac", ".mid", ".midi", ".mp3", ".oga", ".opus", ".wav", ".weba"]
    application = [".abw", ".arc", ".bin", ".azw", ".bz", ".bz2", ".cda", ".csh", ".doc", ".docx", ".eot", ".epub", ".gz", ".jar", ".json", ".jsonld", ".mpkg", ".odp", ".ods", ".odt", ".ogx", ".pdf", ".php", ".ppt", ".pptx", ".rar", ".rtf", ".sh", ".tar", ".vsd", ".webmanifest", ".xhtml", ".xls", ".xlsx", ".xml", ".xul", ".zip"]
    image = [".apng", ".avif", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".tif", ".tiff", ".webp"]
    font = [".otf", ".ttf", ".woff", ".woff2"]
    text = [".css", ".csv", ".html", ".ics", ".js", ".md", ".mjs", ".txt"]
    video = [".avi", ".mp4", ".mpeg", ".ogv", ".ts", ".webm"]

    fileName = input("File name: ")

    global dot
    dot = fileName.rfind('.')

    for ext in audio:
        if ext in fileName:
            if dot != -1:
                print("audio/" + fileName[dot+1:])
            else:
                print("audio/")
            break

    for ext in application:
        if ext in fileName:
            if dot != -1:
                print("application/" + fileName[dot+1:])
            else:
                print("application/")
            break
    
    for ext in image:
        if ext in fileName:
            if dot != -1:
                print("image/" + fileName[dot+1:])
            else:
                print("image/")
            break

    for ext in font:
        if ext in fileName:
            if dot != -1:
                print("font/" + fileName[dot+1:])
            else:
                print("font/")
            break

    for ext in text:
        if ext in fileName:
            if dot != -1:
                print("text/" + fileName[dot+1:])
            else:
                print("text/")
            break

    for ext in video:
        if ext in fileName:
            if dot != -1:
                print("video/" + fileName[dot+1:])
            else:
                print("video/")
            break

fileType()