# A tutorial on the free-energy framework for modelling perception and learning

Rafal Bogacz

Journal of Mathematical Psychology 76 (2017), 198–211. https://doi.org/10.1016/j.jmp.2015.11.003

© 2015 The Author. Open access under the Creative Commons Attribution (CC BY) license.

*Markdown transcription. Figure images are omitted; their captions are retained. Mathematical notation has been converted to LaTeX.*

## Abstract

This paper provides an easy to follow tutorial on the free-energy framework for modelling perception developed by Friston, which extends the predictive coding model of Rao and Ballard. These models assume that the sensory cortex infers the most likely values of attributes or features of sensory stimuli from the noisy inputs encoding the stimuli. Remarkably, these models describe how this inference could be implemented in a network of very simple computational elements, suggesting that this inference could be performed by biological networks of neurons. Furthermore, learning about the parameters describing the features and their uncertainty is implemented in these models by simple rules of synaptic plasticity based on Hebbian learning. This tutorial introduces the free-energy framework using very simple examples, and provides step-by-step derivations of the model. It also discusses in more detail how the model could be implemented in biological neural circuits. In particular, it presents an extended version of the model in which the neurons only sum their inputs, and synaptic plasticity only depends on activity of pre-synaptic and post-synaptic neurons.

## Highlights

- Bayesian inference about stimulus properties can be performed by networks of neurons.

- Learning about statistics of stimuli can be achieved by Hebbian synaptic plasticity.

- Structure of the model resembles the hierarchical organization of the neocortex.

## 1. Introduction

The model of Friston (2005) and the predictive coding model of Rao and Ballard (1999) provide a powerful mathematical framework to describe how the sensory cortex extracts information from noisy stimuli. The predictive coding model (Rao & Ballard, 1999) suggests that visual cortex infers the most likely properties of stimuli from noisy sensory input. The inference in this model is implemented by a surprisingly simple network of neuron-like nodes. The model is called “predictive coding”, because some of the nodes in the network encode the differences between inputs and predictions of the network. Remarkably, learning about features present in sensory stimuli is implemented by simple Hebbian synaptic plasticity, and Rao and Ballard (1999) demonstrated that the model presented with natural images learns features resembling receptive fields of neurons in the primary visual cortex.

Friston (2005) has extended the model to also represent uncertainty associated with different features. He showed that learning about the variance and co-variance of features can also be implemented by simple synaptic plasticity rules based on Hebbian learning. As the extended model (Friston, 2005) learns the variance and co-variance of features, it offers several new insights. First, it describes how the perceptual systems may differentially weight sources of sensory information depending on their level of noise. Second, it shows how the sensory networks can learn to recognize features that are encoded in the patterns of covariance between inputs, such as textures. Third, it provides a natural way to implement attentional modulation as the reduction in variance of the attended features (we come back to these insights in Discussion). Furthermore, Friston (2005) pointed out that this model can be viewed as an approximate Bayesian inference based on minimization of a function referred to in statistics as free-energy. The free-energy framework (Friston, 2003, Friston, 2005) has been recently extended by Karl Friston and his colleagues to describe how the brain performs different cognitive functions including action selection (FitzGerald et al., 2015, Friston et al., 2013). Furthermore, Friston (2010) proposed that the free-energy theory unifies several theories of perception and action which are closely related to the free-energy framework.

There are many articles which provide an intuition for the free-energy framework and discuss how it relates with other theories and experimental data (Friston, 2003, Friston, 2005, Friston, 2010, Friston et al., 2013). However, the description of mathematical details of the theory in these papers requires a very deep mathematical background. The main goal of this paper is to provide an easy to follow tutorial on the free-energy framework. To make the tutorial accessible to a wide audience, it only assumes basic knowledge of probability theory, calculus and linear algebra. This tutorial is planned to be complementary to existing literature so it does not focus on the relationship to other theories and experimental data, and on applications to more complex tasks which are described elsewhere (Friston, 2010, Friston et al., 2013).

In this tutorial we also consider in more detail the neural implementation of the free-energy framework. Any computational model would need to satisfy the following constraints to be considered biologically plausible:

1. Local computation: A neuron performs computations only on the basis of the activity of its input neurons and synaptic weights associated with these inputs (rather than information encoded in other parts of the circuit).

2. Local plasticity: Synaptic plasticity is only based on the activity of pre-synaptic and post-synaptic neurons.

The model of Rao and Ballard (1999) fully satisfied these constraints. The model of Friston (2005) did not satisfy them fully, but we show that after small modifications and extensions it can satisfy them. So the descriptions of the model in this tutorial slightly differ in a few places or extend the original model to better explain how the proposed computation could be implemented in the neural circuits. All such differences or extensions are indicated by footnotes or in text, and the original model is presented in Appendix A.

It is commonly assumed in theoretical neuroscience, (O’Reilly & Munakata, 2000) that the basic computations a neuron performs are the summation of its input weighted by the strengths of synaptic connections, and the transformation of this sum through a (monotonic) function describing the relationship between neurons’ total input and output (also termed firing-Input or f-I curve). Whenever possible, we will assume that the computation of the neurons in the described model is limited to these computations (or even just to linear summation of inputs).

We feel that the neural implementation of the model is worth considering, because if the free-energy principle indeed describes the computations in the brain, it can provide an explanation for why the cortex is organized in a particular way. However to gain such insight it is necessary to start comparing the neural networks implementing the model with those in the real brain. Consequently, we consider in this paper possible neural circuits that could perform the computations required by the theory. Although the neural implementations proposed here are not the only possible ones, it is worth considering them as a starting point for comparison of the model with details of neural architectures in the brain. We hope that such comparison could iteratively lead to refined neural implementations that are more and more similar to real neural circuits.

To make this tutorial as easy to follow as possible we introduce the free-energy framework using a simple example, and then illustrate how the model can scale up to more complex neural architectures. The tutorial provides step-by-step derivation of the model. Some of these derivations are straightforward, and we feel that it would be helpful for the reader to do them on their own to gain a better understanding of the model and to “keep in mind” the notation used in the paper. Such straightforward derivations are indicated by “(TRY IT YOURSELF)”, so after encountering such label we recommend trying to do the calculation described in the sentence with this label and then compare the obtained results with those in the paper. To illustrate the model we include simple simulations, but again we feel it would be helpful for a reader to perform them on their own, to get an intuition for the model. Therefore we describe these simulations as exercises.

The paper is organized as follows. Section  2 introduces the model using a very simple example using as basic mathematical concepts as possible, so it is accessible to a particularly wide audience. Section  3 provides mathematical foundations for the model, and shows how the inference in the model is related to minimization of free-energy. Section  4 then shows how the model scales up to describe the neural circuits in sensory cortex. In these three sections we use notation similar to that used by Friston (2005). Section  5 describes an extended version of the model which satisfies the constraint of local plasticity described above. Finally, Section  6 discusses insights provided by the model.

## 2. Simplest example of perception

We start by considering in this section a simple perceptual problem in which a value of a single variable has to be inferred from a single observation. To make it more concrete, consider a simple organism that tries to infer the size or diameter of a food item, which we denote by $v$, on the basis of light intensity it observes. Let us assume that our simple animal has only one light sensitive receptor which provides it with a noisy estimate of light intensity, which we denote by $u$. Let $g$ denote a non-linear function relating the average light intensity with the size. Since the amount of light reflected is related to the area of an object, in this example we will consider a simple function of $g(v) = v^{2}$. Let us further assume that the sensory input is noisy—in particular, when the size of food item is $v$, the perceived light intensity is normally distributed with mean $g(v)$, and variance $\Sigma_{u}$ (although a normal distribution is not the best choice for a distribution of light intensity, as it includes negative numbers, we will still use it for a simplicity):

$$
p\left( u \middle| v \right) = f\left( u;g(v),\Sigma_{u} \right)\text{.} \tag{1}
$$

In Eq. (1)$f(x;\mu,\Sigma)$ denotes the density of a normal distribution with mean $\mu$ and variance $\Sigma$:

$$
f(x;\mu,\Sigma) = \frac{1}{\sqrt{2\pi\Sigma}}\exp\left( - \frac{(x - \mu)^{2}}{2\Sigma} \right)\text{.} \tag{2}
$$

Due to the noise present in the observed light intensity, the animal can refine its guess for the size $v$ by combining the sensory stimulus with the prior knowledge on how large the food items usually are, that it had learnt from experience. For simplicity, let us assume that our animal expects this size to be normally distributed with mean $v_{p}$ and variance $\Sigma_{p}$ (subscript $p$ stands for “prior”), which we can write as:

$$
p(v) = f\left( v;v_{p},\Sigma_{p} \right)\text{.} \tag{3}
$$

Let us now assume that our animal observed a particular value of light intensity, and attempts to estimate the size of the food item on the basis of this observation. We will first consider an exact solution to this problem, and illustrate why it would be difficult to compute it in a simple neural circuit. Then we will present an approximate solution that can be easily implemented in a simple network of neurons.

### 2.1. Exact solution

To compute how likely different sizes $v$ are given the observed sensory input $u$, we could use Bayes’ theorem:

$$
p\left( v \middle| u \right) = \frac{p(v)p\left( u \middle| v \right)}{p(u)}\text{.} \tag{4}
$$

Term $p(u)$ in the denominator of Eq. (4) is a normalization term, which ensures that the posterior probabilities of all sizes $p\left( v \middle| u \right)$ integrate to 1:

$$
p(u) = \int p(v)p\left( u \middle| v \right)dv\text{.} \tag{5}
$$

The integral in the above equation sums over the whole range of possible values of $v$, so it is a definite integral, but for brevity of notation we do not state the limits of integration in this and all other integrals in the paper.

Now combining Eqs. (1), (2), (3), (4), (5) we can compute numerically how likely different sizes are given the sensory observation. For readers who are not familiar with such Bayesian inference we recommend doing the following exercise now.

> #### Exercise 1
>
> *Assume that our animal observed the light intensity* $u = 2$*, the level of noise in its receptor is* $\Sigma_{u} = 1$*, and the mean and variance of its prior expectation of size are* $v_{p} = 3$ *and* $\Sigma_{p} = 1$*. Write a computer program that computes the posterior probabilities of sizes from*  0.01  *to*  5*, and plots them.*

The Matlab code performing this calculation is given at the end of the paper, and the resulting plot is shown in Fig. 1. It is worth observing that such Bayesian approach integrates the information brought by the stimulus with prior knowledge: please note that the most likely value of $v$ lies between that suggested by the stimulus (i.e. $\sqrt{2}$) and the most likely value based on prior knowledge (i.e. 3). It may seem surprising why the posterior probability is so low for $v = 3$, i.e. the mean prior expectation. It comes from the fact that $g(3) = 9$, which is really far from observed value $u = 2$, so $p\left( u = 2 \middle| v = 3 \right)$ is very close to zero. This illustrates how non-intuitive Bayesian inference can be once the relationship between variables is non-linear.

> **Fig. 1.** *[Figure image omitted.]*
>
> The posterior probability of the size of the food item in the problem given in Exercise 1 .

Let us now discuss why performing such exact calculation is challenging for a simple biological system. First, as soon as function $g$ relating the variable we wish to infer with observations is non-linear, the posterior distribution $p\left( v \middle| u \right)$ may not take a standard shape—for example the distribution in Fig. 1 is not normal. Thus representing the distribution $p\left( v \middle| u \right)$ requires representing infinitely many values $p\left( v \middle| u \right)$ for different possible $u$ rather than a few summary statistics like mean and variance. Second, the computation of the posterior distribution involves computation of the normalization term. Although it has been proposed that circuits within the basal ganglia can compute the normalization term in case of the discrete probability distributions (Bogacz & Gurney, 2007), computation of the normalization for continuous distributions involves evaluating the integral of Eq. (5). Calculating such integral would be challenging for a simple biological system. This is especially true when the dimensionality of the integrals (i.e., the number of unknown variables) increases beyond a trivial number. Even mathematicians resort to (computationally very expensive) numerical or sampling techniques in this case.

