import time  # for receive_messages and slow_print()
import sys  # for slow_print()

# ------- variables and constants -------

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", "?", "!", "°"]

codes = {
    1: ["b", "c", "d", "f", "g", "#", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
        "x", "y", "z", "a", "9", "8", "7", "6", "5", "4", "3", "2", "1", ")", ":", "?", "!", "°"],

    2: ["+", "#", "&", "$", "l", "(", "°", "*", "<", "v", "d",
        "/", "|", "J", "f", "t", "w", "y", "x", "z", "h", "k",
        ":", "m", "n", "c", "4", "2", "3", "1", "0", "6", "5", "9", "8", "7", ")", "?", "!", "€"],

    3: ["c", "z", "i", "j", "l", "Z", "0", "t", "r", "x", "y",
        "b", "d", "g", "k", "e", "q", "s", "u", "5", "1", "2",
        "a", "f", "h", "G", "n", "o", "v", "w", "4", "3", "6", "8", "9", "7", ":", "?", "!", "°"],

    4: ["&", "#", "b", "a", "P", "M", "°", "V", "D", "v", "d",
        "/", "§", "K", "f", "t", "w", "g", "x", "z", "h", "k",
        "l", ":", "n", "c", "5", "2", "7", "4", "0", "X", "q", "9", "8", "S", "T", "?", "!", "€"],

    5: ["1", "4", "7", "0", "l", "Z", "°", "*", "<", "v", "d",
        "2", "5", "8", "f", "t", "w", "y", "x", "z", "h", "k",
        "3", "6", "9", "T", "q", "e", "#", "P", "o", "g", "a", "r", "u", ":", "U", "?", "!", "€"],
}


def slow_print(string: str, speed: float = 0.05) -> None:
    """
    Print the string on the console with a specific writing speed.
    Speed is adjustable.
    Warning: No new line after printing!

    Parameters
    ----------
    string : str
        Text to print
    speed : float, optional
        printing speed, by default 0.05
    """
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def receive_messages() -> list[str]:
    '''
    Connect to a Server and receive secret messages.

    Returns
    -------
    list[str]
        encoded messages.
    '''
    messages = ["1°l8z xt1yd2lU *122f zl15, 0y<8°l80l 5l20h8°!",
                "+°lJz &*h&d/l|+xzly) :+x °<#z'x, xt+yd/l?",
                "c0lg5 uecsybl: jrl zöularit5l tczlg lrgl brlZls1g0 yr5Glb0cu 0lu5ktblg. url ebcglg, jrl alb5 dr5 bcitcgZäbblg G1 üzlsgltdlg!",
                "bhgou divdlmgnbtugs: gsotuib#u? ljuagmhbt?",
                "&°PKz xt&gd/PT v&, xDP V&#PK PDKPK dDzcP/d&KfKPKdfaP: PKzlDbdP/z. lDg §üxxPK xDP &hMV&/zPK, #Pkfg aDP lP/z DK VnxzPgDxbVPx °P/äbVzPg &hx#gDbVz.",
                "&°PKz bVhbd/P§&xzPgT DbV lPgaP aDP /&bV&#lPVgzghttP &dzDkDPgPK. lf °PK&h xDKa aDP #öxPlDbVzP?",
                "1°l8z xt1yd2lU dffy0<81zl8 o#.:ura€ 8, ru.ru:q€ 3. <8 0ly 8ä*l 0lx xt1ßkh2d18-21°lyx.",
                "+°lJz &*h&d/l|+xzly) fd+n, :<y #y+h&*lJ $<l +Jz<-d<zcl/-|+xdlJ. $<l |<z $lJ °h||<*ü*JlyJ, y<&*z<°?",
                "bhgou tqbslmg: hgobv, vof wgshjtt fjg dmpxoobtgo ojdiu. fbt ljuagmhbt jtu gsotuib#u botugdlgof.",
                "c0lg5 it1iybldcu5ls: bcuu5 1gu jcu bcitlg zllgjlg, zl2ks lu c1ßls ykg5skbbl 0lsä5. uecß5s1ee, c1Z 0lt5'u!",
                "+°lJz xt+yd/l) |ö°l $ly *h|fy |<z hJx xl<J!"
                ]

    # connect to server
    slow_print("Try To Connect To Server\n")
    slow_print("...\n", speed=0.5)

    slow_print("Connection Successful!\n")
    time.sleep(1)

    # Load messages
    slow_print("\nLoad Messages\n")
    slow_print("...\n", speed=0.5)
    slow_print("Messages Loaded!\n")

    # return messages
    return messages


# ---------- Write Your Code Here ----------

def decode(encrypted_text: str, key: int, codeset: dict[int, list[str]], alphabet: list[str]) -> str:
    """
    Decode a given encrypted text using the specified key and codeset.

    Parameters
    ----------
    encrypted_text : str
        The encrypted text to decode.
    key : int
        The key used for decoding.
    codeset : dict[int, list[str]]
        The dictionary containing the codes for decryption.
    alphabet : list[str]
        The original alphabet list.

    Returns
    -------
    str
        The decoded text.
    """
    code = codeset[key]
    decoded_text = ""

    for char in encrypted_text:
        if char in code:
            decoded_text += alphabet[code.index(char)]
        else:
            decoded_text += char

    return decoded_text


def find_key(encrypted_text: str, codeset: dict[int, list[str]], alphabet: list[str]) -> int:
    """
    Find the key that can decode the given encrypted text.

    Parameters
    ----------
    encrypted_text : str
        The encrypted text for which to find the key.
    codeset : dict[int, list[str]]
        The dictionary containing the codes for decryption.
    alphabet : list[str]
        The original alphabet list.

    Returns
    -------
    int
        The key that can decode the encrypted text.
    """
    for key in codeset:
        decoded_text = decode(encrypted_text, key, codeset, alphabet)
        if decoded_text.startswith("agent"):
            return key
    return -1  # Return -1 if no key is found


def decode_messages(messages: list[str], codeset: dict[int, list[str]], alphabet: list[str]) -> list[str]:
    """
    Decode a list of encrypted messages.

    Parameters
    ----------
    messages : list[str]
        The list of encrypted messages.
    codeset : dict[int, list[str]]
        The dictionary containing the codes for decryption.
    alphabet : list[str]
        The original alphabet list.

    Returns
    -------
    list[str]
        The list of decoded messages.
    """
    decoded_messages = []
    for message in messages:
        key = find_key(message, codeset, alphabet)
        if key != -1:
            decoded_messages.append(decode(message, key, codeset, alphabet))
        else:
            decoded_messages.append("No valid key found for this message.")
    return decoded_messages


def print_messages(messages: list[str]) -> None:
    """
    Print a list of messages to the console.

    Parameters
    ----------
    messages : list[str]
        The list of messages to print.
    """
    for message in messages:
        slow_print(message + "\n", 0.01)


def main() -> None:
    """
    The main function to execute the decryption process.
    """
    encrypted_messages = receive_messages()
    decoded_messages = decode_messages(encrypted_messages, codes, ALPHABET)
    print_messages(decoded_messages)


# ---------- End of Your Code --------------

if __name__ == "__main__":
    main()  # run script, if it's top-level execution
