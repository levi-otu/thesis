

## Sets 

A 1l of mathematics can be described with sets. This becomes more and.more apparent the deeper into mathematics you go. It will be apparent.in most of your upper level courses, and certainly in this course. The theory of sets is a language that is perfectly suited to describing and explaining all types of mathematical structures.



### 1.1 Introduction to Sets 

A set is a collection of things. The things are called elements of the set. We are mainly concerned with sets whose elements are mathematical entities,such as numbers, points, functions, etc.



A set is often expressed by listing its elements between commas, enclosed.by braces. For example, the collection {2,4,6,8} is a set which has four elements, the numbers 2, 4,6 and 8. Some sets have infinitely many elements.For example, consider the collection of all integers,.



$$\{\ldots,-4,-3,-2,-1,0,1,2,3,4,\ldots\}.$$

Here the dots indicate a pattern of numbers that continues forever in both the positive and negative directions. A set is called an infinite set if it has infinitely many elements; otherwise it is called a finite set..

Two sets are equal if they contain exactly the same elements. Thus.$\{2,4,6,8\}=\{4,2,8,6\}$  because even though they are listed in a different order,.the elements are identical; but $\left\{2,4,6,8\right\}\neq\left\{2,4,6,7\right\}$ :. Also 

$$\{\ldots-4,-3,-2,-1,0,1,2,3,4\ldots\}=\{0,-1,1,-2,2,-3,3,-4,4,\ldots\}.$$

We often let uppercase letters stand for sets. In discussing the set.{2,4,6,8} we might declare $A=\{2,4,6,8\}$ . and then use A to stand for {2, 4, 6, 8}.To express that 2 is an element of the set A, we write.$2\in A$ , and read this as "2 is an element of A," or "2 is in A," or just "2 in A." We also have 4 e A, 6 e A and $8\in A$ , but ${\bf5}\notin A$ ..We read this last expression as "5 is not an element of.A," or "5 not in A." Expressions like 6,$2\in A$ . or 2,4,8 e A are used to indicate that several things are in a set.



Some sets are so significant that we reserve special symbols for them.The set of natural numbers (i.e., the positive whole numbers) is denoted by N, that is,

$$\mathbb{N}=\{1,2,3,4,5,6,7,\ldots\}.$$

The set of integers 

$$\mathbb{Z}=\left\{\dots,-3,-2,-1,0,1,2,3,4,\dots\right\}$$

is another fundamental set. The symbol R stands for the set of all real numbers, a set that is undoubtedly familiar to you from calculus. Other special sets will be listed later in this section.



Sets need not have just numbers as elements. The set $B=\left\{\boldsymbol{T},\boldsymbol{F}\right\}$ : consists of two letters, perhaps representing the values "true" and "false." The set $C=\left\{a,e,i,o,u\right\}$ : consists of the lowercase vowels in the English alphabet.The set $D=\left\{(0,0),(1,0),(0,1),(1,1)\right\}$ . has as elements the four corner points of a square on the x-y coordinate plane. Thus $(0,0)\in D,\;(1,0)\in D$ , etc.,but (1,2)  D (for instance). It is even possible for a set to have other sets as elements. Consider $E=\{1,\{2,3\},\{2,4\}\}$ :, which has three elements: the number 1, the set {2,3} and the set {2,4}. Thus 1e E and $\{2,3\}\in E$  and $\{2,4\}\in E$ . But note that 2 E, 3E and 4  E.



Consider the set $M=\left\{\left[00\right],\left[10\right],\left[10\right]\right\}$  of three two-by-two matrices. We have $\left[{0\atop00}\right]\in M$ , but [1]  M. Letters can serve as symbols denoting a set's elements: If $a=\left[00\atop00\right],b=\left[10\atop01\right]$ and $c=\left[{1\atop1}{0\atop1}\right]$ , then $M=\left\{a,b,c\right\}$ 

If X is a finite set, its cardinality or size is the number of elements it has, and this number is denoted as |X|. Thus for the sets above,$|A|=4$ ',|B|=2,|C|=5,|D|=4,|E|=3 and |M|=3.



