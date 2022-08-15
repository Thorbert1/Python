import pyperclip
from datetime import datetime
import time

forbidden = [
    "@rahmay_24",
    "@belajarmandarin.id",
    "@belajarmandarin.id",
    "@sinotif.official",
    "@sinotif.official",
    "@sinotif.official",
    "@excellentstudycentre",
    "@excellentstudycentre"
]

cur_hour = datetime.now().time().hour

preset = """\
{1}

Selamat {0} kak, saya Thorbert Anson Shi dari OSIS SMA Narada. Saya cukup terkesan melihat produk-produk yang dijual oleh {1} karena kelihatannya menarik dan berkualitas tinggi.

Namun, sepertinya ada banyak calon pelanggan yang tertarik dengan produk-produk {1} namun belum kenal atau sadar akan keberadaan produk-produk tersebut.

Oleh karena itu, kami dari OSIS Narada ingin menawarkan kesempatan untuk mengenalkan dan memamerkan bisnis kakak pada calon-calon pelanggan tersebut melalui kerja sama sponsorship untuk acara sekolah kami pada bulan Oktober yang mendatang.

Jika kakak tertarik, saya bersedia menjelaskan tawaran-tawaran promosi dari OSIS kami dan menjelaskan proses persetujuannya. Terima kasih banyak sebelumnya 🙏"""

def main():
    unames = get_name("Username: ")
    time_sig = get_time_sig()
    final_arr = check_if_forbidden(unames, forbidden)
    print(final_arr)
    for uname in final_arr:
        pyperclip.copy(preset.format(str(time_sig), final_arr))
        time.sleep(1)


def get_name(prompt):
    names = []
    while True:
        try:
            names.append(input(prompt))
        except EOFError:
            break

    return names


def get_time_sig():
    if cur_hour >= 6 and cur_hour <= 11:
        return "pagi"
    elif cur_hour > 11 and cur_hour <= 15:
        return "siang"
    elif cur_hour > 15 and cur_hour <= 17:
        return "sore"
    elif cur_hour > 17 and cur_hour <= 23:
        return "malam"
    else:
        pass

def check_if_forbidden(arr, forbidden):
    allowed = []
    for i in range(len(arr)):
        if arr[i] not in forbidden:
            allowed.append(arr[i])
    return allowed
    
if __name__ == "__main__":
    main()