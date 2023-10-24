# Directory: 0x00-pagination

## Task Descriptions

### Task 0: Simple helper function
- **File:** `0-simple_helper_function.py`
- **Description:** This file contains a simple helper function called `index_range` that takes two integer arguments, `page` and `page_size`. It returns a tuple with start and end indices for pagination.

### Task 1: Simple pagination
- **File:** `1-simple_pagination.py`
- **Description:** This file extends the previous task by adding a `Server` class. This class has a method `get_page` that paginates a dataset of popular baby names from a CSV file.

### Task 2: Hypermedia pagination
- **File:** `2-hypermedia_pagination.py`
- **Description:** This task builds on the previous task by adding a method `get_hyper` to the `Server` class. This method returns paginated data along with additional hypermedia information like page size, current page number, next page number, previous page number, and total number of pages.

### Task 3: Deletion-resilient hypermedia pagination
- **File:** `3-hypermedia_del_pagination.py`
- **Description:** This task introduces a new method `get_hyper_index` in the `Server` class. It provides a resilient pagination mechanism that ensures users won't miss items in the dataset even if rows are deleted between queries.
