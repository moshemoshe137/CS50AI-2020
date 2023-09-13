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
    # print(corpus)
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    # print(f"sum = {sum(list(ranks.values()))}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    # print(f"sum = {sum(list(ranks.values()))}")


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
    transition_dict = dict()
    links_to = corpus[page]
    num_links = len(links_to)
    num_total_pages = len(corpus)
    all_pages = corpus.keys()

    for link in all_pages:
        transition_dict[link] = (1 - damping_factor) / num_total_pages
        if link in links_to:
            transition_dict[link] += damping_factor / num_links

    return transition_dict

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    all_pages = list(corpus.keys())
    page = random.choice(all_pages)

    pr_dict = {x: 0 for x in all_pages}

    for sample in range(n):
        model = transition_model(corpus, page, damping_factor)
        next_page = random.choices(
            list(model.keys()), list(model.values())
        )[0]
        pr_dict[next_page] += (1 / n)
        page = next_page

    return pr_dict
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    max_change = float('inf')
    all_pages = list(corpus.keys())
    num_pages = len(all_pages)
    pr_dict = {x: (1 / num_pages) for x in all_pages}

    while max_change > 10 ** -3:
        # print(pr_dict)
        # print(f"sum = {sum(list(pr_dict.values()))}")
        # print(max_change)
        max_change = 0
        old_pr_dict = pr_dict.copy()
        for page in pr_dict:
            links_to_me = {x for x in all_pages if (page in corpus[x]) or (len(corpus[x]) == 0)}
            # if len(corpus[page]) == 0:
            #     links_to_me = set(all_pages)
            # print(f"{', '.join(links_to_me)} link(s) to {page}")

            old_value = old_pr_dict[page]
            pr_dict[page] = (1 - damping_factor) / num_pages
            summation_portion = 0
            for linker in links_to_me:
                try:
                    summation_portion += old_pr_dict[linker] / len(corpus[linker])
                except ZeroDivisionError:
                    summation_portion += old_pr_dict[linker] / num_pages
            pr_dict[page] += damping_factor * summation_portion
            # try:
            #     pr_dict[page] += damping_factor * sum(
            #         [old_pr_dict[i] / len(corpus[i]) for i in links_to_me]
            #     )
            # except ZeroDivisionError:
            #     pr_dict[page] += damping_factor * sum(
            #         [old_pr_dict[i] / num_pages for i in links_to_me]
            #     )
            max_change = max(max_change, abs(pr_dict[page] - old_value))
    return pr_dict
    raise NotImplementedError


if __name__ == "__main__":
    main()
