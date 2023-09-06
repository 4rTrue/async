#chapar o pão
#frita o hamburguer
#faz o milk shake
#monta o sanduíche

from time import sleep,time
import asyncio

class SyncSpongeBob:
    def cook_bread(self):
        sleep(3)
    
    def cook_hamburger(self):
        sleep(10)
    
    def assemble_sandwich(self):
        sleep(3)

    def make_milkshake(self):
        sleep(5)
    
    def cook(self):
        self.cook_bread()
        self.cook_hamburger()
        self.assemble_sandwich()
        self.make_milkshake()

class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)
    
    async def cook_hamburger(self):
        await asyncio.sleep(10)
    
    async def assemble_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger()
        )
        #renomeando a instancia do event_loop
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.assemble_sandwich())
    
    async def cook(self):
        await asyncio.gather(
            self.make_sandwich(),
            self.make_milkshake()
        )

tempo = time()
sync_spongebob = SyncSpongeBob()
sync_spongebob.cook()
print('\nTempo assincrono de',time()-tempo,'segundos\n')

tempo = time()
async_spongebob = AsyncSpongeBob()
asyncio.run(async_spongebob.cook())
print('\nTempo assincrono de',time()-tempo,'segundos\n')