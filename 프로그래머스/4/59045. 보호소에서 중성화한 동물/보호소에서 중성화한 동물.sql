-- 코드를 입력하세요
-- 중성화를 거친 동물은 Spayed 혹은 Neutered라고 표기됨.
SELECT ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME
FROM ANIMAL_INS AS ai
    INNER JOIN ANIMAL_OUTS AS ao
    ON ai.ANIMAL_ID = ao.ANIMAL_ID -- 외래 키
WHERE (ao.SEX_UPON_OUTCOME LIKE "Spayed%" OR ao.SEX_UPON_OUTCOME LIKE "Neutered%") AND (ai.SEX_UPON_INTAKE LIKE "Intact%")
ORDER BY ai.ANIMAL_ID;