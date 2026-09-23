# Demo: Module 10: Prompting Techniques for Python Development

**Duration:** 12 minutes
**Prerequisite:** VS Code open at the repository root, your preferred approved AI assistant ready in a **new** chat. Have `prompts.txt` open to copy from. AI output varies; narrate what you actually get.

## Part 1: Weak prompt vs business context (3 min)
- Paste prompt **1**. Ask the room: "What did it have to guess?" (which indicator, countries, years, output).
- Start a new chat. Paste prompt **2**. Point out that the business context ("briefing for trade policy colleagues") changes the tone and the choices, and the indicator code removes guesswork.

## Part 2: Format and constraints (3 min)
Paste prompt **3** in the same chat. Show that the column names and types now match what the rest of our pipeline expects. Run the code.

## Part 3: Iterate, do not restart (3 min)
- Paste prompt **4**. "One requirement at a time, and run after each."
- Deliberately introduce an error (for example, rename the cache file path) and paste the traceback back into the chat. Show how the assistant uses the error text.

## Part 4: Documentation and review (3 min)
- Paste prompt **5**: docstrings and an assumptions list. Read the assumptions out loud: "Would you have spotted all of these?"
- Paste prompt **6**: the assistant as critical reviewer.
- Show `project-instructions.md`: standing instructions so you do not repeat context in every prompt.

## Key message
Better prompts come from better context: say who it is for, what data you have, what shape you want and what rules apply, then improve the result one step at a time.
