from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app.forms import  BookSearchForm
# Create your views here.



from app.models import Author, Book, Publisher

# a) uma página com a lista dos títulos de todos os livros;
def bookTitles(request):
    books = Book.objects.all()
    assoc = {}
    for c in books:
        assoc[c.title] = c.id
    tparams = {
        'designation_list': assoc,
        'category': 'book/'
    }
    return render(request, 'list.html', tparams)

# c) uma página com a lista dos nomes de todos os autores;
def authorNames(request):
    authors = Author.objects.all()
    assoc = {}
    for c in authors:
        assoc[c.name] = c.id
    tparams = {
        'designation_list': assoc,
        'category': 'author/'
    }
    return render(request, 'list.html', tparams)

# e) uma página com a lista dos nomes de todos as editoras;
def publishersNames(request):
    pubs = Publisher.objects.all()
    assoc = {}
    for c in pubs:
        assoc[c.name] = c.id

    tparams = {
        'designation_list': assoc,
        'category': 'publisher/'
    }
    return render(request, 'list.html', tparams)

# b) na página anterior, o título de cada livro deve ser um link para outra página com osdetalhes desse livro;
def detailsBook(request, num):
    current = Book.objects.get(id=num)
    tparams = {
        'categ': 'book',
        'title': current.title,
        'date': current.date,
        'pub':current.publisher,
        'auth':current.authors
    }
    return render(request, 'details.html', tparams)

# d) na página anterior, o nome de cada autor deve ser um link para outra página com os detalhes desse autor;
def detailsAuthor(request, num):
    current = Author.objects.get(id=num)
    tparams = {
        'categ': 'author',
        'name': current.name,
        'email': current.email,
    }
    return render(request, 'details.html', tparams)

# f) na página anterior, o nome de cada editora deve ser um link para outra página com os detalhes dessa editora
def detailsPublisher(request, num):
    current = Publisher.objects.get(id=num)
    tparams = {
        'categ': 'pub',
        'name': current.name,
        'city': current.city,
        'country': current.country,
        'web': current.website
    }
    return render(request, 'details.html', tparams)
#g. na página com a lista de autores, à frente do nome de cada autor, deve encontrarse um link “Livros” para uma página com a lista de livros desse autor;
#h. na página com a lista de editoras, à frente do nome de cada editora, deve
#encontrar-se um link “Autores” para uma página com a lista de autores dessa
#editora.



def booksearch(request):
    #Types: 0=books, 1=authors, 2=pubs
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            assoc = {}
            for c in books:
                assoc[c.title] = c.id
            tparams = {
                'designation_list': assoc,
                'category': 'book/'
            }
            return render(request, 'list.html', tparams)
        else:
            return render(request, 'search.html',{'error':True})
    else:
        return render(request, 'search.html',{'error':False})


def bookquery(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            assoc = {}
            for c in books:
                assoc[c.title] = c.id
            tparams = {
                'designation_list': assoc,
                'category': 'book/'
            }
            return render(request, 'list.html', tparams)
        else:
            return render(request, 'search.html',{'error':True})
    else:
        form = BookSearchForm()

    return render(request, 'search.html',{'error':False})