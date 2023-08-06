import ctypes
import string
import os

PATH = os.path.dirname(__file__)
cgaddag = ctypes.cdll.LoadLibrary(os.path.join(PATH, "cgaddag.so"))


class cResult(ctypes.Structure):
    pass

cResult._fields_ = [("str", ctypes.c_char_p),
                    ("next", ctypes.POINTER(cResult))]


class cGADDAG(ctypes.Structure):
    _fields_ = [("num_words", ctypes.c_uint),
                ("num_nodes", ctypes.c_uint),
                ("num_edges", ctypes.c_uint),
                ("edges", ctypes.POINTER(ctypes.c_uint)),
                ("letter_sets", ctypes.POINTER(ctypes.c_uint))]


cgaddag.newGADDAG.restype = ctypes.POINTER(cGADDAG)
cgaddag.add_word.restype = ctypes.c_void_p
cgaddag.add_word.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_char_p]
cgaddag.has.restype = ctypes.c_bool
cgaddag.has.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_char_p]
cgaddag.starts_with.restype = ctypes.POINTER(cResult)
cgaddag.starts_with.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_char_p]
cgaddag.contains.restype = ctypes.POINTER(cResult)
cgaddag.contains.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_char_p]
cgaddag.ends_with.restype = ctypes.POINTER(cResult)
cgaddag.ends_with.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_char_p]
cgaddag.edges.restype = ctypes.c_void_p
cgaddag.edges.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_uint, ctypes.c_char_p]
cgaddag.letter_set.restype = ctypes.c_void_p
cgaddag.letter_set.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_uint, ctypes.c_char_p]
cgaddag.is_end.restype = ctypes.c_bool
cgaddag.is_end.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_uint, ctypes.c_char]
cgaddag.follow_edge.restype = ctypes.c_uint
cgaddag.follow_edge.argtypes = [ctypes.POINTER(cGADDAG), ctypes.c_uint, ctypes.c_char]
cgaddag.destroy_result.restype = ctypes.c_void_p
cgaddag.destroy_result.argtypes = [ctypes.POINTER(cResult)]


class Node():
    """A node in a GADDAG."""
    def __init__(self, gdg, node):
        self.node = node
        self.gdg = gdg

    def __str__(self):
        return "[{}] {}".format(", ".join(sorted([edge for edge in self])),
                                self.is_end)

    def __len__(self):
        return len(self.edges)

    def __iter__(self):
        for char in self.edges:
            yield char

    def __contains__(self, char):
        char = char.lower()
        return char in self.edges

    def __getitem__(self, char):
        char = char.lower()
        next_node = cgaddag.follow_edge(self.gdg, self.node, char.encode("ascii"))

        if not next_node:
            raise KeyError(char)

        return Node(self.gdg, next_node)

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if self.letter_set != other.letter_set or self.edges != other.edges:
            return False

        for child in self:
            if self[child] != other[child]:
                return False

        return True

    @property
    def edges(self):
        """Return the edges of this node."""
        edge_str = ctypes.create_string_buffer(27)

        cgaddag.edges(self.gdg, self.node, edge_str)

        return [char for char in edge_str.value.decode("ascii")]

    @property
    def letter_set(self):
        """Return the letter set of this node."""
        end_str = ctypes.create_string_buffer(27)

        cgaddag.letter_set(self.gdg, self.node, end_str)

        return [char for char in end_str.value.decode("ascii")]

    def is_end(self, char):
        """Return `True` if this node is an end node, `False` otherwise."""
        char = char.lower()

        return bool(cgaddag.is_end(self.gdg, self.node, char.encode("ascii")))

    def follow(self, chars):
        """
        Traverse the GADDAG to the node at the end of the given characters.

        Args:
            chars: An string of characters to traverse in the GADDAG.

        Returns:
            The Node which is found by traversing the tree.
        """
        chars = chars.lower()

        node = self.node
        for char in chars:
            node = cgaddag.follow_edge(self.gdg, node, char.encode("ascii"))
            if not node:
                raise KeyError(char)

        return Node(self.gdg, node)


class GADDAG():
    """A data structure that allows extremely fast searching of words."""
    def __init__(self, words=None):
        self.gdg = cgaddag.newGADDAG().contents
        self.num_words = 0

        if words:
            if type(words) is str:
                raise TypeError("Input must be an iterable of strings")

            for word in words:
                self.add_word(word)

    def __len__(self):
        return self.num_words

    def __contains__(self, word):
        word = word.lower()

        return cgaddag.has(self.gdg, word.encode(encoding="ascii"))

    def __iter__(self):
        for word in self.ends_with(""):
            yield word

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if len(self) != len(other):
            return False

        return self.root == other.root

    @property
    def root(self):
        """Returns the root node of the GADDAG."""
        return Node(self.gdg, 0)

    def starts_with(self, prefix):
        """
        Find all words starting with a prefix.

        Args:
            prefix: A prefix to be searched for.

        Returns:
            A set of all words found.
        """
        prefix = prefix.lower()
        found_words = []

        res = cgaddag.starts_with(self.gdg, prefix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.destroy_result(res)
        return found_words

    def contains(self, sub):
        """
        Find all words containing a substring.

        Args:
            sub: A substring to be searched for.

        Returns:
            A set of all words found.
        """
        sub = sub.lower()
        found_words = set()

        res = cgaddag.contains(self.gdg, sub.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.add(word)
            tmp = tmp.contents.next

        cgaddag.destroy_result(res)
        return list(found_words)

    def ends_with(self, suffix):
        """
        Find all words ending with a suffix.

        Args:
            suffix: A suffix to be searched for.

        Returns:
            A set of all words found.
        """
        suffix = suffix.lower()
        found_words = []

        res = cgaddag.ends_with(self.gdg, suffix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.destroy_result(res)
        return found_words

    def add_word(self, word):
        """
        Add a word to the GADDAG.

        Args:
            word: A word to be added to the GADDAG.
        """
        word = word.lower()

        if not (word.isascii() and word.isalpha()):
            raise ValueError(f"Invalid character in word '{word}'")

        self.num_words += 1

        word = word.encode(encoding="ascii")
        cgaddag.add_word(self.gdg, word)

