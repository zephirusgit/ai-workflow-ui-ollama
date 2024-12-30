This project works with ollama, installed on windows, although it may also be able to run on linux, mac

It is used to generate logical nodes, which interact with the llm ollama.

The Html generates the nodes, these are sent to the backend in python, and the backend communicates with the ollama server, ollama must be installed and active for the server to start.
The backend can be modified to use the gpt/claude/gemini/grok api etc.
Since I don't have any api, only the gemini one, which is limited for this type of things, don't even try to modify it.
If someone can do it and it works for them, you can collaborate and we will add it.

To compile the backend use:
pip install pyinstaller
pyinstaller --onefile backend3flaskcoors.py

The server can also be started from powershell
with
ollama serve

The backend was compiled to exe, to simplify its use in windows
but it can be activated from powershell as well with
python backend3flaskcoors.py
It requires having flask and coors

By editing the backend you can choose another model of ollama,
But by default llama3 comes

How does it work?

You run ollama, so that the llama icon appears in the taskbar, or you launch ollama serve in powershell (after installation).

You run the backend, either the exe or the .py

and then you open the html, which will open the interface.
There are certain colors that the nodes have, which can vary if they require something that they don't have, which serve as a guide.
Green connected well:
Blue Requires an input (text or another node)
Red has no input or output.

We have several different types of nodes,
with them we can create logic circuits to interact with the llm,

this can be extremely useful for many things in which we want the llm to do something and take that response for something else,

Nodes:
LLm Input: this node enters a text which will go to the llm, the response obtained will go to the next node,

you can put only one output to see the response, or some other node,

Output: this node can receive and display the response,
it saves it to a txt, and if necessary it can continue to another node,

Route: it takes an output and directs it to 2 different nodes.

Connection: it is only used to verify the connection to the Backend, red if it does not connect, and green if it connects,
I was thinking of adding options for the llm model there, but for now it does nothing, it only checks if it connects or not.
by default it will use llama3, if you do not have it installed it will download ollama, and it depends on the hardware of your system whether it works or not.

Combiner: it takes two inputs, and combines them one after the other, with this, one can take two different texts and combine them, or a response from the input, and combine it with a text, or with another input etc.
it is very useful to define a prompt, which will analyze the response next, (that the llm gives for the second input) and that combination will be forwarded to the llm with Redirect.
It will flash blue if it is missing an input.

Redirect: This node takes an input and forwards it to the llm,
If you create a prompt, it will receive it and forward it to the llm, you can also add a prompt, which will be triggered together with the input, if the check mark is marked, usually if it is empty the check mark should also be marked,

Text: With this node we can write a prompt, which can go directly to the combiner or another node,
If you use it before a combiner, you must press send text to send it to the next node.

Random: This node requires that a list of objects be loaded, separated by ";" its function will be to take a random value from that list. These could be names for example
Hugo;Paco;Luis, or for example races, Orcs;Mages;Archers;Paladin;Robot;Human;Farmer
The node will select one at random.
In this way, it will pass the selection to the next node.

List Selection: This node, like Random, will take an object from the list, and then the next one, and at the end it will start over, as a result it will send that object to the next node,

Both list selection and random have an Input,
this is in case you want to enter the list directly from the llm,
for example if the inputllm says: create a list separated by ";" of for example names, car brands, foods, etc. if the answer is correct, the node will work fine, if not not.., you can add to the list generator prompt, things like do not comment anything, limit yourself to answering only the list separated by ; without adding anything else, etc.
with the correct prompt it works very well.

Output: The output will display the response from inputllm or Redirect. and it can also continue to another node, saving the response to text, if the response already exists it will generate a txt (1) (2) (3) etc, but that can vary depending on the browser. These responses will go to downloads
The Auto-relaunch check mark is used so that when you reach the end, the whole process starts again.

This way you can iterate by taking new names from a list, or creating new lists, etc.

Save Workflow to file: This node saves the project to a json, but there I have a bug, which I could not solve yet,
the code was created with ia, and I reached the limit available for free, on several platforms, I do not program in html, but as much as I understand the basics I have not had time to see what is wrong, so, if someone understands the code and sees the error, your help is welcome,
for now it saves the nodes and the text inside, but not the unions, and when opening it in open, it does not show the connections or let you reconnect them, I think the problem is in the numbering of the nodes, or something like that..

maybe someone who has paid Gpt4o or Claude, can solve it, I have tried with gemini/1.5 pro/2 flast etc, but I do not fully understand the solution, I also tried with deepseek, gpt4, and others. I need an llm that has a lot of context to solve that, I haven't had much time to continue investigating, I added some things by hand, but since I understand little or nothing about html, it took me a long time.
Unfortunately I lost my job after 11 years in a school, due to circumstances beyond my control, so the little free time I had will disappear.

Donations are accepted, to access an llm that has enough context window, to see if I can solve that saving problem. and expand the nodes.

What can be done for example?

I have asked him to create lists of elven names separated by ;
to take those names at random, or by list and create a story located in a random location, among several.

