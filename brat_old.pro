PRO BRAT

;; These variables are used to calculate branching ratios

dxl=1            ; level we are exciting from
dxu=2            ; level we are exciting to
zzero=1e-10      ; floor. used as a tolerance setting
last_level = 57  ; number of the last level in the adf04 file.

read, dxl, prompt='Enter lower level: ', format = '(i2)'
read, dxu, prompt='Enter upper level: ', format = '(i2)'
read, last_level, prompt='Enter total # of levels in adf04: ', format = '(i2)'

;; Lines 11 through 35 pull out indx values for dstgsig
;; this part of the code is straight from Stuart
indx_init=dxl-1.0
indx_col=indx_init*(last_level-1)-(indx_init*(indx_init-1.0))/2. +1.
indx_trans=indx_col+(dxu-dxl)-1.
indx_init=indx_init+1.0
indx_trans_final=indx_init*(last_level-1)-(indx_init*(indx_init-1.0))/2.
;print,'indx_col,=',fix(indx_trans)
;print,'NTRMN=',fix(indx_trans)
;print,'NTRANS=',fix(indx_trans_final)

read_adf04,file='adf04_NIST',fulldata=data

openw,2,'dstgsg_indx_vals'
for i=dxu+1,n_elements(data.wa) do begin
   indx1=where((data.lower eq dxu) and (data.upper eq i))
   indx2=where(data.upper eq i)

   ratio=data.aval[indx1]/total(data.aval[indx2])

   printf,2,ratio,format='(1e12.4)'
;   print,i,dxu,ratio,format='(i4,2x,i4,2x,1e12.4)'
endfor
close,2

;; the A-value matrix (aval_mat) is a 3D array.
;; column1 = lower level
;; column2 = upper level
;; column3 = corresponding A-value

aval_mat=fltarr(3,n_elements(data.lower))
aval_mat(0,*)=data.lower
aval_mat(1,*)=data.upper
aval_mat(2,*)=data.aval


;; atot holds the sum of all the A-values below the current level.
;; So atot(2) = A_21
;;    atot(3) = A_32 + A_31
;;    atot(4) = A_43 + A_42 + A_41
;;  And so on.....

atot=dblarr(n_elements(data.wa)+1)

for i=2,n_elements(data.wa) do begin
    indx2=where(data.upper eq i)
    atot[i]=total(data.aval[indx2])
endfor

;; we need a matrix of branching ratios
;; all this block does is take each A-value in aval_mat
;; and multiply it by the sum of all the A-values with
;; upper indices equal or below the current level

indx2=where(aval_mat(0,*) ge dxu)
ratio_mat=aval_mat(*,indx2)

for i = 0, n_elements(ratio_mat(0,*))-1 do begin
	ratio_mat(2,i)=ratio_mat(2,i) / atot(ratio_mat(1,i))
endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; IMPORTANT !!!!!! At this point we have an array of branching fractions sorted by lower level.
;; This array only contains single jumps, i.e. 10-11, 10-12, 10-14, etc..... As of yet there are NO
;; multi jump ratios. So no 10-11-14-57, or 10-12-34-56-57 , etc....
;; Our next task is to complete the branches, so if we have a 10-12, find all the fractions
;; that start in 12, and then compute the 10-12-?? fractions. Repeat this until we get all the way
;; to the last level.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; Calculating branching ratios generates extremely small values, which triggers underflow errors
;; These can be ignored, since we are discarding all ratios below zzero.
;; The following three lines turns off these messages.

