import random

# Example questions for each level
questions = {
    "Kmet": [
        ("\33[92mKateri je najmanjši planet v našem sončnem sistemu?", "Merkur"),
        ("\33[92mKateri planet je znan kot Rdeči planet?", "Mars"),
        ("\33[92mKateri planet ima največ lun?", "Saturn"),
    ],
    "Meščan": [
        ("\33[92mKateri planet je znan po svojih prstanih?", "Saturn"),
        ("\33[92mKateri je najbolj vroč planet v našem sončnem sistemu?", "Venera"),
        ("\33[92mKateri planet je znan po veliki rdeči pegi?", "Jupiter"),
    ],
    "Kralj": [
        ("\33[92mKateri je pritlikavi planet?", "Pluton"),
        ("\33[92mKateri planet se vrti na svoji strani?", "Uran"),
        ("\33[92mKateri planet ima dan daljši od svojega leta?", "Venera"),
    ],
    "Kadet": [
        ("\33[92mKatera je najsvetlejša zvezda na nočnem nebu?", "Severnica"),
        ("\33[92mKatera galaksija je najbližja Mlečni cesti?", "Andromena"),
    ],
    "Astronaut": [
        ("\33[92mKoliko zvezd vsebuje Rimska cesta?", "200" or "300" or "400"),
        ("\33[92mKako se imenuje supermasivna črna luknja naše galaksije?", "Sagitarija"),
        ("\33[92mKakšna je teorija, ki opisuje zgodnji razvoj vesolja?", "Veliki pok"),
    ]
}

# Level names
levels = ["Kmet", "Meščan", "Kralj", "Kadet", "Astronaut"]

def ask_question(question):
    print(question[0])
    user_answer = input("\33[92mOdgovor: ").strip()
    return user_answer.lower() == question[1].lower()

def main():
    print("\33[92mDobrodošel \33[92mv \33[92mGalactic \33[92mChallenge!")

    for i, level in enumerate(levels):
        if level in questions and questions[level]:
            print(f"\33[92mLevel {i + 1}: {level}")

            level_questions = questions[level]
            random.shuffle(level_questions)

            for question in level_questions:
                if ask_question(question):
                    print("\33[92mPravilno!")
                else:
                    print("\33[92mNarobe. Pravilni odgovor je:", question[1])
                    print("\33[92mIgre je konec. Poskusi ponovno!")
                    return
            print("\33[92mČestitke! Naredil si level.", level)
        else:
            print(f"\33[92mNi uprasanj '{level}'. Nedokoncana igra.")
            break
    else:
        print("\33[92mČestitke! Si pravi galastični raziskovalec!")

if __name__ == "__main__":
    main()
