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

def update_details(request):
    cur_false_user = FalseUser.objects.get(user=request.user)

    if request.method == 'POST':
        try:
            age = request.POST['age']
            height = request.POST['height']
            weight = request.POST['weight']
        except:
			return render(request, 'nutritiontracker/index.html', {error: 'You have left one or more fields blank.'})
        else:
            BMR = 10 * weight - 5 * age
            if cur_false_user.gender = 'M':
                BMR += 6.25 * height + 5
            else:
                BMR += 6.25 * height - 161
            f = FalseUser (
                age=age,
                height=height,
                weight=weight,
                calorieGoal=BMR*7
            )

            f.save()

            return render()
    else:
        return render(request, '404.html')