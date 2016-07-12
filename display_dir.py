
class Display_Dir:
    def getM(object):
        rtn = ''
        cnt = 0
        for m in dir(object):
            if cnt <= 5:
                rtn += str(m) + ', '
            else:
                cnt = 0
                rtn += '\n' + str(m)
            cnt += 1
        print(rtn)