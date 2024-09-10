-- 코드를 입력하세요
SELECT count(*) as USERS
from user_info
where year(joined) = 2021
    AND AGE BETWEEN 20 AND 29;