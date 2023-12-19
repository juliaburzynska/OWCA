class Node:
    def __init__(self, node_id, x, y):
        self.id = node_id
        self.x = x
        self.y = y

class FromConfig:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_config(self):
        nodes = []
        n_value = None
        with open(self.file_path, 'r') as config_file:
            lines = config_file.readlines()
        for line in lines:
            if not line.startswith('#'):
                if ',' in line:
                    node_data = line.strip().split(',')
                    node = Node(int(node_data[0]), int(node_data[1]), int(node_data[2]))
                    nodes.append(node)
                elif line.startswith("n="):
                    n_value = int(line[2:])
        
        return n_value, nodes

fromConfig = FromConfig('config.txt')
n, nodes = fromConfig.read_config()



print(nodes[1].id)
print(n)