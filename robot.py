#! /usr/bin/python3

# 2017-06-22 - initial version

import pyautogui, time

ul = ( 1213, 210 )

pyautogui.PAUSE = 0.1
activetab = 'GIRLS'
activegirl = 'none'
jobscroll = 'UP'
girlscroll = 0

places = {
	"GIRLS": (78, 530),
	"JOBS": (215, 530),
	"HOBBIES": (336, 530),
	"STATS": (460, 530),
	"STATS/RESET": (875, 351),
	"RESET/okay": (412, 434),

	"GIRLS/CASSIE": (100, 206),
	"GIRLS/MIO":    (100, 303),
	"GIRLS/QUILL":  (100, 400),
	"GIRLS/SCROLL": (100, 303),
	"GIRLS/ELLE":  (100, 249),
	"GIRLS/NUTAKU":  (100, 348),
	"GIRLS/IRO":  (100, 195),
	"GIRLS/BONNIBEL":  (100, 300),
	"GIRLS/AYANO":  (100, 386),
	"GIRLS/FUMI":  (100, 242),
	"GIRLS/BEARVERLY":  (100, 343),
	"GIRLS/NINA":  (100, 441),
	"GIRLS/ALPHA": (100, 210),
	"GIRLS/PAMU":  (100, 313),
	"GIRLS/LUNA":  (100, 410),

	"JOBS/fastfood":   (328, 210),
	"JOBS/restaurant": (328, 274),
	"JOBS/lifeguard":  (328, 344),
	"JOBS/cleaning":   (328, 406),
	"JOBS/computers":  (672, 210),
	"JOBS/zoo":        (672, 274),
	"JOBS/hunting":    (672, 344),
	"JOBS/casino":     (672, 406),
	"JOBS/SCROLL": (570, 292),
	"JOBS/art":     (328, 253),
	"JOBS/movies":  (328, 322),
	"JOBS/slaying": (328, 391),
	"JOBS/wizard":  (328, 459),
	"JOBS/sports":  (672, 253),
	"JOBS/legal":   (672, 322),
	"JOBS/space":   (672, 391),
	"JOBS/love":    (672, 459),

	"GIRLS/dismiss": (893, 459),
	"GIRLS/flirt": (578, 175),
	"GIRLS/gift":  (578, 256),
	"GIRLS/date":  (578, 296),

	"HOBBIES/suave":     (350, 218),
	"HOBBIES/funny":     (350, 288),
	"HOBBIES/buff":      (350, 365),
	"HOBBIES/techsavvy": (350, 438),
	"HOBBIES/tenderness": (585, 218),
	"HOBBIES/motivation": (585, 288),
	"HOBBIES/wisdom":     (585, 365),
	"HOBBIES/badass":     (585, 438),
	"HOBBIES/smart":      (816, 218),
	"HOBBIES/angst":      (816, 288),
	"HOBBIES/mysterious": (816, 365),
	"HOBBIES/lucky":      (816, 438),

	"GIFT/PAY":       (700, 311),
	"GIFT/INCREMENT": (636, 354),
	"GIFT/NEXTPAGE":  (478, 177),
	"GIFT/shell":       (315, 232),
	"GIFT/lotion":  (315, 303),
	"GIFT/fruitbasket": (315, 371),
	"GIFT/book":        (315, 434),
	"GIFT/rose":        (467, 232),
	"GIFT/donut":       (467, 303),
	"GIFT/chocolates":  (467, 371),
	"GIFT/earrings":    (467, 434),
	"GIFT/drink":       (315, 232),
	"GIFT/cake":      (315, 303),
	"GIFT/teaset":    (315, 371),
	"GIFT/puppy":     (315, 434),
	"GIFT/flowers":   (467, 232),
	"GIFT/plushytoy": (467, 303),
	"GIFT/shoes":     (467, 371),
	"GIFT/necklace":  (467, 434),
	"GIFT/cake":      (315, 303),
	"GIFT/designerbag": (315, 232),
	"GIFT/car":         (467, 232),

	"DATE/PAY":      (700, 311),
	"DATE/GOAGAIN":  (347, 441),
	"DATE/COMPLETE": (692, 441),
	"DATE/stroll":      (370, 247),
	"DATE/movies":      (370, 310),
	"DATE/sightseeing": (370, 372),
	"DATE/beach":       (370, 437),
}

maintabs = ( "GIRLS", "JOBS", "HOBBIES", "STATS" )

giftpages = {
	"shell":       0,
	"lotion":  0,
	"fruitbasket": 0,
	"book":        0,
	"rose":        0,
	"donut":       0,
	"chocolates":  0,
	"earrings":    0,
	"drink":       1,
	"cake":        1,
	"teaset":      1,
	"puppy":       1,
	"flowers":     1,
	"plushytoy":   1,
	"shoes":       1,
	"necklace":    1,
	"cake":        1,
	"designerbag": 2,
	"car":         2,
}

giftqtys = ( 1, 5, 10, 25, 50, 100, 1000, 10000 )

girlpages = {
	"CASSIE": 0,
	"MIO": 0,
	"QUILL": 0,
	"ELLE": 3,
	"NUTAKU": 3,
	"IRO": 6,
	"BONNIBEL": 6,
	"AYANO": 6,
	"FUMI": 9,
	"BEARVERLY": 9,
	"NINA": 9,
	"ALPHA": 13,
	"PAMU": 13,
	"LUNA": 13,
}

jobs1 = ( "fastfood", "restaurant", "lifeguard", "cleaning", "computers", "zoo", "hunting", "casino" )
jobs2 = ( "art", "movies", "slaying", "wizard", "sports", "legal", "space", "love" )

