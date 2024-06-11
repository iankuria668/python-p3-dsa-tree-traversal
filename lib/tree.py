class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    pass

  def breadth_first_traversal(self, node):
    result = []
    nodes_to_visit = [node]

    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      result.append(node)
      nodes_to_visit  =  nodes_to_visit + node['children']
    
    return result


child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}
print(breadth_first_traversal(root))