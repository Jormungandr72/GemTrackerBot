from interactions import slash_command, SlashContext, OptionType, slash_option
from data.DBManager import DBManager as DBManager

class CommandList:
    """
    -------------------------------------------------------------------------------
    Program:    CommandList.py
    Author:     Patrick J. McGranahan
    Date:       05.10.2025
    Language:   python
    Purpose:    The purpose of this class is to handle slash commands for the
                GemTrackerBot discord bot.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  05.19.2025     Started working on the quests command, formerly the list
                        command. Renamed to avoid confusion. Also made minor 
                        spelling adjustments to the create command, and re-wrote
                        purpose to be more acurate.
    PJM  05.19.2025     Create command is functional. Added it to the list of
                        implemented commands.
    PJM  05.19.2025     Fixed the issue of data not appearing in the database- 
                        needed to commit it using commit()
    PJM  05.19.2025     The create command seemed to work, but the information is
                        not appearing in the db. Currently troubleshooting.
    PJM  05.19.2025     Minor text formatting changed in the create command.
    PJM  05.19.2025     Removed constructor from class CommandList
    PJM  05.19.2025     Began incorporating database connections into the create
                        command.
    PJM  05.17.2025     Removed '_' from the beginning of methods.
    PJM  05.12.2025     Began rewiring for the interactions module.
    PJM  05.10.2025     Started working on the command 'create'. Finished the 
                        documentation for command 'create'.
    PJM  05.10.2025     Added constructor and a sample method 'test'.
    PJM  05.10.2025     Changed class name to CommandList and updated relevant
                        references.
    PJM  05.10.2025     Created class EventHandler, created comment block.
    -------------------------------------------------------------------------------
    """
    # Slash Commands
    @slash_command(name='test', description='hello world', scopes=[1154837347632947313])
    async def test(ctx: SlashContext) -> None:

        await ctx.send(content="Hello World")

    @slash_command(name='commands', description='lists all possible commands', scopes=[1154837347632947313])
    async def commands(ctx: SlashContext) -> bool:
        """
        Lists out all of te bot's possible commands.

        Parameters:
            ctx             (SlashContext): the context of the command

        Return:
            boolean:        {true} if the commands were successfully listed; {false} otherwise.
        """
        await ctx.send(content="Here's a list of all implemented commands:\n" \
                       "/test\n" \
                       "/commands\n" \
                       "/create\n")
        print("User {} used the command 'commands'.".format(ctx.author))
        return True

    @slash_command(name='create', description='create a new investigation', scopes=[1154837347632947313])
    @slash_option(
        name="main_monster",
        description="name of the quest's primary monster",
        required=True,
        opt_type=OptionType.STRING
    )
    @slash_option(
        name="is_tempered",
        description="'True' if the monster is tempered",
        required=False,
        opt_type=OptionType.BOOLEAN,
    )
    @slash_option(
        name="has_gem",
        description="'True' if the quest has a gem",
        required=False,
        opt_type=OptionType.BOOLEAN
    )
    @slash_option(
        name="artian_count",
        description="the total number of artian drops in the quest",
        required=False,
        opt_type=OptionType.INTEGER
    )
    @slash_option(
        name="decoration_count",
        description="the total number of decoration drps in the quest",
        required=False,
        opt_type=OptionType.INTEGER
    )
    async def create(ctx: SlashContext, main_monster: str, is_tempered: bool = False, has_gem: bool = False, 
                      artian_count: int = 0, decoration_count: int = 0) -> bool:
        """
        Command to create and store a quest.

        Parameters:
            ctx                 (SlashContext): the context of the command
            main_monster        (string):       the main monster of the quest
            is_tempered         (boolean):      {true} if the main monster is tempered; {false} otherwise
            has_gem             (boolean):      {true} if the quest has a guaranteed gem reward; {false} otherwise
            artian_count        (integer):      the total number of artian drops in the quest
            decoration_count    (integer):      the total number of decoration drops in the quest

        Return:
            boolean:        {true} if the quest was successfully created; {false} if the creation failed.
        """
        # Repeat the entered fields
        await ctx.send(content="Attepting to create a quest where\n" \
        "- {} is the main monster\n" \
        "- Tempered is {}\n" \
        "- Gem is {}\n" \
        "- Artian count is {}\n" \
        "- Decoration count is {}".format(main_monster, is_tempered, has_gem, artian_count, decoration_count), ephemeral=True)
        
        # Add entry to the DB FIXME add try excepts here
        DBManager.cur.execute("insert into quests (main_monster, is_tempered, has_gem, artian_count, decoration_count, user_id) " \
                              "values (?, ?, ?, ?, ?, ?);",
                              (main_monster, is_tempered, has_gem, artian_count, decoration_count, ctx.author_id))
        
        DBManager.con.commit() # FIXME might need to move lower in the method

        # Tell the user they were successful TODO tell the user the quest ID
        await ctx.send(content="The quest was successfully created.")

        print("User {} used the command 'create'.".format(ctx.author))

        return True
    
    @slash_command(name='quests', description='lists all of your quests', scopes=[1154837347632947313])
    async def quests(ctx: SlashContext) -> bool:
        """
        Command to list all of the user's quests.

        Args:
            ctx (SlashContext): the context of the command
        
        Return: {True} if the quests were created successfully; {False} otherwise
        """
        user_id = ctx.author_id