"""Pattern-first interview training.

GOOGLE-FOCUSED ROADMAP

Do not. postpone graphs until every exotic DP track is finished Interleave the
four foundational DP families with core graph traversal/modeling immediately.

PHASE 1 -- core DP + core graph in parallel:
  DP: dp_linear_take_skip, dp_grid, dp_two_sequence,
      dp_knapsack_coin_change
  GRAPH: dfs_flood_fill, bfs_shortest_path, multi_source_bfs, graph_modeling

PHASE 2 -- trees + advanced graph:
  tree_dfs, tree_bfs, topological_sort, union_find, dijkstra,
  state_space_search

PHASE 3 -- composable array/string fundamentals:
  sliding_window, prefix_sum_hashmap, hashing, two_pointers, intervals,
  heap_top_k

PHASE 4 -- Google-useful secondary topics:
  trie, backtracking, binary_search_answer, greedy, stream_design

PHASE 5 -- depth / lower-frequency material:
  dp_lis, dp_interval_partition, dp_state_machine, minimum_spanning_tree,
  monotonic_stack, linked_list_pointers, sweep_line_ordered_intervals

Suggested daily mix while finishing DP:
  python3 leetcode.py learn dp
  python3 leetcode.py learn graph
  python3 leetcode.py redo
  python3 leetcode.py random dp graph tree arrays_strings

Broad category aliases are supported. Examples:
  python3 leetcode.py learn dp             # next fresh problem in DP roadmap
  python3 leetcode.py practice dp          # any DP track
  python3 leetcode.py redo graph           # any due graph review
  python3 leetcode.py random dp graph       # hidden pattern from both groups
  python3 leetcode.py learn dp_knapsack_coin_change  # one narrow track

Daily loop:
  python3 leetcode.py learn sliding_window
  python3 leetcode.py record 209 hinted     # needed meaningful help
  python3 leetcode.py record 209 solved     # independent, but slow/difficult
  python3 leetcode.py record 209 mastered --follow-up
  python3 leetcode.py practice sliding_window
  python3 leetcode.py random                # pattern intentionally hidden
  python3 leetcode.py redo                  # spaced failures/diagnostics
  python3 leetcode.py redo --within 1w      # attempts from the last week

Use `patterns` and `progress` to inspect the curriculum. Progress is stored in
leetcode_progress.json next to this file; Accepted is deliberately not tracked.

MASTERED requires all five:
  1. Derived independently
  2. Implemented without major bugs
  3. Explained time and space complexity
  4. Explained the invariant / why the algorithm works
  5. Answered one unseen follow-up
"""

import argparse
import json
import random
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path


# ============================================================
# PROBLEM BANK
# ============================================================
#
# Format:
# (leetcode_id, name, (tags...))
#
# A problem can belong to multiple categories.
# ============================================================

