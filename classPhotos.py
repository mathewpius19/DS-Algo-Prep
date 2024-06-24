#O(Nlog(N)) Time, because it takes Nlog(N) time to sort the array | O(1) Space
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtsSorted = sorted(redShirtHeights)
	blueShirtsSorted = sorted(blueShirtHeights)
	redShirts = False
	blueShirts = False
	if redShirtsSorted[0]>blueShirtsSorted[0]:
		redShirts = True
	if blueShirtsSorted[0]>redShirtsSorted[0]:
		blueShirts = True
	for i in range(len(redShirtsSorted)):
		if redShirtsSorted[i]==blueShirtsSorted[i]:
			return False
		elif redShirtsSorted[i] < blueShirtsSorted[i] and redShirts is True:
			return False
		elif blueShirtsSorted[i] < redShirtsSorted[i] and blueShirts is True:
			return False
	return True

print(classPhotos([5, 8, 1, 3, 4],[6, 9, 2, 4, 5]))