that creates characters based on their name, a random profession and their history,

that creates 20 chapter titles,
that takes them from a list,
that generates one chapter at a time,
that summarizes it, that takes the summary to generate the second chapter, and so on.

In this way, by iterating automatically one can create books, stories, material for RPG games, etc.

Another example:
There is a type of llms jailbreak, which works by changing some characters to numbers etc., this works in all llms, some say that it needs 10 thousand iterations, so that it gives a forbidden response, but in some cases it is much less, 10, 20, 30 iterations,
In this way one can ask it in a text node
to convert the following text with letters and numbers and characters.

In another text input, the prompt (blocked)
For example, it creates a proxy

Text1 Inputllm >
text2 > Combine > Combine, (converted text sends it to the llm to see if it takes it) >>Redirect > Output (automatic)

This will convert the prompt, and send it as a prompt,
the llm tends to respond sooner or later.

This will generate many txt files, failed I can't answer that, etc. but it is simply a matter of comparing the size of the answers, to filter out the long answers that are usually the unblocked ones, from the negative ones..

Another example,
input (give me a list of the nuclear power plants in the USA separated by ;) >>>>

Output >>> List >>> Redirect (give me the geoposition gps coordinates of each plant) >> output with the list one by one

Output >>> Redirect (give me the geoposition gps coordinates of each plant) >> output with the list of the total with their gps coordinates.

That example occurred to me, to see what it would respond, but fantastically it returned its gps coordinates, I don't know if they are real, but oh well, it responded,

Continuation of the project:

I have created another git, still empty, with new ideas,
Future:

Hallucinations:

I have tried prompts like, you are a linux console, and you must solve such code, or Jupiter console, etc.
and it has given very good answers, as if it were executing the code, "hallucinating" it

Now, based on the hallucinations, it is also possible to create a workflow to solve tasks, and auto-generate the workflow.. (just as it sounds, I tried to solve several things that way, and it solved them the same or differently using the nodes)

if one then takes that answer and creates them, they work!
the idea is that one day it will do them automatically.

(I have created a new git for that project called
https://github.com/zephirusgit/thinkflow
for now empty-

I don't know when I will be able to continue it since it becomes much more complex in some sense, and I need more advanced tools for it, such as paid gpt or claude, etc.) so if you want and can donate to contribute you are welcome
(also if you have those tools and you can ask him to solve the bug when saving)

or the auto-generate nodes,
the request would be something like this, (but first you have to correct the problem when saving since it will depend on it to auto-generate the nodes,

based on the source code of this code (the html)
and this prompt, which generates a problem resolution using the same nodes it contains, creates a new html with a node called thinkflow, which uses the current tools, and the result of the llm, to generate a file and save it, from the workflow proposed by the llm, following the same format to be able to import it like any other workflow.

Would this work? I think so!

An example of this type of prompt

Based on the following nodes, it creates
a workflow to create a list of nuclear reactors in the USA, and to geoposition them,

LLm Input, sends a prompt to the llm and generates an output, this node does not have inputs, only manual, but writing could be simulated, for a node that receives from another node you have to use redirect;
Output. receives Output from the llm or previous node and saves it, it can also continue to another node;
Redirect, forwards to the llm what it receives plus a prompt and generates an output;
Router, sends to 2 nodes what it receives;
Combine, takes two inputs either from the llm, text, another combine, etc., and joins it to the second input;
Random, takes a random word from text separated by (;) this text must be generated previously, if you ask the llm for a random or a list, you must specify that it does not comment, and only creates the list and the separation with (;);
List, takes a word from a list separated by (;) and returns one word per cycle of the list;
Text, is used to enter a text, for example to the combine or the redirect, basically it is a text for the next node, it is not sent to the direct llm, so the next node does not receive a response itself, but the text it includes. etc;

Here is a workflow to create a list of nuclear reactors in the US and then geoposition them:

1. **Router** -> **Input**
- Send prompt: "Enter information about nuclear reactors in the US."

2. **Input**
- Takes no input, only manual.
- Generate manual prompt for the list of nuclear reactors in the US.

3. **Output** -> **Redirect**
- Send message: "Collect the information from the input and create a list with the names and locations of nuclear reactors in the US."

4. **Redirect**
- Include prompt: "Create a list of nuclear reactors in the US."
- Generate output.

5. **Output** -> **Combine**
- Combine the output with the text "Geoposition the following nuclear reactors:"

6. **Combine**
- Output: "Geoposition the following nuclear reactors:" + list of reactors

7. **Redirect**
- Include prompt: "Geoposition the following nuclear reactors: [generated list]"
- Generate output with the geoposition of each reactor.

8. **Output** -> **Combine**
- Combine the output of the geopositioning with the text "Summary:"

9. **Combine**
- Final output: "Summary:" + list of reactors and their geographic locations

This workflow follows a logical sequence to create a list of nuclear reactors in the US, geoposition them, and present a summary of the information.

