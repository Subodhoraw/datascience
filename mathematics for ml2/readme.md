Great! Let's build a solid Math for ML curriculum together — theory + practice. Here's what we'll cover across our sessions:

**Core topics in Math for ML:**

1. **Linear Algebra** — vectors, matrices, dot products, eigenvalues
2. **Calculus & Optimization** — derivatives, gradients, chain rule, gradient descent
3. **Probability & Statistics** — distributions, Bayes' theorem, expectation
4. **Information Theory** — entropy, KL divergence (used in many ML loss functions)

Let me start with a visual roadmap, then we'll dive into **Topic 1: Linear Algebra** with interactive practice.We'll go in order — **Linear Algebra first**, since it's the foundation everything else builds on. Here's our plan for **Session 1**:

**Linear Algebra for ML — what we'll cover:**

Scalars, vectors, and matrices — what they are and why ML uses them. Then the key operations: dot product (used in every neuron), matrix multiplication (the engine of neural networks), transpose and inverse, and finally the big ideas — eigenvalues and SVD (used in PCA, embeddings, and attention).

Each concept comes with an **interactive demo + practice problems**.

---

Ready to jump in? Let's start with the most fundamental building block:

**What is a vector, and why does ML care about it?**

A vector is just an ordered list of numbers — but in ML, it represents something meaningful. An image patch, a word embedding, a data point. Every input to a neural network is a vector.

Let's build intuition interactively:**Try it:** drag the sliders and watch the vectors move. Notice how the dot product changes as the angle between them changes — that's the core intuition.

---

**The dot product formula:**

`A · B = a₁×b₁ + a₂×b₂ = |A| × |B| × cos(θ)`

In ML, this shows up *everywhere*: every neuron computes `weights · inputs`, every attention score in a transformer is `query · key`, and cosine similarity (used in embeddings) is just the normalized dot product.

---

**Your first practice problem:**

Given vectors `A = [2, 3, -1]` and `B = [4, -1, 2]`:

1. Compute `A · B` by hand
2. What does the sign of the result tell you about the angle between them?

Try it and reply with your answer — I'll check it and then we move to **matrix multiplication**!
