from random import randint
import cv2
import numpy
import test
def mode(list):
    d = {}
    for elm in list:
        try:
            d[elm] += 1
        except(KeyError):
            d[elm] = 1
    keys = d.keys()
    max = d[keys[0]]

    for key in keys[1:]:
        if d[key] > max:
            max = d[key]

    max_k = []
    for key in keys:
        if d[key] == max:
            max_k.append(key),
    return max_k[0]

t=["rock", 'paper', 'scissors']
player=False
while player==False:
	lst=test.rps()
	print("LISTTTTTT", lst)
	rnd=randint(0,2)
	computer=t[rnd]
	player=mode(lst)

#account for multiple hand positions rock=0,1 paper=4,5 scissors=2,3
	if computer=='rock':
		img = cv2.imread('rock.png',0)
		cv2.putText(img,"Opponent picked:", (30,170), cv2.FONT_HERSHEY_SIMPLEX, .70,(0,0,0),2)
		if player==1 or player==0:
			cv2.putText(img,"Tie!!!", (85,70), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		elif player==2 or player==3:
			cv2.putText(img,"You Lose!!!", (47,70), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		elif player==5 or player==4:
			cv2.putText(img,"You Win!!!", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, 0,3)
		else:
			img=cv2.imread('Harambe.jpg')

		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
	elif computer=='paper':
		img = cv2.imread('paper.png',0)
		cv2.putText(img,"Opponent picked:", (30,175), cv2.FONT_HERSHEY_SIMPLEX, .70,(0,0,0),2)
		if player==5 or player==4:
			cv2.putText(img,"Tie!!!", (95,70), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		elif player==1 or player==0:
			cv2.putText(img,"You Lose!!!", (53,70), cv2.FONT_HERSHEY_SIMPLEX, .9, 0,3)
		elif player==2 or player==3:
			cv2.putText(img,"You Win!!!", (55,70), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		else:
			img=cv2.imread('Harambe.jpg')

		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
	else:
		img = cv2.imread('scissor.png',0)
		cv2.putText(img,"O", (75,170), cv2.FONT_HERSHEY_SIMPLEX, .70,(255,255,255),2)
		cv2.putText(img,"pponent picked:", (90,170), cv2.FONT_HERSHEY_SIMPLEX, .70,(0,0,0),2)
		if player==2 or player==3:
			cv2.putText(img,"Tie!!!", (130,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		elif player==5 or player==4:
			cv2.putText(img,"You Lose!!!", (100,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		elif player==1 or player==0:
			cv2.putText(img,"You Win!!!", (105,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 3)
		else:
			img=cv2.imread('Harambe.jpg')

		cv2.imshow('image',img)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