PROBLEMS = [

    # ========================================================
    # ARRAYS / HASH MAPS
    # ========================================================

    (1, "Two Sum", ("array", "hash_map")),
    (49, "Group Anagrams", ("array", "hash_map", "string")),
    (128, "Longest Consecutive Sequence", ("array", "hash_set")),
    (169, "Majority Element", ("array",)),
    (217, "Contains Duplicate", ("array", "hash_set")),
    (238, "Product of Array Except Self", ("array", "prefix")),
    (347, "Top K Frequent Elements", ("array", "hash_map", "heap")),
    (380, "Insert Delete GetRandom O(1)", ("hash_map", "design")),
    (560, "Subarray Sum Equals K", ("array", "prefix", "hash_map")),
    (525, "Contiguous Array", ("array", "prefix", "hash_map")),
    (41, "First Missing Positive", ("array",)),


    # ========================================================
    # TWO POINTERS
    # ========================================================

    (11, "Container With Most Water", ("two_pointers", "array")),
    (15, "3Sum", ("two_pointers", "array")),
    (16, "3Sum Closest", ("two_pointers", "array")),
    (42, "Trapping Rain Water", ("two_pointers", "stack")),
    (125, "Valid Palindrome", ("two_pointers", "string")),
    (167, "Two Sum II", ("two_pointers", "array")),
    (283, "Move Zeroes", ("two_pointers", "array")),
    (287, "Find the Duplicate Number", ("two_pointers", "linked_list_pattern")),


    # ========================================================
    # SLIDING WINDOW
    # ========================================================

    (3, "Longest Substring Without Repeating Characters",
        ("sliding_window", "string")),

    (76, "Minimum Window Substring",
        ("sliding_window", "string", "hash_map")),

    (209, "Minimum Size Subarray Sum",
        ("sliding_window", "array")),

    (239, "Sliding Window Maximum",
        ("sliding_window", "deque")),

    (424, "Longest Repeating Character Replacement",
        ("sliding_window", "string")),

    (567, "Permutation in String",
        ("sliding_window", "string")),

    (904, "Fruit Into Baskets",
        ("sliding_window", "array")),


    # ========================================================
    # STACK / MONOTONIC STACK
    # ========================================================

    (20, "Valid Parentheses", ("stack",)),
    (84, "Largest Rectangle in Histogram", ("stack", "monotonic_stack")),
    (150, "Evaluate Reverse Polish Notation", ("stack",)),
    (155, "Min Stack", ("stack", "design")),
    (739, "Daily Temperatures", ("stack", "monotonic_stack")),
    (853, "Car Fleet", ("stack",)),
    (907, "Sum of Subarray Minimums", ("stack", "monotonic_stack")),
    (1249, "Minimum Remove to Make Valid Parentheses", ("stack", "string")),


    # ========================================================
    # BINARY SEARCH
    # ========================================================

    (4, "Median of Two Sorted Arrays", ("binary_search", "hard")),
    (33, "Search in Rotated Sorted Array", ("binary_search",)),
    (34, "Find First and Last Position of Element", ("binary_search",)),
    (69, "Sqrt(x)", ("binary_search",)),
    (74, "Search a 2D Matrix", ("binary_search", "matrix")),
    (153, "Find Minimum in Rotated Sorted Array", ("binary_search",)),
    (704, "Binary Search", ("binary_search",)),

    (875, "Koko Eating Bananas",
        ("binary_search", "binary_search_answer")),

    (1011, "Capacity To Ship Packages Within D Days",
        ("binary_search", "binary_search_answer")),

    (410, "Split Array Largest Sum",
        ("binary_search", "binary_search_answer", "hard")),


    # ========================================================
    # LINKED LIST
    # ========================================================

    (2, "Add Two Numbers", ("linked_list",)),
    (19, "Remove Nth Node From End of List", ("linked_list", "two_pointers")),
    (21, "Merge Two Sorted Lists", ("linked_list",)),
    (23, "Merge k Sorted Lists", ("linked_list", "heap", "hard")),
    (25, "Reverse Nodes in k-Group", ("linked_list", "hard")),
    (83, "Remove Duplicates from Sorted List", ("linked_list",)),
    (138, "Copy List with Random Pointer", ("linked_list", "hash_map")),
    (141, "Linked List Cycle", ("linked_list", "two_pointers")),
    (143, "Reorder List", ("linked_list", "two_pointers")),
    (146, "LRU Cache", ("linked_list", "hash_map", "design")),
    (206, "Reverse Linked List", ("linked_list",)),


    # ========================================================
    # INTERVALS
    # ========================================================

    (56, "Merge Intervals", ("intervals",)),
    (57, "Insert Interval", ("intervals",)),
    (435, "Non-overlapping Intervals", ("intervals", "greedy")),
    (452, "Minimum Number of Arrows to Burst Balloons",
        ("intervals", "greedy")),


    # ========================================================
    # GREEDY
    # ========================================================

    (45, "Jump Game II", ("greedy", "array")),
    (53, "Maximum Subarray", ("greedy", "dp")),
    (55, "Jump Game", ("greedy", "array")),
    (121, "Best Time to Buy and Sell Stock", ("greedy", "array")),
    (122, "Best Time to Buy and Sell Stock II", ("greedy", "array")),
    (134, "Gas Station", ("greedy",)),
    (334, "Increasing Triplet Subsequence", ("greedy",)),
    (621, "Task Scheduler", ("greedy", "heap")),


    # ========================================================
    # HEAP / PRIORITY QUEUE
    # ========================================================

    (215, "Kth Largest Element in an Array", ("heap", "quickselect")),
    (295, "Find Median from Data Stream", ("heap", "design", "hard")),
    (347, "Top K Frequent Elements", ("heap", "hash_map")),
    (621, "Task Scheduler", ("heap", "greedy")),
    (703, "Kth Largest Element in a Stream", ("heap", "design")),
    (767, "Reorganize String", ("heap", "greedy")),
    (973, "K Closest Points to Origin", ("heap",)),
    (1046, "Last Stone Weight", ("heap",)),


    # ========================================================
    # BACKTRACKING
    # ========================================================

    (17, "Letter Combinations of a Phone Number", ("backtracking",)),
    (22, "Generate Parentheses", ("backtracking",)),
    (39, "Combination Sum", ("backtracking",)),
    (40, "Combination Sum II", ("backtracking",)),
    (46, "Permutations", ("backtracking",)),
    (47, "Permutations II", ("backtracking",)),
    (78, "Subsets", ("backtracking",)),
    (79, "Word Search", ("backtracking", "matrix")),
    (90, "Subsets II", ("backtracking",)),
    (131, "Palindrome Partitioning", ("backtracking", "string")),


    # ========================================================
    # TREES / BST
    # ========================================================

    (94, "Binary Tree Inorder Traversal", ("tree", "dfs")),
    (98, "Validate Binary Search Tree", ("tree", "bst")),
    (100, "Same Tree", ("tree", "dfs")),
    (101, "Symmetric Tree", ("tree", "dfs")),
    (102, "Binary Tree Level Order Traversal", ("tree", "bfs")),
    (104, "Maximum Depth of Binary Tree", ("tree", "dfs")),

    (105, "Construct Binary Tree from Preorder and Inorder Traversal",
        ("tree", "dfs")),

    (110, "Balanced Binary Tree", ("tree", "dfs")),
    (112, "Path Sum", ("tree", "dfs")),
    (118, "Pascal's Triangle", ("dp", "dp_grid")),
    (119, "Pascal's Triangle II", ("dp", "dp_grid")),
    (114, "Flatten Binary Tree to Linked List", ("tree", "dfs")),
    (124, "Binary Tree Maximum Path Sum", ("tree", "dfs", "dp", "hard")),
    (199, "Binary Tree Right Side View", ("tree", "bfs")),
    (222, "Count Complete Tree Nodes", ("tree", "binary_search")),
    (226, "Invert Binary Tree", ("tree", "dfs")),
    (230, "Kth Smallest Element in a BST", ("tree", "bst")),
    (236, "Lowest Common Ancestor of a Binary Tree", ("tree", "dfs")),

    (297, "Serialize and Deserialize Binary Tree",
        ("tree", "dfs", "design", "hard")),

    (314, "Binary Tree Vertical Order Traversal", ("tree", "bfs")),
    (337, "House Robber III", ("tree", "dp")),
    (437, "Path Sum III", ("tree", "dfs", "prefix")),
    (450, "Delete Node in a BST", ("tree", "bst")),
    (543, "Diameter of Binary Tree", ("tree", "dfs")),
    (572, "Subtree of Another Tree", ("tree", "dfs")),
    (637, "Average of Levels in Binary Tree", ("tree", "bfs")),
    (700, "Search in a Binary Search Tree", ("tree", "bst")),
    (863, "All Nodes Distance K in Binary Tree", ("tree", "graph", "bfs")),
    (1448, "Count Good Nodes in Binary Tree", ("tree", "dfs")),


    # ========================================================
    # GRAPHS — DFS / BFS
    # ========================================================

    (127, "Word Ladder", ("graph", "bfs")),
    (130, "Surrounded Regions", ("graph", "dfs", "matrix")),
    (133, "Clone Graph", ("graph", "dfs", "bfs")),
    (200, "Number of Islands", ("graph", "dfs", "bfs", "matrix")),
    (417, "Pacific Atlantic Water Flow", ("graph", "dfs", "matrix")),
    (695, "Max Area of Island", ("graph", "dfs", "matrix")),
    (752, "Open the Lock", ("graph", "bfs")),
    (994, "Rotting Oranges", ("graph", "bfs", "matrix")),

    (1091, "Shortest Path in Binary Matrix",
        ("graph", "bfs", "matrix")),

    (864, "Shortest Path to Get All Keys",
        ("graph", "bfs", "state_search", "hard")),


    # ========================================================
    # TOPOLOGICAL SORT / DAG
    # ========================================================

    (207, "Course Schedule", ("graph", "topological_sort")),
    (210, "Course Schedule II", ("graph", "topological_sort")),
    (269, "Alien Dictionary", ("graph", "topological_sort", "hard")),
    (329, "Longest Increasing Path in a Matrix",
        ("graph", "dfs", "dp", "dag", "hard")),


    # ========================================================
    # UNION FIND
    # ========================================================

    (323, "Number of Connected Components in an Undirected Graph",
        ("graph", "union_find")),

    (547, "Number of Provinces", ("graph", "union_find")),
    (684, "Redundant Connection", ("graph", "union_find")),
    (721, "Accounts Merge", ("graph", "union_find")),


    # ========================================================
    # SHORTEST PATH / WEIGHTED GRAPH
    # ========================================================

    (399, "Evaluate Division", ("graph", "weighted_graph")),
    (743, "Network Delay Time", ("graph", "dijkstra")),
    (787, "Cheapest Flights Within K Stops", ("graph", "shortest_path")),


    # ========================================================
    # TRIE
    # ========================================================

    (208, "Implement Trie", ("trie", "design")),
    (211, "Design Add and Search Words Data Structure", ("trie", "design")),
    (212, "Word Search II", ("trie", "backtracking", "hard")),
    (421, "Maximum XOR of Two Numbers in an Array",
        ("trie", "bit_manipulation")),


    # ========================================================
    # DP — LINEAR
    # ========================================================

    (70, "Climbing Stairs", ("dp", "dp_linear")),
    (91, "Decode Ways", ("dp", "dp_linear")),
    (198, "House Robber", ("dp", "dp_linear", "dp_take_skip")),
    (213, "House Robber II", ("dp", "dp_linear", "dp_take_skip")),
    (740, "Delete and Earn", ("dp", "dp_take_skip")),
    (746, "Min Cost Climbing Stairs", ("dp", "dp_linear")),


    # ========================================================
    # DP — GRID
    # ========================================================

    (62, "Unique Paths", ("dp", "dp_grid")),
    (63, "Unique Paths II", ("dp", "dp_grid")),
    (64, "Minimum Path Sum", ("dp", "dp_grid")),
    (120, "Triangle", ("dp", "dp_grid", "dag")),
    (221, "Maximal Square", ("dp", "dp_grid")),


    # ========================================================
    # DP — TWO SEQUENCES
    # ========================================================

    (72, "Edit Distance", ("dp", "dp_two_sequence")),
    (115, "Distinct Subsequences", ("dp", "dp_two_sequence", "hard")),
    (583, "Delete Operation for Two Strings", ("dp", "dp_two_sequence")),
    (712, "Minimum ASCII Delete Sum for Two Strings",
        ("dp", "dp_two_sequence")),

    (1035, "Uncrossed Lines", ("dp", "dp_two_sequence")),
    (1143, "Longest Common Subsequence", ("dp", "dp_two_sequence")),


    # ========================================================
    # DP — KNAPSACK / SUBSET
    # ========================================================

    (416, "Partition Equal Subset Sum", ("dp", "dp_knapsack")),
    (474, "Ones and Zeroes", ("dp", "dp_knapsack")),
    (494, "Target Sum", ("dp", "dp_knapsack")),
    (1049, "Last Stone Weight II", ("dp", "dp_knapsack")),


    # ========================================================
    # DP — COIN CHANGE
    # ========================================================

    (279, "Perfect Squares", ("dp", "dp_coin_change")),
    (322, "Coin Change", ("dp", "dp_coin_change")),
    (377, "Combination Sum IV", ("dp", "dp_coin_change")),
    (518, "Coin Change II", ("dp", "dp_coin_change")),


    # ========================================================
    # DP — LIS / SINGLE SEQUENCE
    # ========================================================

    (300, "Longest Increasing Subsequence", ("dp", "dp_lis")),
    (673, "Number of Longest Increasing Subsequence", ("dp", "dp_lis")),
    (646, "Maximum Length of Pair Chain", ("dp", "dp_lis")),


    # ========================================================
    # DP — PALINDROME / INTERVAL
    # ========================================================

    (5, "Longest Palindromic Substring", ("dp", "dp_interval", "string")),
    (516, "Longest Palindromic Subsequence", ("dp", "dp_interval")),
    (647, "Palindromic Substrings", ("dp", "dp_interval")),
    (1312, "Minimum Insertion Steps to Make a String Palindrome",
        ("dp", "dp_interval")),


    # ========================================================
    # DP — STATE MACHINE
    # ========================================================

    (123, "Best Time to Buy and Sell Stock III", ("dp", "dp_state_machine")),
    (188, "Best Time to Buy and Sell Stock IV", ("dp", "dp_state_machine")),
    (309, "Best Time to Buy and Sell Stock with Cooldown",
        ("dp", "dp_state_machine")),

    (714, "Best Time to Buy and Sell Stock with Transaction Fee",
        ("dp", "dp_state_machine")),


    # ========================================================
    # DP — PARTITION
    # ========================================================

    (139, "Word Break", ("dp", "dp_partition")),
    (312, "Burst Balloons", ("dp", "dp_partition", "hard")),
    (1039, "Minimum Score Triangulation of Polygon",
        ("dp", "dp_partition")),

    (1547, "Minimum Cost to Cut a Stick",
        ("dp", "dp_partition")),


    # ========================================================
    # BIT MANIPULATION
    # ========================================================

    (136, "Single Number", ("bit_manipulation",)),
    (190, "Reverse Bits", ("bit_manipulation",)),
    (191, "Number of 1 Bits", ("bit_manipulation",)),
    (268, "Missing Number", ("bit_manipulation",)),
    (338, "Counting Bits", ("bit_manipulation", "dp")),
    (371, "Sum of Two Integers", ("bit_manipulation",)),


    # ========================================================
    # MATRIX
    # ========================================================

    (36, "Valid Sudoku", ("matrix", "hash_set")),
    (48, "Rotate Image", ("matrix",)),
    (54, "Spiral Matrix", ("matrix",)),
    (73, "Set Matrix Zeroes", ("matrix",)),


    # ========================================================
    # STRINGS
    # ========================================================

    (14, "Longest Common Prefix", ("string",)),
    (151, "Reverse Words in a String", ("string",)),
    (205, "Isomorphic Strings", ("string", "hash_map")),
    (242, "Valid Anagram", ("string", "hash_map")),
    (271, "Encode and Decode Strings", ("string", "design")),
    (392, "Is Subsequence", ("string", "two_pointers", "dp")),
    (443, "String Compression", ("string", "two_pointers")),


    # ========================================================
    # DESIGN
    # ========================================================

    (146, "LRU Cache", ("design", "hash_map", "linked_list")),
    (155, "Min Stack", ("design", "stack")),
    (208, "Implement Trie", ("design", "trie")),
    (295, "Find Median from Data Stream", ("design", "heap")),
    (380, "Insert Delete GetRandom O(1)", ("design", "hash_map")),
    (981, "Time Based Key-Value Store", ("design", "binary_search")),
]

