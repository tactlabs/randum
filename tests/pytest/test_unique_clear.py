def test_unique_clears(testdir):
    """Successive uses of the `randum` pytest fixture have the
    generated unique values cleared between functions."""

    testdir.makepyfile(
        """
        import pytest
        from randum.exceptions import UniquenessException

        NUM_SAMPLES = 100

        def test_fully_exhaust_unique_booleans(randum):
            _dummy = [randum.boolean() for _ in range(NUM_SAMPLES)]

            randum.unique.boolean()
            randum.unique.boolean()
            with pytest.raises(UniquenessException):
                randum.unique.boolean()
            _dummy = [randum.boolean() for _ in range(NUM_SAMPLES)]

        def test_do_not_exhaust_booleans(randum):
            randum.unique.boolean()

        def test_fully_exhaust_unique_booleans_again(randum):
            _dummy = [randum.boolean() for _ in range(NUM_SAMPLES)]

            randum.unique.boolean()
            randum.unique.boolean()
            with pytest.raises(UniquenessException):
                randum.unique.boolean()
            _dummy = [randum.boolean() for _ in range(NUM_SAMPLES)]
        """,
    )

    result = testdir.runpytest()

    result.assert_outcomes(passed=3)
