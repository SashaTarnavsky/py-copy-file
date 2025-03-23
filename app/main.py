import os


def copy_file(command: str) -> None:
    parts = command.split()

    # Перевіряємо, що команда має правильний формат: 'cp source target'
    if len(parts) != 3 or parts[0] != "cp":
        return

    source, target = parts[1], parts[2]

    # Якщо джерело і цільове ім'я однакові, нічого не робимо
    if source == target:
        return

    # Перевіряємо, чи існує вихідний файл
    if not os.path.exists(source):
        return

    # Копіюємо файл
    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
