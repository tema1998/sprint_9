## Environment
```
Create research/.env using research/.env.example.
```

## Research results
In researching was used laptop "Dell latitude 5520".

|                                                                                                                                                               |              MongoDB              |            PostgreSQL             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:---------------------------------:|
| **Average parallel insert time of 1 entry - 5 attempts, sek**                                                                                                 |              0.00344              |             0.003212              |
| **Average parallel insert time of 1m likes, 1m reviews and 1m bookmarks - 5 attempts, sek**                                                                   |              861.045              |             1021.132              |
| **Extract time, sek:**<br/> *Count number of likes of the film*<br/> *Count average film rating* <br/> *Count number of user's bookmarks*                     | <br/>0,3989<br/>0,0014<br/>0,3090 | <br/>0,0572<br/>0,1537<br/>0,0555 |
| **Extract time during database load, sek:**<br/> *Count number of likes of the film*<br/> *Count average film rating* <br/> *Count number of user's bookmarks* | <br/>0,8224<br/>0,0015<br/>0,6483  | <br/>0,0848<br/>0,2225<br/>0,0793 |
