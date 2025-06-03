clear all
set more off 

Data 

encode date, gen(Date) //converting from string to long

tsset Date 

**Line Graphs 
twoway line closem Date


**Series at first difference 
gen dclosem=d.closem


**line graph
twoway line dclosem Date


**correlograms 
corrgram closem // Q testing autocorrelation 


**Ac and PAC for stationary data 
ac dclosem  


pac dclosem 


**test for stationary
pperron dclosem

dfuller dclosem // stationary 

**Second difference 
gen d2closem = d2.closem
dfuller d2closem

**estimation 
arima d2closem, arima(#,#,#)

**Natural log
gen lnclosem=ln(closem)
twoway (tsline lnclosem)
//Making data smooth 

gen lnclosec=ln(closec)
twoway (tsline lnclosec)

**ARIMA for motor 
arima lnclosem, arima(0,1,0) //BIC = 15.70819
arima lnclosem, arima(1,1,1) //BIC = 19.54651
arima lnclosem, arima(0,1,1) //BIC = 17.28894
arima lnclosem, arima(1,1,0) //BIC = 17.51754
arima lnclosem, arima(3,1,1) //not feasible
arima lnclosem, arima(2,1,0) //BIC= 18.27006
arima lnclosem, arima(2,1,1) //BIC= 15.44103
arima lnclosem, arima(2,1,2) //not feasible
arima lnclosem, arima(1,1,2) //not feasible 
arima lnclosem, arima(0,1,1) //BIC = 17.52049
//After trying all the possibilities we get that arima (0,1,0) because here BIC is less 


**ARIMA
arima d2closem, arima(0,1,1) //BIC= 109.6398
arima d2closem, arima(0,1,0)//BIC=112.185
arima d2closem, arima(0,1,2)//BIC=107.537
arima d2closem, arima(0,1,3)//BIC=109.6144
arima d2closem, arima(0,1,4)//BIC=111.5545
arima d2closem, arima(0,1,5)//BIC=108.3522
arima d2closem, arima(0,1,6)//BIC=113.9582
arima d2closem, arima(0,1,7)//BIC=116.0138
arima d2closem, arima(1,1,0)//BIC=111.2233
arima d2closem, arima(1,1,1)//BIC=108.4113   
arima d2closem, arima(1,1,2)//BIC = 111.694
arima d2closem, arima(1,1,3)//not feasible 
arima d2closem, arima(2,1,0)//BIC = 112.672
arima d2closem, arima(2,1,1)//BIC = 110.4334
arima d2closem, arima(2,1,1)//not feasible 
arima d2closem, arima(3,1,0)//BIC = 113.6486
arima d2closem, arima(3,1,1)//BIC = 111.8576
arima d2closem, arima(3,1,2)//not feasible
so final that ARImA for motor will be (0,1,2)

***Log data
**Predicting residuals
predict error2, resid

**WHite noise 
twoway(tsline error2)

wntestq error2
//p value is 0.3801 that is gretaer than 0.05 so fail to reject so good to go 


****Forecasting 
tsappend, add(3)
predict fclosem2, y dynamic(y(2023))
tsline lnclosem, fclosem2


****double difference data 
**Predicting residuals
predict error3, resid

**WHite noise 
twoway(tsline error3)

wntestq error3
//p value is 0.8255 that is gretaer than 0.05 so fail to reject so good to go 


****Forecasting 
tsappend, add(3)
predict fclosem3, y dynamic(y(2023))
twoway (tsline closem fclosem3)
twoway (tsline d2closem fclosem3)

