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
	"GIRLS/MISC": (100, 206),
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
	"GIRLS/EVA": (100, 183),
	"GIRLS/KARMA": (100, 272),
	"GIRLS/SUTRA": (100, 361),

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
	"GIFT/potion": (315, 371),
	"GIFT/usb":    (315, 371),
	"GIFT/magiccandles":   (315, 303),
	"GIFT/enchantedscarf": (467, 303),
	"GIFT/bewitchedjam":   (315, 371),
	"GIFT/mysticslippers": (467, 371),

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

dates = {
	'MISC': {
		0: (
			'unjob fastfood',
			'unjob restaurant',
			'unjob lifeguard',
			'unjob cleaning',
			'unjob hunting',
			'job space',
			"selectgirl ELLE",
			"selectgirl NUTAKU",
			"selectgirl IRO",
			"selectgirl BONNIBEL",
			"selectgirl AYANO",
			"selectgirl FUMI",
			"selectgirl BEARVERLY",
			"selectgirl NINA",
		),
		1: (
			'unjob computers',
			'unjob zoo',
			'unjob sports',
			'job art 3',
			'job movies 2',
			"selectgirl ALPHA",
			"selectgirl PAMU",
			"selectgirl LUNA",
		),
		2: (
			'unjob wizard',
			"selectgirl EVA",
		),
	},
	'CASSIE': {
		0: (
			'job fastfood',
			'sleep 1',
			'sorry 5',
		),
		1: (
			'hobby suave',
			'sorry 13',
		),
		2: (
			'hobby funny',
			'hobby buff',
			'hobby techsavvy',
			'buy shell',
		),
		3: (
			'job restaurant',
			'buy rose',
		),
		4: (
			'hobby tenderness',
			'hobby motivation',
			'buy lotion',
			'date stroll',
			'job lifeguard',
		),
		5: (
			'buy donut',
			'date stroll 3',
		),
		6: (
			'hobby wisdom',
			'hobby badass',
			'buy fruitbasket',
			'date beach',
		),
		7: (
			'job cleaning',
			'job zoo',
			'job hunting',
			'buy chocolates',
			'date beach 3',
		),
		8: ( 'buy book', ),
	},
	"MIO": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy rose', ),
		3: ( 'buy lotion', ),
		4: ( 'buy donut', 'date stroll 2', ),
		5: ( 'buy book', 'date beach 2', ),
		6: ( 'hobby smart', 'buy drink', 'date sightseeing', ),
		7: (
			'buy flowers',
			'date movies',
			'job sports',
			'job computers',
		),
		8: ( 'buy cake', ),
	},
	"QUILL": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy shell', ),
		3: ( 'buy fruitbasket', ),
		4: ( 'buy earrings', 'date stroll 3', ),
		5: ( 'buy flowers', 'date beach 3', ),
		6: ( 'buy plushytoy', 'date sightseeing 3', ),
		7: ( 'buy teaset', 'date movies 3', ),
		8: ( 'buy necklace', ),
	},
	"ELLE": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy rose 5', ),
		3: ( 'buy chocolates 3', ),
		4: ( 'buy drink 2', 'date stroll 4', ),
		5: (
				'hobby lucky',
				'hobby mysterious',
				'hobby angst',
				'buy flowers 2',
				'date beach 4',
				'sleep 5',
				'job casino',
			),
		6: ( 'buy cake', 'date sightseeing 4', ),
		7: ( 'buy plushytoy', 'date movies 4', ),
		8: ( 'buy puppy', ),
	},
	"NUTAKU": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy lotion 3', ),
		3: ( 'buy book', ),
		4: ( 'buy drink 2', 'date stroll 5', ),
		5: ( 'buy plushytoy', 'date beach 5', ),
		6: ( 'buy shoes', 'date sightseeing 5', ),
		7: ( 'buy necklace', 'date movies 5', ),
		8: ( 'buy designerbag', ),
	},
	"IRO": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy lotion 5', ),
		3: ( 'buy fruitbasket 5', ),
		4: ( 'buy drink 3', 'date stroll 6', ),
		5: ( 'buy shoes 2', 'date beach 6', ),
		6: ( 'buy puppy', 'date sightseeing 6', ),
		7: ( 'buy necklace', 'date movies 6', ),
		8: ( 'buy car', ),
	},
	"BONNIBEL": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy shell 10', 'job art' ),
		3: ( 'buy donut 10', ),
		4: ( 'buy chocolates 10', 'date stroll 7', ),
		5: ( 'buy book 5', 'date beach 7', ),
		6: ( 'buy cake 3', 'date sightseeing 7', ),
		7: ( 'buy teaset 2', 'date movies 7', ),
		8: ( 'nothing', ),
	},
	"AYANO": {
		0: ( 'job slaying', ),
		1: ( 'nothing', ),
		2: ( 'nothing', ),
		3: ( 'buy flowers 5', ),
		4: ( 'buy plushytoy 1000', 'date stroll 20', ),
		5: ( 'date beach 20', ),
		6: ( 'buy designerbag 50', 'date sightseeing 20', ),
		7: ( 'buy car 50', 'date movies 20', ),
		8: ( 'nothing', ),
	},
	"FUMI": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy drink 25', ),
		3: ( 'buy plushytoy 25', ),
		4: ( 'buy shoes 10', 'date stroll 10', ),
		5: ( 'buy necklace 10', 'date beach 10', ),
		6: ( 'buy designerbag 5', 'date sightseeing 10', ),
		7: ( 'buy car 2', 'date movies 10', ),
		8: ( 'nothing', ),
	},
	"BEARVERLY": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy chocolates 50', ),
		3: ( 'buy cake 50', ),
		4: ( 'buy teaset 25', 'date stroll 12', ),
		5: ( 'buy puppy 25', 'date beach 12', ),
		6: ( 'buy necklace 10', 'date sightseeing 12', ),
		7: ( 'buy designerbag 10', 'date movies 12', 'sorry 10' ),
		8: ( 'buy potion', 'sorry 50' ),
	},
	"NINA": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy car', ),
		3: ( 'buy car 2', ),
		4: ( 'buy car 3', 'date stroll 15', ),
		5: ( 'buy car 4', 'date beach 15', ),
		6: ( 'buy car 5', 'date sightseeing 15', ),
		7: ( 'buy car 6', 'date movies 15', 'sorry 10' ),
		8: ( 'buy car 7', ),
	},
	"ALPHA": {
		0: ( 'job legal', ),
		1: ( 'job love 2', ),
		2: ( 'buy shell 5000', ),
		3: ( 'buy rose 5000', ),
		4: ( 'buy book 5000', 'date stroll 20', ),
		5: ( 'buy flowers 5000', 'date beach 20', ),
		6: ( 'buy shoes 500', 'date sightseeing 20', ),
		7: ( 'buy designerbag 500', 'date movies 20', 'unjob legal', ),
		8: ( 'buy usb', ),
	},
	"PAMU": {
		0: ( 'job wizard', ),
		1: ( 'nothing', ),
		2: ( 'buy lotion 5000', ),
		3: ( 'buy drink 5000', ),
		4: ( 'buy lotion 10000', 'date stroll 50', ),
		5: ( 'buy car 100', 'date beach 50', ),
		6: ( 'buy lotion 10000', 'buy lotion 10000', 'buy lotion 10000', 'buy lotion 10000', 'buy lotion 10000', 'date sightseeing 50', 'sorry 15' ),
		7: ( 'buy drink 10000', 'buy drink 10000', 'buy drink 10000', 'buy drink 10000', 'buy drink 10000', 'date movies 50', 'sorry 50' ),
		8: ( 'nothing', ),
	},
	"LUNA": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'buy shoes 10000', ),
		3: ( 'buy necklace 10000', ),
		4: ( 'buy car 10000', 'date stroll 100', ),
		5: ( 'buy magiccandles 10', 'date beach 100', ),
		6: ( 'date sightseeing 100', 'buy enchantedscarf 5', ),
		7: ( 'date movies 100', 'buy bewitchedjam 3', ),
		8: ( 'nothing', ),
	},
	"EVA": {
		0: ( 'nothing', ),
		1: ( 'nothing', ),
		2: ( 'sorry 5', ),
		3: ( 'sorry 50', ),
		4: ( 'date stroll 25', ),
		5: ( 'date beach 50', ),
		6: ( 'date sightseeing 75', ),
		7: ( 'date movies 25', ),
		8: ( 'sorry 50', ),
	},
}

