__author__ = 'yuyue'


def solution(s):
    maxlen = 1
    maxi = maxj = 0
    length = len(s)
    table = [[None for i in range(length)] for j in range(length)]
    for i in range(length - 1):
        table[i][i] = True
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            maxlen = 2
            maxi = i
            maxj = j
        else:
            table[i][i + 1] = False
    table[length - 1][length - 1] = True
    for i in range(2, length):
        for j in range(length - i):
            table[j][j + i] = (table[j + 1][j + i - 1] and (s[j] == s[j + i]))
            if table[j][j + i] == True and (i + 1) > maxlen:
                maxlen = i + 1
                maxi = j
                maxj = j + i
    return s[maxi:maxj + 1]


print solution('"kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"')
