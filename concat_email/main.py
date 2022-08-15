from multiline_input import get_minput
import pyperclip


def main():
    names = get_minput("Input name: ")

    pyperclip.copy(name_to_email(names).lower())


def name_to_email(arr):
    final_str = ""
    for item in arr:
        name_arr = item.split(" ")
        final_str = final_str + f"{name_arr[0]}{name_arr[-1]}.s@narada.sch.id "
    
    return final_str


if __name__ == "__main__":
    main()