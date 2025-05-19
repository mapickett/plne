# Python Concurrency EcoSystem

# 1 Parallelism
# Performing multiple operations at the same time
# Concurrency does not imply parallelism
# The standard multiprocessing module implements parallelism in Python

# 2 Threading
# Concurrent execution model whereby multiple threads take turns
# Threads do not run in parallel
# Good for IO-bound tasks - implies waiting
# Downsides are memory safety and race conditions.
# Child threads operate in the same memory space.
# The standard threading module implements threading in Python

# 3 Async IO
# Single threaded, single process design using cooperative multitasking
# Cooperative = no os intervention, each task decides whenb to give up control
# Asynchronous functions are able to pause while waiting on their ultimate result
# It gives the look and feel of concurrency.
# asyncio is the Python standard library for Async IO using async/await syntax.

# Coroutines are functions that can suspend execution before reaching return and
# can indirectly pass control to another coroutine.
# A coroutine is a function defined using the async keyword.

# An object is awaitable if it can be used in an await expression.
# There are 2 awaitable objects: coroutine, task, future
