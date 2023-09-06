import asyncio

async def sum(a,b):
    return a+b

async def print_sum(a,b):
    result = await sum(a,b)
    print(f'resultado igual a {result}')


# EVENT LOOP
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_sum(2,6))