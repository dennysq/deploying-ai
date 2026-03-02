# Assignment 2:

This assignement is based on the course_chat sample.

The goal of this assignment is to design and implement an AI system with a conversational interface.

Before you begin, keep in mind that meeting the requirements is important, but more important is that you solve the technical problems associated with the implementation. The assignment is fairly open-ended and can easily become an expansive project. My recommendation is that you implement a simplified version of the services, before moving to more complex implementation. Remember to test your code constantly.  

## Services

This implementation is based on LangGraph's tools. 

The file main.py contains the llm model calls that controls the chat. Tools are in the files tools_*.py.

### Service 1: API Calls

+ There are a few API calls that we implemented throughout the course. They are organized in tools_facts.py and tools_jokes.py. 
+ Each tool is imported to main and included in the list `tools`.
+ The tools node uses LangGraph's `ToolNode` class and `tools_condition` is the standard tool stopping criteria.
+ All restrictions and tone requirements are in the instructions prompt. It can be found in prompts.py.

### Service 2: Semantic Query

+ This simple implementation is based on our Pitchfork exercise.
+ The tool is also imported from its tools_*.py file.
+ Ensure that the Docker implementation of ChromaDB and Postgres are running.

### Service 3: Your Choice

+ Not implemented

## User Interface

+ Added conversational style with 2 personalities.
+ Implemented in Gradio

---

## Guardrails and Other Limitations

* Include guardrails that prevent users from:

  * Accessing or revealing the system prompt.
  * Modifying the system prompt directly.

* The model must not respond to questions on certain restricted topics:

  * The asisstant has an hipnotism issue, so if the response contains certains words, it will be replaced accordingly 
  * The 2 personalities are part of the tone and they use a tool accordingly
  * You can switch the personality during the conversation if the user requests it.
  * Hope you enjoy this because I did by doing it. 



