from django.shortcuts import render

def renderAll(request):
	if not request.user.is_authenticated:
		return render(request, 'nutritiontracker/index.html', {'error': 'You must be signed in to view this page.'})
	else:
		falseUser = FalseUser.objects.get(user=request.user)
		if (falseUser.height == -1):
			return render(request, 'nutritiontracker/index.html', {'displayForm': 'True'})
		else:
			resultsDict = {calGol: falseUser.calorieGoal, calDate: falseUser.calorieDate}
			return render(request, 'nutritiontracker/index.html', {'resultsDict': resultsDict})