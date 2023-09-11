import requests

def fetch_news(api_key, category, number, country):
    # List of valid keywords
    valid_categories = ["business", "entertainment", "health", "general", "science", "sports", "technology"]

    # Check if the entered keyword is valid
    if category.lower() not in valid_categories:
        print(f'Invalid keyword. Please enter one of the valid keywords: {valid_categories}')
        return

    # Check if 'number' is a positive integer
    try:
        number = int(number)
        if number <= 0:
            raise ValueError
    except ValueError:
        print('Invalid number. Please enter a positive integer for the number of articles.')
        return

    # Specify the API endpoint URL
    url = 'https://newsapi.org/v2/top-headlines'  # Change to the top-headlines endpoint

    # Define the parameters for your request
    params = {
        'apiKey': api_key,
        'category': category,  # Keyword to search for
        'pageSize': number,  # Number of articles to fetch
        'country': country,
        'language': 'en'
    }

    # Send the HTTP GET request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Loop through and print the news articles
        for article in data['articles']:
            print(article['title'])
            print(article['description'])
            print(article['url'])
            print('\n')
    else:
        print('Error:', response.status_code)

if __name__ == '__main__':
    api_key = 'cd52a26d106b496b953ecc200c981590'
    print("Types of news available")
    l = ["Business", "Entertainment", "Health", "General", "Science", "Sports", "Technology"]
    for type in l:
        print(type)
    category = input('Enter a valid type to search for news articles: ')
    number = input("Enter the number of articles you want to see: ")
    country = input("Enter the country specific news(us for United States):")

    print()

    fetch_news(api_key, category, number, country)