We will now present an approximate solution to the above inference problem, that could be easily implemented in a simple biological system.

### 2.2. Finding the most likely feature value

Instead of finding the whole posterior distribution $p\left( v \middle| u \right)$, let us try to find the most likely size of the food item $v$ which maximizes $p\left( v \middle| u \right)$. We will denote this most likely size by $\phi$, and its posterior probability density by $p\left( \phi \middle| u \right)$. It is reasonable to assume that in many cases the brain represents at a given moment of time only most likely values of features. For example in case of binocular rivalry, only one of the two possible interpretations of sensory inputs is represented.

We will look for the value $\phi$ which maximizes $p\left( \phi \middle| u \right)$. According to Eq. (4), the posterior probability $p\left( \phi \middle| u \right)$ depends on a ratio of two quantities, but the denominator $p(u)$ does not depend on $\phi$. Thus the value of $\phi$ which maximizes $p\left( \phi \middle| u \right)$ is the same one which maximizes the numerator of Eq. (4). We will denote the logarithm of the numerator by $F$, as it is related to the negative of free energy (as we will describe in Section  3):

$$
F = \ln p(\phi) + \ln p\left( u \middle| \phi \right)\text{.} \tag{6}
$$

In the above equation we used the property of logarithm $\ln(ab) = \ln a + \ln b$. We will maximize the logarithm of the numerator of Eq. (4), because it has the same maximum as the numerator itself as $\ln$ is a monotonic function, and is easier to compute as the expressions for $p\left( u \middle| \phi \right)$ and $p(\phi)$ involve exponentiation.

To find the parameter $\phi$ that describes the most likely size of the food item, we will use a simple gradient ascent: i.e. we will modify $\phi$ proportionally to the gradient of $F$, which will turn out to be a very simple operation. It is relatively straightforward to compute $F$ by substituting Eqs. (1), (2), (3) into Eq. (6) and then to compute the derivative of $F$ (TRY IT YOURSELF).

$$
F = \ln f\left( \phi;v_{p},\Sigma_{p} \right) + \ln f\left( u;g(\phi),\Sigma_{u} \right) = \ln\left\lbrack \frac{1}{\sqrt{2\pi\Sigma_{p}}}\exp\left( - \frac{\left( \phi - v_{p} \right)^{2}}{2\Sigma_{p}} \right) \right\rbrack + \ln\left\lbrack \frac{1}{\sqrt{2\pi\Sigma_{u}}}\exp\left( - \frac{\left( u - g(\phi) \right)^{2}}{2\Sigma_{u}} \right) \right\rbrack = \ln\frac{1}{\sqrt{2\pi}} - \frac{1}{2}\ln\Sigma_{p} - \frac{\left( \phi - v_{p} \right)^{2}}{2\Sigma_{p}} + \ln\frac{1}{\sqrt{2\pi}} - \frac{1}{2}\ln\Sigma_{u} - \frac{\left( u - g(\phi) \right)^{2}}{2\Sigma_{u}} = \frac{1}{2}\left( - \ln\Sigma_{p} - \frac{\left( \phi - v_{p} \right)^{2}}{\Sigma_{p}} - \ln\Sigma_{u} - \frac{\left( u - g(\phi) \right)^{2}}{\Sigma_{u}} \right) + C\text{.} \tag{7}
$$

We incorporated the constant terms in the 2nd line above into a constant $C$. Now we can compute the derivative of $F$ over $\phi$:

$$
\frac{\partial F}{\partial\phi} = \frac{v_{p} - \phi}{\Sigma_{p}} + \frac{u - g(\phi)}{\Sigma_{u}}g^{\prime}(\phi)\text{.} \tag{8}
$$

In the above equation we used the chain rule to compute the second term, and $g^{\prime}(\phi)$ is a derivative of function $g$ evaluated at $\phi$, so in our example $g^{\prime}(\phi) = 2\phi$. We can find our best guess $\phi$ for $v$ simply by changing $\phi$ in proportion to the gradient:

$$
\overset{˙}{\phi} = \frac{\partial F}{\partial\phi}\text{.} \tag{9}
$$

In the above equation $\overset{˙}{\phi}$ is the rate of change of $\phi$ with time. Let us note that the update of $\phi$ is very intuitive. It is driven by two terms in Eq. (8): the first moves it towards the mean of the prior, the second moves it according to the sensory stimulus, and both terms are weighted by the reliabilities of prior and sensory input respectively.

Now please note that the above procedure for finding the approximate distribution of distance to food item is computationally much simpler than the exact method presented at the start of the paper. To gain more appreciation for the simplicity of this computation we recommend doing the following exercise.

> #### Exercise 2
>
> *Write a computer program finding the most likely size of the food item* $\phi$ *for the situation described in*   Exercise  1*. Initialize* $\phi = v_{p}$*, and then find its values in the next*  5  *time units (you can use Euler’s method, i.e. update* $\phi(t + \Delta t) = \phi(t) + \Delta t\partial F/\partial\phi$ *with* $\Delta t = 0.01$ *).*

Fig. 2(a) shows a solution to Exercise 2. Please notice that it rapidly converges to the value of $\phi \approx 1.6$, which is also the value that maximizes the exact posterior probability $p\left( v \middle| u \right)$ shown in Fig. 1.

> **Fig. 2.** *[Figure image omitted.]*
>
> Solutions to Exercise 2 , Exercise 3 . In panel b we have also included quantities that we will see later can be regarded as prediction errors.

### 2.3. A possible neural implementation

One can envisage many possible ways in which the computation described in previous subsection could be implemented in neural circuits. In this paper we will present a possible implementation which satisfies the constraints of local computation and plasticity described in the Introduction. It slightly differs from the original implementation which is contained in Appendix A.

While thinking about the neural implementation of the above computation, it is helpful to note that there are two similar terms in Eq. (8), so let us denote them by new variables.

$$
\varepsilon_{p} = \frac{\phi - v_{p}}{\Sigma_{p}} \tag{10}
$$

$$
\varepsilon_{u} = \frac{u - g(\phi)}{\Sigma_{u}}\text{.} \tag{11}
$$

The above terms are the prediction errors[^1]: $\varepsilon_{u}$ expresses how much the light intensity differs from that expected if the size of the food item was $\phi$, while $\varepsilon_{p}$ denotes how the inferred size differs from prior expectations. With these new variables the equation for updating $\phi$ simplifies to:

$$
\overset{˙}{\phi} = \varepsilon_{u}g^{\prime}(\phi) - \varepsilon_{p}\text{.} \tag{12}
$$

The neural implementation of the model assumes that the model parameters $v_{p}$, $\Sigma_{p}$, and $\Sigma_{u}$ are encoded in the strengths of synaptic connections (as they need to be maintained over the animal’s lifetime), while variables $\phi$, $\varepsilon_{u}$, and $\varepsilon_{p}$ and the sensory input $u$ are maintained in the activity of neurons or neuronal populations (as they change rapidly when the sensory input is modified). In particular, we will consider very simple neural “nodes” which simply change their activity proportionally to the input they receive, so for example, Eq. (12) is implemented in the model by a node receiving input equal to the right hand side of this equation. The prediction errors could be computed by the nodes with the following dynamics[^2]:

$$
\overset{˙}{\varepsilon_{p}} = \phi - v_{p} - \Sigma_{p}\varepsilon_{p} \tag{13}
$$

$$
\overset{˙}{\varepsilon_{u}} = u - g(\phi) - \Sigma_{u}\varepsilon_{u}\text{.} \tag{14}
$$

It is easy to show that the nodes with dynamics described by Eqs. (13)–(14) converge to the values defined in Eqs. (10)–(11). Once Eqs. (13)–(14) converge, then $\overset{˙}{\varepsilon} = 0$, so setting $\overset{˙}{\varepsilon} = 0$ and solving Eqs. (13)–(14) for $\varepsilon$, one obtains Eqs. (10)–(11).

The architecture of the network described by Eqs. (12), (13), (14) is shown in Fig. 3. Let us consider the computations in its nodes. The node $\varepsilon_{p}$ receives excitatory input from node $\phi$, inhibitory input from a tonically active neuron via a connection with strength $v_{p}$, and inhibitory input from itself via a connection with strength $\Sigma_{p}$, so it implements Eq. (13). The nodes $\phi$ and $\varepsilon_{u}$ analogously implement Eqs. (12), (14), but here the information exchange between them is additionally affected by function $g$, and we will discuss this issue in more detail in Section  2.5. We have now described all the details necessary to simulate the model.

> #### Exercise 3
>
> *Simulate the model from*   Fig.  3   *for the problem from*   Exercise  1*. In particular, initialize* $\phi = v_{p},\varepsilon_{p} = \varepsilon_{u} = 0$*, and find their values for the next*  5  *units of time.*

> **Fig. 3.** *[Figure image omitted.]*
>
> The architecture of the model performing simple perceptual inference. Circles denote neural “nodes”, arrows denote excitatory connections, while lines ended with circles denote inhibitory connections. Labels above the connections encode their strength, and lack of label indicates the strength of 1. Rectangles indicate the values that need to be transmitted via the connections they label.

Solution to Exercise 3 is shown in Fig. 2(b). The model converges to the same value as in Fig. 2(a), but the convergence is just slower, as the model now includes multiple nodes connected by excitatory and inhibitory connections and such networks have oscillatory tendencies, so these oscillations need to settle for the network to converge.

### 2.4. Learning model parameters

As our imaginary animal perceives food items through its lifetime, it may wish to refine its expectation about typical sizes of food items described by parameters $v_{p}$ and $\Sigma_{p}$, and about the amount of error it makes observing light intensity, described by parameter $\Sigma_{u}$. Thus it may wish to update the parameters $v_{p},\Sigma_{p}$, and $\Sigma_{u}$ after each stimulus to gradually refine them.

We wish to choose the model parameters for which the perceived light intensities $u$ are least surprising, or in other words most expected. Thus we wish to choose parameters that maximize $p(u)$. However, please recall that $p(u)$ is described by a complicated integral of Eq. (5), so it would be difficult to maximize $p(u)$ directly. Nevertheless, it is simple to maximize a related quantity $p(u,\phi)$, which is the joint probability of sensory input $u$ and our inferred food size $\phi$. Note that $p(u,\phi) = p(\phi)p\left( u \middle| \phi \right)$, so $F = \ln p(u,\phi)$, thus maximization of $p(u,\phi)$ can be achieved by maximizing $F$. A more formal explanation for why the parameters can be optimized by maximizing $F$ will be provided in Section  3.

The model parameters can be hence optimized by modifying them proportionally to the gradient of $F$. Starting with the expression in Eq. (7) it is straightforward to find the derivatives of $F$ over $v_{p},\Sigma_{p}$ and $\Sigma_{u}$ (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial v_{p}} = \frac{\phi - v_{p}}{\Sigma_{p}} \tag{15}
$$

$$
\frac{\partial F}{\partial\Sigma_{p}} = \frac{1}{2}\left( \frac{\left( \phi - v_{p} \right)^{2}}{\Sigma_{p}^{2}} - \frac{1}{\Sigma_{p}} \right) \tag{16}
$$

$$
\frac{\partial F}{\partial\Sigma_{u}} = \frac{1}{2}\left( \frac{\left( u - g(\phi) \right)^{2}}{\Sigma_{u}^{2}} - \frac{1}{\Sigma_{u}} \right)\text{.} \tag{17}
$$

