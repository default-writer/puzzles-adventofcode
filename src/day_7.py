"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

To begin, get your puzzle input.

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag 
(and the 7 bags within it) 
plus 2 vibrant plum bags 
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

import re

def get_rules(rules, input):
    full_regex = r"(\w+ \w+) bag[s]{0,1} contain (?:(no other bags)?|(?:(\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?(?:, (\d+) (\w+ \w+) bag[s]{0,1})?)?\."
    line_rule_regex = re.compile(full_regex)
    line_rules = input.split("\n")
    for line_rule in line_rules:
        rule = line_rule_regex.match(line_rule)
        if not rule.group(1) in rules.keys():
            rules[rule.group(1)] = {}
        index = 3
        while rule.group(index) and rule.group(index + 1):
            rules[rule.group(1)][rule.group(index + 1)]=rule.group(index)
            index += 2

def get_rules_by_name(rules, rule, colors):
    for key in rules:
        for r in rules[key]:
            if r == rule:
                if key not in colors:
                    get_rules_by_name(rules, key, colors)
                    colors.append(key)

def get_bags_by_name(rules, current):
    counter = 0
    for rule in rules[current].keys():
        counter += int(rules[current][rule]) * (get_bags_by_name(rules, rule) + 1)
    print(f"{current} bags contain {counter} bags.")
    return counter
