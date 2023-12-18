import numpy as np
from scipy.optimize import minimize


class Map:
    def __init__(self, receiver_list, distance):
        self.receiver_list = receiver_list
        self.distance = distance

    def objective_function(self, point):
        total_distance = 0
        centers = np.array(self.receiver_list)
        radii = np.array(self.distance)
        for center, radius in zip(centers, radii):
            distance = np.linalg.norm(point - center) - radius
            total_distance += distance ** 2
        return total_distance

    def Localize(self):

        minimization_function = lambda point: Map.objective_function(self, point)
        initial_guess = np.array([0.0, 0.0])
        result = minimize(minimization_function, initial_guess, method='L-BFGS-B')
        return result.x


if __name__ == "__main__":  #przykładowe użycie, przed skończeniem projektu usunąć
    map = Map([[1, 1], [-1, 1], [-1, -2],[2,5],[-3,-1],[20,20]], [1, 1, 2,5,4,1])
    print(map.Localize())