There is a special set that, although small, plays a big role. The empty set is the set {} that has no elements. We denote it as , so $\varnothing=\left\{\begin{array}{l l}{\end{array}\right\}$ . Whenever you see the symbol , it stands for {}. Observe that $|\emptyset|=0$ I. The empty set is the only set whose cardinality is zero.



Be careful in writing the empty set. Don't write {} when you mean .These sets can't be equal because  contains nothing while $\{\phi\}$ . contains one thing, namely the empty set. If this is confusing, think of a set as a box with things in it, so, for example, {2, 4, 6,8} is a "box" containing four numbers. The empty set $\varnothing=\left\{{\begin{array}{r l}\end{array}}\right.$ is an empty box. By contrast, {} is a box with an empty box inside it. Obviously, there's a difference: An empty box is not the same as a box with an empty box inside it. Thus $\varnothing\neq\left\{\varnothing\right\}$ :.(You might also note ||=0 and $\left|\left\{\varnothing\right\}\right|=1$ . as additional evidence that $\varnothing\neq\left\{\varnothing\right\}$ .)

This box analogy can help us think about sets. The set.$\boldsymbol{F}=\left\{\boldsymbol{\emptyset},\left\{\boldsymbol{\emptyset}\right\},\left\{\boldsymbol{\emptyset}\right\}\right\}$ may look strange but it is really very simple. Think of it as a box containing three things: an empty box, a box containing an empty box, and a box containing a box containing an empty box. Thus.$|{\pmb F}|=3$ . The set $G=\left\{\mathbb{N},\mathbb{Z}\right\}$ is a box containing two boxes, the box of natural numbers and the box of integers. Thus.$|G|=2$ 



A special notation called set-builder notation is used to describe sets that are too big or complex to list between braces. Consider the infinite set of even integers $E=\left\{\ldots,-6,-4,-2,0,2,4,6,\ldots\right\}$ :. In set-builder notation this.set is written as 



$$E=\{2n:n\in\mathbb{Z}\}.$$

We read the first brace as "the set of all things of form," and the colon as "such that." So the expression $E=\left\{2n:n\in\mathbb{Z}\right\}$ reads as "E equals the set of all things of form 2n, such that n is an element.$o f\mathbb{Z}.$ The idea is that E.consists of all possible values of 2n, where n takes on all values in Z.

In general, a set X written with set-builder notation has the syntax.

$$X=\{\mathrm{e x p r e s s i o n:r u l e}\},$$

where the elements of X are understood to be all values of "expression" that are specified by "rule."' For example, above E is the set of all values of the expression 2n that satisfy the rule n e Z. There can be many ways to express the same set. For example,$E=\left\{2n:n\in\mathbb{Z}\right\}=\left\{n:n\right.$  is an even integer} =$\left\{n:n=2k,k\in\mathbb{Z}\right\}$ . Another common way of writing it is.

$$E=\{n\in\mathbb{Z}:n is even\},$$

read "E is the set of all n in  such that n is even." Some writers use a bar instead of a colon; for example,.$E=\{n\in\mathbb{Z}\mid n$ is even}. We use the colon.

Items 6-8 above highlight a conflict of notation that we must always be alert to. The expression X| means absolute value if X is a number and cardinality if X is a set. The distinction should always be clear from.context. Consider $\left\{x\in\mathbb{Z}:|x|<4\right\}$ : in Example 1.1 (6) above. Here $x\in\mathbb{Z}$ , so x is a number (not a set), and thus the bars in |x| must mean absolute value,.not cardinality. On the other hand, suppose.$A=\left\{\{1,2\},\{3,4,5,6\},\{7\}\right\}$ : and $B=\left\{X\in A:|X|<3\right\}$ :. The elements of A are sets (not numbers), so the |X| in.the expression for B must mean cardinality. Therefore.$B=\left\{\{1,2\},\{7\}\right\}$ 

$$A=\left\{7a+3b:a,b\in\mathbb{Z}\right\}$$

Solution: This set contains all numbers of form.$7a+3b$ ,where a and b are integers. Each such number.$7a+3b$  is an integer, so A contains only.integers. But which integers? If n is any integer, then.$n=7n+3(-2n)$ I, so $n=7a+3b$  where $a=n$ and $b=-2n$ .. Therefore $n\in A$ .. We've now shown that A contains only integers, and also that every integer is an element of A..Consequently $A=\mathbb{Z}$ 



We close this section with a summary of special sets. These are sets.that are so common that they are given special names and symbols.

The empty set:$\varnothing=\left\{\begin{array}{l l}{\end{array}\right\}$ 

The natural numbers:$\mathbb{N}=\{1,2,3,4,5,\ldots\}$ 

The integers:$\mathbb{Z}=\left\{\ldots,-3,-2,-1,0,1,2,3,4,5,\ldots\right\}$ 

The rational numbers:$\mathbb{Q}=\left\{x:x={\frac{m}{n}}\right.$ , where m,n e Z and n = 0}

The real numbers: R 

We visualize the set R of real numbers as an infinitely long number line.


<div style="text-align: center;"><html><body><table border="1"><tr><td>1+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 </td><td></td><td></td><td></td><td>-4-3-2-10123</td><td></td><td></td><td></td><td></td></tr></table></body></html></div>


Notice that Q is the set of all numbers in R that can be expressed as a fraction of two integers. You may be aware that $\mathbb{Q}\neq\mathbb{R}$ , as ${\sqrt{2}}\notin\mathbb{Q}$ . but ${\sqrt{2}}\in\mathbb{R}$ (If not, this point will be addressed in Chapter 6.).



In calculus you encountered intervals on the number line. Like R, these too are infinite sets of numbers. Any two numbers a,b e R with.$a<b$ give rise to various intervals. Graphically, they are represented by a darkened.segment on the number line between a and b. A solid circle at an endpoint.indicates that that number is included in the interval. A hollow circle indicates a point that is not included in the interval..

$$\left[a,b\right]=\left\{x\in\mathbb{R}:a\leq x\leq b\right\}$$

Open interval:$(a,b)=\left\{x\in\mathbb{R}:a<x<b\right\}$ 

$$\left(a,b\right]=\left\{x\in\mathbb{R}:a<x\leq b\right\}$$

Half-open interval:$\left[a,b\right)=\left\{x\in\mathbb{R}:a\leq x<b\right\}$ 

Infinite interval:$\left(a,\infty\right)=\left\{x\in\mathbb{R}:a<x\right\}$ 

Infinite interval:$\left[a,\infty\right)=\left\{x\in\mathbb{R}:a\leq x\right\}$ 

Infinite interval:$\left(-\infty,b\right)=\left\{x\in\mathbb{R}:x<b\right\}$ 

Infinite interval:$\left(-\infty,b\right]=\left\{x\in\mathbb{R}:x\leq b\right\}$ 

Each of these intervals is an infinite set containing infinitely many.numbers as elements. For example, though its length is short, the interval.(0.1,0.2) contains infinitely many numbers, that is, all numbers between.0.1 and 0.2. It is an unfortunate notational accident that (a,b) can denote.both an open interval on the line and a point on the plane. The difference is usually clear from context. In the next section we will see yet another.meaning of (a, b).



### Exercises for Section 1.1

A. Write each of the following sets by listing their elements between braces..

$$\left\{5x-1:x\in\mathbb{Z}\right\}$$

$$\left\{x\in\mathbb{R}:\sin\pi x=0\right\}$$

$$\left\{3x+2:x\in\mathbb{Z}\right\}$$

$$\left\{x\in\mathbb{R}:\cos x=1\right\}$$

$$\left\{x\in\mathbb{Z}:-2\leq x<7\right\}$$

$$\left\{x\in\mathbb{Z}:|x|<5\right\}$$

$$\left\{x\in\mathbb{N}:-2<x\leq7\right\}$$

$$\left\{x\in\mathbb{Z}:|2x|<5\right\}$$

$$\left\{x\in\mathbb{R}:x^{2}=3\right\}$$

$$\left\{x\in\mathbb{Z}:|6x|<5\right\}$$

$$\left\{x\in\mathbb{R}:x^{2}=9\right\}$$

$$\left\{5x:x\in\mathbb{Z},|2x|\leq8\right\}$$

$$\left\{x\in\mathbb{R}:x^{2}+5x=-6\right\}$$

$$\left\{5a+2b:a,b\in\mathbb{Z}\right\}$$

$$\left\{x\in\mathbb{R}:x^{3}+5x^{2}=-6x\right\}$$

B. Write each of the following sets in set-builder notation..

$$\left\{\ldots,-8,-3,2,7,12,17,\ldots\right\}$$

C. Find the following cardinalities.

29. |{1},{2,{3,4},}34.I{x EN:IxI<10}|

30.|{1,4},a,b,{{3,4},{}|35.j{x E Z:x2<10}|

31. |{{{1},{2,{3,4},}36.J{x EN:x2<10}]

32.|{{{1,4},a,b,{3,4},{}|37.J{x EN:x2<0}]

33.I{x E Z:|x]<10}|38.J{x E N: 5x  20}]

D. Sketch the following sets of points in the x-y plane..

39.{(x,y):x E[1,2],y E[1,2]}46.{(x,y):x,y ER,x2+y21}
40.{x,y):x E[0,1],y E[1,2]}47.{x,y):x,yER,yx2-1}
41.{(x,y):xE[-1,1],y=1}48.{(x,y):x,yER,x>1}
42.{(x,y):x=2,y E[0,1]}49.{(x,x+y):xER,y EZ}
43.{(x,y):|x|=2,y E[0,1]}50.{x,t2y ):xE R, y E N}
44.{(x,x2):xER}51.{(x,y)ER2:(y-x)y+x)=0}
45.{x,y):x,yER,x2+y2=1}52.{(x,y)ER2 :(y-x2)(y+x2)=0}