# High-value additions for Google-style interviews: graph modeling and
# follow-ups, multi-source/state-space BFS, MST, interval event processing, and
# fresh Medium variations of core patterns. These are not a leaked question
# list; they are transferable representatives of repeatedly reported skills.
PROBLEMS += [
    (51, "N-Queens", ("backtracking", "hard")),
    (93, "Restore IP Addresses", ("backtracking", "string")),
    (126, "Word Ladder II", ("graph", "bfs", "backtracking", "hard")),
    (149, "Max Points on a Line", ("geometry", "hash_map", "hard")),
    (162, "Find Peak Element", ("binary_search",)),
    (218, "The Skyline Problem", ("sweep_line", "heap", "hard")),
    (224, "Basic Calculator", ("stack", "recursion", "hard")),
    (253, "Meeting Rooms II", ("intervals", "heap", "sweep_line")),
    (277, "Find the Celebrity", ("graph", "two_pointers")),
    (281, "Zigzag Iterator", ("design", "queue", "iterator")),
    (317, "Shortest Distance from All Buildings", ("graph", "bfs", "matrix", "hard")),
    (332, "Reconstruct Itinerary", ("graph", "dfs", "eulerian_path", "hard")),
    (359, "Logger Rate Limiter", ("design", "hash_map", "queue")),
    (362, "Design Hit Counter", ("design", "queue", "sliding_window")),
    (310, "Minimum Height Trees", ("graph", "topological_sort")),
    (394, "Decode String", ("stack", "string")),
    (438, "Find All Anagrams in a String", ("sliding_window", "string")),
    (433, "Minimum Genetic Mutation", ("graph", "bfs", "state_search")),
    (528, "Random Pick with Weight", ("prefix", "binary_search", "randomized")),
    (542, "01 Matrix", ("graph", "bfs", "multi_source_bfs")),
    (636, "Exclusive Time of Functions", ("stack", "simulation")),
    (658, "Find K Closest Elements", ("binary_search", "two_pointers")),
    (698, "Partition to K Equal Sum Subsets", ("backtracking", "dp")),
    (713, "Subarray Product Less Than K", ("sliding_window",)),
    (729, "My Calendar I", ("intervals", "binary_search", "design")),
    (785, "Is Graph Bipartite?", ("graph", "bfs", "dfs")),
    (815, "Bus Routes", ("graph", "bfs", "graph_modeling")),
    (827, "Making A Large Island", ("graph", "dfs", "union_find", "hard")),
    (847, "Shortest Path Visiting All Nodes", ("graph", "bfs", "state_search", "hard")),
    (886, "Possible Bipartition", ("graph", "bfs", "dfs")),
    (934, "Shortest Bridge", ("graph", "bfs", "dfs", "multi_source_bfs")),
    (986, "Interval List Intersections", ("intervals", "two_pointers")),
    (1004, "Max Consecutive Ones III", ("sliding_window",)),
    (1048, "Longest String Chain", ("dp", "dp_lis", "string")),
    (1094, "Car Pooling", ("intervals", "prefix", "sweep_line")),
    (1095, "Find in Mountain Array", ("binary_search", "hard")),
    (1129, "Shortest Path with Alternating Colors", ("graph", "bfs", "state_search")),
    (1136, "Parallel Courses", ("graph", "topological_sort")),
    (1162, "As Far from Land as Possible", ("graph", "bfs", "multi_source_bfs")),
    (1192, "Critical Connections in a Network", ("graph", "dfs", "hard")),
    (1584, "Min Cost to Connect All Points", ("graph", "mst", "union_find")),
    (1631, "Path With Minimum Effort",
     ("graph", "dijkstra", "binary_search_answer", "union_find")),
]


