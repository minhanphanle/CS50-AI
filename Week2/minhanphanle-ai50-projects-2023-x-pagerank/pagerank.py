import os
import random
import re
import sys


DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # print(f"PAGE: {page}")
    probability_distribution = {}

    random_chosen = 1 - damping_factor
    count_all = len(corpus)
    base_prob = (random_chosen/count_all)
    prob_eq_all = (1 / count_all)
    linked = set()
    unlinked = set()
    count_linked = 0

    # print(corpus.items())

    for key, value in corpus.items():

        probability_distribution[key] = 0

        if key != page:
            continue

        # somehow this returns 0 for all probability #BUG
        # if value == {}:
        #     for i in corpus:
        #         probability_distribution[i] = prob_eq_all

        else:
            linked = value
            # remaining pages in the corpus
            for key in corpus:
                if key not in linked:
                    # print(key)
                    unlinked.add(key)

    # print(linked)
    # print(unlinked)
    for key in probability_distribution:
        count_linked = len(linked)

        # page has no outgoing links
        if count_linked == 0:
            probability_distribution[key] = prob_eq_all
            continue

        prob_linked = (damping_factor/count_linked +
                       base_prob)
        if key in linked:
            probability_distribution[key] = prob_linked
        else:
            probability_distribution[key] = base_prob

    # print(probability_distribution)
    # print("-------------------")
    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    probability_distribution = {}

    start_page = random.choice(list(corpus.keys()))
    previous_distribution = transition_model(
        corpus, start_page, damping_factor)
    # to ensure that the keys are in the transition model order
    pages = list(previous_distribution.keys())

    # initialize intial PageRank values
    for page in pages:
        probability_distribution[page] = 0

    # update page count for start page
    probability_distribution[start_page] += 1

    for i in range(0, n - 1):
        page_chosen = random.choices(
            pages, weights=[weight for weight in previous_distribution.values()])[0]
        probability_distribution[page_chosen] += 1
        previous_distribution = transition_model(
            corpus, page_chosen, damping_factor)

    # normalize
    for key in probability_distribution.keys():
        probability_distribution[key] /= n

    return probability_distribution


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    probability_distribution = {}
    pages = list(corpus.keys())
    N = len(pages)
    initial_prob = 1 / N
    random_prob = (1 - damping_factor) / N

    # initialize PageRank values and assign equal 1 / N probability to each page
    for page in pages:
        probability_distribution[page] = initial_prob

    def PR(p):
        # if p has links from i
        sum_pr = 0
        for i, value in corpus.items():
            # if p is linked in i
            if p in value:
                linked = True
                # NumLinks(i)
                sum_pr += probability_distribution[i] / len(value)

            # i has no links at all should be interpreted as having one link
            # for every page in the corpus (including itself).
            elif value == {}:
                sum_pr += probability_distribution[i] / N

        result = random_prob + damping_factor * sum_pr

        return result

    iterations = 0
    max_change = initial_prob

    while max_change > 0.001:

        # print(f"iterations: {iterations}")

        iterations += 1

        max_change = 0

        # copy the old distribution so it does not change during loop
        old_prob_distribution = probability_distribution.copy()
        # print(f"old distribution: {old_prob_distribution}")

        for page in pages:
            new_prob = PR(page)
            old_prob = old_prob_distribution[page]
            change = abs(new_prob - old_prob)

            # only update if change > 0.001
            if change > 0.001:
                probability_distribution[page] = new_prob

                # update the max_change to terminate the outer loop if every change is less than 0.001
                if max_change < change:
                    max_change = change

        # print(f"new distribution: {probability_distribution}")

    # normalize so they add up to 1
    normalization_factor = 0
    for values in probability_distribution.values():
        normalization_factor += values

    probability_distribution = {page: round(
        rank / normalization_factor, 4) for page, rank in probability_distribution.items()}

    return probability_distribution


if __name__ == "__main__":
    main()
