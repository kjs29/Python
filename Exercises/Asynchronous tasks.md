
Let's build a corountine called fetch_data which simulates the

collection of data from a network database. 

Let's assume that takes a few seconds. 

It should return a dictionary {"data": 100}. 

Next, Build a new coroutine which counts down from 10 to 1(using range).

Using await, have each number print to the screen every 2seconds.

Finally build a coroutine called main() and run fetch_data and the countdown coroutine concurrently.

Print the data that is returned from fetch_data whilst also counting down from 10.

<details>
  
  <summary>Answer</summary>
  
  ```py
  import asyncio

  async def fetch_data():
      print("fetching data...")
      await asyncio.sleep(6)
      return {'data':100}

  async def count_down():
      for number in range(10,0,-1):
          print(number)
          await asyncio.sleep(2)

  async def main():
      task_fetch_data = asyncio.create_task(fetch_data())
      task_count_down = asyncio.create_task(count_down())
      await task_fetch_data
      print(task_fetch_data.result())
      await task_count_down

  asyncio.run(main())
  ```
</details>
