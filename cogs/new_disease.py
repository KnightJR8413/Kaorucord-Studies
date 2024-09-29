from discord.ext import commands
import asyncio
import sqlite3

class New_Disease(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect('diseases.db')
        c = conn.cursor()
        c.execute(
            '''
            CREATE TABLE IF NOT EXISTS diseases
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, 
            name TEXT, 
            vaccinations BOOLEAN
            vector TEXT, 
            diagnoses TEXT, 
            symptoms TEXT, 
            treatments TEXT)
            '''
        )
        conn.commit()
        conn.close()
    
    @commands.command(name='create_disease')
    async def create_disease_entry(self, user_id, name, vector, diagnoses, symptoms, treatments):
        conn = sqlite3.connect('diseases.db')
        c = conn.cursor
        c.execute("INSERT INTO diseases (user_id, name, vector, diagnoses, symptoms, treatments)")
            

    async def start_disease_creation(self, ctx):
        questions = [
            "What is the name of the disease?",
            "Are any vaccinations available?",
            "How is the disease transmitted?",
            "What are the differential diagnoses? (comma-separated)",
            "What are the symptoms? (comma-separated)",
            "What is the best course of treatment?"
        ]
        answers = []

        for question in questions:
            await ctx.send(question)
            try:
                response = await self.bot.wait_for('message', check=lambda m: 
                                                   m.author == ctx.author and m.channel ==
                                                   ctx.channel, timeout = 120)
                answers.append(response.content)
            
            except asyncio.TimeoutError:
                await ctx.send('Disease creation timed out. Please try again.')
                return
        
        self.create_disease_entry(ctx.author.id, *answers)
        bot_commands_channel = ctx.guild.get_channel(self.bot.commands_channel_id)
        await ctx.send(f'Disease created successfully! Your disease ID is {disease_id}.')