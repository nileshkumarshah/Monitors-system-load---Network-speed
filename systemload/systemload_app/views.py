from django.shortcuts import render

# Create your views here.
import psutil
import speedtest

def system_dashboard(request):
    # Get system load (CPU usage)
    cpu_load = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    # Get network speed (using speedtest-cli)
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    # Prepare data for the template
    context = {
        'cpu_load': cpu_load,
        'memory': {
            'total': memory.total / (1024 ** 3),  # Convert to GB
            'available': memory.available / (1024 ** 3),  # Convert to GB
            'percent': memory.percent,
        },
        'network_speed': {
            'download_mbps': round(download_speed, 2),
            'upload_mbps': round(upload_speed, 2),
        }
    }

    # Render the data on the dashboard template
    return render(request, 'dashboard.html', context)
