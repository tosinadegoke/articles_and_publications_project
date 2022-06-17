from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    # return render(request, 'my_page/home.html', {})
    return render(request, 'my_page/index.html', {})

    
def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'number' : 12334,
        'my_list': [21, 2, 34, 'dwds', 12],
        'value':20000000,
        'blog_title': 'A wonderful service today of 5hrs'
    }
    
    return render(request, 'my_page/about.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'my_page/contact.html', {})