currentExcept =!Except
!except = 0
void = Check_Math()

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; This for loop does all the work. We create temporary matrices: temp_mat1,2,3.
;;
;; temp_mat1: at the beginning of each iteration, temp_mat1 pulls out branching ratios
;;            that correspond to the next level up, starting from one level above the
;;            level that we are exciting into.
;;            on the first iteration, it only checks for levels in the ratio_mat matrix.
;;            for every consecutive iteration it checks ratio_mat and temp_mat3.
;;
;; temp_mat2: stores branching ratios for every level in ratio_mat that has a lower level
;;            corresponding to the upper level stored in temp_mat1. We then use the values
;;            in temp_mat1 and temp_mat2 to calculate branching ratios that go to all the
;;            upper levels stored in temp_mat2.
;;
;; temp_mat3: at the end of each loop, temp_mat3 stores any branching ratios temp_mat1
;;            will need on the next iteration, if they are above zzero.
;;
;; data_mat: all the new branching ratios are concatenated into data_mat.
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;AN EXAMPLE: Let's assume that we are exciting from level 2 into level 10 (dxl=2;dxu=10)
;;             and there are only 13 total levels.
;;
;;  BEGIN LOOP
;;
;;      temp_mat1 = [ 10  11  Br_10,11]
;;
;;      temp_mat2 = [ 11  12  Br_11,12
;;	              11  13  Br_11,13]
;;
;;calculate new branching ratios, ' indicates a newly calculated branch
;;
;;	temp_mat2 = [ 10  12  Br_10,12'
;;	              10  13  Br_10,13']
;;
;;	store branching ratios into data_mat
;;
;;	data_mat =  [ 10  11   Br_10,11
;;	              10  12   Br_10,12'
;;		      10  13   Br_10,13']
;;
;;the next loop requires temp_mat1 has an upper level of 12
;;store everything from data_mat with an upper level of 12
;;in temp_mat3, assuming that these new ratios are gt zzero
;;
;;      temp_mat3 =  [10  12   Br_10,12']
;;
;;  LOOP
;;
;;temp_mat1 will now check temp_mat3 AND ratio_mat for upper levels = 12
;;
;;      temp_mat1 =  [10  12   Br_10,12     <------ this one's in ratio_mat
;;                    10  12   Br_10,12']   <------ this one's in temp_mat3
;;                                                 from previous loop
;;
;;      temp_mat2 =  [12  13   Br_12,13]
;;
;;caluculate new branching ratios
;;
;;	temp_mat2 = [ 10  13  Br_10,13''
;;	              10  13  Br_10,13'']
;;
;;cat ratios from last loop with new  branching ratios into data_mat
;;
;;	data_mat =  [ 10  11   Br_10,11
;;	              10  12   Br_10,12'
;;		      10  13   Br_10,13'
;;                    10  13   Br_10_13''   <------ These two are DIFFERENT branches
;;                    10  13   Br_10,13'']  <------ calculated in loop 2
;;
;;      temp_mat3 = [ 10  13   Br_10,13'
;;                    10  13   Br_10,13''
;;                    10  13   Br_10,13'']
;;
;;  LOOP   (this last loop only pulls out the last braching ratio --> Br_10,last_level
;;
;;
;;	data_mat =  [ 10  11   Br_10,11
;;                    10  12   Br_10,12
;;                    10  13   Br_10,13
;;	              10  12   Br_10,12'
;;		      10  13   Br_10,13'
;;                    10  13   Br_10,13''
;;                    10  13   Br_10,13'']
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; There is only one branch from 10 to 11
;; There are two branches from 10 to 12
;; There are four branches from 10 to 13
;;
;; 11  12  13   12  13  13  13
;; 10  10  10   11  12  11  12
;;              10  10  10  11
;;                          10
;;
;;  data_mat stores all of them.
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

for i=1,last_level-dxu do begin
    indx2 = where(ratio_mat(0,*) eq dxu and ratio_mat(1,*) eq dxu+i)
       if(isa(temp_mat3,/ARRAY)) then begin
   	    print,'temp_mat3 !!!'
   	    temp_mat1=[[ratio_mat(*,indx2)],[temp_mat3]]
       endif else begin
   	    print,'no temp_mat3!!!!!'
               temp_mat1=ratio_mat(*,indx2)
       endelse

       indx2=where(ratio_mat(0,*) eq dxu+i)
       temp_mat2=ratio_mat(*,indx2)


    for j = 0,n_elements(temp_mat1(0,*))-1 do begin
        for k = 0,n_elements(temp_mat2(0,*))-1 do begin
	    temp_mat2(2,k) = temp_mat2(2,k) * temp_mat1(2,j)
	endfor
	temp_mat2(0,*)=temp_mat1(0,0)
         if(isa(data_mat,/ARRAY)) then begin
            data_mat=[[temp_mat1(*,j)],[temp_mat2],[data_mat]]
         endif else begin
            data_mat=[[temp_mat1(*,j)],[temp_mat2]]
         endelse
    endfor



    delvar,temp_mat3

    indx4=where(data_mat(1,*) eq dxu+i+1 and data_mat(2,*) ge zzero)

    if(indx4(0) ge 0) then begin
        temp_mat3=data_mat(*,indx4)
       endif

       if(isa(temp_mat3,/ARRAY)) then begin
         print,'temp_mat3'
         print,temp_mat3
       endif
endfor

;; This next loop sorts the data_mat array

indx2 = where(data_mat(2,*) gt zzero)
data_mat=data_mat(*,indx2)
sort_indx=sort(data_mat(1,*))
data_mat=data_mat(*,sort_indx)
;print,'data_mat'
;print,data_mat

;; We only need the sum of all the braches with a common upper level.
;; These sums are stored in branch_mat.
;;
;; data_mat   = ALL non-zzero branches
;; branch_mat = array of the sum of branches with a common upper level,
;;              sorted by upper level.

branch_mat=fltarr(2,last_level)
branch_mat(0,0) = dxu
branch_mat(1,0) = 1.0

for i=1,last_level-dxu do begin
    indx2 = where(data_mat(1,*) eq dxu + i)
    branch_mat(0,i) = dxu+i
     if(indx2(0) ge 0) then begin
        branch_mat(1,i)=total(data_mat(2,indx2))
     endif
endfor


;; print data to file

print, 'branch_mat'
print,branch_mat

string1=strcompress(string(dxl))
strput, string1, '_', 0
string2 = strcompress(string(dxu))
strput, string2, '_', 0
filestring = 'bratio' + string1 + string2

openw,19,'rawdata.dat'
printf,19,data_mat,format='(1i3,3x,1e12.4)'
close,19
openw,27,filestring
printf,27,'## NTRMN=',fix(indx_trans)
printf,27,'## NTRANS=',fix(indx_trans_final)
printf,27,branch_mat,format='(1i3,3x,1e12.4)'
close,27

print, 'Data file written to ', filestring
print, 'Program ending!!!!'
print, 'type .c to exit (erases all stored matrices)'
stop

print,'indx_col,=',fix(indx_trans)
print,'NTRMN=',fix(indx_trans)
print,'NTRANS=',fix(indx_trans_final)
END
