program io
!Some basic calculation
real :: x,y,z,answer
print *,'enter values for x,y,z'
read *,x
read *,y
read *,z
print *,'the values you enetered for x,y,z ',x,y,z
answer = x+y+z
print *,'the sum of the numbers entered are ',answer
end program io