def mbti_personality_test():
    print("---------------------------")
    print("MBTI Personality Test")
    print("---------------------------")

    name_response = input("What is your name? ")

    choices = [
        "1. (A) Expand energy, enjoy groups  \n(B)Conserve energy, enjoy one-on-one",
        "2. (A) Interpret literally \n(B) Look for meaning and possibilities",
        "3. (A) Logical thinking, questioning  \n(B)Empathetic, feeling, accommodating",
        "4. (A) Organized, orderly \n(B) Flexible, adaptable",
        "5. (A) More outgoing, think out loud \n(B)More reserved, think to yourself",
        "6. (A) Practical, realistic, experiential \n(B)Imaginative, innovative, theoretical",
        "7. (A) Candid, straightforward, frank  \n(B)Tactful, kind, encouraging",
        "8. (A) Plan, schedule \n(B)Unplanned, spontaneous",
        "9. (A) Seek many tasks, public activities, interaction with others \n(B)Seek private, solitary activities       		   with quiet to concentrate",
        "10. (A) Standard, usual, conventional \n(B)Different, novel, unique",
        "11. (A) Firm, tend to criticize, hold the line \n(B)Gentle, tend to appreciate, conciliate",
        "12. (A) Regulated, structured  \n(B)Easy-going, live and let live",
        "13. (A) External, communicative, express yourself \n(B)Internal, reticent, keep to yourself",
        "14. (A) Focus on task, achievement \n(B)Sensitive, people-oriented, compassionate",
        "15. (A) Tough-minded, just \n(B)Tender-hearted, merciful",
        "16. (A) Preparation, plan ahead \n(B)Go with the flow, adapt as you go",
        "17. (A) Active, initiate \n(B)Reflective, deliberate",
        "18. (A) Facts, things, what is \n(B)Ideas, dreams, what could be, philosophical",
        "19. (A) Matter of fact, issue-oriented \n(B)Sensitive, people-oriented, compassionate",
        "20. (A) Control, govern \n(B)Latitude, freedom"
    ]

    categories = [
        "EI", "SN", "TF", "JP", "EI", 
        "SN", "JP", "EI", "EI", "SN", 
        "TF", "JP", "EI", "SN", "TF", 
        "JP", "EI", "JP", "TF", "JP"
    ]

    score = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    count_a = 0
    count_b = 0

    for i, question in enumerate(choices):
        while True:
            print(question)
            answer = input("Your answer (A/B): ").strip().upper()
            if answer in ["A", "B"]:
                if answer == "A":
                    count_a += 1
                    category = categories[i]
                    score[category[0]] += 1
                else:
                    count_b += 1
                    category = categories[i]
                    score[category[1]] += 1
                break
            else:
                print("Invalid input. Please answer A or B.")

    personality_type = ""
    personality_type += "E" if score["E"] > score["I"] else "I"
    personality_type += "S" if score["S"] > score["N"] else "N"
    personality_type += "T" if score["T"] > score["F"] else "F"
    personality_type += "J" if score["J"] > score["P"] else "P"

    traits = {
        "ISTJ": "The Inspector - Practical, fact-minded, and reliable.",
        "ISFJ": "The Protector - Caring, loyal, and hardworking.",
        "INFJ": "The Advocate - Insightful, creative, and idealistic.",
        "INTJ": "The Mastermind - Strategic, logical, and independent.",
        "ISTP": "The Virtuoso - Bold, practical, and experiment-oriented.",
        "ISFP": "The Adventurer - Flexible, charming, and artistic.",
        "INFP": "The Mediator - Empathetic, imaginative, and driven by values.",
        "INTP": "The Thinker - Analytical, curious, and innovative.",
        "ESTP": "The Entrepreneur - Energetic, spontaneous, and action-oriented.",
        "ESFP": "The Entertainer - Sociable, enthusiastic, and fun-loving.",
        "ENFP": "The Campaigner - Optimistic, curious, and enthusiastic.",
        "ENTP": "The Debater - Witty, innovative, and intellectually curious.",
        "ESTJ": "The Executive - Organized, outgoing, and leader-like.",
        "ESFJ": "The Consul - Supportive, caring, and people-oriented.",
        "ENFJ": "The Protagonist - Inspiring, empathetic, and charismatic.",
        "ENTJ": "The Commander - Strategic, confident, and ambitious."
    }

    description = traits.get(personality_type, "Unknown Personality Type")

    print("---------------------------")
    print(f"Hello, {name_response}!")
    print(f"Your MBTI Personality Type is: {personality_type}")
    print(description)
    print("---------------------------")
    print(f"Total 'A' selections: {count_a}")
    print(f"Total 'B' selections: {count_b}")


mbti_personality_test()
