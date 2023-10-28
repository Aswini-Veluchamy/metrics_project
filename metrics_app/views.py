from django.shortcuts import render

# Create your views here.
def create_metrics(request):
    if request.method == "POST":
        servername = request.POST['servername']
        print(servername)
        return render(request, 'metrics_app/create_metrics.html')
    else:
        return render(request, 'metrics_app/create_metrics.html')

def correlation_table(request):
    return render(request, 'metrics_app/correlation_table.html')