# Ordered tracks are the heart of the trainer. Each list moves from the cleanest
# version of a pattern to variants that force deeper recognition.
TRACKS = {
    "hashing": [1, 242, 49, 128, 380, 41],
    "two_pointers": [125, 167, 283, 11, 15, 42],
    "sliding_window": [209, 3, 1004, 904, 424, 438, 713, 567, 76],
    "prefix_sum_hashmap": [238, 560, 525, 437],
    "monotonic_stack": [739, 853, 84, 907],
    "expression_stack": [394, 636, 224],
    "binary_search": [704, 69, 34, 74, 162, 658, 153, 33, 1095, 4],
    "binary_search_answer": [875, 1011, 410],
    "linked_list_pointers": [206, 21, 141, 19, 143, 138, 25],
    "intervals": [56, 986, 57, 253, 435, 452],
    "heap_top_k": [1046, 703, 215, 973, 347, 295],
    "backtracking": [78, 46, 17, 39, 93, 40, 22, 79, 698, 51, 131],
    "tree_dfs": [104, 98, 543, 236, 105, 124, 437, 297],
    "tree_bfs": [102, 863],
    "dfs_flood_fill": [200, 695, 130, 417],
    "bfs_shortest_path": [994, 1091, 815, 127, 126],
    "multi_source_bfs": [994, 542, 934, 1162],
    "state_space_search": [433, 752, 1129, 847, 864],
    "topological_sort": [207, 210, 1136, 310, 269],
    "union_find": [547, 684, 323, 721, 827],
    "dijkstra": [743, 1631, 787],
    "graph_modeling": [133, 399, 277, 785, 886, 815, 332, 1192],
    "grid_graph_advanced": [317, 827],
    "minimum_spanning_tree": [684, 1584],
    "trie": [208, 211, 212],
    "stream_design": [359, 362, 281, 981, 146, 295],
    "weighted_random": [528],
    "geometry": [149],
    "greedy": [121, 55, 45, 435, 134, 621],
    "dp_linear_take_skip": [70, 746, 198, 213, 740, 91],
    "dp_grid": [118, 119, 62, 64, 63, 120, 221],
    "dp_two_sequence": [392, 1143, 1035, 583, 712, 72, 115],
    "dp_knapsack_coin_change": [322, 518, 377, 416, 494, 474, 1049],
    "dp_lis": [300, 646, 1048, 673],
    "dp_interval_partition": [647, 5, 516, 139, 1039, 1547, 312],
    "dp_state_machine": [309, 714, 123, 188],
    "sweep_line_ordered_intervals": [986, 1094, 253, 729, 218],
    "google_priority_additions": [1631, 317, 827, 126, 253, 362, 1095, 149, 332, 1136],
    "google_core": [
        200, 133, 994, 1091, 934, 815, 785, 207, 210, 684, 721, 743,
        1631, 752, 127,
        104, 98, 543, 236, 105, 124, 863, 297,
        198, 91, 221, 1143, 72, 322, 416, 300, 139,
        3, 76, 560, 238, 239,
        208, 211, 212, 146, 362,
    ],
}

