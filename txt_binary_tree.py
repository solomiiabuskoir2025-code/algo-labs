import os


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = str(value)
        self.left = left
        self.right = right

    @staticmethod
    def build_from_inorder(inorder):
        if not inorder:
            return None
        mid = len(inorder) // 2
        node = BinaryTree(inorder[mid])
        node.left = BinaryTree.build_from_inorder(inorder[:mid])
        node.right = BinaryTree.build_from_inorder(inorder[mid + 1:])
        return node

    def __str__(self):
        def g(node): return node.value if node else "  "

        root_val = self.value

        l_mid = g(self.left)
        l_up = g(self.left.left) if self.left else "  "
        l_down = g(self.left.right) if self.left else "  "
        l_tip = g(self.left.right.left) if self.left and self.left.right else "  "

        r_mid = g(self.right)
        r_up = g(self.right.left) if self.right else "  "
        r_down = g(self.right.right) if self.right else "  "
        r_tip = g(self.right.right.right) if self.right and self.right.right else "  "

        lines = [
            f"   {l_up:<2}                    {r_up:>2}   ",
            f"     \\                  /      ",
            f"      {l_mid:<2}  —   {root_val}   —  {r_mid:>2}       ",
            f"     /                  \\      ",
            f"   {l_down:<2}                    {r_down:>2}   ",
            f"   /                       \\    ",
            f"{l_tip:<2}                   {r_tip:>2} "
        ]
        return "\n".join(lines)


def read_data_from_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("10 25 28 30 50 60 75 90 80")
        print(f"Файл {filename} створено автоматично.")

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().split()
    return content


if __name__ == "__main__":
    file_path = "derevo.txt"

    numbers = read_data_from_file(file_path)

    if numbers:
        my_tree = BinaryTree.build_from_inorder(numbers)

        print(f"\nДерево-метелик з файлу {file_path}:\n")
        print(my_tree)
    else:
        print("Файл порожній!")