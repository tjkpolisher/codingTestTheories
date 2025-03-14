# [Silver II] Artificial Intelligence? - 6582 

[문제 링크](https://www.acmicpc.net/problem/6582) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 3월 14일 13:45:11

### 문제 설명

<p>Physics teachers in high school often think that problems given as text are more demanding than pure computations. After all, the pupils have to read and understand the problem first!</p>

<p>So they don't state a problem like "U=10V, I=5A, P=?" but rather like "You have an electrical circuit that contains a battery with a voltage of U=10V and a light-bulb. There's an electrical current of I=5A through the bulb. Which power is generated in the bulb?".</p>

<p>However, half of the pupils just don't pay attention to the text anyway. They just extract from the text what is given: U=10V, I=5A. Then they think: "Which formulae do I know? Ah yes, P=U*I. Therefore P=10V*5A=500W. Finished."</p>

<p>OK, this doesn't always work, so these pupils are usually not the top scorers in physics tests. But at least this simple algorithm is usually good enough to pass the class. (Sad but true.)</p>

<p>Today we will check if a computer can pass a high school physics test. We will concentrate on the P-U-I type problems first. That means, problems in which two of power, voltage and current are given and the third is wanted.</p>

<p>Your job is to write a program that reads such a text problem and solves it according to the simple algorithm given above.</p>

### 입력 

 <p>The first line of the input file will contain the number of test cases.</p>

<p>Each test case will consist of one line containing exactly two data fields and some additional arbitrary words. A data field will be of the form I=<em>x</em>A, U=<em>x</em>V or P=<em>x</em>W, where <em>x</em> is a real number. Directly before the unit (A,V or W) one of the prefixes m (milli), k (kilo) and M (Mega) may also occur. To summarize it: Data fields adhere to the following grammar:</p>

<pre>DataField ::= Concept '=' RealNumber [Prefix] Unit
Concept   ::= 'P' | 'U' | 'I'
Prefix    ::= 'm' | 'k' | 'M'
Unit      ::= 'W' | 'V' | 'A'
</pre>

<p>Additional assertions:</p>

<ul>
	<li>The equal sign ('=') will never occur in an other context than within a data field.</li>
	<li>There is no whitespace (tabs,blanks) inside a data field.</li>
	<li>Either P and U, P and I, or U and I will be given.</li>
</ul>

### 출력 

 <p>For each test case, print three lines:</p>

<ul>
	<li>a line saying "Problem #<em>k</em>" where <em>k</em> is the number of the test case</li>
	<li>a line giving the solution (voltage, power or current, dependent on what was given), written without a prefix and with two decimal places as shown in the sample output</li>
	<li>a blank line</li>
</ul>