### 1.2 The Cartesian Product 

Given two sets A and B, it is possible to "multiply" them to produce a new set denoted as $A\times B$ . This operation is called the Cartesian product. To.understand it, we must first understand the idea of an ordered pair..

Definition 1.1 An ordered pair is a list (x,y) of two things x and y,enclosed in parentheses and separated by a comma..

For example, (2,4) is an ordered pair, as is (4,2). These ordered pairs are. different because even though they have the same things in them, the order is different. We write (2,4) (4,2). Right away you can see that ordered pairs can be used to describe points on the plane, as was done in calculus, but they are not limited to just that. The things in an ordered pair don't have to be numbers. You can have ordered pairs of letters, such as (l,m), ordered pairs of sets such as ({2,5},{3,2}), even ordered pairs of ordered pairs like ((2,4),(4,2)). The following are also ordered pairs: (2,{1,2,3}), (R, (0,0)). Any list of two things enclosed by parentheses is an ordered pair. Now we are ready to define the Cartesian product..



Definition 1.2 The Cartesian product of two sets A and B is another set, denoted as A  B and defined as.$A\times B=\left\{(a,b):a\in A,b\in B\right\}$ 

Thus $A\times B$ is a set of ordered pairs of elements from A and B. For example, if $A=\left\{k,\ell,m\right\}$ : and $B=\left\{q,r\right\}$ ., then 