# Aggregate priority lists are selectable, but should not make every contained
# family count as "begun" for the no-argument random mode.
META_TRACKS = {"google_core", "google_priority_additions"}

# Broad aliases preserve the narrow pattern taxonomy while making it convenient
# to train a family. Order matters for `learn <group>` and acts as its roadmap.
CATEGORY_GROUPS = {
    "dp": [
        "dp_linear_take_skip", "dp_grid", "dp_two_sequence",
        "dp_knapsack_coin_change", "dp_lis", "dp_interval_partition",
        "dp_state_machine",
    ],
    "graph": [
        "dfs_flood_fill", "bfs_shortest_path", "multi_source_bfs",
        "graph_modeling", "grid_graph_advanced", "topological_sort",
        "union_find", "dijkstra", "state_space_search",
        "minimum_spanning_tree",
    ],
    "tree": ["tree_dfs", "tree_bfs"],
    # Convenience alias for the older tag name.
    "dp_knapsack": ["dp_knapsack_coin_change"],
    "binary_search_all": ["binary_search", "binary_search_answer"],
    "arrays_strings": [
        "hashing", "two_pointers", "sliding_window", "prefix_sum_hashmap",
        "monotonic_stack", "expression_stack", "intervals",
        "sweep_line_ordered_intervals",
    ],
    "google_phase_1": [
        "dp_linear_take_skip", "dfs_flood_fill", "dp_grid",
        "bfs_shortest_path", "dp_two_sequence", "multi_source_bfs",
        "dp_knapsack_coin_change", "graph_modeling",
    ],
    "google_phase_2": [
        "tree_dfs", "tree_bfs", "topological_sort", "union_find",
        "dijkstra", "state_space_search", "grid_graph_advanced",
    ],
    "google_phase_3": [
        "sliding_window", "prefix_sum_hashmap", "hashing", "two_pointers",
        "intervals", "heap_top_k",
    ],
    "google_phase_4": [
        "trie", "backtracking", "binary_search_answer", "greedy",
        "stream_design", "expression_stack", "weighted_random", "geometry",
    ],
    "google_phase_5": [
        "dp_lis", "dp_interval_partition", "dp_state_machine",
        "minimum_spanning_tree", "monotonic_stack", "linked_list_pointers",
        "sweep_line_ordered_intervals",
    ],
}

