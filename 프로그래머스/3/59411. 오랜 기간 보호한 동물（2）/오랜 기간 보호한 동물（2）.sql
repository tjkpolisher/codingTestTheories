-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME -- 아이디, 이름
FROM ANIMAL_INS AS ai
    RIGHT JOIN ANIMAL_OUTS AS ao -- 입양을 간 동물들로 한정
        ON ai.ANIMAL_ID = ao.ANIMAL_ID
ORDER BY (ao.DATETIME - ai.DATETIME) DESC -- 보호 기간이 긴 순서대로
LIMIT 2; -- 두 마리