Let us now provide an intuition for why the parameter update rules have their particular form. We note that since parameters are updated after observing each food item, and different food items observed during animal’s life time have different sizes, the parameters never converge. Nevertheless it is useful to consider the values of parameters for which the expected value of change is 0, as these are the values in vicinity of which the parameters are likely to be. For example, according to Eq. (15), the expected value of change in $v_{p}$ is 0 when $\left\langle \left( \phi - v_{p} \right)/\Sigma_{p} \right\rangle = 0$, where $\langle\rangle$ denotes the expected value over trials. This will happen if $v_{p} = \left\langle \phi \right\rangle$, i.e. when $v_{p}$ is indeed equal to the expected value of $\phi$. Analogously, the expected value of change in $\Sigma_{p}$ is 0 when:

$$
\left\langle \frac{\left( \phi - v_{p} \right)^{2}}{\Sigma_{p}^{2}} - \frac{1}{\Sigma_{p}} \right\rangle = 0\text{.} \tag{18}
$$

Rearranging the above condition one obtains $\Sigma_{p} = \left\langle \left( \phi - v_{p} \right)^{2} \right\rangle$, thus the expected value of change in $\Sigma_{p}$ is 0, when $\Sigma_{p}$ is equal to the variance of $\phi$. An analogous analysis can be made for $\Sigma_{u}$.

Eqs. (15), (16), (17) for update of model parameters simplify significantly when they are written in terms of prediction errors (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial v_{p}} = \varepsilon_{p} \tag{19}
$$

$$
\frac{\partial F}{\partial\Sigma_{p}} = \frac{1}{2}\left( \varepsilon_{p}^{2} - \Sigma_{p}^{- 1} \right) \tag{20}
$$

$$
\frac{\partial F}{\partial\Sigma_{u}} = \frac{1}{2}\left( \varepsilon_{u}^{2} - \Sigma_{u}^{- 1} \right)\text{.} \tag{21}
$$

The above rules for update of parameters correspond to very simple synaptic plasticity mechanisms. All rules include only values that can be “known” by the synapse, i.e. the activities of pre-synaptic and post-synaptic neurons, and the strengths of the synapse itself. Furthermore, the rules are Hebbian, in the sense that they depend on the products of activity of pre-synaptic and post-synaptic neurons. For example, the change in $v_{p}$ in Eq. (19) is equal to the product of pre-synaptic activity (i.e. 1) and the post-synaptic activity $\varepsilon_{p}$. Similarly, the changes in $\Sigma$ in Eqs. (20)–(21) depend on the products of pre-synaptic and post-synaptic activities, both equal to $\varepsilon$.

The plasticity rules of Eqs. (20)–(21) also depend on the value of synaptic weights themselves, as they include terms $\Sigma^{- 1}$. For the simple case considered in this section, the synapse “has access” to the information on its weight. Moreover, the dependence of synaptic plasticity on initial weights has been seen experimentally (Chen et al., 2013), so we feel it is plausible for the dependence predicted by the model to be present in real synapses. However, when the model is scaled up to include multiple features and sensory inputs in Section  4.1, terms $\Sigma^{- 1}$ will turn into a matrix inverse (in Eqs. (48)–(49)), so the required changes in each weight will depend on the weights of other synapses in the network. Nevertheless, we will show in Section  5 how this problem can be overcome.

Finally, we would like to discuss the limits on parameters $\Sigma$. Although in principle the variance of a random variable can be equal to 0, if $\Sigma_{p} = 0$ or $\Sigma_{u} = 0$, then Eq. (13) or (14) would not converge but instead $\varepsilon_{p}$ or $\varepsilon_{u}$ would diverge to positive or negative infinity. Similarly, if $\Sigma$ were close to 0, the convergence would be very slow. To prevent this from happening, the minimum value of 1 is imposed by Friston (2005) on the estimated variance.[^3]

### 2.5. Learning the relationship between variables

So far we have assumed for simplicity that the relationship $g$ between the variable being inferred and the stimulus is known. However, in general it may not be known, or may need to be tuned. So we will now consider function $g(v,\theta)$ that also depends on parameter which we denote by $\theta$.

We will consider two special cases of function $g(v,\theta)$, where the parameter $\theta$ has a clear biological interpretation. First, let us consider a simple case of a linear function: $g(v,\theta) = \theta v$, as then the model has a straightforward neural implementation. In this case, Eqs. (12), (13), (14) describing the model simplify to:

$$
\overset{˙}{\phi} = \theta\varepsilon_{u} - \varepsilon_{p} \tag{22}
$$

$$
\overset{˙}{\varepsilon_{p}} = \phi - v_{p} - \Sigma_{p}\varepsilon_{p} \tag{23}
$$

$$
\overset{˙}{\varepsilon_{u}} = u - \theta\phi - \Sigma_{u}\varepsilon_{u} \tag{24}
$$

In this model, nodes $\phi$ and $\varepsilon$ simply communicate through connections with weight $\theta$ as shown in Fig. 4(a). Furthermore, we can also derive the rule for updating the parameter $\theta$ by finding the gradient of $F$ over $\theta$, as now function $g$ in Eq. (7) depends on $\theta$ (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial\theta} = \varepsilon_{u}\phi\text{.} \tag{25}
$$

> **Fig. 4.** *[Figure image omitted.]*
>
> Architectures of models with linear and nonlinear function g . Circles and hexagons denote linear and nonlinear nodes respectively. Filled arrows and lines ended with circles denote excitatory and inhibitory connections respectively, and an open arrow denotes a modulatory influence.

Please note that this rule is again Hebbian, as the synaptic weights encoding $\theta$ are modified proportionally to the activities of pre-synaptic and post-synaptic neurons (see Fig. 4(a)).

Second, let us consider a case of a nonlinear function[^4]$g(v,\theta) = \theta h(v)$, where $h(v)$ is a nonlinear function that just depends on $v$, as it results in only slightly more complex neural implementation. Furthermore, this situation is relevant to the example of the simple animal considered at the start of this section, as the light is proportional to the area, but the proportionality constant may not be known (this case is also relevant to the network that we will discuss in Section  4.1). In this case, Eqs. (12), (13), (14) describing the model become:

$$
\overset{˙}{\phi} = \theta\varepsilon_{u}h^{\prime}(\phi) - \varepsilon_{p} \tag{26}
$$

$$
\overset{˙}{\varepsilon_{p}} = \phi - v_{p} - \Sigma_{p}\varepsilon_{p} \tag{27}
$$

$$
\overset{˙}{\varepsilon_{u}} = u - \theta h(\phi) - \Sigma_{u}\varepsilon_{u}\text{.} \tag{28}
$$

A possible network implementing this model is illustrated in Fig. 4(b), which now includes non-linear elements. In particular, the node $\phi$ sends to node $\varepsilon_{u}$ its activity transformed by a non-linear function, i.e. $\theta h(\phi)$. One could imagine that this could be implemented by an additional node receiving input from node $\phi$, transforming it via a non-linear transformation $h$ and sending its output to node $\varepsilon_{u}$ via a connection with the weight $\theta$. Analogously, the input from node $\varepsilon_{u}$ to node $\phi$ needs to be scaled by $\theta h^{\prime}(\phi)$. Again one could imagine that this could be implemented by an additional node receiving input from node $\phi$, transforming it via a non-linear transformation $h^{\prime}$ and modulating input received from node $\varepsilon_{u}$ via a connection with weight $\theta$ (alternatively, this could be implemented within the node $\phi$ by making it react to its input differentially depending on its level of activity). The details of the neural implementation of these non-linear transformations depend on the form of function $h$, and would be an interesting direction of the future work.

We also note that the update of the parameter $\theta$, i.e. gradient of $F$ over $\theta$ becomes:

$$
\frac{\partial F}{\partial\theta} = \varepsilon_{u}h(\phi)\text{.} \tag{29}
$$

This rule is Hebbian for the top connection labelled by $\theta$ in Fig. 4(b), as it is a product of activity of the pre-synaptic and post-synaptic nodes. It would be interesting to investigate how such a plasticity rule could be realized for the other connection with the weight of $\theta$ (from node $\varepsilon_{u}$ to $\phi$). We just note that for this connection the rule also satisfies the constraint of local plasticity (stated in the Introduction), as $\phi$ fully determines $h(\phi)$, so the change in weight is fully determined by the activity of pre-synaptic and post-synaptic neurons.

## 3. Free-energy

In this section we discuss how the computations in the model relate to a technique of statistical inference involving minimization of free-energy. There are three reasons for describing this relationship. First, it will provide more insight for why the parameters can be optimized by maximization of $F$. Second, the concept of free-energy is critical for understanding of more complex models (Friston et al., 2013), which not only estimate the most likely values of variables, but their distribution. Third, the free-energy is a very interesting concept on its own, and has applications in mathematical psychology (Ostwald, Kirilina, Starke, & Blankenburg, 2014).

We now come back to the example of an inference by a simple organism, and discuss how the exact inference described in Section  2.1 can be approximated. As we noted in Section  2.1, the posterior distribution $p\left( v \middle| u \right)$ may have a complicated shape, so we will approximate it with another distribution, which we denote $q(v)$. Importantly, we will assume that $q(v)$ has a standard shape, so we will be able to characterize it by parameters of this typical distribution. For example, if we assume that $q(v)$ is normal, then to fully describe it, we can infer just two numbers: its mean and variance, instead of infinitely many numbers potentially required to characterize a distribution of an arbitrary shape.

For simplicity, here we will use an even simpler shape of the approximate distribution, namely the delta distribution, which has all its mass cumulated in one point which we denote by $\phi$ (i.e. the delta distribution is equal to 0 for all values different from $\phi$, but its integral is equal to 1). Thus we will try to infer from observation just one parameter $\phi$ which will characterize the most likely value of $v$.

We now describe what criterion we wish our approximate distribution to satisfy. We will seek the approximate distribution $q(v)$ which is as close as possible to the actual posterior distribution $p\left( v \middle| u \right)$. Mathematically, the dissimilarity between two distributions in measured by the Kullback–Leibler divergence defined as:

$$
\mathit{KL}\left( q(v),p\left( v \middle| u \right) \right) = \int q(v)\ln\frac{q(v)}{p\left( v \middle| u \right)}dv\text{.} \tag{30}
$$

For readers not familiar with Kullback–Leibler divergence we would like clarify why it is a measure of dissimilarity between the distributions. Please note that if the two distributions $q(v)$ and $p\left( v \middle| u \right)$ were identical, the ratio $q(v)/p\left( v \middle| u \right)$ would be equal to 1, so its logarithm would be equal to 0, and so the whole expression in Eq. (30) would be 0. The Kullback–Leibler divergence also has a property that the more different the two distributions are, the higher its value is (see Ostwald et al. (2014) for more details).

Since we assumed above that our simplified distribution is a delta function, we will simply seek the value of its centre parameter $\phi$ which minimizes the Kullback–Leibler divergence defined in Eq. (30).

It may seem that the minimization of Eq. (30) is still difficult, because to compute term $p\left( v \middle| u \right)$ present in Eq. (30) from Bayes’ theorem (Eq. (4)) one needs to compute the difficult normalization integral (Eq. (5)). However, we will now show that there exists another way of finding the approximate distribution $q(v)$ that does not involve the complicated computation of the normalization integral.

Substituting the definition of conditional probability $p\left( v \middle| u \right) = p(u,v)/p(u)$ into Eq. (30) we obtain:

$$
\mathit{KL}\left( q(v),p\left( v \middle| u \right) \right) = \int q(v)\ln\frac{q(v)p(u)}{p(u,v)}dv = \int q(v)\ln\frac{q(v)}{p(u,v)}dv + \int q(v)dv\ln p(u) = \int q(v)\ln\frac{q(v)}{p(u,v)}dv + \ln p(u)\text{.} \tag{31}
$$

In the transition from the second to the third line we used the fact that $q(v)$ is a probability distribution so its integral is 1. The integral in the last line of the above equation is called free-energy, and we will denote its negative by $F$, because we will show below, that for certain assumptions the negative free-energy is equal (modulo a constant) to the function $F$ we defined and used in the previous section:

