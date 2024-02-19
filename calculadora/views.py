from django.shortcuts import render, HttpResponse

def home(request):
    if request.method =="POST":
        n1 = float(request.POST.get('n1', 0))
        n2 = float(request.POST.get('n2', 0))
        operaciones = request.POST.get('operaciones')

        resultado = calcular_resultado(n1, n2, operaciones)
        return render(request,'index.html', {'resultado': resultado})

    return render(request, 'index.html')

def calculate(request):
     if request.method =="POST":
        n1 = float(request.POST.get('n1', 0))
        n2 = float(request.POST.get('n2', 0))
        operaciones = request.POST.get('operaciones')
        resultado = calcular_resultado(n1, n2, operaciones)
        return render(request,'index.html', {'resultado': resultado})
     
     return HttpResponse('Invalid Request')

def calcular_resultado(n1, n2, operaciones):
    if operaciones == 'sumar':
        return n1 + n2
    elif operaciones == 'restar':
        return n1 - n2
    elif operaciones == 'multiplicar':
        return n1 * n2
    elif operaciones == 'dividir':
        if n2 !=0:
            return n1/n2
        else:
            return 'Syntax Error'
    else:
        return 'Syntax Error'