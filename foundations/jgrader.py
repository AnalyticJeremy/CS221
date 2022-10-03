#!/usr/bin/env python3

import collections
import graderUtil
import random

grader = graderUtil.Grader()
submission = grader.load('submission')

############################################################
# Problem 4a: findAlphabeticallyFirstWord

grader.add_basic_part('4a-0-basic', lambda:
                      grader.require_is_equal('apple', submission.find_alphabetically_first_word(
                        'banana apple peach orage')),
                      description='simple test case')

grader.add_basic_part('4a-1-basic',
                      lambda: grader.require_is_equal('17', submission.find_alphabetically_first_word('My son is 17')),
                      description='sentence has a number')

grader.add_basic_part('4a-2-basic',
                      lambda: grader.require_is_equal('The', submission.find_alphabetically_first_word('The big red dog barks often')),
                      description='mixed case')

grader.add_basic_part('4a-3-basic',
                      lambda: grader.require_is_equal('apple', submission.find_alphabetically_first_word('pear apple orange apple cherry')),
                      description='duplicate word')

############################################################
# Problem 4b: euclideanDistance

grader.add_basic_part('4b-0-basic', lambda: grader.require_is_equal(5, submission.euclidean_distance((1, 5), (4, 1))),
                      description='simple test case')

grader.add_basic_part('4b-1-basic', lambda: grader.require_is_equal(0, submission.euclidean_distance((1, 5), (1, 5))),
                      description='same point')

grader.add_basic_part('4b-2-basic', lambda: grader.require_is_equal(6.4031242374328485, submission.euclidean_distance((1, 5), (-4, 1))),
                      description='negative')

grader.add_basic_part('4b-3-basic', lambda: grader.require_is_equal(5, submission.euclidean_distance((-1, 5), (-4, 1))),
                      description='negatives')

grader.add_basic_part('4b-4-basic', lambda: grader.require_is_equal(4.123105625617661, submission.euclidean_distance((0, 0), (4, 1))),
                      description='origin')

grader.add_basic_part('4b-5-basic', lambda: grader.require_is_equal(409391.00001954124, submission.euclidean_distance((1, 5), (409392, 1))),
                      description='go to space')



############################################################
# Problem 4c: mutateSentences

def test4c0():
    grader.require_is_equal(sorted(['Jeremy and Mayha are friends']), sorted(submission.mutate_sentences('Jeremy and Mayha are friends')))
    grader.require_is_equal(sorted([]), sorted(submission.mutate_sentences('the')))
    grader.require_is_equal(sorted(['the cat and the cat', 'cat and the cat and', 'and the cat and the']), sorted(submission.mutate_sentences('the cat and the cat')))
    grader.require_is_equal(sorted(['the cat and the cat and the cat', 'the cat and the cat and the moose', 'cat and the cat and the cat and', 'and the cat and the cat and the']), sorted(submission.mutate_sentences('the cat and the cat and the moose')))
    grader.require_is_equal(
        sorted(['the cat and the cat and the cat and', 'the cat and the cat and the mouse and', 'the cat and the cat and the grizzly bear', 'the cat and the mouse and the cat and', 'the cat and the mouse and the mouse and', 'the cat and the mouse and the grizzly bear', 'the mouse and the cat and the cat and', 'the mouse and the cat and the mouse and', 'the mouse and the cat and the grizzly bear', 'the mouse and the mouse and the cat and', 'the mouse and the mouse and the mouse and', 'the mouse and the mouse and the grizzly bear', 'cat and the cat and the cat and the', 'cat and the cat and the mouse and the', 'cat and the mouse and the cat and the', 'cat and the mouse and the mouse and the', 'and the cat and the cat and the cat', 'and the cat and the cat and the mouse', 'and the cat and the cat and the grizzly', 'and the cat and the mouse and the cat', 'and the cat and the mouse and the mouse', 'and the cat and the mouse and the grizzly', 'and the mouse and the cat and the cat', 'and the mouse and the cat and the mouse', 'and the mouse and the cat and the grizzly', 'and the mouse and the mouse and the cat', 'and the mouse and the mouse and the mouse', 'and the mouse and the mouse and the grizzly', 'mouse and the cat and the cat and the', 'mouse and the cat and the mouse and the', 'mouse and the mouse and the cat and the', 'mouse and the mouse and the mouse and the']),
        sorted(submission.mutate_sentences('the cat and the mouse and the grizzly bear')))


grader.add_basic_part('4c-0-basic', test4c0, max_points=1, description='simple test')




############################################################
# Problem 4d: dotProduct

def test4d0():
    grader.require_is_equal(21, submission.sparse_vector_dot_product(collections.defaultdict(float, {'a': 5, 'c': 4, 'b': 3}),
                                                                     collections.defaultdict(float, {'b': 2, 'a': 3, 'd': 12})))

    grader.require_is_equal(9, submission.sparse_vector_dot_product(collections.defaultdict(float, {'a': 5, 'c': 4, 'b': -3}),
                                                                    collections.defaultdict(float, {'b': 2, 'a': 3, 'd': 12})))

    grader.require_is_equal(0, submission.sparse_vector_dot_product(collections.defaultdict(float, {'a': 5, 'c': 4, 'b': -3}),
                                                                    collections.defaultdict(float, {'e': 2, 'f': 3, 'd': 12})))


grader.add_basic_part('4d-0-basic', test4d0, max_points=1, description='simple test')


############################################################
# Problem 4e: incrementSparseVector

def test4e0():
    v1 = collections.defaultdict(float, {'a': 5, 'c': 12})
    submission.increment_sparse_vector(v1, 2, collections.defaultdict(float, {'b': 2, 'a': 3}))
    grader.require_is_equal(collections.defaultdict(float, {'a': 11, 'b': 4, 'c': 12}), v1)

    # Scale is 0
    v1 = collections.defaultdict(float, {'a': 5, 'c': 12})
    submission.increment_sparse_vector(v1, 0, collections.defaultdict(float, {'b': 2, 'a': 3}))
    grader.require_is_equal(collections.defaultdict(float, {'a': 5, 'b': 0, 'c': 12}), v1)


grader.add_basic_part('4e-0-basic', test4e0, description='simple test')



############################################################
# Problem 4f: findNonsingletonWords

def test4f0():
    grader.require_is_equal({'fox'}, submission.find_nonsingleton_words('The quick brown fox jumps over the lazy fox'))
    grader.require_is_equal(set(), submission.find_nonsingleton_words('The quick brown fox jumps over the lazy dog'))
    grader.require_is_equal({'foxy', 'fox'}, submission.find_nonsingleton_words('foxy fox foxes a fox for fox foxy fox fox'))


grader.add_basic_part('4f-0-basic', test4f0, description='simple test')




############################################################
grader.grade()
