from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib import messages
from .models import Graph, Formulas
from django_user_agents.utils import get_user_agent

# Create your views here.
#delete from sqlite_sequence where name='graphics_graph'
def graph(request):
    user_agent = get_user_agent(request)

    obj_list = []
    formulas_list = []
    for i in range(0, 100):
        try:    obj_list.append(Graph.objects.get(id=i))
        except: continue
    for i in range(0, 100):
        try:   formulas_list.append(Formulas.objects.get(id=i))
        except: continue

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        name = request.POST['input']
        try:
            obj = Graph.objects.get(graph_name=name)
        except:
            obj = None
        if form.is_valid() and not obj:
                instance = form.save(commit=False)
                instance.graph_name = name
                form.save()
                obj = Graph.objects.get(graph_name=name)
                x, y = excel_reader(obj.file.path)
                obj.graph_name = name
                obj.x, obj.y = x, y
                obj.save()
                messages.success(request, x, y)

                if user_agent.is_mobile:
                    return render(request, 'graph.html', {'x': x, 'y': y, 'name': name, 'mobile': "mobile", 'obj_list': obj_list, 'formulas_list': formulas_list})
                else:
                    return render(request, 'graph.html', {'x': x, 'y': y, 'name': name, 'obj_list': obj_list, 'formulas_list': formulas_list})
        else:
            return render(request, 'graph.html', {'error': "Graph with this name already exists!", })
    else:
        form = UploadFileForm()
    if user_agent.is_mobile:
        return render(request, 'graph.html', {'mobile': "mobile", 'obj_list': obj_list, 'formulas_list': formulas_list})
    else:
        return render(request, 'graph.html', {'obj_list': obj_list, 'formulas_list': formulas_list})



def about(request):
    return render(request, 'about.html')

def test(request):
    return render(request, 'test.html')


def excel_reader(excel_file):
    import xlrd

    read = xlrd.open_workbook(excel_file)#'C:/Users/Rust/Desktop/test.xlsx'
    sheet = read.sheet_by_index(0)

    x, y = [], []
    num = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    if sheet.nrows == 3:
        for i in range(sheet.nrows):
            for a in range(0, 30):
                if i == 0: x.append(sheet.row_values(a)[i])
                if i == 1: y.append(sheet.row_values(a)[i])
        return  x, y
    
    for i in range(sheet.nrows):
        for a in range(0, 10):
            if i == 0: x.append(sheet.row_values(a)[i])
            if i == 1: y.append(sheet.row_values(a)[i])
    return  x, y
