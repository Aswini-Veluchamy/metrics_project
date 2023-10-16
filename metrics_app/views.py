from django.shortcuts import render

# Create your views here.
def create_metrics(request):
    if request.method == "POST":
        servername = request.POST['servername']
        workload_id = request.POST['workload_id']
        metric_type = request.POST['metric_type']
        date_range = request.POST['date_range']
        print(date_range)
        return render(request, 'metrics_app/create_metrics.html')
    else:
        return render(request, 'metrics_app/create_metrics.html')

def correlation_table(request):
    return render(request, 'metrics_app/correlation_table.html')