$$A\times B=\left\{(k,q),(k,r),(\ell,q),(\ell,r),(m,q),(m,r)\right\}.$$

Figure 1.1 shows how to make a schematic diagram of $A\times B$ . Line up the.elements of A horizontally and line up the elements of B vertically, as if A and B form an x- and y-axis. Then fill in the ordered pairs so that each element (x,y) is in the column headed by x and the row headed by y.

<div style="text-align: center;"><img src="imgs/img_in_image_box_357_440_696_579.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">Figure 1.1. A diagram of a Cartesian product </div>


For another example,.$\left\{0,1\right\}\times\left\{2,1\right\}=\left\{(0,2),(0,1),(1,2),(1,1)\right\}$ . If you are a visual thinker, you may wish to draw a diagram similar to Figure 1.1. The rectangular array of such diagrams give us the following general fact.

Fact 1.1If A and B are finite sets, then $\left|\boldsymbol{A}\times\boldsymbol{B}\right|=\left|\boldsymbol{A}\right|\cdot\left|\boldsymbol{B}\right|$ 

Example 1.3Let $A=\{\square,\square,\square,\square,\square,\square,\square\}$ . be the set consisting of the six faces of a dice. The Cartesian product A  A is diagramed below. By Fact 1.1 (or by simple counting),.$|A\times A|=6\cdot6=36$ .We might think of.$A\times A$ as the set of possible outcomes in rolling a dice two times in a row. Each element of the product is an ordered pair of form (result of 1st roll, result of 2nd roll).Such constructions are useful in the study of probability.

<div style="text-align: center;"><img src="imgs/img_in_image_box_253_1024_800_1293.jpg" alt="Image" width="54%" /></div>


