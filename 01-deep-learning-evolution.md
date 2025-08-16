# 1. Deep Learning Evolution and Algorithm Families

Modern generative AI builds on decades of research in neural networks and deep learning.  This module surveys the major deep‑learning architectures and explains how the **Transformer** revolution transformed sequence modelling.  By understanding these algorithm families you will be better equipped to appreciate why today’s models work the way they do.

## 1.1 Early neural networks

The earliest artificial neural networks (ANNs) were inspired by biological neurons.  A network consists of many **perceptrons**, each taking weighted inputs, adding a bias and applying an activation function.  When organised into layers and trained via backpropagation, these networks can learn to approximate complex functions.  The TechTarget primer notes that combining perceptrons into multilayer networks enabled researchers to build models capable of solving more challenging tasks and that backpropagation iteratively adjusts weights and biases until predictions match the desired outputs【345178980226592†L117-L149】.  These **multilayer perceptrons** (MLPs) are still used for tabular data and as building blocks for more advanced architectures.

## 1.2 Convolutional Neural Networks (CNNs)

To handle **spatial** data like images, researchers developed **convolutional neural networks**.  A CNN uses filters that slide across an input image to detect edges, textures and other features, followed by pooling layers that reduce dimensionality and fully connected layers that produce a prediction.  The TechTarget article highlights that CNNs are feedforward networks with fixed‑size inputs and outputs, making them well suited for tasks such as facial recognition, medical image analysis and image classification【345178980226592†L103-L116】.  In early layers, filters detect low‑level features (edges and colours); deeper layers build on these to recognise shapes and entire objects【345178980226592†L159-L186】.  CNNs powered breakthroughs in computer vision and remain a cornerstone of deep learning.

## 1.3 Recurrent Neural Networks (RNNs) and LSTMs

Some tasks involve **sequential** data, where the order of elements matters.  **Recurrent neural networks** address this by feeding the output of each time step back into the network.  The same weights are applied repeatedly, enabling the model to “remember” previous inputs.  TechTarget explains that RNNs process sequential data by combining new data with information from prior steps and updating internal states over time【345178980226592†L200-L223】.  This allows RNNs to perform tasks like machine translation and speech recognition.  However, basic RNNs suffer from vanishing gradients, meaning later inputs may dominate earlier ones【345178980226592†L230-L235】.  **Long Short‑Term Memory (LSTM)** networks and **Gated Recurrent Units (GRUs)** were introduced to alleviate this issue by adding gating mechanisms that control information flow.

## 1.4 The evolution to Transformer architectures

While RNNs were the standard for sequence modelling in the early 2010s, they scale poorly to long sequences and cannot easily be parallelised.  The **Transformer** architecture, introduced in the 2017 paper *“Attention is All You Need”*, replaced recurrence with **self‑attention** mechanisms.  A transformer learns to relate each element of a sequence to every other element, allowing it to capture long‑range dependencies and process all tokens in parallel.  DataCamp’s tutorial notes that transformers learn the context of sequential data and generate new data by analysing patterns in large amounts of text【975884836488476†L115-L124】.  They rely almost entirely on attention rather than recurrent connections【975884836488476†L120-L133】 and were first devised to solve machine translation problems【975884836488476†L106-L108】.

The self‑attention mechanism ushered in a **seismic shift** in deep learning.  DataCamp emphasises that transformer models revolutionised natural language processing and broadened the horizons of AI by enabling efficient parallel processing and long‑range reasoning【975884836488476†L74-L90】.  The article points out that the introduction of transformers led to a surge in “foundation models” and large language models like GPT‑3【975884836488476†L142-L166】.  Because transformers can scale effectively to billions of parameters, they have become the backbone of today’s generative systems.

## 1.5 Summary of deep‑learning algorithm families

The following table summarises the main deep‑learning algorithm families and their typical applications:

| Algorithm | Key idea | Typical use cases |
|---|---|---|
| **MLP / Feed‑forward network** | Stacks fully connected layers; learns from tabular or low‑dimensional data | Structured data, regression, classification |
| **Convolutional Neural Network (CNN)** | Uses convolution and pooling layers to extract spatial features | Image classification, object detection, medical imaging【345178980226592†L103-L116】 |
| **Recurrent Neural Network (RNN)** | Loops hidden state through time to model sequences | Language modelling, speech recognition, machine translation【345178980226592†L200-L223】 |
| **Long Short‑Term Memory (LSTM) / GRU** | Gated RNN variant that mitigates vanishing gradients | Longer sequences, time‑series forecasting【345178980226592†L230-L235】 |
| **Transformer** | Relies on self‑attention; processes sequences in parallel; captures long‑range dependencies | Large language models, text generation, machine translation, multimodal models【975884836488476†L115-L133】 |

Deep learning continues to evolve, but understanding these core architectures provides a solid foundation for exploring generative models and the large language models discussed in the next module.