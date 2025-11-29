
# Budget

Playing with the Up API. Learning via Marko's API examples in `joel.ipynb`.

## 25.3.31

make basic requests to the up api

## 25.4.1

1. find out what pydantic is

2. why might you want to use it

3. create types for the up apis

4. make fn that takes an enum and returns the appropriate data type

## 25.4.4

- .ipynb

- .toml

## 25.11.30

#### example 3

when you are first writing except blocks: how do you know which errors to catch? by trial and error?

- e.g. when you first used `requests.exceptions.RequestException`

	- although `RequestException` sounds rather broad(?)

#### example 4

- same question as above, e.g. how did you know to use these:

```python
    except requests.exceptions.Timeout:
		print("Request timed out. Please try again later.")
		return None
	except requests.exceptions.HTTPError as e:
		print(f"HTTP Error: {e}")
		return None
	except requests.exceptions.RequestException as e:
		print(f"Error fetching data: {e}")
		return None
	except json.JSONDecodeError:
		print("Error decoding JSON response")
		return None
```

- thoughts:
	
    - `Timeout` -> makes sense
	
    - `HTTPError` -> this makes sense, it comes from `raise_for_status()`
	
    - `RequestException` -> is this a catch-all? is this meaningfully different from just using `Exception`?
	
    - `JSONDecodeError` -> i can imagine this happening, but wouldn't `RequestException` always catch it first?
    
    	- ohh no it wouldn't, because maybe the whole request process goes fine, but the json content is somehow bullshit and the decoding process fails

#### example 5

`APIConnectionError` and `APIResponseError`

- i don't understand what these are adding to the functionality. who are they for?

- APIError was made from using `class APIError(Exception)`; but how do you know something non-API-related isn't gonna go wrong? by saying `except APIError as e:` we are framing all possible exceptions as API errors. what if something else went wrong? we would catch it but we would be naming at an API error

- but we never print or log `APIConnectionError` and `APIResponseError`; we just raise them; so they will never appear in the terminal/log. so who are they for? for me, for when i am looking at the code itself?

- **EDIT: ohhh okay,** Claude has informed me how this works. the exceptions you created are subclasses of `Exception`, but they behave independently of `Exception`. just because you defined them with `class APIError(Exception)`, doesn't mean that all exceptions will get sfunnelled into `APIError`... RATHER, you raise `APIError` exactly when you want to, and you catch it yourself. if some other error gets thrown, we will not catch it

	- you're saying when there's a `Timeout` or `ConnectionError` or `RequestException`, we are naming it an `APIConnectionError` 
	
	- and when there's a `HTTPError` or `JSONDecodeError`, we are calling that an `APIResponseError`

- so why use `except APIError as e:` in the fn that calls the fn? is it a way to get all remaining un-caught errors? or does every error in the sub-fn bubble up into this except block? i think not the latter

	- if there's a `Timeout`, we raise an `APIConnectionError`, which bubbles up a level, but why would `except APIError` catch an `APIConnectionError`? i wouldn't expect it to. it seems to contradict my epiphany above, where i thought that we only throw and catch specific errors by their specific names, therefore the class we inherit from is kind of irrelevant in that sense.

- it says `def fetch_api_data(...) -> list[dict[str, Any]]:` but if we reach `raise()`, doesn't that fn return nothing? 

Joel's conclusion: Marko is obsessed with error handling. but it's just a facade. he never actually writes code that DOES anything :p
