-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS AS ai
    JOIN ANIMAL_OUTS AS ao
        ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.DATETIME > ao.DATETIME  -- 보호 시작일보다 입양일이 더 빠른 동물
ORDER BY ai.DATETIME;