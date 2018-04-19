# -*- coding: utf-8 -*-
dataStr='''
Montana Birth Data 2016;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;36.4;34th;39.8
Cesarean Delivery Rate;29.1;34th;31.9
Preterm Birth Rate;8.8;42nd (tie);9.9
Teen Birth Rate ‡;23.7;15th (tie);20.3
Low Birthweight Rate;7.9;29th (tie);8.2
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
MT Leading Causes of Death, 2016;Deaths;Rate***;State Rank*;U.S. Rate**
1. Heart Disease;2,138;154.4;30th;165.5
2. Cancer;2,031;145.9;41st;155.8
3. Chronic Lower Respiratory Disease;722;51.9;11th;40.6
4. Accidents;626;54.1;22nd;47.4
5. Stroke;440;32.5;39th (tie);37.3
6. Alzheimer’s Disease;314;22.6;41st;30.3
7. Diabetes;311;23.6;16th;21.0
8. Suicide;267;25.9;1st;13.5
9. Chronic Liver Disease/Cirrhosis;160;13.6;6th;10.7
10. Kidney Disease;155;11.3;30th (tie);13.1
Montana Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;194;18.9;38,658;11.8
Homicide;42;4.3;19,103;6.1
Drug Overdose Deaths;119;11.7;63,632;19.8
Other Montana Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);5.9;5.9
Percentage of Persons Without Health Insurance;9.3;9.0††
Marriage Rate;7.8;6.9†
Divorce Rate;3.1;3.2†
Montana Birth Data 2015;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;36.3;34th;40.3¹
Cesarean Delivery Rate;29.7;31st;32.0
Preterm Birth Rate;8.4;43rd (tie);9.6
Teen Birth Rate ‡;25.3;20th;22.3
Low Birthweight Rate;7.1;35th (tie);8.1
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
MT Leading Causes of Death, 2015;Deaths;Rate***;State Rank*;U.S. Rate**
1. Cancer;2,130;156.9;31st;158.5
2. Heart Disease;2,104;155.8;31st;168.5
3. Chronic Lower Respiratory Disease;679;50.2;14th;41.6
4. Accidents;637;56.3;10th;43.2
5. Stroke;458;33.8;35th;37.6
6. Diabetes;321;24.5;14th;21.3
7. Alzheimer’s Disease;277;20.7;42nd;29.4
8. Suicide;272;25.3;3rd;13.3
9. Flu/Pneumonia;183;13.7;37th;15.2
10. Chronic Liver Disease/Cirrhosis;179;15.7;4th;10.8
Montana Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;205;19.2;36,252;11.1
Homicide;38;4.0;17,793;5.7
Drug Poisoning Deaths;138;13.8;52,404;16.3
Other Montana Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);6.0;5.9
Percentage of Persons Without Health Insurance 2015 2016;10.0 9.3;9.1 9.0††
Marriage Rate;8.0;6.9†
Divorce Rate;3.4;3.1†
Montana Birth Data 2014;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;36.9;34th;40.2¹
Cesarean Delivery Rate;31.4;23rd;32.2
Preterm Birth Rate;9.3;25th (tie);9.6
Teen Birth Rate ‡;26.4;20th;24.2
Low Birthweight Rate;7.4;33rd;8.0
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
MT Leading Causes of Death, 2014;Deaths;Rate***;State Rank*;U.S. Rate**
1. Cancer;2066;156.3;33rd;161.2
2. Heart Disease;1957;147.8;38th;167.0
3. Chronic Lower Respiratory Disease;668;50.3;13th;40.5
4. Accidents;581;52.6;9th;40.5
5. Stroke;480;36.4;27th;36.5
6. Alzheimer’s disease;253;19.2;39th;25.4
7. Suicide;251;23.9;1st;13.0
8. Diabetes;250;19.2;34th (tie);20.9
9. Flu/Pneumonia;179;13.7;36th (tie);15.1
10. Chronic Liver Disease/Cirrhosis;150;12.2;10th (tie);10.4
Montana Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;172;16.1;33,594;10.3
Homicide;30;2.9;15,872;5.1
Drug Poisoning Deaths;125;12.4;47,055;14.7
Other Montana Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);5.5;5.8
Percentage of Persons Without Health Insurance;10.0;9.1
Marriage Rate;7.9;6.9†
Divorce Rate;3.4;3.2††

'''
    
lines = dataStr.split('\n')

with open('../data/data.csv', 'a') as inFile:
    inFile.write('\n'.join(lines[9:24]))
    inFile.write('\n\n')
