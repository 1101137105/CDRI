from django.shortcuts import render

# Create your views here.
def page1 (request):
    return render(request, 'From_1.html', {
    })

def page2 (request):
    return render(request, 'From_2.html', {
    })

def from_index (request):
    return render(request, 'From_Index.html', {
    })
def page1_csv (request):
    return render(request, 'From_1_CSV.html', {
    })
def page2_csv (request):
    return render(request, 'From_2_CSV.html', {
    })