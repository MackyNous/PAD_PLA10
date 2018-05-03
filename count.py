
def main():
    text_file = open("test.txt", "r")
    count = 0

    for line in text_file.readlines():
        line.replace(">", " ")
        line.replace("<", " ")
        print(line)

        for word in line.split():
            word = word.lower()
            if word == 'operational':
                count = count + 1

    print("count: ", count)

    if count == 5:
        print("[*] All APIs are operational")
    else:
        print("[!] Not all APIs are operational, check https://status.planet.com")


main()
