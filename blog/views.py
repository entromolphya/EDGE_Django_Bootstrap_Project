from django.shortcuts import render

# Home Page View
def home(request):
    return render(request, 'index.html')

# Tree Blog Page View
def tree_list(request):
    posts = [
        {
            "id": 1,
            "title": "The Magic of Bonsai Trees",
            "description": "Discover the ancient art of bonsai and how these miniature trees symbolize patience and harmony.",
            "image": "https://www.todaystraveller.net/wp-content/uploads/2023/03/Bonsai-edited-768x768.jpg",
            "buy_url": "https://www.bonsaiempire.com/tree-species"
        },
        {
            "id": 2,
            "title": "Fast-Growing Trees for Your Backyard",
            "description": "Learn about the best trees that grow quickly and provide shade, beauty, and fresh air.",
            "image": "https://www.planetnatural.com/wp-content/uploads/2023/11/Fast-Growing-Trees-1400x788.webp",
            "buy_url": "https://www.fast-growing-trees.com/collections/shade-trees"
        },
        {
            "id": 3,
            "title": "The Importance of Rainforest Trees",
            "description": "Explore the crucial role trees play in the rainforest ecosystem and how they help combat climate change.",
            "image": "https://d3mvlb3hz2g78.cloudfront.net/wp-content/uploads/2020/06/dreamstime_m_135239600.jpg",
            "buy_url": "https://www.worldwildlife.org/initiatives/forests"
        },
    ]
    return render(request, 'blog.html', {'posts': posts})
