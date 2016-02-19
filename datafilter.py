import re
import string

pronouns = ['I', 'me', 'we', 'us', 'you',
            'she', 'he', 'her', 'him', 'it', 'they', 'them',
            'this', 'that', 'those', 'these']

def concatStrings(strings):
    result = ""
    for strng in strings:
        result += " " + strng
    return result

def filterString(strng, filterList):
    result = ""
    for word in strng.split():
        keep = True
        for filt in filterList:
            if word == filt:
                keep = False
                break
        if keep:
            result += " " + word
    return result

def removeHTMLTags(strng):
    re.sub('<[^<]+?>', '', strng)
    return strng


regex = re.compile('[%s]' % re.escape(string.punctuation))
def removePunctuation(strng):
    return regex.sub('', strng)




testSpeech = ["Two hours after she left, I felt great. I had no pain when I woke up the next morning, and that evening,",
             "all of my test results were positive. A miracle? Actually, yes. Study after study has indicated that " ,
             "humor has interesting healing powers. One way that humor can help to heal is that it literally " ,
             "changes our outlook on life. As we laugh, we have trouble seeing life's difficulties the same way." ,
             " Suddenly, our problems don't seem quite as bad. Humor allows one to distance him/herself from a painful",
             " physical or medical situation while also acknowledging that he or she is in such a situation. This " ,
             "change in perspective is a powerful healing force. Distancing yourself from a distressing situation " ,
             "allows you to view certain circumstances from a more objective perspective, and this can help you " ,
             "extract powerful emotions that focus on your pain or sorrow. In doing this, you do not reject the " ,
             "painful circumstances surrounding you, but acknowledge the reality of your situation - the good with" ,
             " the bad Recent mental health studies have shown that laughter can stimulate areas of the brain that" ,
             " release endorphins, helping us to see our situation more clearly. The benefits of humor, though, " ,
             "aren't all mental. Humor triggers laughter. According to physiological studies, the laughter, in turn, " ,
             "stimulates our cardiovascular systems by increasing the rate at which the heart beats and contracting " ,
             "the muscles. In fact, one study suggested that laughing one hundred times per day is the equivalent" ,
             " of spending ten minutes on a rowing machine. One study went so far as to suggest that the benefits " ,
             "of laughter reach far beyond our body system. Laughter reduces levels of certain stress hormones " ,
             "which suppress the immune system and increase the number of blood platelets - which can cause " ,
             "obstructions in arteries, and raise blood pressure, said one researcher. When we're laughing, natural" ,
             " killer cells that destroy cancer cells increase, as does the level of Gamma-interferon - a " ,
             "disease-fighting protein, T-cells - a major part of the immune system, and B-cells - which make " ,
             "disease-destroying antibodies. Laughter may also increase the concentration of salivary immunoglobulin " ,
             "A, which defends against infectious organisms entering through the respiratory tract so it helps us to " ,
             "resist colds and viruses. That makes quite a case of the adage A barrel of laughs a day keeps the " ,
             "doctor away. The healing power of humor is wide-ranging in scope and situation. Though medically," ,
             " the interesting healing powers of humor are still being studied by many scientists, humor clearly" ,
             " heals the spirit - a part of every one of us which is often neglected by medicine and science. Seeing",
             " the humor in our painful or emotional situations can free us from the chains we have built around" ,
             " ourselves, helping us to recognize that life is more than anger or pain or sorrow, but that it is " ,
             "full of humor and the contagious sound of laughter"]

testlong = concatStrings(testSpeech)
testlong = removePunctuation(testlong)
testlong = filterString(testlong, pronouns)
print(testlong)