def woo(s):
	( girl, levelstr ) = s.split()
	if levelstr in ( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ):
		level = int(levelstr)
	else:
		level = statlookup[levelstr.upper()[:3]]
	fulfill(girl, dates[girl][level])


def generica(girl, d):
	for _ in sorted(d.keys()):
		tasklist = d[_]
		fulfill(girl, tasklist)


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

autolist = (
	"CASSIE 0", "CASSIE 1", "CASSIE 2", "CASSIE 3",
	"CASSIE 4", "CASSIE 5", "CASSIE 6", "CASSIE 7", "CASSIE 8",
	"MIO 0", "MIO 1", "MIO 2", "MIO 3",
	"MIO 4", "MIO 5", "MIO 6", "MIO 7", "MIO 8",
	"MISC 0",
	"ELLE 0", "ELLE 1", "ELLE 2", "ELLE 3", "ELLE 4", "ELLE 5", "ELLE 6", "ELLE 7", "ELLE 8",
	"NUTAKU 0", "NUTAKU 1", "NUTAKU 2", "NUTAKU 3", "NUTAKU 4", "NUTAKU 5",
	"NUTAKU 6", "NUTAKU 7", "NUTAKU 8",
	"MISC 1",
	"QUILL 0", "QUILL 1", "QUILL 2", "QUILL 3", "QUILL 4", "QUILL 5", "QUILL 6", "QUILL 7", "QUILL 8",
	"IRO 0", "IRO 1", "IRO 2", "IRO 3", "IRO 4", "IRO 5", "IRO 6", "IRO 7", "IRO 8",
	"BONNIBEL 0", "BONNIBEL 1", "BONNIBEL 2", "BONNIBEL 3", "BONNIBEL 4",
	"BONNIBEL 5", "BONNIBEL 6", "BONNIBEL 7",
	"FUMI 0", "FUMI 1", "FUMI 2", "FUMI 3", "FUMI 4", "FUMI 5", "FUMI 6", "FUMI 7",
	"AYANO 0", "AYANO 1", "AYANO 2", "AYANO 3", "AYANO 4", "AYANO 5", "AYANO 6", "AYANO 7",
	"BEARVERLY 0", "BEARVERLY 1", "BEARVERLY 2", "BEARVERLY 3", "BEARVERLY 4",
	"BEARVERLY 5", "BEARVERLY 6", "BEARVERLY 7",
	"NINA 0", "NINA 1", "NINA 2", "NINA 3", "NINA 4", "NINA 5", "NINA 6", "NINA 7",
	"ALPHA 0", "ALPHA 1", "ALPHA 2", "ALPHA 3", "ALPHA 4", "ALPHA 5", "ALPHA 6", "ALPHA 7",
	"PAMU 0", "PAMU 1", "PAMU 2", "PAMU 3", "PAMU 4",
	"MISC 2",
	"EVA 0", "EVA 1", "EVA 2", "EVA 3",
	"LUNA 0", "LUNA 1", "LUNA 2", "LUNA 3", "LUNA 4",
	"PAMU 5", "PAMU 6", "PAMU 7",
	"BONNIBEL 8", "FUMI 8", "BEARVERLY 8", "NINA 8", "ALPHA 8",
)

manualonly = (
	"LUNA 5", "PAMU 8",
	"EVA 4", "EVA 5", "EVA 6", "EVA 7",
	"LUNA 6", "LUNA 7", "LUNA 8",
	"AYANO 8", "EVA 8",
)

def main():
	pyautogui.FAILSAFE = True
	reset()
	start = time.time()
	try:
		for _ in autolist:
			woo(_)
			pyautogui.click(400, 600)
			time.sleep(0.5)
	except KeyboardInterrupt:
		elapsed = time.time() - start
		pyautogui.click(400, 600)
		print('Completed in {} seconds'.format(elapsed))

main()
