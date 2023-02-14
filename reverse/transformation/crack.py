






def main():

    with open("./enc") as f:
        cipher = f.read()
        plain_1 = "".join([ (chr( ord(cipher[i]) >> 8 )) for i in range(0, len(cipher)  )])
        plain_2 = "".join([ (chr( ord( cipher[i] ) & 255  )) for i in range(0, len(cipher))  ])
        plain = "".join( [ (plain_1[i] + plain_2[i]) for i in range(0, len(plain_1))  ]  )
        print(plain)

if __name__ == "__main__":
    main()