def die(s):
	import sys
	print(s, flush=True)
	sys.exit(1)

def travel(place):
	if place not in places:
		die("Undefined place: '{}'".format(place))
	dest = places[place]
	x = ul[0] + dest[0]
	y = ul[1] + dest[1]
	pyautogui.moveTo(x, y, duration=0.1)

def activate(place):
	travel(place)
	pyautogui.click()
	global activetab
	if place in maintabs and activetab != place:
		activetab = place
		time.sleep(1)

def selectgirl(girl):
	ensure("GIRLS")
	global activegirl
	if girl == activegirl:
		return
	if activegirl == 'none':
		log("Scrolling up girl list just to be safe.")
		travel("GIRLS/SCROLL")
		pyautogui.scroll(30)
		time.sleep(1)
	lvl = girlpages[girl]
	scrollgirls(lvl)
	activate("GIRLS/"+girl)
	activegirl = girl
	time.sleep(0.6)

def scrollgirls(level):
	global girlscroll
	if girlscroll == level:
		return
	ensure("GIRLS")
	travel("GIRLS/SCROLL")
	diff = girlscroll - level
	pyautogui.scroll(diff)
	girlscroll = level
	time.sleep(0.5)

def repeatclick(n):
	for _ in range(n):
		pyautogui.click()

def ensure(place):
	global activetab
	if place in maintabs and activetab != place:
		activate(place)

def qty2clicks(wanted):
	for i, qty in enumerate(giftqtys):
		if qty >= wanted:
			return i
	return 0

def buy(gift, qty=1):
	ensure("GIRLS")
	activate("GIRLS/gift")
	if not gift in giftpages:
		die("Unknown gift '{}'".format(gift))
	page = giftpages[gift]
	for _ in range(page):
		activate("GIFT/NEXTPAGE")
	activate("GIFT/"+gift)
	clicks = qty2clicks(qty)
	if clicks > 0:
		for _ in range(clicks):
			activate("GIFT/INCREMENT")
	activate("GIFT/PAY")

def date(activity, qty=1):
	ensure("GIRLS")
	activate("GIRLS/date")
	activate("DATE/"+activity)
	activate("DATE/PAY")
	if qty > 1:
		travel("DATE/GOAGAIN")
		repeatclick(qty-1)
	activate("DATE/COMPLETE")

def dialogskip():
	activate("GIRLS/dismiss")
	repeatclick(2)

def log(s):
	print(s)

def scrolljob(direction):
	global jobscroll
	if jobscroll == direction:
		return
	ensure("JOBS")
	travel("JOBS/SCROLL")
	if direction == 'UP':
		pyautogui.scroll(3)
	else:
		pyautogui.scroll(-3)
	jobscroll = direction
	time.sleep(0.5)

def job(j):
	global jobs1, jobs2
	ensure("JOBS")
	if j in jobs1:
		scrolljob("UP")
	elif j in jobs2:
		scrolljob("DOWN")
	else:
		die("Unknown job '{}'".format(j))
	activate("JOBS/"+j)
	time.sleep(0.5)

def hobby(h):
	ensure("HOBBIES")
	activate("HOBBIES/"+h)

def sleep(s):
	secs = float(s)
	time.sleep(secs)


def sorry(affection):
	n = int(affection) - 1
	ensure("GIRLS")
	activate("GIRLS/flirt")
	repeatclick(n)

def reset():
	print("Initiating reset.... ", end='', flush=True)
	activate("STATS")
	activate("STATS/RESET")
	time.sleep(0.5)
	activate("RESET/okay")
	print("waiting for 6 seconds.... ", end='', flush=True)
	time.sleep(6.5)
	print("done.")

def cassie0():
	selectgirl('CASSIE')
	log("CASSIE 0")
	job('fastfood')
	sleep(1)
	sorry(5)

def cassie1():
	selectgirl('CASSIE')
	log("CASSIE 1")
	hobby('suave')
	sorry(13)

def cassie2():
	selectgirl('CASSIE')
	log("CASSIE 2")
	hobby('funny')
	hobby('buff')
	hobby('techsavvy')
	buy('shell')

def cassie3():
	selectgirl('CASSIE')
	log("CASSIE 3")
	job('restaurant')
	buy('rose')

def cassie4():
	selectgirl('CASSIE')
	log("CASSIE 4")
	hobby('tenderness')
	hobby('motivation')
	buy('lotion')
	date('stroll')
	job('lifeguard')


def mio0():
	selectgirl('MIO')
	log("MIO 0")
	pass

def mio1():
	selectgirl('MIO')
	log("MIO 1")
	pass

def mio2():
	selectgirl('MIO')
	log("MIO 2")
	buy('rose')

def mio3():
	selectgirl('MIO')
	log("MIO 3")
	buy('lotion')


def misc0():
	selectgirl('CASSIE')
	job('fastfood')
	job('restaurant')
	job('lifeguard')
	job('cleaning')
	selectgirl('ELLE')
	selectgirl('NUTAKU')
	selectgirl('IRO')

current = (
	cassie0, cassie1, cassie2, cassie3, cassie4,
	mio0, mio1, mio2, mio3,
	misc0,
)


def main():
	pyautogui.FAILSAFE = True
	# reset()
	start = time.time()
	for doit in current:
		ensure("GIRLS")
		doit()
		dialogskip()
		pyautogui.moveTo(400, 600)
		time.sleep(1)
	elapsed = time.time() - start
	print('Completed in {} seconds'.format(elapsed))

main()
