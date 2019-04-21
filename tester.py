from implementation import return_orders_list
import called_time


def tester():
    counter = called_time.Counter()

    liste_choix = [[5, 0, 3], [5, 1, 4], [5, 2, 6], [10, 1, 6], [10, 2, 10], [15, 3, 11], [15, 4, 15]]
    #reponse []

    # liste_choix = [[0, 5, 3], [1, 5, 6], [1, 10, 6], [2, 5, 6], [2, 10, 10], [3, 15, 11], [4, 15, 15]]
    #reponse []

    # liste_choix = [[0, 5, 3], [1, 5, 6], [1, 10, 6], [2, 5, 6], [2, 10, 10], [3, 15, 11], [4, 15, 15]]
    #reponse []

    print(return_orders_list(liste_choix, counter))
    print("\n" + str(counter.count))


tester()
