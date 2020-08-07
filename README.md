# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
    Hashing functions can take an input and run it through some sort of algorithm (there are a bunch of them) and produce the same
    result based on the given input. We as developers can use this behavior to locate things inside a collection based on an input.
    also known as a hash table.
2. Collision resolution
    When a developer has a constraint on the size of the internal data structure representing the hash map, collisions are inveitable
    the act of dealing with an index (produced by our hashing function) that is shared by a prev entry in our data structure is collision resoulotion.
    For example a simple way of dealing with these occurences is using Linked lists! Having 1-3 values at most sharing a space is not going to have 
    a noticable impact on runtime.
3. Performance of basic hash table operations
    resizing a hash table (depending on the implementation) might be o(n) because we have to work our way through the datastructure
    and preform the hash on each item. Fetching/Removing items from the hash table will be O(1) beacuse we feed the value we are searching for
    into our hashing algorithm which will produce the location of the item that we are searching for.
4. Load factor
    Is information held within the hash table that decides when the size of the underlying data structure needs to be increased or decreased
    it can be calculated by taking the number of "occupied slots" by the total number of slots. In practice when the load factor moves past 
    0.7 collisions will start to happen more so in order to deal with this we just increase size
5. Automatic resizing
    this is an implementation that looks at ^^load factor^^ and deals with the details of how to go about re hasing everything and
    increasing/decreasing list size. Usally it is refrenced whenever a new item is added or removed
6. Various use cases for hash tables
    hash tables are great for efficentcy and "big data". They allow programers to compute things once and store the answer (aka memoization) or (caching)
    as well as save on time complexity by implementing their hash methods in order to quickly find and access diffrent areas of their underlying data set.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [x] Create a forked copy of this project
- [x] Add your team lead as a collaborator on Github
- [x] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [x] Create a new branch: git checkout -b `<firstName-lastName>`.
- [x] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [x] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [x] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [x] Navigate into each exercise's directory
- [x] Read the instructions for the exercise in the README
- [x] Implement your solution in the `.py` skeleton file
- [x] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [x] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

