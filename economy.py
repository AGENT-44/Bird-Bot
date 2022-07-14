import discord
from discord.ext import commands
import json
import os
import random
import asyncio


class economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx,member: discord.Member = None):
        member = ctx.author if not member else member

        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) in users:
            await ctx.send("Already Regsitered")
            return

        else:
            data = {
            str(ctx.author.id) : {
            "wallet" : 0,
            "bank" : 0
            }
        }

            with open("C:/Users/Vinay/Desktop/Bot/bank.json", "r+") as file:
                newusers = json.load(file)
                newusers.update(data)
                file.seek(0)
                json.dump(newusers, file)

        em = discord.Embed(title= ":bank: Welcome To Bird's Bank. :bank:",description= "Thanks, For Registering.", color = 0x2471A3,timestamp=ctx.message.created_at)
        em.add_field(name="Account Holder's Name :", value =f"{ctx.author}", inline=False)
        em.add_field(name="Account Number :", value = member.id, inline=False)
        await ctx.send(embed = em)

        

    @commands.command()
    async def give(self,ctx,member:discord.Member = None,amount = None):

        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) not in users:
            await ctx.send("**You Don't Have An Account! Type `#register` to Register a Account For You.**")
            return



        if member == None:
            await ctx.send("Please Mention User You Want to Give Coins to.")
            return
        
        if amount == None:
            await ctx.send("Please Enter Amount.")
            return
        
        bal = await jsonfunc.update_bank(self,ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You Don't have Enough Money To Give 'First Get Some Money Then Try Again'!")
            return
        if amount<0:
            await ctx.send("Amount Must Be Positive!")
            return
        else:
            await ctx.send("Try Again Later. `Try Using Command - #give {usermention} {amount}`")
        
        
            

        await jsonfunc.update_bank(self, ctx.author,-1*amount,"bank")
        await jsonfunc.update_bank(self, member,amount,"bank")
        
        


        #ex = await jsonfunc.updated_bank(self, ctx.author,-1*amount,"bank")
        ex = await jsonfunc.updated_bank(self,ctx.author)
        
        em = discord.Embed(title= f"Transaction Done By {ctx.author}" ,description=f"Gave __{member.name}__  **{amount}** $", color = 0x0000FF,timestamp=ctx.message.created_at)
        em.add_field(name="Your Remaining Balance:", value=ex)

        await ctx.send(embed = em)
        


    # @commands.command()
    # async def balance(self, ctx,member: discord.Member = None):
    #     member = ctx.author if not member else member

        

    #     user = ctx.author
    #     users = await jsonfunc.get_bank_data(self, user)
        
    #     wallet_amt = users[str(user.id)]["wallet"]
    #     bank_amt = users[str(user.id)]["bank"]

    #     em = discord.Embed(title = ":bank: Welcome To Bird's Bank. :bank:",color = discord.Color.red(), timestamp=ctx.message.created_at)
    #     em.add_field(name="Account Holder's Name :", value=f"{ctx.author}",inline=False)
    #     em.add_field(name= "Account Number :", value=member.id,inline=False)
    #     em.add_field(name= "Bank Balance :", value=f"**{bank_amt}** $",inline=False)
    #     em.add_field(name= "Wallet Balance :", value=f"**{wallet_amt}** $")
    #     await ctx.send(embed = em)

    @commands.command(aliases=['bal'])
    async def balance(self, ctx,member: discord.Member = None):
        member = ctx.author if not member else member

        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) not in users:
            await ctx.send("**You Don't Have An Account! Type `#register` to Register a Account For You.**")
            return

    
        
        user = ctx.author
        users = await jsonfunc.get_bank_data(self, user)
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = ":bank: Welcome To Bird's Bank. :bank:",color = discord.Color.red(), timestamp=ctx.message.created_at)
        em.add_field(name="Account Holder's Name :", value=f"{ctx.author}",inline=False)
        em.add_field(name= "Account Number :", value=member.id,inline=False)
        em.add_field(name= "Bank Balance :", value=f"**{bank_amt}** $",inline=False)
        em.add_field(name= "Wallet Balance :", value=f"**{wallet_amt}** $")
        await ctx.send(embed = em)
        

    @commands.command()
    async def beg(self, ctx):
        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) not in users:
            await ctx.send("**You Don't Have An Account! Type `#register` to Register a Account For You.**")
            return
        user = ctx.author
        userss = await jsonfunc.get_bank_data(self, user)


        earnings = random.randrange(500)

        await ctx.send(f"Someone Gave You {earnings} coins!!.")

        userss[str(user.id)]["wallet"] += earnings

        with open("bank.json", "w") as f:
            json.dump(userss,f)


    @commands.command()
    async def withdraw(self, ctx,amount = None,member: discord.Member = None):
        member = ctx.author if not member else member
        

        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) not in users:
            await ctx.send("**You Don't Have An Account! Type `#register` to Register a Account For You.**")
            return

        if amount == None:
            await ctx.send("Please Enter Amount.")
            return
        
        bal = await jsonfunc.update_bank(self,ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You Don't have Enough Money To Withdraw!")
            return
        elif amount<0:
            await ctx.send("Amount Must Be Positive!")
            return

        await jsonfunc.update_bank(self,ctx.author,amount)
        await jsonfunc.update_bank(self,ctx.author,-1*amount,"bank")

        
        em = discord.Embed(title= ":bank: Welcome To Bird's Bank. :bank:", color = 0x2471A3,timestamp=ctx.message.created_at)
        em.add_field(name= "Amount Withdrew From Your Account :",value=f"**{amount}** $",inline=False)
        em.add_field(name="Account Holder's Name :", value =f"{ctx.author}", inline=False)
        em.add_field(name="Account Number :", value =member.id, inline=False)
        await ctx.send(embed = em)

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx,amount = None,member: discord.Member = None):
        member = ctx.author if not member else member
        

        with open("bank.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) not in users:
            await ctx.send("**You Don't Have An Account! Type `#register` to Register a Account For You.**")
            return

        if amount == None:
            await ctx.send("Please Enter Amount.")
            return
        
        bal = await jsonfunc.update_bank(self,ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You Don't have Enough Money To Withdraw!")
            return
        if amount<0:
            await ctx.send("Amount Must Be Positive!")
            return

        await jsonfunc.update_bank(self, ctx.author,-1*amount)
        await jsonfunc.update_bank(self, ctx.author,amount,"bank")

        
        em = discord.Embed(title= ":bank: Welcome To Bird's Bank. :bank:", color = 	0x0000FF,timestamp=ctx.message.created_at)
        em.add_field(name= f"Amount Deposited in your Account :",value=f"**{amount}** $",inline=False)
        em.add_field(name="Account Holder's Name :", value =f"{ctx.author}", inline=False)
        em.add_field(name="Account Number :", value =member.id, inline=False)
        await ctx.send(embed = em)



class jsonfunc():
    async def get_bank_data(self, user):
        with open("bank.json", "r") as f:
            users = json.load(f)
        return users

    async def open_account(self, user):

        users = await jsonfunc.get_bank_data(self, user)

        if int(user.id) in users:
            return
        else:
            users[int(user.id)] = {}
            users[int(user.id)]["wallet"] = 0
            users[int(user.id)]["bank"] = 0

        with open("bank.json", "w") as f:
            json.dump(users,f)
        return True


    async def update_bank(self, user,change = 0,mode = "wallet"):
        users = await jsonfunc.get_bank_data(self, user)

        users[str(user.id)][mode] += change

        with open("bank.json", "w") as f:
            json.dump(users,f)

        bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
        return bal


    async def updated_bank(self, user,change = 0,mode = "wallet"): #used in give command to tell remaining balance
        users = await jsonfunc.get_bank_data(self, user)

        users[str(user.id)][mode] += change

        with open("bank.json", "w") as f:
            json.dump(users,f)

        bal = users[str(user.id)]["bank"]
        return bal




    

def setup (client):
    client.add_cog(economy(client))

