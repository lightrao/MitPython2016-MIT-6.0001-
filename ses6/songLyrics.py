lyrics="""The Beatles were an English rock band formed in Liverpool in 1960. With a line-up comprising John Lennon, Paul McCartney, George Harrison and Ringo Starr, they are generally regarded as the most influential band of all time.[1] The group were integral to the evolution of pop music into an art form and to the development of the counterculture of the 1960s.[2] Their sound, rooted in skiffle, beat and 1950s rock and roll, incorporated elements of classical music and traditional pop in innovative ways. They also pioneered recording techniques and explored music styles ranging from ballads and Indian music to psychedelia and hard rock. As they continued to draw influences from a variety of cultural sources, their musical and lyrical sophistication grew, and they came to be seen as embodying the era's socio-cultural movements.

Led by the band's primary songwriters, Lennon and McCartney, the Beatles built their reputation playing clubs in Liverpool and Hamburg over a three-year period from 1960, initially with Stuart Sutcliffe playing bass. The core trio of Lennon, McCartney and Harrison, who had been together since 1958, went through a succession of drummers, including Pete Best, before asking Starr to join them in 1962. Manager Brian Epstein moulded them into a professional act, and producer George Martin guided and developed their recordings, greatly expanding their domestic success after their first hit, "Love Me Do", in late 1962. As their popularity grew into the intense fan frenzy dubbed "Beatlemania", the band acquired the nickname "the Fab Four", with Epstein, Martin and other members of the band's entourage sometimes given the informal title of "fifth Beatle".

The Beatles were international stars by early 1964, leading the "British Invasion" of the United States pop market and breaking numerous sales records. They soon made their film debut with A Hard Day's Night (1964). From 1965 onwards, they produced increasingly innovative recordings, including the albums Rubber Soul (1965), Revolver (1966) and Sgt. Pepper's Lonely Hearts Club Band (1967), and enjoyed further commercial success with The Beatles (also known as the "White Album", 1968) and Abbey Road (1969). In 1968, they founded Apple Corps, a multi-armed multimedia corporation that continues to oversee projects related to the band's legacy. After the group's break-up in 1970, all four members enjoyed success as solo artists. Lennon was shot and killed in December 1980, and Harrison died of lung cancer in November 2001. McCartney and Starr remain musically active.

The Beatles are the best-selling band in history, with estimated sales of over 800 million albums worldwide. They are the best-selling music artists in the US, with certified sales of over 178 million units, and have had more number-one albums on the British charts, and have sold more singles in the UK, than any other act. The group were inducted into the Rock and Roll Hall of Fame in 1988, and all four main members were inducted individually between 1994 and 2015. In 2008, the group topped Billboard magazine's list of the all-time most successful artists; as of 2019, the Beatles hold the record for most number-one hits on the Hot 100 chart with twenty. The band have received seven Grammy Awards, an Academy Award (for Best Original Song Score for the 1970 film Let It Be) and fifteen Ivor Novello Awards. They were also collectively included in Time magazine's compilation of the twentieth century's 100 most influential people.

"""

def lyrics_to_freqencies(lyrics):
    """CREATING A DICTIONARY：返回字典，该字典的键为某单词值为该单词出现的次数"""
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
    return myDict

def most_common_words(freqs):
    """USING THE DICTIONARY：返回出现次数最多的单词构成的列表及它们的出现次数"""
    if len(freqs)==0:
        return([],0)
    values=freqs.values()
    best=max(values)
    words=[]
    for k in freqs:
        if freqs[k]==best:
            words.append(k)
    return(words,best)

def words_ofen(freqs,minTimes):
    """LEVERAGING DICTIONARY PROPERTIES"""
    result=[]
    done=False
    while not done:
        temp=most_common_words(freqs)
        if temp[1]>=minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done=True
    return result

num=int(input('你要我显示出现次数大于几的字母? '))
dict=lyrics_to_freqencies(lyrics)
print(words_ofen(dict,num))
# dict={'a':1,'b':2,'c':3,'d':5,'e':4,'f':5}
# # dict=lyrics_to_freqencies(lyrics)
# print(dict)
# print(most_common_words(dict))

# s='aabbbcccddddeefffjjjggghhiijjkklllmmnnppqqddaabbccnnhh'
# print(lyrics_to_freqencies(s))

# dict={'a': 4, 'b': 5, 'c': 5, 'd': 6, 'e': 2, 'f': 3, 'j': 5, 'g': 3, 'h': 4, 'i': 2, 'k': 2, 'l': 3, 'm': 2, 'n': 4, 'p': 2, 'q': 2,'r':1,'s':0}
# print(words_ofen(dict,0))
# print(most_common_words(dict))