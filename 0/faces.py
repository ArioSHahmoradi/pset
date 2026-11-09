def convert(text : str):
    text = text.replace(":)","happy")
    text = text.replace(":(","sad")
    return text


def main():
    text = input("enter a string --> ")
    result = convert(text)
    print(result)

main()