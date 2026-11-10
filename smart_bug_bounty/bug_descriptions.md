# Xətaların Təsviri (Bug Descriptions)

## bug1.py
- **Nəzərdə tutulan davranış**: 
  1. `get_last_n_items`: Siyahıdan son `n` elementi qaytarmaq.
  2. `calculate_average_score`: Balların cəmini ümumi element sayına (`len(scores)`) bölərək dəqiq ədədi ortanı hesablamaq.
- **Mövcud xəta**: 
  1. `get_last_n_items` funksiyasında dili dilimləmə (slicing) indeksində off-by-one xətası var (`len(lst) - n + 1`), bu da tələb olunan aralığın ilk elementini buraxır.
  2. `calculate_average_score` ümumi cəmi `len(scores) - 1` ədədinə bölür ki, bu da yanlış və yüksək orta göstərici qaytarır.

## bug2.js
- **Nəzərdə tutulan davranış**: 
  1. `fetchUserProfile`: Məlumatı qaytarmazdan əvvəl istifadəçi məlumatlarının yüklənməsini asinxron şəkildə gözləmək.
  2. `getActiveUsers`: Orijinal obyekt xassələrini dəyişdirmədən yalnız `isActive` xassəsi `true` olan istifadəçiləri süzgəcdən keçirmək.
- **Mövcud xəta**: 
  1. `fetchUserProfile` funksiyası `setTimeout` kənarlaşdırması bitmədən `userData`-nı sinxron olaraq `null` qaytarır.
  2. `getActiveUsers` müqayisə (`===`) əvəzinə mənimsətmə (`=`) operatorundan istifadə edir, bu da bütün istifadəçilərin `isActive` dəyərini `true` edir və hamısını nəticəyə daxil edir.

## bug3.java
- **Nəzərdə tutulan davranış**: 
  1. `removeShortStrings`: Uzunluğu `minLength`-dən qısa olan bütün mətnləri orijinal siyahıdan təhlükəsiz şəkildə silmək.
  2. `compareUserIds`: İki `Integer` obyektinin dəyər bərabərliyini düzgün müqayisə etmək.
- **Mövcud xəta**: 
  1. `removeShortStrings` dözümlülük dövrü əsnasında siyahını dəyişdirir, bu da silinmiş elementlərin yanındakı elementlərin ötürülməsinə səbəb olur.
  2. `compareUserIds` `.equals()` əvəzinə `==` istinad bərabərliyindən istifadə edir, bu da primitiv keşləmə diapazonundan (-128-dən 127-yə kimi) kənar `Integer` dəyərlərində xəta verir.

## bug4.cpp
- **Nəzərdə tutulan davranış**: 
  1. `createArray`: Massivi dinamik şəkildə ayırmaq və ya kənardan verilən buferi dolduraraq çağırılan sahədə etibarlı yaddaş göstəricisi qaytarmaq.
  2. `computeVectorMean`: Vektor elementlərini düzgün sərhədlər daxilində (index `0`-dan `size - 1`-ə qədər) toplamaq.
- **Mövcud xəta**: 
  1. `createArray` lokal sahədə yaradılmış stək yaddaşına (`tempArray`) asılı göstərici (dangling pointer) qaytarır.
  2. `computeVectorMean` funksiyasındakı `i <= numbers.size()` şərti sərhəddən kənar yaddaşa müraciətə (segmentation fault) səbəb olur.

## bug5.py
- **Nəzərdə tutulan davranış**: 
  1. `process_batch`: Əgər xüsusi keş göstərilməyibsə, elementləri hər çağırış üçün müstəqil keşdə emal etmək.
  2. `retry_operation`: Uğursuz əməliyyat zamanı `False` qaytarmazdan əvvəl tapşırığı `max_attempts` dəfəyə qədər təkrar cəhd etmək.
- **Mövcud xəta**: 
  1. `process_batch` dəyişdirilə bilən susmaya görə arqumentdən (`default_cache={}`) istifadə edir, bu da vəziyyətin (state) müxtəlif çağırışlar arasında qalmasına səbəb olur.
  2. `retry_operation` xəta zamanı `attempts += 1` sayğacını artırmağı unudur, bu da `task_func()` uğursuz olduqda sonsuz dövr yaradır.
