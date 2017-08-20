from sys import argv
import requests
import bs4
import webbrowser


def main():

    if len(argv) < 2:
        print("Please input a Google search query as CL arg.")
        return

    searchPhrase = '+'.join(argv[1:])

    results = requests.get('https://www.google.com/search?q=' + searchPhrase)

    results.raise_for_status()

    resultsSoup = bs4.BeautifulSoup(results.text, 'html.parser')

    resultsLinks = resultsSoup.select('div div div cite')

    for link in resultsLinks:
        webbrowser.open(link.getText())

main()