UNSEEN, HINTED, SOLVED, MASTERED = range(4)
STATUS_NAMES = ["UNSEEN", "HINTED", "SOLVED", "MASTERED"]
STATUS_VALUES = {name.lower(): value for value, name in enumerate(STATUS_NAMES)}
# When multiple reviews are due, weaker evidence gets sampled more often.
REDO_WEIGHTS = {UNSEEN: 6, HINTED: 5, SOLVED: 2, MASTERED: 1}

# LeetCode difficulty is intentionally separate from pattern tags. Problems not
# listed here are Medium, which is the dominant interview-simulation tier.
EASY_IDS = {
    1, 20, 21, 53, 69, 70, 83, 94, 100, 101, 104, 110, 112, 118,
    119, 121, 125, 136, 141, 169, 190, 191, 205, 206, 217, 226, 242,
    268, 283, 338, 359, 392, 543, 572, 637, 700, 704, 746, 1046,
}
HARD_IDS = {
    4, 23, 25, 42, 51, 72, 76, 84, 115, 124, 126, 127, 149, 188,
    212, 218, 224, 239, 269, 295, 297, 312, 317, 332, 410, 827,
    847, 864, 1095, 1192, 1547,
}
DIFFICULTY_WEIGHTS = {"easy": 2, "medium": 6, "hard": 2}
RANDOM_MASTERY_WEIGHTS = {UNSEEN: 4, HINTED: 3, SOLVED: 2, MASTERED: 1}
STATE_FILE = Path(__file__).with_name("leetcode_progress.json")

# Old accepts are diagnostic evidence only. They enter redo; they do not start
# as SOLVED or MASTERED. Recent DP work explicitly starts as HINTED.
DIAGNOSTICS = {
    3, 15, 33, 42, 49, 84, 98, 105, 128, 138, 146, 200, 215,
    236, 239, 560, 739, 875, 973,
}
INITIAL_HINTED = {70, 118, 119, 392, 1143, 300, 62}

# Historical Accepted submissions are not proof of mastery, but they should not
# consume the ordered LEARN queue again. PRACTICE and REDO can still select them.
HISTORICAL_SOLVED = {
    1, 2, 3, 4, 5, 11, 15, 16, 17, 19, 20, 21, 22, 33, 34, 36, 39,
    42, 45, 46, 49, 53, 54, 55, 56, 57, 62, 64, 69, 70, 74, 78, 83,
    84, 94, 98, 100, 101, 102, 104, 105, 110, 112, 114, 118, 119, 121,
    122, 125, 128, 134, 138, 141, 143, 146, 150, 153, 155, 167, 169,
    189, 190, 199, 200, 205, 206, 209, 215, 217, 219, 222, 226, 230,
    236, 238, 239, 242, 257, 268, 271, 274, 283, 287, 300, 303, 314,
    334, 339, 345, 347, 349, 374, 380, 383, 389, 392, 424, 443, 525,
    530, 539, 543, 560, 567, 572, 605, 637, 643, 700, 704, 724, 739,
    767, 853, 872, 875, 884, 904, 933, 973, 981, 1046, 1071, 1143,
    1207, 1249, 1448, 1480, 1496, 1567, 1679, 2055,
}
BY_ID = {problem[0]: problem for problem in PROBLEMS}


def _utcnow():
    return datetime.now(timezone.utc)


