from termcolor import cprint
import colorama
# Укажите путь к файлу с адресами
address_file_path = "wallets.txt"
names_file_path = "names.txt"
js_path="add_wallets_js.txt"

def line_control(file_txt):
    # Удаление пустых строк
    with open(file_txt) as f1:
        lines = f1.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        with open(file_txt, "w") as n_f1:
            n_f1.writelines(non_empty_lines)


def js_changer(addresses, names):

    with open(js_path, 'r', encoding="utf-8") as read:
        lines = read.readlines()
    key_edt = [False, False]
    # Изменяет переменную wallets
    with open(js_path, 'w', encoding="utf-8") as read:
        for line in lines:
            if "const wallets =" in line:
                line = f'	const wallets = {addresses};\n'
                key_edt[0] = True
                cprint("Адреса успешно добавлены", "green")
            if ("const names =" in line) & (len(names) > 0):
                line = f'	const names = {names};\n'
                key_edt[1] = True
                cprint("Названия успешно добавлены", "green")
            read.write(line)
    return key_edt


def main():
    colorama.init()

    line_control(address_file_path)
    line_control(names_file_path)

    # Считываем содержимое файла и создаем список адресов
    with open(address_file_path, "r") as file:
        addresses = [line.strip() for line in file]

    # Считываем содержимое файла и создаем список названий
    with open(names_file_path, "r") as file:
        names = [line.strip() for line in file]

    if len(names) == 0:
        cprint("Названия кошелей отсутствуют.", "red")

    # Меняем содержимое файла при наличии адресов
    if len(addresses) == 0:
        cprint("Добавьте адреса кошельков в файл wallets.txt", "red")
    else:
        changes = js_changer(addresses, names)

    colorama.deinit()


if __name__ == '__main__':
    main()
