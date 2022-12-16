from re import findall
from typing import IO, Tuple
from time import time

# Expects y-values as keys and a tuple of ints as values representing covered ranges of x for y
class Intervals:
    def __init__(self, lower_cap: int, upper_cap: int):
        self.row = {}
        self.upper_cap = upper_cap
        self.lower_cap = lower_cap

    def __get_sorted_intervals(self):
        for y, row in self.row.items():
            yield y, sorted(row)

    def add_interval(self, y: int, interval: Tuple[int, int]):    
        if row := self.row.get(y):
            row.append(interval)
        else:
            self.row[y] = [interval] 

    # Unions sorted intervals. Returns any value found missing in the interval [lower_cap, upper_cap]
    def find_distress_beacon(self):
        for y, row in self.__get_sorted_intervals():
            stack = [row[0]]

            for row in row[1:]:
                prev_lower_bound, prev_upper_bound = stack.pop()
                lower_bound, upper_bound = row

                if prev_upper_bound + 1 < lower_bound:
                    return prev_upper_bound + 1, y
                elif upper_bound > prev_upper_bound:
                    stack.append((prev_lower_bound, upper_bound))
                else:
                    stack.append((prev_lower_bound, prev_upper_bound))

            lower_bound, upper_bound = stack.pop()
            if lower_bound > self.lower_cap:
                  return lower_bound, y
            elif upper_bound < self.upper_cap:
                return upper_bound, y
            

# Returns length of space searched at row which does not contain a beacon
def search_space_size_on_row(row: int, file: IO[str]) -> int:
    row_cannot_contain_beacon_at = set()
    beacons = set()

    with open(file, 'r') as file:
        for line in file:
            x, y, dx, dy = map(int, findall(r'-?\d+', line)) # Sensor = (x, y), Beacon = (dx, dy)
            manhattan_distance = abs(x - dx) + abs(y - dy) 
            beacons.add((dx, dy))

            # Sensor expands outwards in y-axis at rate 1 + 2*(manhattan distance to beacon)
            sensor_row_len = 1 + manhattan_distance*2 

            # At equal x, search distance is withdrawn by 2*|y-dy| where dy is row to be investigated
            row_delta = abs(y - row)  
            row_len = sensor_row_len - (2 * row_delta) 
            
            # If sensor search space reaches row: 
            if row_len > 0: 
                start = x - (row_len // 2)
                end = x + (row_len // 2)
                row_cannot_contain_beacon_at.update(set((x, row) for x in range(start, end+1)))
    
    return len(row_cannot_contain_beacon_at.difference(beacons))

# Identifies distress beacon coordinates by identifying every point it could not be at
def find_distress_beacon(file: IO[str], lower_cap: int, upper_cap: int):
    intervals = Intervals(lower_cap, upper_cap)

    with open(file, 'r') as file:
        for line in file:
            x, y, dx, dy = map(int, findall(r'-?\d+', line)) # Sensor = (x, y), Beacon = (dx, dy)
            manhattan_distance = abs(x - dx) + abs(y - dy) 

            # Sensor expands outwards in y-axis at rate 1 + 2*(manhattan distance to beacon)
            sensor_row_len = 1 + manhattan_distance*2 
            lowest_row = max(lower_cap, y - manhattan_distance)
            highest_row = min(upper_cap, y + manhattan_distance)

            # For every row reached by the search space
            for row in range(lowest_row, highest_row+1):

                # At equal x, search distance is withdrawn by 2*|y-row| where row is to be investigated
                row_delta = abs(y - row)  
                row_len = sensor_row_len - (2 * row_delta) 

                # Add interval of search space to intervals
                start = max(lower_cap, x - (row_len // 2))
                end = min(x + (row_len // 2), upper_cap)
                intervals.add_interval(row, (start, end))
    
    return intervals.find_distress_beacon()

def main():
    row = 2000000 # y-line on which to evaluate how many points have been searched for beacon
    lower_cap = 0 
    upper_cap = 4000000
    file = "input.txt"
    print("Search nodes without beacon on row 2.000.000:", search_space_size_on_row(row, file))
    distress_beacon = find_distress_beacon(file, lower_cap, upper_cap)
    print("Distress beacon found at:", distress_beacon)
    print("Tuning signal:", distress_beacon[0] * 4000000 + distress_beacon[1])


if __name__ == "__main__":
    start_time = time()
    main()
    print("Runtime: ", time() - start_time, "s", sep='')
