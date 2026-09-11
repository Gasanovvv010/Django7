from django.shortcuts import render

movies = [
    {
        'id': 1,
        'title': 'film1',
        'genre': 'Drama',
        'duration': 169,
        'age': '19+',
        'seats': 210
    },
    {
        'id': 2,
        'title': 'film2',
        'genre': 'Drama',
        'duration': 148,
        'age': '12+',
        'seats': 5
    },
    {
        'id': 3,
        'title': 'film3',
        'genre': 'Action',
        'duration': 152,
        'age': '16+',
        'seats': 0
    },
    {
        'id': 4,
        'title': 'film4',
        'genre': 'Drama',
        'duration': 195,
        'age': '12+',
        'seats': 8
    },
    {
        'id': 5,
        'title': 'film5',
        'genre': 'Action',
        'duration': 136,
        'age': '16+',
        'seats': 3
    },
    {
        'id': 6,
        'title': 'film6',
        'genre': 'fantasy',
        'duration': 81,
        'age': '6+',
        'seats': 0
    }
]


def home(request):
    return render(request, 'Cinema/home.html')


def movie_list(request):
    genre = request.GET.get('genre')
    available = request.GET.get('available')

    filtered_movies = movies

    if genre:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie['genre'] == genre
        ]

    if available:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie['seats'] > 0
        ]

    genres = set(movie['genre'] for movie in movies)

    return render(request, 'Cinema/movies.html', {
        'movies': filtered_movies,
        'genres': genres
    })
def movie_detail(request, movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)

    if movie is None:
        return render(request, 'Cinema/not_found.html')

    return render(request, 'Cinema/movie_detail.html', {'movie': movie})


def booking(request, movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)

    if movie is None:
        return render(request, 'Cinema/not_found.html')

    error = None
    success = False
    customer_name = ''
    tickets = ''

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        tickets = request.POST.get('tickets', '')

        if not customer_name:
            error = 'Customer name cannot be empty.'

        elif movie['seats'] == 0:
            error = 'This movie is SOLD OUT.'

        else:
            try:
                tickets = int(tickets)

                if tickets <= 0:
                    error = 'Number of tickets must be greater than zero.'

                elif tickets > movie['seats']:
                    error = 'Not enough free seats.'

                else:
                    movie['seats'] -= tickets
                    success = True

            except ValueError:
                error = 'Number of tickets must be a number.'

    return render(request, 'Cinema/booking.html', {
        'movie': movie,
        'error': error,
        'success': success,
        'customer_name': customer_name,
        'tickets': tickets
    })


def bookings(request):
    return render(request, 'Cinema/booking.html')





