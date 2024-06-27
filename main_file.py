from sentence_generator import generate_sentence
from colorama import Fore, Style
from pynput.keyboard import Listener, Key
import os
import time
import pymorphy3


sentence = generate_sentence(10).lower()
written = ""
text = ""
now_pos = 0
print(Fore.LIGHTBLACK_EX + sentence)
fl = True
started = 0
started_time = 0
errors = 0
morph = pymorphy3.MorphAnalyzer()


def on_press(key):
    global fl, now_pos, started, started_time, errors, written
    started += 1
    if started == 1:
        started_time = time.time()
    os.system("cls")
    try:
        if key.char == sentence[now_pos]:
            if fl:
                print(Fore.WHITE + sentence[0:now_pos + 1] + Fore.LIGHTBLACK_EX + sentence[now_pos + 1:])
                written += key.char
                now_pos += 1
                if now_pos >= len(sentence) - 1:
                    print("")
                    t = time.time() - started_time
                    print(Style.RESET_ALL + "Готово! Время: " + Fore.CYAN +
                          str(round(t, 2)) + Style.RESET_ALL + " сек., точность " + Fore.CYAN +
                          str(round((1 - errors / len(sentence)) * 100, 2)) + "%" + Style.RESET_ALL + ".")
                    print("Скорость печати: " + Fore.CYAN +
                          str(round((len(sentence) / t) * 60, 2)) + Style.RESET_ALL + " слов в минуту.")
                    time.sleep(2)
                    exit(0)
            else:
                print(Fore.WHITE + sentence[0:now_pos - 1] + Fore.LIGHTRED_EX + sentence[now_pos - 1]
                      + Fore.LIGHTBLACK_EX + sentence[now_pos:])
        else:
            errors += 1
            if fl:
                written += key.char
                print(Fore.WHITE + sentence[0:now_pos] + Fore.LIGHTRED_EX + sentence[now_pos]
                      + Fore.LIGHTBLACK_EX + sentence[now_pos + 1:])
                now_pos += 1
                fl = False
            else:
                print(
                    Fore.WHITE + sentence[0:now_pos - 1] + Fore.LIGHTRED_EX + sentence[now_pos - 1] +
                    Fore.LIGHTBLACK_EX + sentence[now_pos:])
    except AttributeError:
        if key == Key.space:
            if sentence[now_pos] == " ":
                if fl:
                    print(Fore.WHITE + sentence[0:now_pos + 1] + Fore.LIGHTBLACK_EX + sentence[now_pos + 1:])
                    written += " "
                    now_pos += 1
                    if now_pos >= len(sentence) - 1:
                        print("")
                        t = time.time() - started_time
                        print(Style.RESET_ALL + "Готово! Время: " + Fore.CYAN +
                              str(round(t, 2)) + Style.RESET_ALL + " сек., точность " + Fore.CYAN +
                              str(round((1 - errors / len(sentence)) * 100, 2)) + "%" + Style.RESET_ALL + ".")
                        print("Скорость печати: " + Fore.CYAN +
                              str(round((len(sentence) / t) * 60, 2)) + Style.RESET_ALL + " слов в минуту.")
                        time.sleep(2)
                        exit(0)
                else:
                    print(Fore.WHITE + sentence[0:now_pos - 1] + Fore.LIGHTRED_EX + sentence[now_pos - 1]
                          + Fore.LIGHTBLACK_EX + sentence[now_pos:])
            else:
                errors += 1
                if fl:
                    written += " "
                    print(Fore.WHITE + sentence[0:now_pos] + Fore.LIGHTRED_EX + sentence[now_pos]
                          + Fore.LIGHTBLACK_EX + sentence[now_pos + 1:])
                    now_pos += 1
                    fl = False
                else:
                    print(
                        Fore.WHITE + sentence[0:now_pos - 1] + Fore.LIGHTRED_EX + sentence[now_pos - 1] +
                        Fore.LIGHTBLACK_EX + sentence[now_pos:])
        elif key == Key.backspace:
            if now_pos > 0:
                written = written[:-1]
                print(Fore.WHITE + sentence[0:now_pos - 1] + Fore.LIGHTBLACK_EX + sentence[now_pos - 1:])
                now_pos -= 1
                fl = True
            else:
                print(Fore.LIGHTBLACK_EX + sentence[:])
        else:
            print(Fore.WHITE + sentence[0:now_pos] + Fore.LIGHTBLACK_EX + sentence[now_pos:])

    print(written)
    print(Fore.CYAN + str(now_pos) + Style.RESET_ALL + " " +
          morph.parse("символ")[0].make_agree_with_number(now_pos).word)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()