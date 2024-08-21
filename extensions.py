# Get user file details
file_name = str(input("File Name: "))

# Only execute if the file contains an extension
if "." in file_name:

# Capture file extension
    file, extension  = file_name.rsplit(".", 1)
    file_extension = extension.lower().strip()


# Check extension
    if file == "plain" and extension == "txt":
        print("text/plain")
    elif file == "plain":
        print(f"{file_extension}/plain")
    else:

        match file_extension:
            case "jpeg" | "jpg":
                print("image/jpeg")
            case "png" | "gif" :
                print(f"image/{file_extension}")
            case "pdf" | "txt" | "zip" :
                print(f"application/{file_extension}")
            case _:
                print("application/octet-stream")

else:
    print("application/octet-stream")











