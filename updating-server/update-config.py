def update_server_config(file_path, key, value):
    updated = False
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                # Update the existing key with the new value
                file.write(f"{key} = {value}\n")
                updated = True
            else:
                file.write(line)

        # If the key is not present, add it to the end of the file
        if not updated:
            file.write(f"{key} = {value}\n")

# Example usage
update_server_config("server.config", "MAX_CONNECTIONS", "900")
