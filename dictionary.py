meme_dict = {
    "CRINGE": "Coś dziwnego, zawstydzającego, żenującego",
    "LOL": "Laugh out loud, czyli coś bardzo śmiesznego, które powoduje głośny śmiech",
    "IMO": "In my opinion, czyli według mnie...",
    "REL": "Relatable, czyli coś co już doświadczyłeś/aś w życiu lub się z tym utozsamiaż"
}

print("Witaj w programie, który tłumaczy słowa używane przez wnuki, wnuczki, młodzież. \nAby dostać definicje sloganu wystarczy napisać skrót wielkimi literami!")

word = input("Wpisz słowo, którego nie rozumiesz: ").upper()

while True:
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("nie ma w słowniku")
    
    koniec = input("czy chcesz zakończyć działanie?(y/n)")
    
    if koniec == "n":
        break
    else:
        continue
