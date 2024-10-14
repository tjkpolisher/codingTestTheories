# [Silver IV] Lemonade Line - 15761 

[문제 링크](https://www.acmicpc.net/problem/15761) 

### 성능 요약

메모리: 42036 KB, 시간: 60 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 10월 14일 15:07:06

### 문제 설명

<p>It's a hot summer day out on the farm, and Farmer John is serving lemonade to his $N$ cows! All $N$ cows (conveniently numbered $1 \dots N$) like lemonade, but some of them like it more than others. In particular, cow $i$ is willing to wait in a line behind at most $w_i$ cows to get her lemonade. Right now all $N$ cows are in the fields, but as soon as Farmer John rings his cowbell, the cows will immediately descend upon FJ's lemonade stand. They will all arrive before he starts serving lemonade, but no two cows will arrive at the same time. Furthermore, when cow $i$ arrives, she will join the line if and only if there are at most $w_i$ cows already in line.</p>

<p>Farmer John wants to prepare some amount of lemonade in advance, but he does not want to be wasteful. The number of cows who join the line might depend on the order in which they arrive. Help him find the minimum possible number of cows who join the line.</p>

### 입력 

 <p>The first line contains $N$, and the second line contains the $N$ space-separated integers $w_1, w_2, \dots, w_N$. It is guaranteed that $1 \leq N \leq 10^5$, and that $0 \leq w_i \leq 10^9$ for each cow $i$.</p>

### 출력 

 <p>Print the minimum possible number of cows who might join the line, among all possible orders in which the cows might arrive.</p>

