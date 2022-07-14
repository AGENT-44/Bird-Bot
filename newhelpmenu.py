from operator import mod
from os import name
import discord
from discord import client
from discord.ext import commands
from reactionmenu import ReactionMenu, Button, ButtonType


class helpmenu(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help3(self, ctx):
        user = ctx.author
        
        home=discord.Embed(title=":robot: COMMANDS FOR BIRD BOT :robot:", description="`You Can Use Below Emoticons To Directly Go To Specific Category.`", color=0xff0000)
        home.set_author(name=f"{user}", icon_url=user.avatar_url)
        home.add_field(name="Admin Commands : :shield:", value="\u200b", inline=False)
        home.add_field(name="Fun Commands : <:Angrypanda:768423787179540520>", value="\u200b", inline=False)
        home.add_field(name="Economy Commands : :moneybag:", value="\u200b", inline=False)
        home.add_field(name="Moderation Commands : :bangbang:", value="\u200b", inline=False)
        home.add_field(name="Misc Commands : :black_joker:", value="\u200b", inline=False)
        home.set_footer(text="Made By: @ΔGΣNT#6841")
        home.set_image(url="https://yt3.ggpht.com/ytc/AKedOLQc1OCf9gztVmcVnmI_41uN9axrRP8wd4a-GflFRQ=s900-c-k-c0x00ffffff-no-rj")

        admin_menu = discord.Embed(title=":shield: Admin Commands :shield:", description="`Only User's With Administrator Permission Can Use These Command's.`", color=0x185ddc)
        admin_menu.add_field(name="1. Ban", value="Usage: `#ban {@User.mention}`", inline=False)
        admin_menu.add_field(name="2. Unban", value="Usage: `#unban {Username#0000}`", inline=False)
        admin_menu.add_field(name="3. Nuke", value="Usage: `#nuke` (__:warning: WARNING--> This Command Will Delete Every Single Channel In Your Server!:warning:__)", inline=False)
        
        fun_menu = discord.Embed(title="<:Angrypanda:768423787179540520> Fun Commands <:Angrypanda:768423787179540520>", color=0x170047)
        fun_menu.add_field(name="1. Ask Jinni", value="Usage: `#askjinni` `(question)`", inline=False)
        fun_menu.add_field(name="2. Avatar", value="Usage: `#avatar`", inline=False)
        fun_menu.add_field(name="3. Meme", value="Usage: `#meme`", inline=False)
        fun_menu.add_field(name="4. Roll Dice", value="Usage: `#rolldice` (Give's You Random Number Between 1 to 6)", inline=False)
        fun_menu.add_field(name="5. Server Icon", value="Usage: `#servericon` (Get Your Server Icon)", inline=False)
        fun_menu.add_field(name="6. Translate", value="Usage:  `#translate` `{language}` `{text you want to translate}`",inline= False)
        fun_menu.add_field(name="7. UserInfo", value="Usage: `#userinfo` `{user.mention}`", inline=False)

        eco_menu = discord.Embed(title=":moneybag: Economy Commands :moneybag:", description="` ECONOMY MENU `", color=0xeebb2f)
        eco_menu.add_field(name="1. Balance", value="Usage: `#balance`", inline=False)
        eco_menu.add_field(name="2. Beg", value="Usage: `#beg`", inline=False)
        eco_menu.add_field(name="3. Deposit", value="Usage: `#deposit` `{amount}`", inline=False)
        eco_menu.add_field(name="4. Give", value="Usage: `#give`     `{user.mention}` `{amount}`", inline=False)
        eco_menu.add_field(name="5. Withdraw", value="Usage: `#withdraw` `{amount}`", inline=False)


        mod_menu = discord.Embed(title=":bangbang: Moderation Commands :bangbang:", description="` MODERATION MENU `", color=0xf72b2b)
        mod_menu.add_field(name="1. Clear", value="Usage: `#clear` `{msg amount}`", inline=False)
        mod_menu.add_field(name="2. Kick", value="Usage: `#kick` `{user.mention}`", inline=False)
        
        


        menu = ReactionMenu(ctx, back_button='◀️', next_button='▶️', config=ReactionMenu.STATIC)
        fpb = Button(emoji='⏪', linked_to=ButtonType.GO_TO_FIRST_PAGE)
        lpb = Button(emoji='⏩', linked_to=ButtonType.GO_TO_LAST_PAGE)
        esb = Button(emoji='❌', linked_to=ButtonType.END_SESSION)
        admin_button = Button(emoji='🛡', linked_to=ButtonType.CUSTOM_EMBED, embed = admin_menu)
        fun_button = Button(emoji="<:Angrypanda:768423787179540520>", linked_to=ButtonType.CUSTOM_EMBED, embed = fun_menu)
        eco_button = Button(emoji="💰", linked_to=ButtonType.CUSTOM_EMBED, embed = eco_menu)

        
        menu.add_button(fpb)
        menu.add_button(lpb)
        menu.add_button(esb)
        menu.add_button(admin_button)
        menu.add_button(fun_button)
        menu.add_button(eco_button)

        menu.add_page(home)
        menu.add_page(admin_menu)
        menu.add_page(fun_menu)
        menu.add_page(eco_menu)

        await menu.start(send_to=715157691734949909)
        



def setup(client):
    client.add_cog(helpmenu(client))