$$
F = \int q(v)\ln\frac{p(u,v)}{q(v)}dv\text{.} \tag{32}
$$

In the above equation we used the property of logarithms that $- \ln a/b = \ln b/a$. So, the negative free-energy is related to the Kullback–Leibler divergence in the following way:

$$
\mathit{KL}\left( q(v),p\left( v \middle| u \right) \right) = - F + \ln p(u)\text{.} \tag{33}
$$

Now please note that $\ln p(u)$ does not depend on $\phi$ (which is a parameter describing $q(v)$), so the value of $\phi$ that minimizes the distance between $q(v)$ and $p\left( v \middle| u \right)$ is the same value as that which maximizes $F$. Therefore instead of minimizing the Kullback–Leibler divergence we can maximize $F$, and this will have two benefits: first, as we already mentioned above, $F$ is easier to compute as it does not involve the complicated computation of the normalization term. Second, as we will see later, it will allow us to naturally introduce learning about the parameters of the model.

Let us first note that by assuming that $q(v)$ is a delta distribution, the negative free energy simplifies to:

$$
F = \int q(v)\ln\frac{p(u,v)}{q(v)}dv = \int q(v)\ln p(u,v)dv - \int q(v)\ln q(v)dv = \ln p(u,\phi) + C_{1}\text{.} \tag{34}
$$

In the transition from the first to the second line above we used the property of logarithms $\ln(a/b) = \ln a - \ln b$. In the transition from the second line to the third line we used the property of a delta function $\delta(x)$ with centre $\phi$ that for any function $h(x)$, the integral of $\delta(x)h(x)$ is equal to $h(\phi)$. Furthermore, since the value of the second integral in the second line of the above equation does not depend on $\phi$ (so it will cancel when we compute the derivative over $\phi$) we denote it by a constant $C_{1}$.

Now using $p(u,\phi) = p(\phi)p\left( u \middle| \phi \right)$, and ignoring constant $C_{1}$, we obtain the expression for $F$ we introduced previously in Eq. (6). Thus finding approximate delta distribution $q(v)$ through minimization of free-energy is equivalent to the inference of features in the model described in the previous section. It is worth noting that Eq. (34) states that the best centre for our approximate distribution (i.e. our best guess for the size of the food item) is the value $v = \phi$ which maximizes the joint probability $p(u,\phi)$.

We now discuss how the concept of free-energy will help us to understand why the parameters of the model can be learnt by maximization of $F$. Recall from Section  2.4 that we wish to find parameters for which the sensory observations are least surprising, i.e. those which maximize $p(u)$. To see the relationship between maximizing $p(u)$ and maximizing $F$, we note that according to Eq. (33), $p(u)$ is related to the negative free-energy in the following way:

$$
\ln p(u) = F + \mathit{KL}\left( q(v),p\left( v \middle| u \right) \right)\text{.} \tag{35}
$$

Since Kullback–Leibler divergence is non-negative, $F$ is a lower bound on $\ln p(u)$, thus by maximizing $F$ we maximize the lower bound on $\ln p(u)$. So in summary, by maximizing $F$ we can both find an approximate distribution $q(v)$ (as discussed earlier), and optimize model parameters. However, there is a twist here: we wish to maximize the average of $p(u)$ across trials (or here observations of different food items). Thus on each trial we need to modify the model parameters just a little bit (rather than until minimum of free energy is reached as was the case for $\phi$).

## 4. Scaling up the model of perception

In this section we will show how the model scales up to the networks inferring multiple features and involving hierarchy.

### 4.1. Increasing the dimension of sensory input

The model naturally scales up to the case of multiple sensory inputs from which we estimate multiple variables. Such scaled model could be used to describe information processing within a cortical area (e.g. primary visual cortex) which infers multiple features (e.g. edges at different position and orientation) on the basis of multiple inputs (e.g. information from multiple retinal receptors preprocessed by the thalamus). This section shows that when the dimensionality of inputs and features is increased, the dynamics of nodes in the networks and synaptic plasticity are described by the same rules as in Section  2, just generalized to multiple dimensions.

The only complication in explaining this case lies in the necessity to use matrix notation, so let us make this notation very explicit: we will denote single numbers in italic (e.g. $x$), column vectors by bar (e.g. $\overline{x}$), and matrices in bold (e.g. $\mathbf{x}$). So we assume the animal has observed sensory input $\overline{u}$ and estimates the most likely values $\overline{\phi}$ of variables $\overline{v}$. We further assume that the animal has prior expectation that the variables $\overline{v}$ come from multivariate normal distribution with mean ${\overline{v}}_{p}$ and covariance matrix $\mathbf{\Sigma}_{\mathbf{p}}$, i.e. $p\left( \overline{v} \right) = f\left( \overline{v};{\overline{v}}_{p},\mathbf{\Sigma}_{\mathbf{p}} \right)$ where:

$$
f\left( \overline{x};\overline{\mu},\mathbf{\Sigma} \right) = \frac{1}{\sqrt{(2\pi)^{N}\left| \mathbf{\Sigma} \right|}}\exp\left( - \frac{1}{2}\left( \overline{x} - \overline{\mu} \right)^{T}\mathbf{\Sigma}^{- 1}\left( \overline{x} - \overline{\mu} \right) \right)\text{.} \tag{36}
$$

In the above equation $N$ denotes the length of vector $\overline{x}$, and $\left| \mathbf{\Sigma} \right|$ denotes the determinant of matrix $\mathbf{\Sigma}$. Analogously, the probability of observing sensory input given the values of variables is given by $p\left( \overline{u} \middle| \overline{v} \right) = f\left( \overline{u};g\left( \overline{v},\mathbf{\Theta} \right),\mathbf{\Sigma}_{\mathbf{u}} \right)$, where $\mathbf{\Theta}$ are parameters of function $g$. We denote these parameters by a matrix $\mathbf{\Theta}$, as we will consider a generalization of the function $g$ discussed in Section  2.5, i.e. $g\left( \overline{v},\mathbf{\Theta} \right) = \mathbf{\Theta}h\left( \overline{v} \right)$, where each element $i$ of vector $h\left( \overline{v} \right)$ depends only on $v_{i}$. This function corresponds to an assumption often made by models of feature extraction (Bell and Sejnowski, 1995, Olshausen and Field, 1995), that stimuli are formed by a linear combination of features.[^5] Moreover, such a function $g$ can be easily computed as it is equal to an input to a layer of neurons from another layer with activity $h\left( \overline{v} \right)$ via connections with strength $\mathbf{\Theta}$.

We can state the negative free energy, analogously as for the simple model considered in Eq. (7) (TRY IT YOURSELF):

$$
F = \ln p\left( \overline{\phi} \right) + \ln p\left( \overline{u} \middle| \overline{\phi} \right) = \frac{1}{2}\left( - \ln\left| \mathbf{\Sigma}_{\mathbf{p}} \right| - \left( \overline{\phi} - {\overline{v}}_{p} \right)^{T}\mathbf{\Sigma}_{\mathbf{p}}^{- 1}\left( \overline{\phi} - {\overline{v}}_{p} \right) - \ln\left| \mathbf{\Sigma}_{\mathbf{u}} \right| - \left( \overline{u} - g\left( \overline{\phi},\mathbf{\Theta} \right) \right)^{T}\mathbf{\Sigma}_{\mathbf{u}}^{- 1}\left( \overline{u} - g\left( \overline{\phi},\mathbf{\Theta} \right) \right) \right) + C\text{.} \tag{37}
$$

Analogously as before, to find the vector of most likely values of features $\overline{\phi}$, we will calculate the gradient (vector of derivatives $\partial F/\partial\phi_{i}$) which we will denote by $\partial F/\partial\overline{\phi}$. We will use the elegant property that rules for computation of derivatives generalize to vectors and matrices. To get an intuition for these rules we recommend the following exercise that shows how the rule $\partial x^{2}/\partial x = 2x$ generalizes to vectors.

> #### Exercise 4
>
> *Show that for any vector* $\overline{x}$*the gradient of function* $y = {\overline{x}}^{T}\overline{x}$ *is equal to:* $\partial y/\partial\overline{x} = 2\overline{x}$*.*

Using an analogous method as that in the solution to Exercise 4 (at the end of the paper) one can see that several other rules generalize as summarized in Table 1. These rules can be applied for symmetric matrices, but since $\mathbf{\Sigma}$ are covariance matrices, they are symmetric, so we can use the top two rules in Table 1 to compute the gradient of the negative free energy (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial\overline{\phi}} = - \mathbf{\Sigma}_{\mathbf{p}}^{- 1}\left( \overline{\phi} - {\overline{v}}_{p} \right) + \frac{{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)}^{T}}{\partial\overline{\phi}}\mathbf{\Sigma}_{\mathbf{u}}^{- 1}\left( \overline{u} - g\left( \overline{\phi},\mathbf{\Theta} \right) \right)\text{.} \tag{38}
$$

#### Table 1.

Rules for computation of derivatives. $\mathbf{A}$ denotes a symmetric matrix.

| Original rule                                                                                                                | Generalization to matrices                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $\frac{\partial ax^{2}}{\partial x} = 2ax$                                                                                   | $\frac{\partial{\overline{x}}^{T}\mathbf{A}\overline{x}}{\partial\overline{x}} = 2\mathbf{A}\overline{x}$                                                                                                                                          |
| if $z = f(y)$, $y = g(x)$, then $\frac{\partial z}{\partial x} = \frac{\partial y}{\partial x}\frac{\partial z}{\partial y}$ | if $z = f\left( \overline{y} \right)$, $\overline{y} = g\left( \overline{x} \right)$, then $\frac{\partial z}{\partial\overline{x}} = \left( \frac{\partial\overline{y}}{\partial\overline{x}} \right)^{T}\frac{\partial z}{\partial\overline{y}}$ |
| $\frac{\partial\ln a}{\partial a} = \frac{1}{a}$                                                                             | $\frac{\partial\ln\left| \mathbf{A} \right|}{\partial\mathbf{A}} = \mathbf{A}^{- 1}$                                                                                                                                                               |
| $\frac{\partial\frac{x^{2}}{a}}{\partial a} = - \frac{x^{2}}{a^{2}}$                                                         | $\frac{\partial{\overline{x}}^{T}\mathbf{A}^{- 1}\overline{x}}{\partial\mathbf{A}} = - \left( \mathbf{A}^{- 1}\overline{x} \right)\left( \mathbf{A}^{- 1}\overline{x} \right)^{T}$                                                                 |

In the above equation, terms appear which are generalizations of the prediction errors we defined for the simple models:

$$
{\overline{\varepsilon}}_{p} = \mathbf{\Sigma}_{\mathbf{p}}^{- 1}\left( \overline{\phi} - {\overline{v}}_{p} \right) \tag{39}
$$

$$
{\overline{\varepsilon}}_{u} = \mathbf{\Sigma}_{\mathbf{u}}^{- 1}\left( \overline{u} - g\left( \overline{\phi},\mathbf{\Theta} \right) \right)\text{.} \tag{40}
$$

With the error terms defined, the equation describing the update of $\overline{\phi}$ becomes:

$$
\overset{˙}{\overline{\phi}} = - {\overline{\varepsilon}}_{p} + \frac{{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)}^{T}}{\partial\overline{\phi}}{\overline{\varepsilon}}_{u}\text{.} \tag{41}
$$

The partial derivative term in the above equation is a matrix that contains in each entry with co-ordinates $(i,j)$ the derivative of element $i$ of vector $g\left( \overline{\phi},\mathbf{\Theta} \right)$ over $\phi_{j}$. To see how the above equation simplifies for our choice of function $g$, it is helpful without loss of generality to consider a case of 2 features being estimated from 2 stimuli. Then:

