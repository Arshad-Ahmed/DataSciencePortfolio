!simple calculator
program calculate
implicit none
!simple calculator
real :: a,b,c,d
print *,'Enter a number followed by two exponents'
read *,a,b,c
print *, 'you entered ',a,b,c
d = (a**b)**c
print *, 'answer is ',d

end program calculate