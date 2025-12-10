from django.shortcuts import render

def calculate_volume(request):
  result = None

  if request.method == 'POST':

      try:

          length = float(request.POST.get('length', 0))
          width = float(request.POST.get('width', 0))
          height = float(request.POST.get('height', 0))

          result = length * width * height
      except ValueError:

          result = "Invalid input. Please enter valid numbers."

  return render(request, 'math.html', {'result': result})