$$
g\left( \overline{\phi},\mathbf{\Theta} \right) = \mathbf{\Theta}h\left( \overline{\phi} \right) = \left\lbrack \begin{array}{l}
{\theta_{1,1}h\left( \phi_{1} \right) + \theta_{1,2}h\left( \phi_{2} \right)} \\
{\theta_{2,1}h\left( \phi_{1} \right) + \theta_{2,2}h\left( \phi_{2} \right)}
\end{array} \right\rbrack\text{.} \tag{42}
$$

Hence we can find the derivatives of elements of the above vector over the elements of vector $\overline{\phi}$:

$$
\frac{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)}{\partial\overline{\phi}} = \left\lbrack \begin{array}{ll}
{\theta_{1,1}h^{\prime}\left( \phi_{1} \right)} & {\theta_{1,2}h^{\prime}\left( \phi_{2} \right)} \\
{\theta_{2,1}h^{\prime}\left( \phi_{1} \right)} & {\theta_{2,2}h^{\prime}\left( \phi_{2} \right)}
\end{array} \right\rbrack\text{.} \tag{43}
$$

Now we can see that Eq. (41) can be written as:

$$
\overset{˙}{\overline{\phi}} = - {\overline{\varepsilon}}_{p} + h^{\prime}\left( \overline{\phi} \right) \times \mathbf{\Theta}^{T}{\overline{\varepsilon}}_{u}\text{.} \tag{44}
$$

In the above equation × denotes element by element multiplication, so term $h^{\prime}\left( \overline{\phi} \right) \times \mathbf{\Theta}^{T}{\overline{\varepsilon}}_{u}$ is a vector where its element $i$ is equal to a product of $h^{\prime}\left( \phi_{i} \right)$ and element $i$ of vector $\mathbf{\Theta}^{T}{\overline{\varepsilon}}_{u}$. Analogously, as for the simple model, prediction errors could be computed by nodes with the following dynamics:

$$
{\overset{˙}{\overline{\varepsilon}}}_{p} = \overline{\phi} - {\overline{v}}_{p} - \mathbf{\Sigma}_{\mathbf{p}}{\overline{\varepsilon}}_{p} \tag{45}
$$

$$
{\overset{˙}{\overline{\varepsilon}}}_{u} = \overline{u} - \mathbf{\Theta}h\left( \overline{\phi} \right) - \mathbf{\Sigma}_{\mathbf{u}}{\overline{\varepsilon}}_{u}\text{.} \tag{46}
$$

It is easy to see that Eqs. (45)–(46) have fixed points at values given by Eqs. (39)–(40) by setting the left hand sides of Eqs. (45)–(46) to 0. The architecture of the network with the dynamics described by Eqs. (44), (45), (46) is shown in Fig. 5, and it is analogous to that in Fig. 4(b).

> **Fig. 5.** *[Figure image omitted.]*
>
> The architecture of the model inferring 2 features from 2 sensory stimuli. Notation as in Fig. 4 (b). To help identify which connections are intrinsic and extrinsic to each level of hierarchy, the nodes and their projections in each level of hierarchy are shown in green, blue and purple respectively (in the online version). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Analogously as for the simple model, one can also find the rules for updating parameters encoded in synaptic connections, which generalize the rules presented previously. In particular, using the top formula in Table 1 it is easy to see that:

$$
\frac{\partial F}{\partial{\overline{v}}_{p}} = {\overline{\varepsilon}}_{p}\text{.} \tag{47}
$$

Using the two bottom formulas in Table 1 one can find the rules for update of covariance matrices (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial\mathbf{\Sigma}_{\mathbf{p}}} = \frac{1}{2}\left( {\overline{\varepsilon}}_{p}{\overline{\varepsilon}}_{p}^{T} - \mathbf{\Sigma}_{\mathbf{p}}^{- 1} \right) \tag{48}
$$

$$
\frac{\partial F}{\partial\mathbf{\Sigma}_{\mathbf{u}}} = \frac{1}{2}\left( {\overline{\varepsilon}}_{u}{\overline{\varepsilon}}_{u}^{T} - \mathbf{\Sigma}_{\mathbf{u}}^{- 1} \right)\text{.} \tag{49}
$$

The derivation of update of parameters $\mathbf{\Theta}$ is a bit more tedious, but we show in Appendix B that:

$$
\frac{\partial F}{\partial\mathbf{\Theta}} = {\overline{\varepsilon}}_{u}h\left( \overline{\phi} \right)^{T}\text{.} \tag{50}
$$

The above plasticity rules of Eqs. (47), (48), (49), (50) are Hebbian in the same sense they were for the simple model—for example Eq. (48) implies that $\Sigma_{p,i,j}$ should be updated proportionally to $\varepsilon_{p,i}\varepsilon_{p,j}$, i.e. to the product of activity of pre-synaptic and post-synaptic neurons. However, the rules of update of covariance matrices of Eqs. (48)–(49) contain matrix inverses $\mathbf{\Sigma}^{- 1}$. The value of each entry in matrix inverse depends on all matrix elements, so it is difficult how it can be “known” by a synapse that encodes just a single element. Nevertheless, we will show in Section  5 how the model can be extended to satisfy the constraint of local plasticity.

### 4.2. Introducing hierarchy

Sensory cortical areas are organized hierarchically, such that areas in lower levels of hierarchy (e.g. primary visual cortex) infer presence of simple features of stimuli (e.g. edges), on the basis of which the sensory areas in higher levels of hierarchy infer presence of more and more complex features. It is straightforward to generalize the model from 2 layers to multiple layers. In such generalized model the rules describing dynamics of neurons and plasticity of synapses remain exactly the same, and only notation has to be modified to describe presence of multiple layers of hierarchy.

We assume that the expected value of activity in one layer $v_{i}$ depends on the activity in the next layer $v_{i + 1}$:

$$
E\left( \overline{u} \right) = g_{1}\left( {\overline{v}}_{2},\mathbf{\Theta}_{1} \right) \tag{51}
$$

$$
E\left( {\overline{v}}_{2} \right) = g_{2}\left( {\overline{v}}_{3},\mathbf{\Theta}_{2} \right)
$$

$$
E\left( {\overline{v}}_{3} \right) = \ldots\text{.}
$$

To simplify the notation we could denote $u$ by $v_{1}$, and then the likelihood of activity in layer $i$ becomes:

$$p\left( {\overline{v}}_{i} \middle| {\overline{v}}_{i + 1} \right) = f\left( {\overline{v}}_{i};g_{i}\left( {\overline{v}}_{i + 1},\mathbf{\Theta}_{\mathbf{i}} \right),\mathbf{\Sigma}_{\mathbf{i}} \right)\text{.} \tag{52}
$$

In this model, $\mathbf{\Sigma}_{\mathbf{i}}$ parametrize the covariance between features in each level, and $\mathbf{\Theta}_{\mathbf{i}}$ parametrize how the mean value of features in one level depends on the next. Let us assume the same form of function $g$ as before, i.e. $g_{i}\left( {\overline{v}}_{i + 1},\mathbf{\Theta}_{\mathbf{i}} \right) = \mathbf{\Theta}_{\mathbf{i}}h\left( {\overline{v}}_{i + 1} \right)$. By analogy to the model described in the previous subsection, one can see that inference of the features in all layers on the basis of sensory input can be achieved in the network shown in Fig. 6(a). In this network the dynamics of the nodes are described by:

$$
\overset{˙}{{\overline{\phi}}_{i}} = - {\overline{\varepsilon}}_{i} + h^{\prime}\left( {\overline{\phi}}_{i} \right). \ast {\mathbf{\Theta}_{\mathbf{i} - \mathbf{1}}}^{T}{\overline{\varepsilon}}_{i - 1} \tag{53}
$$

$$
{\overset{˙}{\overline{\varepsilon}}}_{i} = {\overline{\phi}}_{i} - \mathbf{\Theta}_{\mathbf{i}}h\left( {\overline{\phi}}_{i + 1} \right) - \mathbf{\Sigma}_{\mathbf{i}}{\overline{\varepsilon}}_{i}\text{.} \tag{54}
$$

> **Fig. 6.** *[Figure image omitted.]*
>
> \(a\) The architecture of the model including multiple layers. For simplicity only the first two layers are shown. Notation as in Fig. 5 . (b) Extrinsic connectivity of cortical layers.

Furthermore, by analogy to the previous section, the rules for modifying synaptic connections in the model become:

$$
\frac{\partial F}{\partial\mathbf{\Sigma}_{\mathbf{i}}} = \frac{1}{2}\left( {\overline{\varepsilon}}_{i}{\overline{\varepsilon}}_{i}^{T} - \mathbf{\Sigma}_{\mathbf{i}}^{- 1} \right) \tag{55}
$$

$$
\frac{\partial F}{\partial\mathbf{\Theta}_{\mathbf{i}}} = {\overline{\varepsilon}}_{i}h\left( {\overline{\phi}}_{i + 1} \right)^{T}\text{.} \tag{56}
$$

The hierarchical structure of the model in Fig. 6(a) parallels the hierarchical structure of the cortex. Furthermore, it is worth noting that different layers within the cortex communicate with higher and lower sensory areas (as illustrated schematically in Fig. 6(b)), which parallel the fact that different nodes in the model communicate with other levels of hierarchy (Fig. 6(a)).

## 5. Local plasticity

The plasticity rules for synapses encoding matrix $\mathbf{\Sigma}$ (describing the variance and co-variance of features or sensory inputs) introduced in the previous section (Eqs. (48), (49), (55)) include terms equal to the matrix inverse $\mathbf{\Sigma}^{- 1}$. Computing each element of the inverse $\mathbf{\Sigma}^{- 1}$ requires not only the knowledge of the corresponding element of $\mathbf{\Sigma}$, but also of other elements. For example, in a case of 2-dimensional vector $\overline{u}$, the update rule for the synaptic connection encoding $\Sigma_{u,1,1}$ (Eq. (49)) requires the computation of $\Sigma_{u,1,1}^{- 1} = \Sigma_{u,2,2}/\left| \mathbf{\Sigma}_{\mathbf{u}} \right|$. Hence the change of synaptic weight $\Sigma_{u,1,1}$ depends on the value of the weight $\Sigma_{u,2,2}$, but these are the weights of connections between different neurons (see Fig. 5), thus the update rule violates the principle of the local plasticity stated in the Introduction. Nevertheless, in this section we show that by slightly modifying the architecture of the network computing prediction errors, the need for computing matrix inverses in the plasticity rules disappears. In other words, we present an extension of the model from the previous section in which learning the values of parameters $\Sigma$ satisfies the constraint of local plasticity. To make the description as easy to follow as possible, we start with considering the case of single sensory input and single feature on each level, and then generalize it to increased dimension of inputs and features.

### 5.1. Learning variance of a single prediction error node

Instead of considering the whole model we now focus on computations in a single node computing prediction error. In the model we wish the prediction error on each level to converge to:

$$
\varepsilon_{i} = \frac{\phi_{i} - g_{i}\left( \phi_{i + 1} \right)}{\Sigma_{i}}\text{.} \tag{57}
$$

In the above equation $\Sigma_{i}$ is the variance of feature $\phi_{i}$ (around the mean predicted by the level above):

$$
\Sigma_{i} = \left\langle \left( \phi_{i} - g_{i}\left( \phi_{i + 1} \right) \right)^{2} \right\rangle\text{.} \tag{58}
$$

A sample architecture of the model that can achieve this computation with local plasticity is shown in Fig. 7(a). It includes an additional inhibitory inter-neuron $e_{i}$ which is connected to the prediction error node, and receives input from it via the connection with weight encoding $\Sigma_{i}$. The dynamics of this model is described by the following set of equations:

$$
\overset{˙}{\varepsilon_{i}} = \phi_{i} - g_{i}\left( \phi_{i + 1} \right) - e_{i} \tag{59}
$$

