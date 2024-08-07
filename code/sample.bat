@echo off
echo Hello, World!

set /a x=10
set /a y=20
set /a sum=x+y
echo Sum: %sum%

set numbers=1 2 3
for %%n in (%numbers%) do (
    echo Number: %%n
)

rem Conditional statements
if %x%==10 (
    echo x is 10
) else (
    echo x is not 10
)

rem Functions (labels and goto)
call :greet Alice
exit /b

:greet
set name=%1
echo Hello, %name%!
exit /b
