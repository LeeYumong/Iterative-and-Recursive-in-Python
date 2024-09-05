import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('binary_tree.db')
cursor = conn.cursor()

# Execute the schema to create the table
with open('binary_tree_schema.sql', 'r') as f:
    cursor.executescript(f.read())
conn.commit()

# Function to insert a node into the binary tree
def insert_node(value, left_id=None, right_id=None):
    cursor.execute('''
    INSERT INTO TreeNode (value, left_id, right_id)
    VALUES (?, ?, ?)
    ''', (value, left_id, right_id))
    conn.commit()
    return cursor.lastrowid

# Recursive function for in-order traversal of the binary tree
def recursive_in_order_traversal(node_id):
    if node_id is None:
        return
    cursor.execute('SELECT * FROM TreeNode WHERE id = ?', (node_id,))
    node = cursor.fetchone()
    if node:
        recursive_in_order_traversal(node[2])  # Visit left child
        print(node[1])  # Print value of the current node
        recursive_in_order_traversal(node[3])  # Visit right child

# Iterative function for in-order traversal of the binary tree
def iterative_in_order_traversal(start_node_id):
    stack = []
    current_node_id = start_node_id

    while stack or current_node_id:
        while current_node_id:
            stack.append(current_node_id)
            cursor.execute('SELECT left_id FROM TreeNode WHERE id = ?', (current_node_id,))
            current_node_id = cursor.fetchone()[0]

        current_node_id = stack.pop()
        cursor.execute('SELECT * FROM TreeNode WHERE id = ?', (current_node_id,))
        node = cursor.fetchone()
        print(node[1])  # Print value of the current node
        cursor.execute('SELECT right_id FROM TreeNode WHERE id = ?', (current_node_id,))
        current_node_id = cursor.fetchone()[0]

def main():
    # Insert nodes into the binary tree
    root_id = insert_node(10)
    left_id = insert_node(5)
    right_id = insert_node(15)
    insert_node(2, left_id=left_id)
    insert_node(7, right_id=left_id)
    insert_node(12, left_id=right_id)
    insert_node(20, right_id=right_id)

    print("Recursive In-Order Traversal:")
    recursive_in_order_traversal(root_id)

    print("\nIterative In-Order Traversal:")
    iterative_in_order_traversal(root_id)

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