$$
\overset{˙}{e_{i}} = \Sigma_{i}\varepsilon_{i} - e_{i}\text{.} \tag{60}
$$

> **Fig. 7.** *[Figure image omitted.]*
>
> Prediction error networks that can learn the uncertainty parameter with local plasticity. Notation as in Fig. 4 (b). (a) Single node. (b) Multiple nodes for multidimensional features.

The levels of activity at the fixed point can be found by setting the left hand sides of Eqs. (59)–(60) to 0 and solving the resulting set of simultaneous equations (TRY IT YOURSELF):

$$
\varepsilon_{i} = \frac{\phi_{i} - g_{i}\left( \phi_{i + 1} \right)}{\Sigma_{i}} \tag{61}
$$

$$
e_{i} = \phi_{i} - g_{i}\left( \phi_{i + 1} \right)\text{.} \tag{62}
$$

Thus we see that the prediction error node has a fixed point at the desired value (cf. Eq. (57)). Let us now consider the following rule for plasticity of the connection encoding $\Sigma_{i}$:

$$
\Delta\Sigma_{i} = \alpha\left( \varepsilon_{i}e_{i} - 1 \right)\text{.} \tag{63}
$$

According to this rule the weight is modified proportionally to the product of activities of pre-synaptic and post-synaptic neurons decreased by a constant, with a learning rate $\alpha$. To analyse to what values this rule converges, we note that the expected change is equal to 0 when:

$$
\left\langle \varepsilon_{i}e_{i} - 1 \right\rangle = 0\text{.} \tag{64}
$$

Substituting Eqs. (61)–(62) into the above equation and rearranging terms we obtain:

$$
\frac{\left\langle \left( \phi_{i} - g_{i}\left( \phi_{i + 1} \right) \right)^{2} \right\rangle}{\Sigma_{i}} = 1\text{.} \tag{65}
$$

Solving the above equation for $\Sigma_{i}$ we obtain Eq. (58). Thus in summary the network in Fig. 7(a) computes the prediction error and learns the variance of the corresponding feature with a local Hebbian plasticity rule. To gain more intuition for how this model works we suggest the following exercise.

> #### Exercise 5
>
> *Simulate learning of variance* $\Sigma_{i}$ *over trials. For simplicity, only simulate the network described by Eqs.*   (59)*–*(60)*, and assume that variables* $\phi$ *are constant. On each trial generate input* $\phi_{i}$ *from a normal distribution with mean*  5  *and variance*  2*, while set* $g_{i}\left( \phi_{i + 1} \right) = 5$ *(so that the upper level correctly predicts the mean of* $\phi_{i}$ *). Simulate the network for*  20  *time units, and then update weight* $\Sigma_{i}$ *with learning rate* $\alpha = 0.01$*. Simulate*  1000  *trials and plot how* $\Sigma_{i}$ *changes across trials.*

The results of simulations are shown in Fig. 8, and they illustrate that the synaptic weight $\Sigma_{i}$ approaches the vicinity of the variance of $\phi_{i}$.

> **Fig. 8.** *[Figure image omitted.]*
>
> Changes in estimated variance during learning in Exercise 5 .

It is also worth adding that $\varepsilon_{i}$ in the model described by Eqs. (59)–(60) converges to the prediction error (Eq. (61)), when one assumes that $\phi$ are constant or change on much slower time-scale than $\varepsilon_{i}$ and $e_{i}$. This convergence takes place because the fixed point of the model is stable, which can be shown using the standard dynamical systems theory (Strogatz, 1994). In particular, since Eqs. (59)–(60) only contain linear functions of variables $\varepsilon_{i}$ and $e_{i}$, their solution has a form of exponential functions of time $t$, e.g. $\varepsilon_{i}(t) = c\exp(\lambda t) + \varepsilon_{i}^{\ast}$, where $c$ and $\lambda$ are constants, and $\varepsilon_{i}^{\ast}$ is the value at the fixed point. The sign of $\lambda$ determines the stability of the fixed point: when $\lambda < 0$, the exponential term decreases with time, and $\varepsilon_{i}$ converges to the fixed point, while if $\lambda > 0$, the fixed point is unstable. The values of $\lambda$ are equal to the eigenvalues of the matrix in the equation below (Strogatz, 1994), which rewrites Eqs. (59)–(60) in a vector form:

$$
\left\lbrack \begin{array}{l}
{\overset{˙}{\varepsilon}}_{i} \\
{\overset{˙}{e}}_{i}
\end{array} \right\rbrack = \left\lbrack \begin{array}{ll}
0 & {- 1} \\
\Sigma_{i} & {- 1}
\end{array} \right\rbrack\left\lbrack \begin{array}{l}
\varepsilon_{i} \\
e_{i}
\end{array} \right\rbrack + \left\lbrack \begin{array}{l}
{\phi_{i} - g_{i}\left( \phi_{i + 1} \right)} \\
0
\end{array} \right\rbrack\text{.} \tag{66}
$$

To show that the eigenvalues of the matrix in the above equation are negative we use the property that sum of eigenvalues is equal to the trace and the product to the determinant. The trace and determinant of this matrix are $- 1$ and $\Sigma_{i}$, respectively. Since the sum of eigenvalues is negative and their product positive, both eigenvalues are negative, so the system is stable.

### 5.2. Learning the covariance matrix

The model described in the previous subsection scales up to larger dimension of features and sensory inputs. The architecture of the scaled up network is shown in Fig. 7(b), and its dynamics is described by the following equations:

$$
\overset{˙}{{\overline{\varepsilon}}_{i}} = {\overline{\phi}}_{i} - g_{i}\left( {\overline{\phi}}_{i + 1} \right) - {\overline{e}}_{i} \tag{67}
$$

$$
\overset{˙}{{\overline{e}}_{i}} = \mathbf{\Sigma}_{\mathbf{i}}{\overline{\varepsilon}}_{i} - {\overline{e}}_{i}\text{.} \tag{68}
$$

Analogously as before, we can find the fixed point by setting the left hand side of the equation to 0:

$$
{\overline{\varepsilon}}_{i} = \mathbf{\Sigma}_{\mathbf{i}}^{- 1}\left( {\overline{\phi}}_{i} - g_{i}\left( {\overline{\phi}}_{i + 1} \right) \right) \tag{69}
$$

$$
{\overline{e}}_{i} = {\overline{\phi}}_{i} - g_{i}\left( {\overline{\phi}}_{i + 1} \right)\text{.} \tag{70}
$$

Thus we can see that nodes $\varepsilon$ have fixed points at the values equal to the prediction errors. We can now consider a learning rule analogous to that in the previous subsection:

$$
\Delta\mathbf{\Sigma}_{\mathbf{i}} = \alpha\left( {\overline{\varepsilon}}_{i}{\overline{e}}_{i}^{T} - 1 \right)\text{.} \tag{71}
$$

To find the values to vicinity of which the above rule may converge, we can find the value of $\mathbf{\Sigma}_{\mathbf{i}}$ for which the expected value of the right hand side of the above equation is equal to 0:

$$
\left\langle {\overline{\varepsilon}}_{i}{\overline{e}}_{i}^{T} - 1 \right\rangle = 0\text{.} \tag{72}
$$

Substituting Eqs. (69)–(70) into the above equation, and solving for $\mathbf{\Sigma}_{\mathbf{i}}$ we obtain (TRY IT YOURSELF):

$$
\mathbf{\Sigma}_{\mathbf{i}} = \left\langle \left( {\overline{\phi}}_{i} - g_{i}\left( {\overline{\phi}}_{i + 1} \right) \right)\left( {\overline{\phi}}_{i} - g_{i}\left( {\overline{\phi}}_{i + 1} \right) \right)^{T} \right\rangle\text{.} \tag{73}
$$

We can see that the learning rule has a stochastic fixed point at the values corresponding to the covariance matrix. In summary, the nodes in network described in this section have fixed points at prediction errors and can learn the covariance of the corresponding features, thus the proposed network may substitute the prediction error nodes in the model shown in Fig. 6, and the computation will remain the same. But importantly in the proposed network the covariance is learnt with local plasticity involving simple Hebbian learning.

## 6. Discussion

In this paper we presented the model of perception and learning in neural circuits based on the free-energy framework. This model extends the predictive coding model (Rao & Ballard, 1999) in that it represents and learns not only mean values of stimuli or features, but also their variances, which gives the model several new computational capabilities, as we now discuss.

First, the model can weight incoming sensory information by their reliability. This property arises in the model, because the prediction errors are normalized by dividing them by the variance of noise. Thus the more noisy is a particular dimension of the stimulus, the smaller the corresponding prediction error, and thus lower its influence on activity on other neurons in the network.

Second, the model can learn properties of features encoded in covariance of sensory input. An example of such feature is texture, which can be efficiently recognized on the basis of covariance, irrespectively of translation (Harwood, Ojala, Pietikäinen, Kelman, & Davis, 1995). To get an intuition for this property, let us consider an example of checker-board texture (Fig. 9). Please note that adjacent nodes have always opposite colour–corresponding to negative covariance, while the diagonal nodes have the same colour–corresponding to positive covariance.

> **Fig. 9.** *[Figure image omitted.]*
>
> An example of a texture.

Third, the attentional modulation can be easily implemented in the model by changing the variance associated with the attended features (Feldman & Friston, 2010). Thus for example, attending to feature $i$ at level $j$ of the hierarchy can be implemented by decreasing synaptic weight $\Sigma_{j,i,i}$, or inhibiting node $e_{j,i}$ in case of the model described in Section  5, which will result in a larger effect of the node encoding this feature on the activity in the rest of the network.

In this paper we included description of the modified or extended version of the model with local computation and plasticity to better illustrate how computation proposed by the free-energy framework can be implemented in neural circuits. However, it will be necessary in the future to numerically evaluate the efficiency of learning in the proposed model and the free-energy framework in general. Existing models of feature extraction (Bell and Sejnowski, 1997, Bogacz et al., 2001, Olshausen and Field, 1995) and predictive coding (Rao & Ballard, 1999) have been shown to be able to find features efficiently and reproduce the receptive fields of neurons in the primary visual cortex when trained with natural images. It would be interesting to explicitly test in simulations if the model based on the free-energy framework can equally efficiently extract features from natural stimuli and additionally learn the variance and covariance of features.

We have also demonstrated that if the dynamics within the nodes computing prediction errors takes place on a time-scale much faster than in the whole network, these nodes converge to stable fixed points. It is also worth noting that under the assumption of separation of time scales, the nodes computing $\phi$ also converge to a stable fixed point, because variables $\phi$ converge to the values that maximize function $F$. It would be interesting to investigate how to ensure that the model converges to desired values (rather than engaging into oscillatory behaviour) also when one considers a more realistic case of time-scales not being fully separated.

In summary, in this paper we presented the free-energy theory, which offers a powerful framework for describing computations performed by the brain during perception and learning. The appeal of the similarity in the organization of networks suggested by this theory and observed in the brain invites attempts to map the currently relatively abstract models on details of cortical micro-circuitry, i.e. to map different elements of the model on different neural populations within the cortex. For example, Bastos et al. (2012) compared a more recent version of the model (Friston, 2008) with the details of the cortical organization. Such comparisons of the models with biological circuits are likely to lead to iterative refinement of the models.

Even if the free-energy framework does describe cortical computation, the mapping between the variables in the model and the elements of neural circuit may not be “clean” but rather “messy” i.e. each model variable or parameter may be represented by multiple neurons or synapses. The particular implementation of the framework in the cortical circuit may be influenced by other constraints the evolutionary pressure optimizes such as robustness to damage, energy efficiency, speed of processing, etc. In any case, the comparison of predictions of theoretical framework like the free-energy with experimental data offers hope for understanding the cortical micro-circuits.

## Acknowledgments