The set $\mathbb{R}\times\mathbb{R}=\{(x,y):x,y\in\mathbb{R}\}$ . should be very familiar. It can be viewed.as the set of points on the Cartesian plane, as drawn in Figure 1.2(a). The set $\mathbb{R}\times\mathbb{N}=\left\{\left(x,y\right):x\in\mathbb{R},y\in\mathbb{N}\right\}$ can be regarded as all of the points on the.plane whose second coordinate is a natural number. This is illustrated in Figure 1.2(b), which shows that R  N looks like infinitely many horizontal lines at integer heights above the x-axis. The set.$\mathbb{N}\times\mathbb{N}$ is the set of all points.on the plane whose coordinates are both natural numbers. It looks like a grid of dots in the first quadrant, as illustrated in Figure 1.2(c)..

<div style="text-align: center;"><img src="imgs/img_in_image_box_377_422_577_581.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">Figure 1.2. Drawings of some Cartesian products.</div>


It is even possible for one factor of a Cartesian product to be a Cartesian product itself, as in.$\mathbb{R}\times(\mathbb{N}\times\mathbb{Z})=\{(x,(y,z)):x\in\mathbb{R},(y,z)\in\mathbb{N}\times\mathbb{Z}\}$ 

We can also define Cartesian products of three or more sets by moving.beyond ordered pairs. An ordered triple is a list.$(x,y,z)$ . The Cartesian product of the three sets R, N and.$\mathbb{Z}\mathrm{is}\mathbb{R}\times\mathbb{N}\times\mathbb{Z}=\left\{(x,y,z):x\in\mathbb{R},y\in\mathbb{N},z\in\mathbb{Z}\right\}$ Of course there is no reason to stop with ordered triples. In general,.

$$A_{1}\times A_{2}\times\cdots\times A_{n}=\left\{(x_{1},x_{2},\ldots,x_{n}):x_{i}\in A_{i}for each i=1,2,\ldots,n\right\}.$$

Be mindful of parentheses. There is a slight difference between.$\mathbb{R}\times(\mathbb{N}\times\mathbb{Z})$ and $\mathbb{R}\times\mathbb{N}\times\mathbb{Z}$ . The first is a Cartesian product of two sets; its elements are.ordered pairs $(x,(y,z))$ . The second is a Cartesian product of three sets; its.elements are ordered triples.$(x,y,z)$ . To be sure, in many situations there is no harm in blurring the distinction between expressions like.$(x,(y,z))$ I and $(x,y,z)$ , but for now we regard them as different..



For any set A and positive integer n, the Cartesian power $A^{n}$  is 

$$A^{n}=A\times A\times\cdots\times A=\left\{\left(x_{1},x_{2},\ldots,x_{n}\right):x_{1},x_{2},\ldots,x_{n}\in A\right\}.$$

In this way,$\mathbb{R}^{2}$  is the familiar Cartesian plane and $\mathbb{R}^{3}$  is three-dimensional space. You can visualize how,.$\mathrm{i f}\mathbb{R}^{2}$ is the plane, then.$\mathbb{Z}^{2}=\left\{(m,n):m,n\in\mathbb{Z}\right\}$ is a grid of points on the plane. Likewise, as $\mathbb{R}^{3}$  is 3-dimensional space,$\mathbb{Z}^{3}=\left\{(m,n,p):m,n,p\in\mathbb{Z}\right\}$  is a grid of points in space..

In other courses you may encounter sets that are very similar to Rn, but.yet have slightly different shades of meaning. Consider, for example, the.set of all two-by-three matrices with entries from R:

$$M=\left\{\left[{u v w\atop x y z}\right]:u,v,w,x,y,z\in\mathbb{R}\right\}.$$

This is not really all that different from the set 

$$\mathbb{R}^{6}=\left\{(u,v,w,x,y,z):u,v,w,x,y,z\in\mathbb{R}\right\}.$$

The elements of these sets are merely certain arrangements of six real.numbers. Despite their similarity, we maintain that.$M\neq\mathbb{R}^{6}$ , for two-bythree matrices are not the same things as sequences of six numbers..

