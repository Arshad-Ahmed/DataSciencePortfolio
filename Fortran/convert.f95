program convert
!Example of how to do conversion
implicit none
integer :: pounds,pence,total
character :: name*10
print *,'Enter your name'
read *,name
print *,'Hello ',name,'enter some values in pounds and pence'
read *,pounds,pence
total = 100 * pounds + pence
print *,'The total in pence is ',total

end program convert