This work was supported by Medical Research Council grant MC UU 12024/5. The author thanks Karl Frison, John-Stuart Brittain, Daniela Massiceti, Linus Schumacher and Rui Costa for reading the previous version of the manuscript and very useful suggestions, and Chris Mathys, Peter Dayan and Diego Vidaurre for discussion.

[^1]: In the original model (Friston, 2005) the prediction errors were normalized slightly differently as explained in Appendix A.
[^2]: The original model does not provide details on the dynamics of the nodes computing prediction error, but we consider sample description of their dynamics to illustrate how these nodes can perform their computation.
[^3]: In the original model, variables $\lambda = \sqrt{\Sigma} - 1$ were defined, and these variables were encoded in the synaptic connections. Formally, this constraint is known as a hyperprior. This is because the variance or precision parameters are often referred to mathematically as hyperparameters. Whenever we place constraints on hyperparameters we necessarily invoke hyperpriors.
[^4]: Although this case has not been discussed by Friston (2005), it was discussed by Rao and Ballard (1999).
[^5]: In the model of Rao and Ballard (1999) the sparse coding was achieved through introduction of additional prior expectation that most $\phi_{i}$ are close to 0, but the sparse coding can also be achieved by choosing a shape of function $h$ such that $h\left( v_{i} \right)$ are mostly close to 0, but only occasionally significantly different from zero (Friston, 2008).

## Appendix A. The original neural implementation

In the original model (Friston, 2005), the prediction errors were defined in a slightly different way:

$$
\xi_{p} = \frac{\phi - v_{p}}{\sigma_{p}} \tag{74}
$$

$$
\xi_{u} = \frac{u - g(\phi)}{\sigma_{u}}\text{.} \tag{75}
$$

In the above equations, $\sigma_{p} = \sqrt{\Sigma_{p}}$, and $\sigma_{u} = \sqrt{\Sigma_{u}}$, i.e. $\sigma_{p}$ and $\sigma_{u}$ denote the standard deviations of distributions $p(v)$ and $p\left( u \middle| v \right)$ respectively. With the prediction error terms defined in this way, the negative free energy computed in Eq. (7) can be written as:

$$
F = - \ln\sigma_{p} - \frac{1}{2}\xi_{p}^{2} - \ln\sigma_{u} - \frac{1}{2}\xi_{u}^{2} + C_{2}\text{.} \tag{76}
$$

The dynamics of variable $\phi$ is proportional to the derivative of the above equation over $\phi$:

$$
\overset{˙}{\phi} = \frac{\xi_{u}g^{\prime}(\phi)}{\sigma_{u}} - \frac{\varepsilon_{p}}{\sigma_{p}}\text{.} \tag{77}
$$

Analogously as in Section  2.3, the prediction errors defined in Eqs. (74)–(75) could be computed in the nodes with the following dynamics:

$$
\overset{˙}{\xi_{p}} = \phi - v_{p} - \sigma_{p}\xi_{p} \tag{78}
$$

$$
\overset{˙}{\xi_{u}} = u - g(\phi) - \sigma_{u}\xi_{u}\text{.} \tag{79}
$$

The architecture of the model described by Eqs. (77), (78), (79) is shown in Fig. 10. It is similar to that in Fig. 3, but differs in the information received by node $\phi$ (we will discuss this difference in more detail at the end of this Appendix).

> **Fig. 10.** *[Figure image omitted.]*
>
> The architectures of the original model performing simple perceptual inference. Notation as in Fig. 3 .

Analogously as before, we can find the rules describing synaptic plasticity in the model, by calculating the derivatives of $F$ (Eq. (76)) over $v_{p}$, $\sigma_{p}$ and $\sigma_{u}$ (TRY IT YOURSELF):

$$
\frac{\partial F}{\partial v_{p}} = \xi_{p}\sigma_{p}^{- 1} \tag{80}
$$

$$
\frac{\partial F}{\partial\sigma_{p}} = \left( \xi_{p}^{2} - 1 \right)\sigma_{p}^{- 1} \tag{81}
$$

$$
\frac{\partial F}{\partial\sigma_{u}} = \left( \xi_{u}^{2} - 1 \right)\sigma_{u}^{- 1}\text{.} \tag{82}
$$

The original model does not satisfy the constraint of local computation stated in the Introduction, because the node computing $\phi$ receives the input from prediction error nodes scaled by parameters $\sigma$ (see Fig. 10), but the parameters $\sigma$ are not encoded in the connections between node $\phi$ and the prediction error nodes, but instead in the connections among the prediction error neurons. Nevertheless, we have shown in Section  2.3 that by just changing the way in which prediction errors are normalized the computation in the model becomes local.

## Appendix B. Derivation of plasticity rule for connections between layers

This Appendix derives the rule for update of $\mathbf{\Theta}$ given in Eq. (50). In order to use the two top formulas in Table 1 we have to reshape the matrix $\mathbf{\Theta}$ into a vector. To avoid death by notation, without loss of generality, let us consider the case of 2 dimensional stimuli and features. So let us define the vector of parameters: $\overline{\theta} = \left\lbrack \theta_{1,1},\theta_{1,2},\theta_{2,1},\theta_{2,2} \right\rbrack$. Now, using two top formulas in Table 1 one can find that:

$$
\frac{\partial F}{\partial\overline{\theta}} = \frac{{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)}^{T}}{\partial\overline{\theta}}{\overline{\varepsilon}}_{u}\text{.} \tag{83}
$$

From Eq. (42) we find:

$$
\frac{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)^{T}}{\partial\overline{\theta}} = \left\lbrack \begin{array}{llll}
{h\left( \phi_{1} \right)} & {h\left( \phi_{2} \right)} & 0 & 0 \\
0 & 0 & {h\left( \phi_{1} \right)} & {h\left( \phi_{2} \right)}
\end{array} \right\rbrack\text{.} \tag{84}
$$

We can now evaluate the right hand side of Eq. (83):

$$
\frac{{\partial g\left( \overline{\phi},\mathbf{\Theta} \right)}^{T}}{\partial\overline{\theta}}{\overline{\varepsilon}}_{u} = \left\lbrack \begin{array}{ll}
{h\left( \phi_{1} \right)} & 0 \\
{h\left( \phi_{2} \right)} & 0 \\
0 & {h\left( \phi_{1} \right)} \\
0 & {h\left( \phi_{2} \right)}
\end{array} \right\rbrack\left\lbrack \begin{array}{l}
\varepsilon_{u,1} \\
\varepsilon_{u,2}
\end{array} \right\rbrack = \left\lbrack \begin{array}{l}
{h\left( \phi_{1} \right)\varepsilon_{u,1}} \\
{h\left( \phi_{2} \right)\varepsilon_{u,1}} \\
{h\left( \phi_{1} \right)\varepsilon_{u,2}} \\
{h\left( \phi_{2} \right)\varepsilon_{u,2}}
\end{array} \right\rbrack\text{.} \tag{85}
$$

Reshaping the right hand side of the above equation into a matrix, we can see how it can be decomposed into the product of vectors in Eq. (50):

$$
\left\lbrack \begin{array}{ll}
{h\left( \phi_{1} \right)\varepsilon_{u,1}} & {h\left( \phi_{2} \right)\varepsilon_{u,1}} \\
{h\left( \phi_{1} \right)\varepsilon_{u,2}} & {h\left( \phi_{2} \right)\varepsilon_{u,2}}
\end{array} \right\rbrack = \left\lbrack \begin{array}{l}
\varepsilon_{u,1} \\
\varepsilon_{u,2}
\end{array} \right\rbrack\left\lbrack \begin{array}{ll}
{h\left( \phi_{1} \right)} & {h\left( \phi_{2} \right)}
\end{array} \right\rbrack\text{.} \tag{86}
$$

## Solutions to exercises

### Exercise 1

```matlab
function exercise1
v_p = 3;       % mean of prior distribution of food size
sigma_p = 1;   % standard deviation of prior = sqrt(1)
sigma_u = 1;   % standard deviation of sensory noise = sqrt(1)

u = 2;         % observed light intensity

MINV = 0.01;   % minimum value of v for which posterior computed
DV = 0.01;     % interval between values of v for which posterior found
MAXV = 5;      % maximum value of v for which posterior computed
vrange = [MINV:DV:MAXV];
numerator = normpdf(vrange, v_p, sigma_p) .* ...
    normpdf(u, vrange.^2, sigma_u);
normalization = sum(numerator * DV);
p = numerator / normalization;
plot(vrange, p, 'k');
xlabel('v');
ylabel('p(v|u)');
```

### Exercise 2

```matlab
function exercise2
v_p = 3;       % mean of prior distribution of food size
Sigma_p = 1;   % variance of prior distribution
Sigma_u = 1;   % variance of sensory noise

u = 2;         % observed light intensity

DT = 0.01;     % integration step
MAXT = 5;      % maximum time considered

phi(1) = v_p;  % initializing the best guess of food size

for i = 2:MAXT/DT
    phi(i) = phi(i-1) + DT * ((v_p - phi(i-1))/Sigma_p + ...
        (u - phi(i-1)^2)/Sigma_u * (2*phi(i-1)));
end
plot([DT:DT:MAXT], phi, 'k');
xlabel('Time');
ylabel('\phi');
axis([0 MAXT -2 3.5]);
```

### Exercise 3

```matlab
function exercise3
v_p = 3;       % mean of prior distribution of food size
Sigma_p = 1;   % variance of prior distribution
Sigma_u = 1;   % variance of sensory noise

u = 2;         % observed light intensity

DT = 0.01;     % integration step
MAXT = 5;      % maximum time considered

phi(1) = v_p;       % initializing the best guess of food size
error_p(1) = 0;     % initializing the prediction error of food size
error_u(1) = 0;     % initializing the prediction error of sensory input

for i = 2:MAXT/DT
    phi(i) = phi(i-1) + DT * (-error_p(i-1) + ...
        error_u(i-1) * (2*phi(i-1)));
    error_p(i) = error_p(i-1) + DT * ...
        (phi(i-1) - v_p - Sigma_p*error_p(i-1));
    error_u(i) = error_u(i-1) + DT * ...
        (u - phi(i-1)^2 - Sigma_u*error_u(i-1));
end
plot([DT:DT:MAXT], phi, 'k');
hold on
plot([DT:DT:MAXT], error_p, 'k--');
plot([DT:DT:MAXT], error_u, 'k:');
xlabel('Time');
ylabel('Activity');
legend('\phi', '\epsilon_p', '\epsilon_u');
axis([0 MAXT -2 3.5]);
```

### Exercise 4

It is easiest to consider a vector of two numbers (analogous can be shown for longer vectors):

$$
\overline{x} = \left\lbrack \begin{array}{l}
x_{1} \\
x_{2}
\end{array} \right\rbrack\text{.} \tag{87}
$$

Then $y = {\overline{x}}^{T}\overline{x} = x_{1}^{2} + x_{2}^{2}$, so the gradient is equal to:

$$
\frac{\partial y}{\partial\overline{x}} = \left\lbrack \begin{array}{l}
\frac{\partial y}{\partial x_{1}} \\
\frac{\partial y}{\partial x_{2}}
\end{array} \right\rbrack = \left\lbrack \begin{array}{l}
{2x_{1}} \\
{2x_{2}}
\end{array} \right\rbrack = 2\overline{x}\text{.} \tag{88}
$$

### Exercise 5

