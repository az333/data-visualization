# -*- coding: utf-8 -*-
dataStr='''
Wyoming Birth Data 2016;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;32.8;43rd;39.8
Cesarean Delivery Rate;27.4;37th (tie);31.9
Preterm Birth Rate;9.5;29th;9.9
Teen Birth Rate ‡;26.1;11th;20.3
Low Birthweight Rate;8.5;17th (tie);8.2
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
WY Leading Causes of Death, 2016;Deaths;Rate***;State Rank*;U.S. Rate**
1. Heart Disease;1,051;157.8;27th;165.5
2. Cancer;962;140.9;44th;155.8
3. Accidents;371;61.9;9th;47.4
4. Chronic Lower Respiratory Disease;327;48.9;12th (tie);40.6
5. Stroke;208;31.7;42nd;37.3
6. Suicide;144;25.2;3rd;13.5
7. Alzheimer’s disease;138;21.2;44th;30.3
8. Diabetes;112;16.6;46th;21.0
9. Flu/Pneumonia;99;15.0;15th (tie);13.5
10. Chronic Liver Disease/Cirrhosis;88;13.2;8th (tie);10.7
Wyoming Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;101;17.4;38,658;11.8
Homicide;17;n/a;19,362;6.2
Drug Overdose Deaths;99;17.6;63,632;19.8
Other Wyoming Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);5.0;5.9
Percentage of Persons Without Health Insurance****;n/a;9.0††
Marriage Rate;7.1;6.9
Divorce Rate;4.2;3.2†
Wyoming Birth Data 2015;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;33.9;42nd;40.3¹
Cesarean Delivery Rate;27.3;39th;32.0
Preterm Birth Rate;9.8;23rd (tie);9.6
Teen Birth Rate ‡;29.2;12th;22.3
Low Birthweight Rate;8.6;14th (tie);8.1
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
WY Leading Causes of Death, 2015;Deaths;Rate***;State Rank*;U.S. Rate**
1. Heart Disease;1,030;159.4;26th;168.5
2. Cancer;931;139.4;47th;158.5
3. Accidents;400;65.8;4th;43.2
4. Chronic Lower Respiratory Disease;368;57.1;5th (tie);41.6
5. Stroke;198;31.4;43rd;37.6
6. Suicide;157;28.0;1st;13.3
7. Alzheimer’s disease;151;24.2;37th;29.4
8. Diabetes;136;20.8;32nd;21.3
9. Chronic Liver Disease/Cirrhosis;118;18.9;2nd;10.8
10. Flu/Pneumonia;99;16.0;16th;15.2
Wyoming Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;113;19.6;36,252;11.1
Homicide;17;n/a;17,793;5.7
Drug Poisoning Deaths;96;16.4;52,404;16.3
Other Wyoming Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);5.0;5.9
Percentage of Persons Without Health Insurance 2015 2016****;11.8 n/a;9.1 9.0††
Marriage Rate;7.3;6.9
Divorce Rate;4.1;3.1†
Wyoming Birth Data 2014;State;Rank*;U.S.**
Percent of Births to Unmarried Mothers;33.2;42nd (tie);40.2¹
Cesarean Delivery Rate;27.8;36th (tie);32.2
Preterm Birth Rate;11.2;4th;9.6
Teen Birth Rate ‡;30.1;11th;24.2
Low Birthweight Rate;9.2;6th;8.0
"¹ Excludes data from U.S. territories
 ‡Number of live births per 1,000 females aged 15-19"
WY Leading Causes of Death, 2014;Deaths;Rate***;State Rank*;U.S. Rate**
1. Heart Disease;1,035;162.2;23rd;167.0
2. Cancer;922;140.7;47th;161.2
3. Accidents;361;60.9;3rd;40.5
4. Chronic Lower Respiratory Disease;343;55.0;5th;40.5
5. Stroke;189;30.2;44th;36.5
6. Alzheimer’s disease;162;26.6;26th;25.4
7. Suicide;120;20.6;4th;13.0
8. Flu/Pneumonia;113;18.1;12th (tie);15.1
9. Diabetes;110;17.6;44th;20.9
10. Chronic Liver Disease/Cirrhosis;89;14.5;3rd;10.4
Wyoming Mortality Data;Deaths;Rate**;U.S. Deaths;U.S. Rate***
Firearm Deaths;93;16.2;33,594;10.3
Homicide;24;4.4;15,872;5.1
Drug Poisoning Deaths;109;19.4;47,055;14.7
Other Wyoming Data;State;U.S.
Infant Mortality Rate (Deaths per 1,000 live births);6.4;5.8
Percentage of Persons Without Health Insurance;10.9;11.5
Marriage Rate;7.7;6.9†
Divorce Rate;4.6;3.2††

'''
    
lines = dataStr.split('\n')

with open('../data/data.csv', 'a') as inFile:
    inFile.write('\n'.join(lines[9:24]))
    inFile.write('\n\n')
