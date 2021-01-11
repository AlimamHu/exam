from time import sleep
def timer(t=int,h=int):
    for i in range(0,t*h):
        sleep(1)
        print(i,' sec','\r',end='')
        if i==t*h-1:
            print('ONE houR is finished')
