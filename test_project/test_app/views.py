# from django.shortcuts import render
# from django.http import HttpResponse

# ProjectList = [
#     {
#         'id': '1',
#         'title':'Ecommerce Website',
#         'description': 'This is the ecommerce website',
#     },
#     {
#         'id': '2',
#         'title':'Social Website',
#         'description': 'This is the Social Media',
#     },
#     {
#         'id': '3',
#         'title':'Food Website',
#         'description': 'This is the food website',
#     },
# ]


# def home(request):
#     # number=100
#     # msg = "I am a licensed Psycologies project"
#     # context={'message': msg,'num': number,'work':ProjectList}
#     projects = table.objects.all()
#     context = {'projects': projects}
#     return render(request,'test_app/template1.html',context)

# def user(request,jaish):
#     projectObj =  None
#     for a in ProjectList:
#         if a["id"] == jaish:
#             projectObj = a
#     return render(request,'test_app/template2.html',{'project':projectObj})



# # def about(request):
# #     return render(request,'about.html')


# def create_project(request):
#     context = {}
#     return render(request, "test_app/form.html", context)


from django.shortcuts import render
from django.http import HttpResponse
from .models import table


def home(request):
    projects = table.objects.all()
    content = {'work':projects}
    return render(request, "test_app/template1.html", content)

def user(request, pk):
    projectobj = table.objects.get(id = pk)
    tags = projectobj.tags.all()
    
    return render(request, 'test_app/template2.html', {'project' : projectobj, 'tags' : tags})

def createproject(request):
    content = {}
    return render(request, "test_app/form.html", content)