```matlab
function exercise5
mean_phi = 5;    % mean of input from the current level
Sigma_phi = 2;   % variance of input from the current level
phi_above = 5;   % input from the level above

DT = 0.01;       % integration step
MAXT = 20;       % maximum time considered
TRIALS = 1000;   % number of simulated trials
LRATE = 0.01;    % learning rate

Sigma(1) = 1;    % initializing the value of weight

for trial = 2:TRIALS
    error(1) = 0;  % initializing the prediction error
    e(1) = 0;      % initializing the interneuron
    phi = mean_phi + sqrt(Sigma_phi) * randn;
    for i = 2:MAXT/DT
        error(i) = error(i-1) + DT * (phi - phi_above - e(i-1));
        e(i) = e(i-1) + DT * (Sigma(trial-1)*error(i-1) - e(i-1));
    end
    Sigma(trial) = Sigma(trial-1) + ...
        LRATE * (error(end)*e(end) - 1);
end
plot(Sigma, 'k');
xlabel('Trial');
ylabel('\Sigma');
```

## References

1.  Bastos Andre M., Usrey W. Martin, Adams Rick A., Mangun George R., Fries Pascal, Friston Karl J. Canonical microcircuits for predictive coding. Neuron. 2012;76:695–711. doi: 10.1016/j.neuron.2012.10.038. \[[DOI](https://doi.org/10.1016/j.neuron.2012.10.038)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/23177956/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neuron&title=Canonical%20microcircuits%20for%20predictive%20coding&author=Andre%20M.%20Bastos&author=W.%20Martin%20Usrey&author=Rick%20A.%20Adams&author=George%20R.%20Mangun&author=Pascal%20Fries&volume=76&publication_year=2012&pages=695-711&pmid=23177956&doi=10.1016/j.neuron.2012.10.038&)\]
2.  Bell Anthony J., Sejnowski Terrence J. An information-maximization approach to blind separation and blind deconvolution. Neural Computation. 1995;7:1129–1159. doi: 10.1162/neco.1995.7.6.1129. \[[DOI](https://doi.org/10.1162/neco.1995.7.6.1129)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/7584893/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neural%20Computation&title=An%20information-maximization%20approach%20to%20blind%20separation%20and%20blind%20deconvolution&author=Anthony%20J.%20Bell&author=Terrence%20J.%20Sejnowski&volume=7&publication_year=1995&pages=1129-1159&pmid=7584893&doi=10.1162/neco.1995.7.6.1129&)\]
3.  Bell Anthony J., Sejnowski Terrence J. The independent components of natural scenes are edge filters. Vision Research. 1997;37:3327–3338. doi: 10.1016/s0042-6989(97)00121-1. \[[DOI](https://doi.org/10.1016/s0042-6989(97)00121-1)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/9425547/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Vision%20Research&title=The%20independent%20components%20of%20natural%20scenes%20are%20edge%20filters&author=Anthony%20J.%20Bell&author=Terrence%20J.%20Sejnowski&volume=37&publication_year=1997&pages=3327-3338&pmid=9425547&doi=10.1016/s0042-6989(97)00121-1&)\]
4.  Bogacz Rafal, Brown Malcolm W., Giraud-Carrier Christophe. Emergence of movement sensitive neurons’ properties by learning a sparse code for natural moving images. Advances in Neural Information Processing Systems. 2001;13:838–844. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Advances%20in%20Neural%20Information%20Processing%20Systems&title=Emergence%20of%20movement%20sensitive%20neurons%E2%80%99%20properties%20by%20learning%20a%20sparse%20code%20for%20natural%20moving%20images&author=Rafal%20Bogacz&author=Malcolm%20W.%20Brown&author=Christophe%20Giraud-Carrier&volume=13&publication_year=2001&pages=838-844&)\]
5.  Bogacz Rafal, Gurney Kevin. The basal ganglia and cortex implement optimal decision making between alternative actions. Neural Computation. 2007;19:442–477. doi: 10.1162/neco.2007.19.2.442. \[[DOI](https://doi.org/10.1162/neco.2007.19.2.442)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/17206871/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neural%20Computation&title=The%20basal%20ganglia%20and%20cortex%20implement%20optimal%20decision%20making%20between%20alternative%20actions&author=Rafal%20Bogacz&author=Kevin%20Gurney&volume=19&publication_year=2007&pages=442-477&pmid=17206871&doi=10.1162/neco.2007.19.2.442&)\]
6.  Chen J.-Y., Lonjers P., Lee C., Chistiakova M., Volgushev M., Bazhenov M. Heterosynaptic plasticity prevents runaway synaptic dynamics. Journal of Neuroscience. 2013;33:15915–15929. doi: 10.1523/JNEUROSCI.5088-12.2013. \[[DOI](https://doi.org/10.1523/JNEUROSCI.5088-12.2013)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/24089497/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Neuroscience&title=Heterosynaptic%20plasticity%20prevents%20runaway%20synaptic%20dynamics&author=J.-Y.%20Chen&author=P.%20Lonjers&author=C.%20Lee&author=M.%20Chistiakova&author=M.%20Volgushev&volume=33&publication_year=2013&pages=15915-15929&pmid=24089497&doi=10.1523/JNEUROSCI.5088-12.2013&)\]
7.  Feldman Harriet, Friston Karl. Attention, uncertainty, and free-energy. Frontiers in Human Neuroscience. 2010;4:215. doi: 10.3389/fnhum.2010.00215. \[[DOI](https://doi.org/10.3389/fnhum.2010.00215)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/21160551/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Frontiers%20in%20Human%20Neuroscience&title=Attention,%20uncertainty,%20and%20free-energy&author=Harriet%20Feldman&author=Karl%20Friston&volume=4&publication_year=2010&pages=215&pmid=21160551&doi=10.3389/fnhum.2010.00215&)\]
8.  FitzGerald Thomas H.B., Schwartenbeck Philipp, Moutoussis Michael, Dolan Raymond J., Friston Karl. Active inference, evidence accumulation and the urn task. Neural Computation. 2015;27:306–328. doi: 10.1162/NECO_a_00699. \[[DOI](https://doi.org/10.1162/NECO_a_00699)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/25514108/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neural%20Computation&title=Active%20inference,%20evidence%20accumulation%20and%20the%20urn%20task&author=Thomas%20H.B.%20FitzGerald&author=Philipp%20Schwartenbeck&author=Michael%20Moutoussis&author=Raymond%20J.%20Dolan&author=Karl%20Friston&volume=27&publication_year=2015&pages=306-328&pmid=25514108&doi=10.1162/NECO_a_00699&)\]
9.  Friston Karl. Learning and inference in the brain. Neural Networks. 2003;16:1325–1352. doi: 10.1016/j.neunet.2003.06.005. \[[DOI](https://doi.org/10.1016/j.neunet.2003.06.005)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/14622888/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Neural%20Networks&title=Learning%20and%20inference%20in%20the%20brain&author=Karl%20Friston&volume=16&publication_year=2003&pages=1325-1352&pmid=14622888&doi=10.1016/j.neunet.2003.06.005&)\]
10. Friston Karl. A theory of cortical responses. Philosophical Transactions of the Royal Society B. 2005;360:815–836. doi: 10.1098/rstb.2005.1622. \[[DOI](https://doi.org/10.1098/rstb.2005.1622)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/15937014/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Philosophical%20Transactions%20of%20the%20Royal%20Society%20B&title=A%20theory%20of%20cortical%20responses&author=Karl%20Friston&volume=360&publication_year=2005&pages=815-836&pmid=15937014&doi=10.1098/rstb.2005.1622&)\]
11. Friston Karl. Hierarchical models in the brain. PLoS Computational Biology. 2008;4:e1000211. doi: 10.1371/journal.pcbi.1000211. \[[DOI](https://doi.org/10.1371/journal.pcbi.1000211)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/18989391/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20Computational%20Biology&title=Hierarchical%20models%20in%20the%20brain&author=Karl%20Friston&volume=4&publication_year=2008&pages=e1000211&pmid=18989391&doi=10.1371/journal.pcbi.1000211&)\]
12. Friston Karl. The free-energy principle: a unified brain theory? Nature Reviews Neuroscience. 2010;11:127–138. doi: 10.1038/nrn2787. \[[DOI](https://doi.org/10.1038/nrn2787)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/20068583/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20Reviews%20Neuroscience&title=The%20free-energy%20principle:%20a%20unified%20brain%20theory?&author=Karl%20Friston&volume=11&publication_year=2010&pages=127-138&pmid=20068583&doi=10.1038/nrn2787&)\]
13. Friston Karl, Schwartenbeck Philipp, FitzGerald Thomas, Moutoussis Michael, Behrens Timothy, Dolan Raymond J. The anatomy of choice: active inference and agency. Frontiers in Human Neuroscience. 2013;7:598. doi: 10.3389/fnhum.2013.00598. \[[DOI](https://doi.org/10.3389/fnhum.2013.00598)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/24093015/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Frontiers%20in%20Human%20Neuroscience&title=The%20anatomy%20of%20choice:%20active%20inference%20and%20agency&author=Karl%20Friston&author=Philipp%20Schwartenbeck&author=Thomas%20FitzGerald&author=Michael%20Moutoussis&author=Timothy%20Behrens&volume=7&publication_year=2013&pages=598&pmid=24093015&doi=10.3389/fnhum.2013.00598&)\]
14. Harwood David, Ojala Timo, Pietikäinen Matti, Kelman Shalom, Davis Larry. Texture classification by center-symmetric auto-correlation, using Kullback discrimination of distributions. Pattern Recognition Letters. 1995;16:1–10. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Pattern%20Recognition%20Letters&title=Texture%20classification%20by%20center-symmetric%20auto-correlation,%20using%20Kullback%20discrimination%20of%20distributions&author=David%20Harwood&author=Timo%20Ojala&author=Matti%20Pietik%C3%A4inen&author=Shalom%20Kelman&author=Larry%20Davis&volume=16&publication_year=1995&pages=1-10&)\]
15. Olshausen Bruno A., Field David J. Emergence of simple-cell receptive field properties by learning a sparse code for natural images. Nature. 1995;381:607–609. doi: 10.1038/381607a0. \[[DOI](https://doi.org/10.1038/381607a0)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/8637596/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature&title=Emergence%20of%20simple-cell%20receptive%20field%20properties%20by%20learning%20a%20sparse%20code%20for%20natural%20images&author=Bruno%20A.%20Olshausen&author=David%20J.%20Field&volume=381&publication_year=1995&pages=607-609&pmid=8637596&doi=10.1038/381607a0&)\]
16. O’Reilly Randall C., Munakata Yuko. MIT Press; 2000. Computational explorations in cognitive neuroscience. \[[Google Scholar](https://scholar.google.com/scholar_lookup?O%E2%80%99Reilly%20Randall%20C.,%20Munakata%20Yuko.%20MIT%20Press;%202000.%20Computational%20explorations%20in%20cognitive%20neuroscience.)\]
17. Ostwald Dirk, Kirilina Evgeniya, Starke Ludger, Blankenburg Felix. A tutorial on variational Bayes for latent linear stochastic time-series models. Journal of Mathematical Psychology. 2014;60:1–19. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Mathematical%20Psychology&title=A%20tutorial%20on%20variational%20Bayes%20for%20latent%20linear%20stochastic%20time-series%20models&author=Dirk%20Ostwald&author=Evgeniya%20Kirilina&author=Ludger%20Starke&author=Felix%20Blankenburg&volume=60&publication_year=2014&pages=1-19&)\]
18. Rao Rajesh P.N., Ballard Dana H. Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. Nature Neuroscience. 1999;2:79–87. doi: 10.1038/4580. \[[DOI](https://doi.org/10.1038/4580)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/10195184/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20Neuroscience&title=Predictive%20coding%20in%20the%20visual%20cortex:%20a%20functional%20interpretation%20of%20some%20extra-classical%20receptive-field%20effects&author=Rajesh%20P.N.%20Rao&author=Dana%20H.%20Ballard&volume=2&publication_year=1999&pages=79-87&pmid=10195184&doi=10.1038/4580&)\]
19. Strogatz Steven. Westview Press; 1994. Nonlinear dynamics and chaos. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Strogatz%20Steven.%20Westview%20Press;%201994.%20Nonlinear%20dynamics%20and%20chaos.)\]
