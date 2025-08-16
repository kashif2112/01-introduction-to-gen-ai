# 2. Large Language Models and Prompt Engineering

The rapid progress of deep learning and transformer architectures gave rise to **large language models (LLMs)**.  These powerful generative models can understand and produce human‑like text, answer questions, translate languages and even write code.  This module explains what LLMs are, how they work and why **prompt engineering** has become an essential skill for getting the most from them.

## 2.1 What are large language models?

Large language models are neural networks trained on vast corpora of text to predict the next token in a sequence.  They build on transformer architectures: instead of processing words sequentially like RNNs, transformers use self‑attention to model relationships between all words in a sentence.  DataCamp notes that a transformer learns the context of sequential data and can generate new data by analysing patterns in large amounts of text【975884836488476†L115-L124】.  Because transformers discard recurrence and rely on attention, they scale efficiently and handle long‑range dependencies【975884836488476†L120-L133】.  

LLMs are typically trained in two stages:

1. **Pre‑training:** The model is exposed to enormous amounts of unlabelled text and learns to predict the next word given its context.  This unsupervised stage teaches the model grammar, facts about the world and high‑level reasoning abilities.
2. **Fine‑tuning or instruction tuning:** After pre‑training, the model is fine‑tuned on curated datasets or instruction‑follow datasets to specialise it for particular tasks or to align its behaviour with human preferences.

Thanks to this two‑stage process and the scalability of transformers, LLMs like GPT‑3 and GPT‑4 can generate coherent paragraphs, summarise documents, write code and perform a wide range of language tasks.  DataCamp emphasises that the introduction of transformer‑based models spurred a surge in large language models and “foundation models”【975884836488476†L142-L166】.

## 2.2 Why prompts matter

Unlike traditional software where behaviour is coded in advance, an LLM’s behaviour is largely controlled by its **prompt**—the text you provide as input.  According to OpenAI’s guide, a prompt is any text (or image/audio) input that triggers a model’s response【856187891024997†L15-L19】.  Because these models are generative, the way you phrase your request can dramatically affect the output.

**Prompt engineering** is the process of designing and refining prompts to guide an LLM’s responses.  The OpenAI help centre notes that prompt engineering aims to design inputs that effectively guide the model【856187891024997†L21-L24】.  General best practices include:

* **Be clear and specific:** Provide enough context and remove ambiguity.  OpenAI’s guide emphasises that prompts should be precise and explicit to obtain accurate responses【856187891024997†L28-L32】.
* **Iterative refinement:** Start with a basic prompt, evaluate the response and adjust wording, add details or simplify as needed.  Prompt engineering often requires an iterative approach【856187891024997†L34-L39】.
* **Specify tone or style:** To adjust the tone, use descriptive adjectives (formal, friendly, humorous, etc.) to tell the model how to respond【856187891024997†L41-L45】.

Other techniques include **few‑shot prompting** (providing examples of the desired input–output pairs), **zero‑shot prompting** (relying on the model’s pretrained knowledge) and **chain‑of‑thought prompting** (encouraging the model to reason step‑by‑step).  The choice of technique depends on the task and the model.

## 2.3 Putting LLMs to work

Large language models power many of today’s generative AI applications.  Chatbots like ChatGPT use LLMs to engage in open‑ended dialogue, while code assistants use them to generate and fix code.  LLMs can also be combined with tools such as retrieval systems or external APIs to create question‑answering systems and search assistants.  A key takeaway is that the quality of the prompt often determines the quality of the output.  As you explore generative AI further, practising prompt engineering will help you unlock the full potential of these models.