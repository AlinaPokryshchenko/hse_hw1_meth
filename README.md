# hse_hw1_meth
-----------------
### [Colab](https://colab.research.google.com/drive/1YrA7o2Go1ImntZAGQ0zuZT_pVYK3yuPu?usp=sharing)
[Доп ссылка на колаб](https://colab.research.google.com/drive/1NWNQXxOnr5Ytbd3rrLfOSxpHtUkaImYV?usp=sharing) 
## Анализ QC прочтений
-------------
По результатам fastQC образца SRR5836475 получился отчет, который можно найти в папке data.
## Какие особенности можно наблюдать по сравнению с секвенированием ДНК или РНК?
По сравнению с секвенированием ДНК и РНК в данном случае наблюдается необычный нуклеотидный состав. Гуанин и аденин присутствуют в нормальном процентном соотношении (23-30%). В то же время тимин преобладает (около 45%), а цитозина очень мало (около 5%). Это объясняется особенностями бисульфитного секвенирования, при котором неметилированные цитозины превращаются в урацил. Урацил в свою очередь считывается как тимин, что мы как рз видим на графике. На другом графике также наблюдаются особенности GC-состава: мы видим два пика примерно на 20% и 68%, что также объясняется особенностями бисульфитного секвенирования.
## Соотношение нуклеотидов в составе
-----------
![1_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/nucleotides.png?raw=true) 
## GC-состав
-----------
![2_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/GC.png?raw=true) 
## Статистика по каждому из 3 образцов
|Номер образца|Тип клеток|Риды на 11347700-11367700 нуклеотидах|Риды на 40185800-40195800 нуклеотидах|% дуплицированных|
|---------------|----------|-------------------------|---------------------------|---------------|
|SRR5836473|8 cell|1090|464|18.31%|
|SRR3824222|Epiblast|2328|1062|2.92%|
|SRR5836475|ICM|1456|630|9.08%|
## M-bias графики
---------------
8 cell

![3_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/8cell_1_bias.png?raw=true)
![4_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/8cell_2_bias.png?raw=true)

Epiblast

![5_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/epiblast_1_bias.png?raw=true)
![6_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/epiblast_2_bias.png?raw=true)

ICM

![7_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/icm_1_bias.png?raw=true)
![8_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/icm_2_bias.png?raw=true)

*В целом, процент метилированных нуклеотидов в клетках Epiblast выше по отношению с другими типами клеток. 
По данным графикам можно отметить также общую закономерность: в ридах с обратными цепями наблюдается чуть больший процент метилирования (CpG) в начале последовательности ( у клеток ICM и 8 cell), в клетках Epiblast процент метилирования (CpG) в начале образца наоборот чуть меньше. M-bias нужен для того чтобы исследователь мог принять решение, следует ли оставлять bias в окончательных данных или удалять его. В данном случае можно сказать, что риды с разбросом метилирования можно игнорировать, так как bias не так значительно отклоняется.


------------
## Гистограммы распределения метилирования цитозинов по хромосоме
8 cell

![9_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/8cell_met_c.png?raw=true) 

Epiblast

![10_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/epiblast_met_c.png?raw=true) 

ICM

![11_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/icm_met_c.png?raw=true) 

Можно сделать вывод, что метилирование сильнее в образце Epiblast, в то время как в ICM большая часть цитозина не метилирована, а в 8 cell распределение равномерное.
В целом, полученные графики идентичны графикам из статьи.

-----------
## Уровень метилирования и покрытия для каждого образца

![12_image](https://github.com/AlinaPokryshchenko/hse_hw1_meth/blob/main/images/level_met_c.png?raw=true) 
