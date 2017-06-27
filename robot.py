#! /usr/bin/python3

# 2017-06-22 - initial version

import pyautogui, time, json

ul = ( 1213, 210 )

pyautogui.PAUSE = 0.1
activetab = 'GIRLS'
activegirl = 'none'
jobscroll = 'UP'
girlscroll = 0

with open('places.json', 'r') as f:
	places = json.load(f)

with open('dates.json', 'r') as f:
	dates = json.load(f)

with open('order.json', 'r') as f:
	autolist = json.load(f)

maintabs = ( "GIRLS", "JOBS", "HOBBIES", "STATS" )

giftpages = {
	"shell":       0,
	"lotion":      0,
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
	"magiccandles":   2,
	"enchantedscarf": 2,
	"bewitchedjam":   2,
	"mysticslippers": 2,
	"potion":      3,
	"usb":         3,
}

giftqtys = ( 1, 5, 10, 25, 50, 100, 1000, 10000 )

girlpages = {
	"MISC": 0,
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
	"EVA": 17,
	"KARMA": 17,
	"SUTRA": 17,
}

girllevel = {
	"MISC": 0,
	"CASSIE": 0,
	"MIO": 0,
	"QUILL": 0,
	"ELLE": 0,
	"NUTAKU": 0,
	"IRO": 0,
	"BONNIBEL": 0,
	"AYANO": 0,
	"FUMI": 0,
	"BEARVERLY": 0,
	"NINA": 0,
	"ALPHA": 0,
	"PAMU": 0,
	"LUNA": 0,
	"EVA": 0,
	"KARMA": 0,
	"SUTRA": 0,
}

jobs1 = ( "fastfood", "restaurant", "lifeguard", "cleaning", "computers", "zoo", "hunting", "casino" )
jobs2 = ( "art", "movies", "slaying", "wizard", "sports", "legal", "space", "love" )

statuslevels = ( 'Adversary', 'Nuisance', 'Frenemy', 'Acquaintance', 'Friendzone',
	'Awkward Besties', 'Crush', 'Sweetheart', 'Girlfriend', 'Lover' )

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

def findLogo():
	print("Finding upper-left corner of game window... ", end='', flush=True)
	logo = pyautogui.locateOnScreen('logoToFind.png')
	if logo:
		global ul
		print("logo found at {}".format(logo[:2]))
		x = logo[0] - 878
		y = logo[1] - 86
		ul = (x, y)
		pyautogui.moveTo(x, y)
		print("\tGame window is at {}".format(ul))
	else:
		die("not found.")


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

def job(j, howlong=0):
	global jobs1, jobs2
	ensure("JOBS")
	if j in jobs1:
		scrolljob("UP")
	elif j in jobs2:
		scrolljob("DOWN")
	else:
		die("Unknown job '{}'".format(j))
	activate("JOBS/"+j)
	if int(howlong) > 0:
		time.sleep(int(howlong))
		activate("JOBS/"+j)
		log("Job '{}' paused after working for {} seconds.".format(j, howlong))
	else:
		time.sleep(0.5)

def unjob(job):
	global jobs1, jobs2
	ensure("JOBS")
	if job in jobs1:
		scrolljob("UP")
	elif job in jobs2:
		scrolljob("DOWN")
	else:
		die("Unknown job '{}'".format(job))
	activate("JOBS/"+job)
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


statlookup = {
	'ADV': 0, 'NUI': 1, 'FRE': 2, 'ACQ': 3, 'FRI': 4,
	'AWK': 5, 'CRU': 6, 'SWE': 7, 'GIR': 8, 'LOV': 9
}

def woo(s):
	( girl, levelstr ) = s.split()
	if levelstr in ( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ):
		level = levelstr
	else:
		level = str(statlookup[levelstr.upper()[:3]])
	fulfill(girl, dates[girl][level])


def execute(task):
	vals = task.split()
	function = vals[0]
	if function == 'nothing':
		return
	if function in ('buy', 'date'):
		param = vals[1]
		if len(vals) == 3:
			qty = int(vals[2])
		else:
			qty = 1
		plist = ( param, qty )
	else:
		plist = vals[1:]
	print("\t"+function, plist)
	if plist:
		globals()[function](*plist)
	else:
		globals()[function]()


def fulfill(girl, steps):
	selectgirl(girl)
	for task in steps:
		execute(task)
	ensure("GIRLS")
	dialogskip()
	if girl != 'MISC':
		girllevel[girl] += 1
		level = girllevel[girl]
		status = statuslevels[level]
		log("You're now {} ({}) with {}!".format(status, level, girl.capitalize()))


def manual():
	while True:
		r = input("> ").strip().upper()
		if r == 'QUIT':
			break
		woo(r)
		pyautogui.click(400, 600)


def automate():
	pyautogui.FAILSAFE = True
	reset()
	start = time.time()
	for _ in autolist:
		if _ == "STOP":
			break
		woo(_)
		pyautogui.click(400, 600)
		time.sleep(0.5)
	elapsed = time.time() - start
	pyautogui.click(400, 600)
	print('Completed in {} seconds'.format(elapsed))


def main():
	findLogo()
	r = input("Autorun as far as possible (Y/n)? ").strip().lower()
	if r != 'n':
		automate()
	manual()

main()