Example 1.4Represent the two sides of a coin by the set.$\mathbf{\boldsymbol{S}}=\left\{\scriptstyle\mathrm{H},\scriptstyle\mathrm{T}\right\}$ . The possible outcomes of tossing the coin seven times in a row can be described.with the Cartesian power $S^{7}$ . A typical element of $S^{7}$  looks like 

$$(\scriptstyle{\mathrm{H}},\scriptstyle{\mathrm{H}},\scriptstyle{\mathrm{T}},\scriptstyle{\mathrm{H}},\scriptstyle{\mathrm{T}},\scriptstyle{\mathrm{T}},\scriptstyle{\mathrm{T}}),$$

meaning a head was tossed first, then another head, then a tail, then a head.followed by three tails. Note that.$\left|S^{7}\right|=2^{7}=128$ , so there are 128 possible outcomes. If this is not clear, then it will be explained fully in Chapter 3.

### Exercises for Section 1.2

$$A=\{1,2,3,4\} : and $$

$$B=\{a,c\}$$

$$A\times(B\times B)$$

$$A\times(B\times B)$$

$$\left\{x\in\mathbb{R}:x^{2}=x\right\}\times\left\{x\in\mathbb{N}:x^{2}=x\right\}$$

$$\left\{(x,y)\in\mathbb{R}^{2}:x^{2}+y^{2}\leq1\right\}\times[0,1]$$

### 1.3 Subsets 

It can happen that every element of a set A is an element of another set B.For example, each element of $A=\{0,2,4\}$ : is also an element of $B=\{0,1,2,3,4\}$ '.When A and B are related this way we say that A is a subset of B.

Definition 1.3 Suppose A and B are sets. If every element of A is also an element of B, then we say A is a subset of B, and we denote this as $A\subseteq B$ . We write A  B if A is not a subset of B, that is, if it is not true that every element of A is also an element of B. Thus A  B means that there is at least one element of A that is not an element of B.

Example 1.5 Be sure you understand why each of the following is true.

This brings us to a significant fact: If B is any set whatsoever, then $\emptyset\subseteq B$ To see why this is true, look at the last sentence of Definition 1.3. It says that   B would mean that there is at least one element of  that is not an element of B. But this cannot be so because  contains no elements! Thus it is not the case that $\varnothing\not\subseteq B$ , so it must be that .$\emptyset\subseteq B$ 

Fact 1.2 The empty set is a subset of all sets, that is,$\emptyset\subseteq B$ for any set B.

Here is another way to look at it. Imagine a subset of B as a thing you make by starting with braces {}, then filling them with selections from B.For example, to make one particular subset of $B=\left\{a,b,c\right\}$ , start with{},select b and c from B and insert them into {} to form the subset {b,c}.Alternatively, you could have chosen just a to make {a}, and so on. But one option is to simply select nothing from B. This leaves you with the subset {}.Thus $\left\{\right\}{\subseteq}B$ .More often we write it as $\emptyset\subseteq B$ 



This idea of "making" a subset can help us list out all the subsets of a.given set B. As an example, let $B=\left\{a,b,c\right\}$ . Let's list all of its subsets. One.way of approaching this is to make a tree-like structure. Begin with the subset {}, which is shown on the left of Figure 1.3. Considering the element a of B, we have a choice: insert it into {}, or not. The lines from {} point to what we get depending whether or not we insert a, either {} or {a}. Now move on to the element b of B. For each of the sets just formed we can either insert or not insert b, and the lines on the diagram point to the resulting sets {}, {b},{a}, or {a,b}. Finally, to each of these sets, we can either insert c or not insert it, and this gives us, on the far right-hand column, the sets {}, {c}, {b}, {b,c}, {a}, {a,c}, {a,b} and{a,b,c}. These are the eight subsets of $B=\{a,b,c\}$ 



<div style="text-align: center;"><img src="imgs/img_in_image_box_294_550_761_972.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">Figure 1.3. A "tree" for listing subsets.</div>


We can see from the way this tree branches that if it happened that $B=\{a\}$ , then B would have just two subsets, those in the second column of.the diagram. If it happened that.$B=\{a,b\}$ :, then B would have four subsets,.those in the third column, and so on. At each branching of the tree, the number of subsets doubles. So in general, if ..$|B|=n$ ,then B has 2n subsets.

Fact 1.3 If a finite set has n elements, then it has 2n subsets..