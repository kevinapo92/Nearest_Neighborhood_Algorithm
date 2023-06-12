import pandas as pd


class tours:
    def __init__(self, dist_matrix):
        self.dist_matrix = dist_matrix
        self.V = len(dist_matrix)
        self.tours = []
        self.lengths = []

    def nearest_neighbour(self):
        for i in range(self.V):
            tour = [] # start with an empty tour
            tour.append(i)
            unvisited = list(range(self.V)) # mark every city as unvisited
            tour_length = 0
            current_city = i # start with city i
            unvisited.remove(i)
            while unvisited: # while an unvisited city exists
                min_dist = float("Inf")
                next = -1
                for j in unvisited:
                    min_dist = min(min_dist, self.dist_matrix[current_city][j])
                    if min_dist == self.dist_matrix[current_city][j]:
                        next = j # find the nearest unvisited city (city with min distance to the current city)
                tour.append(next) # add this city to the tour and update length and unvisited cities
                tour_length += self.dist_matrix[current_city][next]
                unvisited.remove(next)
                current_city = next
            tour.append(i)
            self.tours.append(tour)
            tour_length += self.dist_matrix[next][i]
            self.lengths.append(tour_length)

        shortest = float("Inf")
        shortest_tour = None
        for t in range(self.V):
            shortest = min(shortest, self.lengths[t])
            if shortest == self.lengths[t]:
                shortest_tour = self.tours[t] # find the shortest tour

        print(f"Shortest tour is {shortest_tour}")
        print(f"With distance {shortest}")


if __name__ == "__main__":
    distances = pd.read_excel("TSP_input.xlsx", index_col=0)
    dist_matrix = distances.values.tolist()

    nn_heuristic = tours(dist_matrix)
    nn_heuristic.nearest_neighbour()
