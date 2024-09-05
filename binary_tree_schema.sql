-- Schema for storing nodes in a binary tree
CREATE TABLE IF NOT EXISTS TreeNode (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value INTEGER NOT NULL,
    left_id INTEGER,
    right_id INTEGER,
    FOREIGN KEY (left_id) REFERENCES TreeNode(id),
    FOREIGN KEY (right_id) REFERENCES TreeNode(id)
);
