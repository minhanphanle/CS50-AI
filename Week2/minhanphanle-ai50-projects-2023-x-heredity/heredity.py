import csv
import itertools
import sys
import copy

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    ################
    # print(f"______ JOINT PROB ______ ")
    # print(f"people: {people}")
    # print(f"one gene: {one_gene}")
    # print(f"two genes: {two_genes}")
    # print(f"have trait: {have_trait}")

    people_info = copy.deepcopy(people)
    # add information to people dictionary regarding gene and trait
    for name in one_gene:
        people_info[name]["gene"] = 1

    for name in two_genes:
        people_info[name]["gene"] = 2

    for name in people_info:
        if name not in one_gene | two_genes:
            people_info[name]["gene"] = 0

        if name in have_trait:
            people_info[name]["trait"] = True
        else:
            people_info[name]["trait"] = False

    # joint probability dictionary
    prob_dict = {}

    for name in people_info:

        # GENE PROBABILITY
        gene_number = people_info[name]["gene"]

        # mother and father blank
        if people_info[name]["mother"] == None and people_info[name]["father"] == None:

            # unconditional probability of gene
            gene_prob = PROBS["gene"][gene_number]

        else:
            # child probability of gene based on parents

            def inherit_prob(parent_gene):
                # probability of parents passing down a gene to child

                mutated_prob = PROBS["mutation"]
                unmutated_prob = 1 - mutated_prob

                if parent_gene == 1:
                    return 0.5 * unmutated_prob + 0.5 * mutated_prob
                elif parent_gene == 2:
                    return unmutated_prob
                else:
                    return mutated_prob

            mother = people_info[name]["mother"]
            father = people_info[name]["father"]
            mother_gene = people_info[mother]["gene"]
            father_gene = people_info[father]["gene"]
            mother_gene_prob = inherit_prob(mother_gene)
            father_gene_prob = inherit_prob(father_gene)

            if gene_number == 0:
                gene_prob = (1 - mother_gene_prob) * (1 - father_gene_prob)
            elif gene_number == 1:
                gene_prob = mother_gene_prob * \
                    (1 - father_gene_prob) + \
                    father_gene_prob * (1 - mother_gene_prob)
            elif gene_number == 2:
                gene_prob = mother_gene_prob * father_gene_prob

        # TRAIT PROBABILITY
        trait = people_info[name]["trait"]
        trait_prob = PROBS["trait"][gene_number][trait]

        # GENE & TRAIT PROBABILITY
        prob_dict[name] = gene_prob * trait_prob
        # print(f"person: {name}")
        # print(f"person prob: {prob_dict[name]}")

    joint_prob = 1

    for prob in prob_dict.values():
        # print(f"prob: {prob}")
        joint_prob *= prob

    # print(f"JOINT PROBABILITY: {joint_prob}")
    return joint_prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    for name in probabilities:
        gene_number = (
            1 if name in one_gene else 2 if name in two_genes else 0)
        trait = (True if name in have_trait else False)
        # sum of all joint probabilities
        probabilities[name]["gene"][gene_number] += p
        probabilities[name]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    for name in probabilities:
        gene_sum = sum(probabilities[name]["gene"].values())
        trait_sum = sum(probabilities[name]["trait"].values())

        if gene_sum != 1:
            for gene in probabilities[name]["gene"]:
                probabilities[name]["gene"][gene] /= gene_sum
        if trait_sum != 1:
            for trait in probabilities[name]["trait"]:
                probabilities[name]["trait"][trait] /= trait_sum


if __name__ == "__main__":
    main()