def _load():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    now = _utcnow().isoformat()
    first_review = (_utcnow() + timedelta(days=7)).isoformat()
    problems = {
        str(lc): {"status": HINTED, "attempts": 1, "updated": now,
                  "due": first_review,
                  "history": [{"status": HINTED, "at": now}]}
        for lc in INITIAL_HINTED
    }
    # Diagnostics are immediately eligible for a cold redo, but remain UNSEEN.
    for lc in DIAGNOSTICS:
        problems.setdefault(str(lc), {"status": UNSEEN, "attempts": 0,
                                     "updated": now, "due": now, "history": []})
    return {"problems": problems}


def _save(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def _entry(state, lc):
    return state["problems"].get(str(lc), {"status": UNSEEN, "attempts": 0})


def _slug(name):
    return (name.lower().replace("'", "").replace("(", "")
            .replace(")", "").replace(",", "").replace(".", "")
            .replace(" ", "-"))


def difficulty(lc):
    if lc in EASY_IDS:
        return "easy"
    if lc in HARD_IDS:
        return "hard"
    return "medium"


def format_problem(problem, reveal_pattern=False, pattern=None):
    lc, name, tags = problem
    lines = [f"LC {lc} — {name}"]
    if reveal_pattern:
        lines.append(f"Pattern: {pattern or ', '.join(tags)}")
    lines.append(f"https://leetcode.com/problems/{_slug(name)}/")
    return "\n".join(lines)


def _resolve_category(category):
    """Expand either one exact track or one broad category alias."""
    if category in TRACKS:
        return [category]
    return CATEGORY_GROUPS.get(category)


def _track_for(lc, tracks):
    return next(track for track in tracks if lc in TRACKS[track])


def learn(pattern):
    """Return the next fresh problem in an ordered pattern progression.

    Any real attempt removes a problem from LEARN. HINTED attempts are revisited
    later by REDO instead of blocking access to new variations in the track.
    """
    tracks = _resolve_category(pattern)
    if not tracks:
        return _unknown_pattern(pattern)
    state = _load()
    for track in tracks:
        for lc in TRACKS[track]:
            status = _entry(state, lc)["status"]
            if lc not in HISTORICAL_SOLVED and status == UNSEEN:
                return format_problem(BY_ID[lc], pattern=track)
    return (f"{pattern}: ordered learning queue complete. "
            "Use practice for pattern reps or redo for retention checks.")


def practice(pattern):
    """Random practice inside a known pattern, excluding mastered problems."""
    tracks = _resolve_category(pattern)
    if not tracks:
        return _unknown_pattern(pattern)
    state = _load()
    pool = sorted({lc for track in tracks for lc in TRACKS[track]})
    choices = [lc for lc in pool
               if _entry(state, lc)["status"] < MASTERED]
    choices = choices or pool
    lc = random.choice(choices)
    return format_problem(BY_ID[lc], pattern=_track_for(lc, tracks))


def random_problem(patterns=None):
    """Difficulty-weighted interview simulation with the pattern hidden.

    With no patterns, sample begun tracks. Pass several patterns to create a
    custom mixed interview pool, e.g. random_problem(["dp_grid", "dp_lis"]).
    Previously attempted problems remain possible, at decreasing probability as
    their mastery evidence improves.
    """
    state = _load()
    if patterns:
        unknown = [pattern for pattern in patterns
                   if not _resolve_category(pattern)]
        if unknown:
            return _unknown_pattern(", ".join(unknown))
        selected = list(dict.fromkeys(
            track for pattern in patterns for track in _resolve_category(pattern)
        ))
    else:
        # Only mix in tracks the user has begun; fall back to all tracks on day one.
        begun = [p for p, ids in TRACKS.items() if p not in META_TRACKS
                 if any(_entry(state, lc)["status"] > UNSEEN for lc in ids)]
        selected = begun or list(TRACKS)
    pool = sorted({lc for pattern in selected for lc in TRACKS[pattern]})
    weights = []
    for lc in pool:
        entry = _entry(state, lc)
        mastery_weight = RANDOM_MASTERY_WEIGHTS[entry["status"]]
        # An old Accepted with no current evidence counts as seen, not brand-new.
        if entry["status"] == UNSEEN and lc in HISTORICAL_SOLVED:
            mastery_weight = RANDOM_MASTERY_WEIGHTS[SOLVED]
        weights.append(DIFFICULTY_WEIGHTS[difficulty(lc)] * mastery_weight)
    lc = random.choices(pool, weights=weights, k=1)[0]
    return format_problem(BY_ID[lc], reveal_pattern=False)


def _parse_duration(value):
    """Parse durations such as 7d, 1w, '2 weeks', or 1m (30 days)."""
    match = re.fullmatch(
        r"\s*(\d+)\s*(d|day|days|w|week|weeks|m|month|months)\s*",
        value.lower(),
    )
    if not match or int(match.group(1)) <= 0:
        raise ValueError("Use a positive duration such as 7d, 1w, or 1m.")
    amount, unit = int(match.group(1)), match.group(2)
    multiplier = 1 if unit.startswith("d") else 7 if unit.startswith("w") else 30
    return timedelta(days=amount * multiplier)


def redo(pattern=None, within=None):
    """Choose a review weighted toward lower mastery states.

    Normally only scheduled-due items qualify. `within` explicitly overrides
    due dates and selects attempts made inside that recent window.
    """
    tracks = _resolve_category(pattern) if pattern is not None else None
    if pattern is not None and not tracks:
        return _unknown_pattern(pattern)
    state, now = _load(), _utcnow()
    if within:
        try:
            cutoff = now - _parse_duration(within)
        except ValueError as error:
            return str(error)
    ids = (sorted({lc for track in tracks for lc in TRACKS[track]}) if tracks else
           list(DIAGNOSTICS | INITIAL_HINTED |
                {int(lc) for lc in state["problems"]}))
    ids = [int(lc) for lc in ids if int(lc) in BY_ID]
    due = []
    for lc in ids:
        entry = _entry(state, lc)
        if within:
            # Recency mode requires a real attempt, not an untouched diagnostic.
            if entry.get("attempts", 0) <= 0 or "updated" not in entry:
                continue
            updated_at = datetime.fromisoformat(entry["updated"])
            if cutoff <= updated_at <= now:
                due.append(lc)
        else:
            due_at = datetime.fromisoformat(entry.get("due", now.isoformat()))
            is_review_item = entry.get("attempts", 0) > 0 or lc in DIAGNOSTICS
            if is_review_item and due_at <= now:
                due.append(lc)
    if not due:
        if within:
            scope = f" in {pattern}" if pattern else ""
            return f"No attempted problems found{scope} within the last {within}."
        return "Nothing is due yet. Practice a track or use random."
    lc = random.choices(
        due,
        weights=[REDO_WEIGHTS[_entry(state, candidate)["status"]]
                 for candidate in due],
        k=1,
    )[0]
    return (format_problem(BY_ID[lc], pattern=_track_for(lc, tracks))
            if tracks else format_problem(BY_ID[lc], reveal_pattern=False))


def record(lc, status, follow_up=False):
    """Record honest evidence; MASTERED additionally requires a follow-up."""
    status = status.lower()
    if lc not in BY_ID:
        return f"LC {lc} is not in the problem bank."
    if status not in STATUS_VALUES:
        return "Status must be: hinted, solved, mastered, or unseen."
    value, state, now = STATUS_VALUES[status], _load(), _utcnow()
    if value == MASTERED and not follow_up:
        return ("MASTERED requires one unseen follow-up. If you met all five "
                "criteria, rerun with: record <id> mastered --follow-up")
    old = _entry(state, lc)
    attempts = old.get("attempts", 0) + (value != UNSEEN)
    if value == HINTED:
        # Repeated difficulty earns progressively wider spacing. The objective
        # is retrieval after forgetting has begun, not next-day memorization.
        hinted_delays = (3, 7, 14, 30)
        delay = hinted_delays[min(max(attempts - 1, 0), len(hinted_delays) - 1)]
    else:
        delay = {UNSEEN: 0, SOLVED: 7, MASTERED: 21}[value]
    history = old.get("history", [])
    history.append({"status": value, "at": now.isoformat(),
                    "follow_up": bool(follow_up)})
    state["problems"][str(lc)] = {
        "status": value, "attempts": attempts, "updated": now.isoformat(),
        "due": (now + timedelta(days=delay)).isoformat(), "history": history,
    }
    _save(state)
    return f"LC {lc}: {STATUS_NAMES[value]} recorded; review in {delay} day(s)."


def progress():
    state = _load()
    lines = []
    for pattern, ids in TRACKS.items():
        counts = [0, 0, 0, 0]
        for lc in ids:
            counts[_entry(state, lc)["status"]] += 1
        lines.append(f"{pattern:28} " + "  ".join(
            f"{STATUS_NAMES[i][0]}:{counts[i]}" for i in range(4)))
    return "\n".join(lines)


def categories():
    return sorted(TRACKS)


def groups():
    return sorted(CATEGORY_GROUPS)


def _unknown_pattern(pattern):
    return (f"Unknown category: {pattern}\n"
            f"Broad groups: {', '.join(groups())}\n"
            f"Narrow tracks: {', '.join(categories())}")


def _main():
    parser = argparse.ArgumentParser(description="Pattern-first LeetCode trainer")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("learn", "practice"):
        p = sub.add_parser(command)
        p.add_argument("pattern")
    p = sub.add_parser("redo")
    p.add_argument("pattern", nargs="?")
    p.add_argument(
        "--within",
        help="override due dates and select recent attempts (7d, 1w, 1m)",
    )
    p = sub.add_parser("random")
    p.add_argument("patterns", nargs="*")
    sub.add_parser("progress")
    sub.add_parser("patterns")
    p = sub.add_parser("record")
    p.add_argument("leetcode_id", type=int)
    p.add_argument("status", choices=sorted(STATUS_VALUES))
    p.add_argument(
        "--follow-up", action="store_true",
        help="confirm an unseen follow-up was answered (required for MASTERED)",
    )
    args = parser.parse_args()
    if args.command in ("learn", "practice"):
        result = globals()[args.command](args.pattern)
    elif args.command == "redo":
        result = redo(args.pattern, args.within)
    elif args.command == "random":
        result = random_problem(args.patterns)
    elif args.command == "record":
        result = record(args.leetcode_id, args.status, args.follow_up)
    elif args.command == "progress":
        result = progress()
    else:
        result = ("BROAD GROUPS\n" + "\n".join(groups()) +
                  "\n\nNARROW TRACKS\n" + "\n".join(categories()))
    print(result)


if __name__ == "__main__":
    _main()
