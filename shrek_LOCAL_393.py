import random
response = open("soundclips/shrekquotes", "r").readlines()
while True:
    answer = input('What would you like to ask: ')
    if "song" in answer:
        respond = "We will play a song"
    elif "swamp" in answer:
        rad = "Get out of my swamp!", "that would be my home"
        respond = random.choice(rad)
    elif "book" in answer:
        respond = "i read a book once"
    elif "annoying" in answer:
        rad = "could you be quiet just FOR 5 MINUTES!", "two things ok?Shut..up"
        respond = random.choice(rad)
    elif "story" in answer: 
        respond= "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love, and true love's first kiss."
    elif "remind" in answer:
        respond = "its on my to do list"
    elif "princess" in answer or 'fiona' in answer:
        respond = "the princess will be up in the stairs in the highest room in the tallest tower"
    elif "hate" in answer or "mean" in answer:
        respond = "well,thats not very nice."
    
    else:
        respond = random.choice(response)
    
    print(respond)